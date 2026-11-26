"""Last-click attribution model."""

import pandas as pd


def compute_last_click(journeys: pd.DataFrame) -> pd.DataFrame:
    """Credit each conversion to the last channel of its journey.

    Args:
        journeys: One row per journey, with columns `canaux` (channels joined
            by " > "), `converti` (1 if the journey converted) and `valeur`.

    Returns:
        One row per channel, with columns `channel`, `conversions` and `value`.
    """
    converted = journeys[journeys["converti"] == 1].copy()
    converted["channel"] = converted["canaux"].str.split(" > ").str[-1]

    credit = converted.groupby("channel").agg(
        conversions=("converti", "sum"),
        value=("valeur", "sum"),
    ).reset_index()

    return credit.sort_values("conversions", ascending=False).reset_index(drop=True)