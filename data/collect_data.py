import wget
import os
import zipfile
import pandas as pd

df_total = pd.DataFrame()

for i in range(2020,2021):
    for j in range(1,13):
        try:
            try:
                url = f'https://s3.amazonaws.com/tripdata/{i}{j:02d}-citibike-tripdata.csv.zip'
                print(url)
                wget.download(url, f'{i}{j:02d}-citibike-tripdata.csv.zip')
                with zipfile.ZipFile(f'{i}{j:02d}-citibike-tripdata.csv.zip', 'r') as zip_ref:
                    zip_ref.extractall()
                os.remove(f'{i}{j:02d}-citibike-tripdata.csv.zip')
                try:
                    df_total = pd. concat([df_total, pd.read_csv(f"{i}{j}-citibike-tripdata.csv")])
                except:
                    try:
                        df_total = pd. concat([df_total, pd.read_csv(f"{i}{j:02d} citibike-tripdata.csv")])
                    except:
                        df_total = pd. concat([df_total, pd.read_csv(f"{i}{j:02d}-citibike-tripdata.csv")])
            except:
                url = f'https://s3.amazonaws.com/tripdata/{i}{j:02d} citibike-tripdata.csv.zip'
                print(url)
                wget.download(url, f'{i}{j:02d}-citibike-tripdata.csv.zip')
                with zipfile.ZipFile(f'{i}{j:02d}-citibike-tripdata.csv.zip', 'r') as zip_ref:
                    zip_ref.extractall()
                os.remove(f'{i}{j:02d}-citibike-tripdata.csv.zip')
                try:
                    df_total = pd. concat([df_total, pd.read_csv(f"{i}{j}-citibike-tripdata.csv")])
                except:
                    try:
                        df_total = pd. concat([df_total, pd.read_csv(f"{i}{j:02d} citibike-tripdata.csv")])
                    except:
                        df_total = pd. concat([df_total, pd.read_csv(f"{i}{j:02d}-citibike-tripdata.csv")])
        except:
            pass
df_total.to_csv("total_data.csv")

