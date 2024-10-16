# Postman Workspace Deletion Script

This script is designed to **delete multiple Postman workspaces** using the Postman API and supports retries for any deletion attempts that fail. The workspace IDs are read from an Excel file, and any workspaces that fail to be deleted after all retry attempts are logged and displayed in the console.

## Requirements

- **Python 3.x**
- The following Python packages must be installed:
  - `pandas`
  - `requests`
  - `openpyxl` (required for reading `.xlsx` files with `pandas`)

## Setup Instructions

### 1. Install Required Libraries

You can install the required Python libraries using pip:```bash
pip install pandas requests openpyxl

### 2. Get Your Postman API Key

To delete workspaces via the Postman API, you need your Postman API key. Follow these steps to get the key:

1. Go to your Postman User Settings > API Keys
2. Click **Generate API Key** to create a new key.
3. Give your API key a name for future reference.
4. Click **Create Key** and then copy the key for use in the script.

### 3. Prepare Your Excel File

The script reads workspace IDs from an Excel file. Make sure your file contains a column named `destinationId` with the Postman workspace IDs you want to delete.

Example file structure (`WorkspaceDeleteTestdata.xlsx`):

| destinationId       |
|---------------------|
| f4d3b5e0-1234-5678  |
| a3f3f5c0-9876-5432  |
| ...                 |

### 4. Configure the Script

In the `delete_workspaces_from_excel` function, update the following parameters:

1. **API Key**: Replace `"apikey"` in the script with your actual Postman API key.

   ```python
   api_key = "your-postman-api-key-here"
   ```

2. **Excel File Path**: Update the `excel_file_path` variable with the path to your Excel file containing the workspace IDs.

   ```python
   excel_file_path = "WorkspaceDeleteTestdata.xlsx"
   ```

You can also adjust the retry behavior:

- **Retries**: The number of times the script will attempt to delete a workspace before giving up (default is 3).
- **Delay**: The time (in seconds) between retries (default is 5 seconds).

### 5. Run the Script

Once you have configured the API key and Excel file, run the script.