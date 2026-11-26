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

    # Synthèse des constats de l'exploration
    mo.md(
        """
        ## Constats de l'exploration

        **Données** : 586 737 interactions, 240 108 cookies, juillet 2018 (31 jours).
        Aucune valeur manquante. 5 canaux : Facebook, Paid Search, Online Video,
        Instagram, Online Display.

        **Doublons** : 4 145 lignes en double, toutes des impressions, aucune conversion.
        Conservées : impossible de trancher entre double affichage réel et doublon de
        journal. Effet à tester lors de la comparaison des modèles.

        **Parcours** : 240 108 parcours pour 240 108 cookies, donc un seul parcours par
        cookie : aucune interaction ne suit une conversion. 17 639 parcours convertis,
        chiffre conforme au total des conversions du fichier.

        **Ligne de conversion** : elle porte son propre canal et ne double pas le contact
        précédent. 42 % des parcours convertis tiennent en un seul contact. Les quatre
        modèles donneront donc le même crédit dans ces cas, et les écarts se joueront sur
        les 58 % restants.

        **Valeur** : 110 231 au total sur les parcours convertis. La source ne précise pas
        la devise, point à signaler au moment du calcul des ROAS.
        """
    )


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
