# Twitter Geospatial Data Analytics Pipeline

##  Project Overview
This project implements a **batch data processing and analytics pipeline** for large-scale **Twitter geospatial data** (~14.2M tweets).  
The goal is to perform **data cleansing, transformation, feature engineering, temporal & geospatial aggregation**, and **export structured insights** to support downstream analytics/dashboarding.  

The pipeline is built using **AWS Glue (PySpark)** and leverages **S3 for data storage**.  

---

##  Implemented Tasks

### 1. Data Ingestion & Extraction
- Uploaded raw Twitter dataset (ZIP format) into **S3 (raw-data bucket)**.  
- Created Glue job to:
  - Extract the CSV file from the ZIP archive.  
  - Store parsed data into **S3 output bucket**.  

 **Outcome**: Extracted CSV available in S3 for processing.  

---

### 2. Data Storage & Format Standardization
- Converted raw CSV files into **Parquet format** for optimized storage & querying.  
- Stored into **S3 in partitioned format**.  
- Verified schema and structure using **AWS Athena**.  

 **Outcome**: Compact, query-optimized data format (Parquet).  

---

### 3. Feature Engineering
- Normalized **timestamps** to IST/UTC.  
- Extracted new features:
  - `hour_of_day`  
  - `day_of_week`  
  - `is_weekend`  
  - **Geospatial bins** (lat/lon buckets).  
- Implemented reusable utility functions for transformations.  

 **Outcome**: Enriched dataset with engineered features.  

---

### 4. Timezone Mapping
- Implemented **PySpark Glue job** to map **tweet geocoordinates to US timezones** using bounding box logic.  
- Assigned a `timezone` field to each tweet.  

 **Outcome**: Each tweet now tagged with timezone (Eastern, Central, Mountain, Pacific, Other).  

---

### 5. Aggregation by Timezone
- Aggregated **tweet counts by timezone**.  
- Wrote results into **S3 in Parquet format** partitioned by `timezone`.  

 **Outcome**: Ready-to-query aggregated data by timezone.  

---

### 6. Temporal Activity Analysis
- Performed analysis of **temporal tweet activity** across US timezones.  
- Calculated **hourly tweet flow per timezone**.  
- Identified **peak tweet hours** for each timezone.  
- Compared cross-timezone patterns to highlight behavioral differences.  

 **Outcome**: Temporal trends and peak-hour metrics established.  

---

### 7. Structured Aggregation Exports
- Aggregated results into **structured tables** containing:  
  - Top-hour metrics  
  - Tweet counts per timezone, per hour  
- Exported data to **S3 in CSV/Parquet format**.  
- Organized folder structure for **dashboard consumption**.  

 **Outcome**: Clean, pre-aggregated exports available for BI dashboards.  

---

### 8. Glue Job Profiling & Performance Analysis
- Completed **profiling of all Glue jobs** with multiple runs.  
- Generated a consolidated **CSV performance report** containing:  
  - Job Name  
  - Total Runs  
  - Success/Failure Count  
  - Average Execution Time  
  - Total DPU Hours  
  - DPU Hours (Success Runs Only)  

**Highlights**:  
- Profiled **9 Glue jobs**.  
- Identified variability in execution times across jobs.  
- Baseline established for benchmarking & optimization.  

 **Outcome**: Execution profiling report for cost/performance insights.  

---

### 9. Performance Optimization
- Identified inefficiency in **twitter-feature-engineering job** due to redundant `.count()` operations.  
- Fix applied:  
  - Removed intermediate `.count()` calls.  
  - Replaced with a **single `.count()`** at the end.  
  - Used `.limit(10)` sampling for debugging.  
- Verified correctness and **improved runtime**.  
- All other jobs were already efficient.  

 **Outcome**: Optimized job execution without loss of accuracy.  

---

##  Final Deliverables
- **Processed Data in S3**:  
  - Partitioned **Parquet/CSV outputs** for states, hours, and timezones.  
- **Dashboard-Ready Outputs**:  
  - Clean, structured aggregations for direct ingestion.  
- **Performance Profiling Report**:  
  - Consolidated Glue job execution metrics in CSV format.  

---

##  Key Insights
- Tweets mapped to **US timezones** with bounding box geolocation logic.  
- Clear **temporal trends** identified:  
  - Peak tweeting hours vary across Eastern, Central, Mountain, and Pacific timezones.  
- Optimized pipeline ensures **faster execution and reduced costs**.  

---

##  Conclusion
This project successfully:  
- Implemented an **end-to-end PySpark Glue pipeline** for Twitter geospatial data.  
- Delivered **clean, enriched, and aggregated datasets** for downstream analytics.  
- Performed **job profiling & optimization** to ensure scalability and efficiency.  

The pipeline is production-ready and supports future extensions such as **real-time streaming ingestion** and **advanced geospatial clustering**.  
