import requests
import json
import random
import time

SPLUNK_URL = "https://splunk.siem.com:8088/services/collector"
SPLUNK_TOKEN = "YOUR_SPLUNK_HEC_TOKEN"

def generate_log():
    actions = ["login", "logout", "file_upload", "file_download", "data_query"]
    statuses = ["success", "failure", "timeout"]
    users = ["user1", "user2", "user3", "admin", "guest"]
    hosts = ["web-server-01", "web-server-02", "api-server-01", "db-server"]

    return {
        "event": {
            "action": random.choice(actions),
            "status": random.choice(statuses),
            "user": random.choice(users),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "host": random.choice(hosts),
        "sourcetype": "dummy_logs",
        "index": "main",
    }

def send_to_splunk(log):
    headers = {
        "Authorization": f"Splunk {SPLUNK_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(SPLUNK_URL, headers=headers, data=json.dumps(log), verify=False)
    if response.status_code != 200:
        print(f"Failed to send log: {response.text}")
    else:
        print("Log sent successfully")

if __name__ == "__main__":
    for i in range(1000):
        log = generate_log()
        send_to_splunk(log)
        time.sleep(0.01)  
    print("All logs sent!")
