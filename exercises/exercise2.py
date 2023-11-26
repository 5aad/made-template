import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import *
from pathlib import Path

def TransformBahnhofData(df):
    
#   drop status column and convert numeric type of Laenge and Breite column
    df = df.drop(columns=['Status'])
    df['Laenge'] = df['Laenge'].str.replace(',', '.').astype(float)
    df['Breite'] = df['Breite'].str.replace(',', '.').astype(float)

#   filter the data and drop rows with empty cells
    df = df[
        (df["Verkehr"].isin(["FV", "RV", "nur DPN"])) &
        (df["Laenge"].between(-90, 90)) &
        (df["Breite"].between(-90, 90)) &
        (df["IFOPT"].str.match(r"^[A-Za-z]{2}:\d+:\d+(?::\d+)?$"))
        ].dropna()
    
    return df

def CreateSql(data, file):
    current_directory = Path.cwd()
    parent_directory = current_directory.parent
    database_path = parent_directory / f'exercises/{file}.sqlite'
    engine = create_engine(f"sqlite:///{database_path}")
    data.to_sql('trainstops', engine, index=False, if_exists='replace', dtype={
    "EVA_NR": BigInteger,
    "DS100": Text,
    "IFOPT": Text,
    "NAME": Text,
    "Verkehr": Text,
    "Laenge": Float,
    "Breite": Float,
    "Betreiber_Name": Text,
    "Betreiber_Nr": Integer, 
    })
    data.to_sql(file, engine, if_exists="replace")


def main():
    bahnhof_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    df = pd.read_csv(bahnhof_url, sep=';')
    data = TransformBahnhofData(df)
    CreateSql(data, "trainstops")
    

if __name__ == "__main__":
    main()