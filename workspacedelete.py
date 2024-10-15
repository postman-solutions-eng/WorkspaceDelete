import pandas as pd
import requests

def delete_workspace(api_key, workspace_id):
    url = f"https://api.getpostman.com/workspaces/{workspace_id}"
    headers = {'x-api-key': api_key}
    
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 200:
        print(f"Workspace {workspace_id} deleted successfully.")
    else:
        print(f"Failed to delete workspace {workspace_id}. Status code: {response.status_code}, Response: {response.text}")

def delete_workspaces_from_excel(api_key, excel_file_path):
    df = pd.read_excel(excel_file_path)
    
    if 'destinationId' not in df.columns:
        raise ValueError("The Excel file must contain a 'destinationId' column.")
    
    for index, row in df.iterrows():
        workspace_id = row['destinationId']
        delete_workspace(api_key, workspace_id)

if __name__ == "__main__":
    api_key = "apikey"  # Postman API key goes here
    excel_file_path = "WorkspaceDeleteTestdata.xlsx"
    delete_workspaces_from_excel(api_key, excel_file_path)
