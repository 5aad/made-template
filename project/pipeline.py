import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

def FetchData(file, deli):
    df = pd.read_csv(file, delimiter=deli)
    return df

def TransformAirQuality(file,column):
    extract_data = FetchData(file, ";")
    df = pd.DataFrame(extract_data)
    air_df = df[df['State / Measuring network'].isin(['Bavaria', 'Brandenburg'])].sort_values(by='Station code', ascending=True).reset_index(drop=True)
    if column:
        air_df = air_df.drop(columns='Number of daily mean values above 50 µg/m³')
        air_df = air_df.rename(columns={'Annual mean value in µg/m³': 'Annual P10 mean value in µg/m³'})
    return air_df

def TransformHospital(file, columns):
    extract_data = FetchData(file,",")
    df = pd.DataFrame(extract_data)
    df['TB-Diagnose'] = df['TB-Diagnose'].replace('-', 0)
    hos_df = df.rename(columns=columns)
    return hos_df

# Load data to create a SQLite file
def Load(df, table):
    current_directory = Path.cwd()
    parent_directory = current_directory.parent
    print(parent_directory)
    database_path = f'./data/{table}.sqlite'
    engine = create_engine(f"sqlite:///{database_path}")
    df.to_sql(table, engine, if_exists="replace")

def main():
    airquality_p2_file = "https://www.umweltbundesamt.de/api/air_data/v3/annualbalances/csv?component=9&year=2022&lang=en"
    airquality_p10_file = "https://www.umweltbundesamt.de/api/air_data/v3/annualbalances/csv?component=1&year=2022&lang=en"
    file_id = '1Nmqbq2YQOmVe0ncfwAHeOQDJRXQZVhlB'
    hospital_tb_file = f'https://drive.google.com/uc?id={file_id}'
    columns = {
    "Jahr" : "Year",
    "Bundesländer" : "State",
    "Geschlecht" : "Gender",
    "Insgesamt" : "Total_Patient_Admited"}
    data_p2 = TransformAirQuality(airquality_p2_file, False)
    data_p10 = TransformAirQuality(airquality_p10_file, True)
    data_hospital = TransformHospital(hospital_tb_file, columns)
    merged_df = pd.merge(data_p2, data_p10, on=["State / Measuring network","Station code", "Station name", "Station setting", "Station type"], how='inner')

    Load(merged_df, "Airquality")
    Load(data_hospital, "Hospital")

if __name__ == "__main__":
    main()