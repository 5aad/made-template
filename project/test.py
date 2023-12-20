import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, inspect
from pipeline import FetchData, TransformAirQuality, TransformHospital, Load

# data fetch test function
def FetchDataTest(file_path):
    fetch_data = FetchData(file_path)
    if fetch_data.empty:
        raise AssertionError("Failed")
    print("FetchDataTest -> Passed")
    return fetch_data

# transform air quality test function
def TransformAirQualityTest(file,column):
    air_df = TransformAirQuality(file,column)
    if air_df.isna().any().any():
        raise AssertionError("NAN Found in Data")
    print("TransformAirQualityTest -> Passed")
    return air_df

# transform hospital test function
def TransformHospitalTest(file, columns):
    hos_df = TransformHospital(file, columns)
    if hos_df.isna().any().any():
        raise AssertionError("NAN Found in Data")
    print("TransformHospitalTest -> Passed")
    return hos_df

# load test function
def LoadTest(table):
    current_directory = Path.cwd()
    parent_directory = current_directory.parent
    print(parent_directory)
    database_path =  f'./data/{table}.sqlite'
    engine = create_engine(f"sqlite:///{database_path}")
    inspector = inspect(engine)
    if not inspector.has_table(table):
        raise AssertionError(f"The '{table}' does not exist.")
    print(f"LoadTest -> Table '{table}' exists,  Passed")

def main():
    airquality_p2_file = "https://www.umweltbundesamt.de/api/air_data/v3/annualbalances/csv?component=9&year=2022&lang=en"
    airquality_p10_file = "https://www.umweltbundesamt.de/api/air_data/v3/annualbalances/csv?component=1&year=2022&lang=en"
    file_id = '1_foIecAE8BjeWrT_frgy_FZg_Yz6efsm'
    hospital_tb_file = f'https://drive.google.com/uc?id={file_id}'
    columns = {
    "Jahr" : "Year",
    "Bundesländer" : "State",
    "Geschlecht" : "Gender",
    "Insgesamt" : "Total_Patient_Admited"}
    data_p2 = TransformAirQualityTest(airquality_p2_file, False)
    data_p10 = TransformAirQualityTest(airquality_p10_file, True)
    data_hospital = TransformHospitalTest(hospital_tb_file, columns)
    merged_df = pd.merge(data_p2, data_p10, on=["State / Measuring network","Station code", "Station name", "Station setting", "Station type"], how='inner')

    LoadTest("Airquality")
    LoadTest("Hospital")

if __name__ == "__main__":
    main()