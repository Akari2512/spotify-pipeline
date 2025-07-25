import pandas as pd
from pathlib import Path

RAW_PATH = Path('data/raw/spotify-2023.csv')

def load_raw_data (path: Path = RAW_PATH) -> pd.DataFrame:
    """
    Load raw Spotify dataset from CSV.

    Args:
        path (PATH): path to the CSV file.

    Returns:
        pd.DataFrame: Raw data as DataFrame.
    """

    if not path.exists():
        raise FileNotFoundError (f'File not found: {path.resolve()}')
    
    df = pd.read_csv(path, encoding='latin1')
    print(f'Loaded data from: {path}')
    print(f'Rows: {df.shape[0]}, Columns: {df.shape[1]}')
    print(f'Columns: {df.columns.to_list()}')


    return df

if __name__ == '__main__':
    df = load_raw_data()
    print(df.head(5)) 
    print(df.info())
    print(df.isnull().sum())