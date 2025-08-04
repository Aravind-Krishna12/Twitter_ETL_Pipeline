import os

# ==========================
# Project Paths & Constants
# ==========================

# Base project directory (automatically detected)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Local data directories
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_ZIP_PATH = os.path.join(DATA_DIR, "geotweets.zip")
EXTRACTED_CSV_PATH = os.path.join(DATA_DIR, "geotweets.csv")
PARQUET_LOCAL_PATH = os.path.join(DATA_DIR, "parquet_output")

# ==========================
# AWS Configuration
# ==========================

AWS_REGION = "us-east-1"

# S3 Buckets
S3_RAW_BUCKET = "twitter-etl-raw"
S3_STAGING_BUCKET = "twitter-etl-staging"
S3_OUTPUT_BUCKET = "twitter-etl-output"

# S3 Paths
S3_PARQUET_PATH = f"s3://{S3_OUTPUT_BUCKET}/parquet/"
S3_CSV_PATH = f"s3://{S3_RAW_BUCKET}/geotweets.csv"

# ==========================
# Spark Configuration
# ==========================

SPARK_APP_NAME = "TwitterGeospatialETL"
SPARK_DRIVER_MEMORY = "4g"
SPARK_EXECUTOR_MEMORY = "4g"

# ==========================
# EMR / Glue (Optional IDs)
# ==========================

# These can be filled in later if needed
EMR_CLUSTER_ID = ""
GLUE_JOB_NAME = ""
