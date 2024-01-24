import pandas as pd
import urllib.request
import zipfile
import os
from sqlalchemy import create_engine
from sqlalchemy.types import *
from pathlib import Path


def ReshapeData(downloaded_folder_path):
    
    columns_name = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
    df = pd.read_csv(downloaded_folder_path, sep=";", decimal=",", index_col=False, usecols=columns_name)
    df = df.rename(columns={
        "Temperatur in °C (DWD)": "Temperatur",
        "Batterietemperatur in °C": "Batterietemperatur"
    })
    # print(df.head(5))
    return df


def TransformData(df):
    
    df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
    df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32
    
    return df

def ValidateData(df):
    df = df[df['Geraet'] > 0]
    df = df[df['Monat'].between(1, 12)]
    df = df[pd.to_numeric(df['Temperatur'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df['Batterietemperatur'], errors='coerce').notnull()]
    df = df[df['Geraet aktiv'].isin(['Ja', 'Nein'])]

    return df

def CreateSql(data, file):
    current_directory = Path.cwd()
    parent_directory = current_directory.parent
    database_path = parent_directory / f'exercises/{file}.sqlite'
    engine = create_engine(f"sqlite:///{database_path}")
    data.to_sql(file, engine, index=False, if_exists='replace', dtype={
    "Geraet": Integer,
    "Hersteller": Text,
    "Model": Text,
    "Monat": Text,
    "Temperatur": Float,
    "Batterietemperatur": Float,
    "Geraet_aktiv": Text,
    })
    data.to_sql(file, engine, if_exists="replace")


def main():
    url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
    downloaded_zip_folder = 'mowesta-dataset.zip'
    downloaded_folder = 'mowesta-dataset'

    # Download the zip file and extract the data
    urllib.request.urlretrieve(url, downloaded_zip_folder)
    with zipfile.ZipFile(downloaded_zip_folder, 'r') as zip_ref:
        zip_ref.extractall(downloaded_folder)

    downloaded_folder_path = os.path.join(downloaded_folder, "data.csv")

    # Reshape data
    df = ReshapeData(downloaded_folder_path)
    # Transform data
    df = TransformData(df)
    # Validate data
    df = ValidateData(df)
    
    CreateSql(df, "temperatures")
    

if __name__ == "__main__":
    main()