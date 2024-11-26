import requests
import random
import time
import json

splunk_url = "https://localhost:8088/services/collector"
splunk_token = "3b1dfa5b-b0bc-4d08-ad67-1b0922ec1c9a"

def generate_random_event():
    actions = ["login", "logout", "file_upload", "file_download", "data_query"]
    statuses = ["success", "failure", "timeout"]
    users = ["user1", "user2", "user3", "user4", "admin"]
    hosts = ["web-server-01", "web-server-02", "api-server-01", "db-server"]

    return {
        "event": {
            "action": random.choice(actions),
            "status": random.choice(statuses),
            "user": random.choice(users),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "sourcetype": "access_log",
        "host": random.choice(hosts),
        "index": "main"
    }

def send_to_splunk(data):
    headers = {
        "Authorization": f"Splunk {splunk_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(splunk_url, headers=headers, data=json.dumps(data), verify=False)
        if response.status_code == 200:
            print(f"Success: {response.text}")
        else:
            print(f"Failed: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        while True:
            event = generate_random_event()
            print(f"Sending event: {event}")
            send_to_splunk(event)
            time.sleep(random.uniform(1, 5))
    except KeyboardInterrupt:
        print("Stopped sending events.")