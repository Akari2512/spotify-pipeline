import pandas as pd
from pathlib import Path
from extract import load_raw_data

RAW_PATH = Path('data/raw/spotify-2023.csv')
PROCESSED_PATH = Path('data/processed/spotify-2023-cleaned.csv')

def normalize_columns_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("%", "percent")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
    )
    return df

def convert_percentage_columns(df: pd.DataFrame) -> pd.DataFrame:
    percent_cols = [col for col in df.columns if col.endswith('percent')]
    for col in percent_cols:
        df[col] = df[col] / 100
        new_cols = col.replace('_percent', '')
        df.rename(columns={col: new_cols}, inplace=True)
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print(f'Before the transformation: {df.shape[0]} rows')

    in_cols = [col for col in df.columns if col.lower().startswith('in_')]
    df = df.drop(columns=in_cols)

    drop_cols = ['key', 'mode']
    df = df.drop(columns=[col for col in drop_cols if col in df.columns])

    df = normalize_columns_names(df)

    if 'streams' in df.columns:
        df = df[df["streams"].astype(str).str.isnumeric()]
        df["streams"] = df["streams"].astype(int)


    df = convert_percentage_columns(df)

    print(f'After the transformation: {df.shape[1]} columns')
    return df

def save_cleaned_data(df: pd.DataFrame, output_path = PROCESSED_PATH):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f'Cleaned data saved to: {output_path.resolve()}')

if __name__ == "__main__":
    df_raw = load_raw_data(RAW_PATH)
    df_clean = transform_data(df_raw)
    save_cleaned_data(df_clean)