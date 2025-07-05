# utils/csv_funcs.py

import pandas as pd
import numpy as np
from pathlib import Path
from utils import file_reader
import os

def calculate_csv_summary_statistics(filename: str) -> str:
    """
    Calculate summary statistics for numeric columns in a CSV file.
    
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
        
    Returns:
        A string containing summary statistics (count, mean, std, min, max, quartiles)
        for all numeric columns in the CSV file.
    """
    try:
        # Construct the full file path
        DATA_DIR = Path(__file__).resolve().parent.parent / "data"
        file_path = DATA_DIR / filename
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Get summary statistics for numeric columns only
        numeric_stats = df.describe()
        
        # Format the output as a readable string
        if numeric_stats.empty:
            return f"No numeric columns found in {filename}"
        
        result = f"Summary Statistics for {filename}:\n"
        result += "=" * 50 + "\n"
        result += str(numeric_stats)
        
        # Add additional information
        result += f"\n\nAdditional Information:\n"
        result += f"Total rows: {len(df)}\n"
        result += f"Total columns: {len(df.columns)}\n"
        result += f"Numeric columns: {len(numeric_stats.columns)}\n"
        result += f"Non-numeric columns: {len(df.columns) - len(numeric_stats.columns)}\n"
        
        # List column names and their data types
        result += f"\nColumn Data Types:\n"
        for col, dtype in df.dtypes.items():
            result += f"  {col}: {dtype}\n"
        
        return result
        
    except FileNotFoundError:
        return f"Error: File '{filename}' not found in /data directory"
    except pd.errors.EmptyDataError:
        return f"Error: File '{filename}' is empty"
    except Exception as e:
        return f"Error processing file '{filename}': {str(e)}"
