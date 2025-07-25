
# Spotify Data Pipeline (ETL + AWS + Athena + Streamlit)

## 🎯 Project Goal
This project demonstrates building an **end-to-end data pipeline** using:
- **Python (.venv)** for ETL (Extract – Transform – Load)
- **AWS S3 + Athena** for data storage and querying
- **Streamlit + Plotly** for interactive dashboard and visualization

**Business Question:**  
> How has music listening behavior changed over time (by release year clusters), and who are the top artists in each era?

---

## 📂 Project Structure
```
spotify-pipeline/
│
├── aws/
│   └── query_analysis.py        # Query Athena via PyAthena and save results
├── dashboard/
│   └── dashboard.py             # Streamlit dashboard for visualization
├── data/
│   ├── raw/                     # Original Spotify dataset (from Kaggle)
│   └── processed/               # Transformed and aggregated data
├── extract.py                   # Extract raw CSV file
├── transform.py                 # Clean and transform data
├── load.py                      # Load the transformed data into AWS Bucket 
└── README.md
```

---

## 🛠️ Tech Stack
- **Python 3.11** (virtual environment `.venv`)
- **AWS S3** (data lake)
- **AWS Athena** (SQL analytics on S3)
- **PyAthena** (Python integration with Athena)
- **Pandas** (data wrangling)
- **Streamlit** + **Plotly** (dashboard visualization)

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Akari2512/spotify-pipeline.git
cd spotify-pipeline
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure AWS credentials
```bash
aws configure
```

### 5. Run ETL
```bash
python extract.py
python transform.py
python load.py
```

### 6. Upload processed data to S3 and run Athena queries
```bash
python aws/query_analysis.py
```

### 7. Launch Streamlit dashboard
```bash
cd dashboard
streamlit run dashboard.py
```

---

## 📊 Key Features
- **ETL Workflow**:
  - Extract data from CSV (Spotify dataset from Kaggle)
  - Clean and normalize features (e.g., `streams` to integer, percentages to 0–1)
  - Upload processed data to AWS S3
- **Analytics**:
  - Music feature trends (BPM, Valence, Energy, etc.) by release year clusters
  - Top 4 artists per release group based on streaming counts
- **Visualization**:
  - Interactive dashboard built with Streamlit and Plotly

---

## 📈 Results & Insights
1. Music characteristics have evolved, with modern tracks showing higher danceability and energy compared to vintage eras.  
2. Different top artists dominate each release era, illustrating changing audience preferences.  

---

## 🙌 Author
- **Ngo Nguyen Duc Quang (Akari)** – Data Engineer Enthusiast  

---

## 📄 License
This project is licensed under the MIT License.

