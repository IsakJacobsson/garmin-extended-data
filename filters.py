def filter_activities(df, activities):
    df = df[df["Aktivitetstyp"].isin(activities)].copy()
    return df
