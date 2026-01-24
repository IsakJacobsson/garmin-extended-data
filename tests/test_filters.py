import pandas as pd

from filters import filter_for_distance


def test_filter_for_distance_removes_excluded_activities():
    df = pd.DataFrame(
        {
            "Aktivitetstyp": [
                "Simbassäng",
                "Konditionspass",
                "Styrketräning",
                "Yoga",
                "Löpning",
                "Cykling",
            ],
            "Distans": [5.0, 0.0, 0.0, 0.0, 12.0, 6.0],
        }
    )

    result = filter_for_distance(df)

    assert list(result["Aktivitetstyp"]) == ["Löpning", "Cykling"]


def test_filter_for_distance_does_not_modify_input_df():
    df = pd.DataFrame(
        {
            "Aktivitetstyp": ["Löpning", "Styrketräning"],
            "Distans": [5.0, 0.0],
        }
    )

    df_copy = df.copy(deep=True)

    _ = filter_for_distance(df)

    pd.testing.assert_frame_equal(df, df_copy)


def test_filter_for_distance_all_excluded():
    df = pd.DataFrame(
        {
            "Aktivitetstyp": ["Yoga", "Styrketräning"],
            "Distans": [0.0, 0.0],
        }
    )

    result = filter_for_distance(df)

    assert result.empty
