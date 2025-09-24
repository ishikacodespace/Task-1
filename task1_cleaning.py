import pandas as pd
def clean_netflix_data(file_path):
    """
    Loads, cleans, and saves the Netflix dataset.
    
    Steps:
    - Fill missing values
    - Remove duplicates
    - Standardize text columns
    - Convert date_added to datetime
    - Clean column names
    - Convert numeric columns
    - Save cleaned dataset
    """
    # Load dataset
    df = pd.read_csv(file_path)
    print("Initial dataset info:")
    print(df.info())
    
    # Fill missing values
    fill_cols = ['director', 'cast', 'country', 'date_added', 'rating', 'duration']
    for col in fill_cols:
        df[col] = df[col].fillna("Unknown")
    
    print("\nMissing values after filling:")
    print(df.isnull().sum())
    
    # Remove duplicates
    duplicates = df.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicates}")
    df = df.drop_duplicates()
    
    # Standardize text columns
    text_cols = ['type', 'rating', 'country', 'cast', 'director']
    for col in text_cols:
        df[col] = df[col].str.strip().str.lower()
    
    # Convert date_added to datetime
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    
    # Clean column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    
    # Convert numeric columns
    df['release_year'] = df['release_year'].astype(int)
    
    # Optional: Extract numeric duration for analysis
    df['duration_num'] = df['duration'].str.extract('(\d+)').astype(float)
    
    # Save cleaned dataset
    df.to_csv("cleaned_netflix_dataset.csv", index=False)
    print("\nCleaned dataset saved as 'cleaned_netflix_dataset.csv'")
    
    return df

# Run the cleaning function
df_cleaned = clean_netflix_data("netflix_titles.csv")
print(df_cleaned.head())
