import requests
import pandas as pd
import os
import boto3
import awswrangler as wr
from airflow.models import Variable
from datetime import datetime


def extract_api():
    
    api_key = Variable.get('API_KEY')

    url =f'https://api.weatherbit.io/v2.0/current?lat=6.1858825&lon=6.7297071&key={api_key}'

    response =  requests.get(url)
    if response.status_code == 200:
       data = response.json()['data']
       df = pd.json_normalize(data)
       session = boto3.Session(
            aws_access_key_id= Variable.get('access_key'),
            aws_secret_access_key= Variable.get('secret_key'),
            region_name= Variable.get('region')
        )
       date_str = datetime.today().strftime('%Y-%m-%d')       
       path_s3 = f's3://weather-api-kaycee2025/weatherchecking/weather-{date_str}.parquet'   
       wr.s3.to_parquet(
            df=df,
            path=path_s3,
            dataset=False,
            #mode='append',
            boto3_session=session
        )
       return df
    else:
        print('unable to fetch data')
extract_api()

