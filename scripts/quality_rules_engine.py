import pandas as pd, sqlalchemy
import smtplib

# Configuration
RULE_FILE = "templates/quality_rules.xlsx"
DB_CONN = "postgresql://username:password@your-rds-endpoint:5432/yourdb"

def send_alert(msg):
    # Simple print alert; replace with email/Slack integration
    print("ALERT:", msg)

if __name__ == "__main__":
    rules = pd.read_excel(RULE_FILE)
    engine = sqlalchemy.create_engine(DB_CONN)
    for _, r in rules.iterrows():
        df = pd.read_sql(f"SELECT {r.Column} FROM {r.Asset}", engine)
        null_rate = df[r.Column].isnull().mean()
        if null_rate > r.Threshold:
            send_alert(f"Quality rule violated on {r.Asset}.{r.Column}: null_rate={null_rate}")