# tools/csv_tools.py

from server import mcp
from utils.file_reader import read_csv_summary
from utils.csv_funcs import calculate_csv_summary_statistics
@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Summarize a CSV file by reporting its number of rows and columns.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A string describing the file's dimensions.
    """
    return read_csv_summary(filename)

@mcp.tool()
def csv_summary_statistics(filename: str) -> str:
    """
    Calculate the summary statistics for the CSV File using pandas built-in describe method
    Args:
        filename: Name of CSV File in the /data directory
    Returns:
        A summary of the column statistics, errors accounted for.
    """
    return calculate_csv_summary_statistics(filename)