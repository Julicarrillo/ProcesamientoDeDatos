
import pandas as pd

def transform_date(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["fecha"] = pd.to_datetime(
        dict(
            year=df["Start Year"],
            month=df["Start Month"],
            day=1
        ),
        errors="coerce"
    )

    return df


def clean_categories(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    columnas = ["Disaster Type", "Country", "Continent", "Region"]

    for columna in columnas:
        df[columna] = df[columna].str.strip()

    return df
    

def disasters_by_year(df: pd.DataFrame) -> pd.Series:
    counts = df["Start Year"].value_counts().sort_index()
    return counts


def disasters_by_type_continent(df: pd.DataFrame) -> pd.DataFrame:
    tabla = pd.crosstab(
        df["Disaster Type"],
        df["Continent"]
    )
    return tabla


def disasters_by_month(df: pd.DataFrame) -> pd.Series:
    counts = df["fecha"].dt.month.value_counts().sort_index()
    return counts

    
def disasters_by_type_year(df: pd.DataFrame) -> pd.DataFrame:
    df_reciente = df[df["Start Year"].between(2002, 2021)]

    tabla = pd.crosstab(
        df_reciente["Start Year"],
        df_reciente["Disaster Type"]
    )

    principales = tabla.sum().nlargest(5).index

    return tabla[principales]


def affected_by_continent(df: pd.DataFrame) -> pd.DataFrame:
    df_validos = df.dropna(subset=["Total Affected"])

    tabla = df_validos.groupby("Continent")["Total Affected"].agg(
        ["sum", "count"]
    )

    return tabla.sort_values("sum", ascending=False)
