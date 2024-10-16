import pandas as pd
import requests
import time

def delete_workspace(api_key, workspace_id, retries=3, delay=5):
    url = f"https://api.getpostman.com/workspaces/{workspace_id}"
    headers = {'x-api-key': api_key}
    
    print(f"Workspace deletion starting.")

    for attempt in range(retries):
        response = requests.delete(url, headers=headers)
        
        if response.status_code == 200:
            return True
        else:
            print(f"Attempt {attempt + 1} failed to delete workspace {workspace_id}. Status code: {response.status_code}, Response: {response.text}")
            if attempt < retries - 1:
                print(f"Retrying after {delay} seconds...")
                time.sleep(delay)  # Wait before retrying
                
    print(f"Workspace {workspace_id} deletion failed after {retries} attempts.")
    return False

def delete_workspaces_from_excel(api_key, excel_file_path, retries=3, delay=5):
    df = pd.read_excel(excel_file_path)
    
    if 'destinationId' not in df.columns:
        raise ValueError("The Excel file must contain a 'destinationId' column.")
    
    failed_workspaces = []  # List to track workspaces that failed deletion
    
    for index, row in df.iterrows():
        workspace_id = row['destinationId']
        success = delete_workspace(api_key, workspace_id, retries=retries, delay=delay)
        
        if not success:
            failed_workspaces.append(workspace_id)
    
    if failed_workspaces:
        print("The following workspace IDs failed deletion after all retries:")
        for workspace_id in failed_workspaces:
            print(workspace_id)
    else:
        print("All workspaces deleted successfully.")

if __name__ == "__main__":
    api_key = "apikey"  # Postman API key goes here
    excel_file_path = "WorkspaceDeleteTestdata.xlsx"
    delete_workspaces_from_excel(api_key, excel_file_path)