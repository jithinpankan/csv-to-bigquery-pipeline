# GCP Data Pipeline: CSV to BigQuery using Cloud Functions & Composer

This project demonstrates a serverless data pipeline on Google Cloud that ingests CSV files from a Cloud Storage bucket and loads them into BigQuery on a schedule using Cloud Composer (Apache Airflow).

## 🛠 Tools Used
- Google Cloud Storage (GCS)
- Google BigQuery
- Cloud Functions (Python)
- Cloud Composer (Airflow)
- Terraform (IaC)

## 📁 Project Structure
csv-to-bigquery-pipeline/
├── dags/
│ └── gcs_to_bigquery_dag.py
├── cloud_function/
│ └── main.py
├── terraform/
│ ├── main.tf
│ └── variables.tf
├── data/
│ └── sample_sales.csv
└── requirements.txt

## ⚙️ How It Works
1. CSV is uploaded to GCS bucket.
2. Cloud Function triggers and starts an Airflow DAG.
3. DAG loads CSV into BigQuery table.
4. Terraform provisions all required GCP resources.

## 🧪 Sample Data
```csv
order_id,customer_name,amount
1,John Doe,100
2,Jane Smith,250
🚀 Deployment Steps
Deploy infrastructure with Terraform
Upload CSV to GCS
Monitor DAG execution via Airflow UI
📈 Use Case
Ideal for clients who want to automate ingestion of batch data into cloud-based data warehouses.
