import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

def FetchData(file):
    df = pd.read_csv(file, delimiter=";")
    return df

def TransformAirQuality(file,column):
    extract_data = FetchData(file)
    df = pd.DataFrame(extract_data)
    air_df = df[df['State'] == 'Bavaria'].sort_values(by='Station code', ascending=True).reset_index(drop=True)
    if column:
        air_df = air_df.drop(columns='Number of daily mean values above 50 µg/m³')
        air_df = air_df.rename(columns={'Annual mean value in µg/m³': 'Annual P10 mean value in µg/m³'})
    return air_df

def TransformHospital(file, columns):
    extract_data = FetchData(file)
    df = pd.DataFrame(extract_data)
    df['TB-Diagnose'] = df['TB-Diagnose'].replace('-', 0)
    hos_df = df.rename(columns=columns)
    return hos_df

# Load data to create a SQLite file
def Load(df, table):
    current_directory = Path.cwd()
    parent_directory = current_directory.parent
    print(parent_directory)
    database_path = parent_directory / f'data/{table}.sqlite'
    engine = create_engine(f"sqlite:///{database_path}")
    df.to_sql(table, engine, if_exists="replace")

def main():
    airquality_p2_file = "./Annual-tabulation_Particulate matter_2022_2.5.csv"
    airquality_p10_file = "./Annual-tabulation_Particulate matter_2022_10.csv"
    hospital_tb_file = "./genesis_destatis_health_ICD-10.csv"
    columns = {
    "Jahr" : "Year",
    "Bundesländer" : "State",
    "Geschlecht" : "Gender",
    "Insgesamt" : "Total_Patient_Admited"}
    data_p2 = TransformAirQuality(airquality_p2_file, False)
    data_p10 = TransformAirQuality(airquality_p10_file, True)
    data_hospital = TransformHospital(hospital_tb_file, columns)
    merged_df = pd.merge(data_p2, data_p10, on=["State","Station code", "Station name", "Station setting", "Station type"], how='inner')

    Load(merged_df, "Airquality")
    Load(data_hospital, "Hospital")

if __name__ == "__main__":
    main()