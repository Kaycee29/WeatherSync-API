#  WeatherSync API - Automated Weather Data for Lagos

This data engineering project automates the process of collecting real-time weather data for **Lagos State, Nigeria**, using  data platform tools like **Airflow**, **Docker**, **Terraform**, and ** data lake whcich is AWS S3**.

It connects to  a weather websites (https://www.weatherbit.io/) API, extracts current weather data for Lagos, and stores it in a cloud bucket — all automated, no checking, saving you lot of productive time.

---

## What Does it do?

- This fetches Lagos weather data using the **Weatherbit API**
- Schedules and automates the job using **Apache Airflow**
- Runs everything in containers via **Docker**
- Provisions an **S3 bucket** using **Terraform**
- Uploads the weather data to the S3 bucket for easy access and reuse

---

##  Tools Used

- **Airflow** – for task scheduling  
- **Docker** – to containerize the pipeline  
- **Terraform** – to set up the AWS S3 bucket  
- **AWS S3** – to store the weather data  
- **Python** – to extract and process the API data

---
Why I Built This

To practice building a real-world, automated data pipeline that fetches external data and stores it in the cloud. It’s fast, reusable, and built with production-grade tools.


