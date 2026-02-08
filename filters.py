import pandas as pd


def filter_activities(
    df: pd.DataFrame,
    activities: list[str],
) -> pd.DataFrame:
    mask = df["Aktivitetstyp"].isin(activities)
    return df.loc[mask].copy()
