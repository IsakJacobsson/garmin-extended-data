import pandas as pd
import streamlit as st

from load_data import load_data

SUMMABLE_COLUMNS = [
    "Distans",
    "Tid",
    "Total stigning",
    "Steg",
    "Kalorier",
    "Aerobisk Training Effect",
    "Total stigning",
    "Totalt nedför",
    "Totalt antal årtag",
    "Totalt antal repetitioner",
    "Totalt antal set",
]


def activity_metrics_over_time_section(df):
    st.header("Activity Metrics Over Time")

    col1, col2 = st.columns(2)

    with col1:
        selected_activities = activity_multiselector(df)

    activity_df = filter_activities(df, selected_activities)

    # Create tabs for different metrics
    with col2:
        valid_metrics = get_valid_metrics(activity_df)
        selected_metric = metric_selector(valid_metrics)

    activity_df["Tid"] = activity_df["Tid"].dt.total_seconds() / 60  # minutes

    if len(selected_activities) == 0:
        st.warning("Please select at least one activity type.")
        return

    # Create tabs for different resolutions
    tab_day, tab_week, tab_month, tab_year = st.tabs(["Day", "Week", "Month", "Year"])

    def plot_metric(period_freq, fmt, tab_label):
        temp_df = activity_df.copy()

        # Convert to Period (do NOT convert to start_time yet)
        temp_df["Period"] = temp_df["Datum"].dt.to_period(period_freq)

        # Aggregate with PeriodIndex
        agg_df = temp_df.groupby("Period")[selected_metric].sum().sort_index()

        # Create full period range (including missing periods)
        full_range = pd.period_range(
            start=agg_df.index.min(),
            end=pd.Timestamp.today().to_period(period_freq),
            freq=period_freq,
        )

        # Reindex to include missing periods
        agg_df = agg_df.reindex(full_range, fill_value=0)

        # Convert to timestamps just for plotting / labels
        plot_df = agg_df.to_timestamp(how="start").to_frame(name=selected_metric)
        plot_df["PeriodStr"] = plot_df.index.strftime(fmt)

        with tab_label:
            st.bar_chart(plot_df.set_index("PeriodStr")[selected_metric])

    # Plot each tab
    plot_metric("D", "%Y-%m-%d", tab_day)  # Day
    plot_metric("W", "%Y-%W", tab_week)  # Week
    plot_metric("M", "%Y-%m", tab_month)  # Month
    plot_metric("Y", "%Y", tab_year)  # Year


def activity_multiselector(df):
    activities = df["Aktivitetstyp"].unique()
    selected_activities = st.multiselect(
        "Activity type",
        activities,
        default=activities[0] if len(activities) > 0 else None,
        placeholder="Select activity types",
    )
    return selected_activities


def metric_selector(metrics):
    selected_metric = st.selectbox("Metric", metrics)
    return selected_metric


def filter_activities(df, activities):
    df = df[df["Aktivitetstyp"].isin(activities)].copy()
    return df


def get_valid_metrics(df):
    valid_metrics = []
    for col in SUMMABLE_COLUMNS:
        if not df[col].isna().any():
            valid_metrics.append(col)
    return valid_metrics


def main():
    st.title("Garmin extended data")

    csv_file = st.file_uploader("Upload Garmin CSV file", type="csv")

    if csv_file is not None:
        df = load_data(csv_file)
        activity_metrics_over_time_section(df)


if __name__ == "__main__":
    main()
