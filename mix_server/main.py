# main.py

from server import mcp

import tools.csv_tools
import tools.parquet_tools

# Entry Point to run the server
if __name__ == "__main__":
    mcp.run()
