import marimo

__generated_with = "0.26.0"
app = marimo.App(width="medium")


@app.cell
def _(df, mo, pd):
    ## Conversion de time en date, puis tri par cookie et par date
    df_trie = df.copy()
    df_trie["time"] = pd.to_datetime(df_trie["time"])
    df_trie = df_trie.sort_values(["cookie", "time"]).reset_index(drop=True)
    #df_trie.dtypes


    ## Contrôle des valeurs manquantes, des doublons et de la période couverte
    #print(df_trie.isna().sum())
    #print("Doublons :", df_trie.duplicated().sum())
    #print(df_trie["time"].min(), df_trie["time"].max())

    ## Types d'interaction des lignes en double, hors première occurrence
    #copies = df_trie[df_trie.duplicated()]
    #copies["interaction"].value_counts()

    ## Aperçu de lignes en double avec leur première occurrence
    #df_trie[df_trie.duplicated(keep=False)].head(8)

    ## Nature des lignes en double, hors première occurrence
    #doublons = df_trie[df_trie.duplicated()]
    #print(doublons["interaction"].value_counts())
    #print("Conversions en double :", (doublons["conversion"] == 1).sum())

    ## Identifiant de parcours : un parcours se termine à chaque conversion
    conv_avant = df_trie.groupby("cookie")["conversion"].cumsum() - df_trie["conversion"]
    df_parcours = df_trie.assign(parcours_id=df_trie["cookie"] + "_" + conv_avant.astype(str))
    df_parcours[["cookie", "time", "interaction", "channel", "parcours_id"]].head(8)

    ## Table des parcours : une ligne par parcours
    parcours = df_parcours.groupby("parcours_id").agg(
        cookie=("cookie", "first"),
        nb_contacts=("channel", "size"),
        canaux=("channel", " > ".join),
        converti=("conversion", "max"),
        valeur=("conversion_value", "sum"),
        debut=("time", "min"),
        fin=("time", "max"),
    ).reset_index()

    #print(parcours.shape)
    #print("Parcours convertis :", parcours["converti"].sum())
    #print("Valeur totale :", parcours["valeur"].sum())
    #parcours.head(5)

    ## Cinq parcours convertis
    exemples = parcours[parcours["converti"] == 1].head(5)
    exemples[["parcours_id", "nb_contacts", "canaux", "valeur"]]

    ## Cinq parcours convertis
    exemples = parcours[parcours["converti"] == 1].head(5)
    exemples[["parcours_id", "nb_contacts", "canaux", "valeur"]]

    ## Lignes brutes du premier parcours converti
    premier = exemples["parcours_id"].iloc[0]
    df_parcours[df_parcours["parcours_id"] == premier][["time", "interaction", "channel", "conversion"]]

    ## Six dernières lignes du parcours converti de 24 contacts
    long = df_parcours[df_parcours["parcours_id"] == exemples["parcours_id"].iloc[3]]
    #print(long[["time", "interaction", "channel", "conversion"]].tail(6).to_string())

    ## Part des parcours convertis réduits à un seul contact
    #print((parcours.loc[parcours["converti"] == 1, "nb_contacts"] == 1).mean())

    # Export de la table des parcours
    chemin = mo.notebook_dir() / ".." / "data" / "processed" / "journeys.csv"
    parcours.to_csv(chemin, index=False)
    print(parcours.shape, "lignes exportées")


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
    return df, mo, pd


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
