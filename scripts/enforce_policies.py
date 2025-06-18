import pandas as pd

# Configuration
POLICY_FILE = "templates/data_access_policies.xlsx"

def grant_access(asset, roles, level):
    # Implement your access grant logic here (IAM, DB GRANT, etc.)
    print(f"Granting {level} to {roles} on {asset}")

if __name__ == "__main__":
    policies = pd.read_excel(POLICY_FILE)
    for _, row in policies.iterrows():
        grant_access(asset=row['Asset Qualified Name'],
                     roles=row['Allowed Roles'].split(','),
                     level=row['Access Level'])