from slack_sdk import WebClient

SLACK_TOKEN = "<your-slack-token>"
client = WebClient(token=SLACK_TOKEN)

def notify_request(user, asset, level):
    client.chat_postMessage(
        channel="#data-requests",
        text=f"{user} requests {level} on {asset}"
    )

if __name__ == "__main__":
    notify_request("alice", "sales_bucket@aws", "Read")