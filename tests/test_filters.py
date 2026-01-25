import pandas as pd

from filters import filter_activities


def test_filter_activities_keeps_only_selected_types():
    df = pd.DataFrame(
        {
            "Aktivitetstyp": ["Löpning", "Cykling", "Löpband", "Löpning", "Simbassäng"],
            "Distans": [5, 10, 7, 2, 5],
        }
    )

    result = filter_activities(df, ["Löpning", "Cykling"])

    assert len(result) == 3
    assert set(result["Aktivitetstyp"]) == {"Löpning", "Cykling"}


def test_filter_activities_with_no_matching_activities():
    df = pd.DataFrame(
        {
            "Aktivitetstyp": ["Run", "Bike"],
            "Distans": [5, 10],
        }
    )

    result = filter_activities(df, ["Swim"])

    assert result.empty
