import marimo

__generated_with = "0.26.0"
app = marimo.App(width="medium")


@app.cell
def _():

    import marimo as mo
    import pandas as pd

    # Chargement du fichier de données dans un tableau pandas
    df = pd.read_csv(mo.notebook_dir() / ".." / "data" / "raw" / "attribution_data.csv")
    df.shape

    # Ventilation des interactions par canal
    df["channel"].value_counts()

    # Nombre de cookies uniques, donc de parcours possibles
    df["cookie"].nunique()

    # Ventilation des lignes par type d'interaction
    df["interaction"].value_counts()

    # Nombre total de conversions
    df["conversion"].sum()


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
