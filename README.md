# Splunk Playground by PentestSage

This repository provides a Splunk Playground environment for testing log ingestion, forwarding, and integration with Splunk's HTTP Event Collector (HEC).

## Features
- Configured with a nginx simple container forward logs to Splunk.
- Docker Compose setup for integrating with Splunk seamlessly.
- Example scripts for testing log ingestion using HEC.

---

## Prerequisites
1. **Docker** and **Docker Compose** installed on your system.
2. A running Splunk instance with **HTTP Event Collector (HEC)** enabled.
   - Example Splunk URL: `http://splunk.siem.com:8000`
3. Access to a valid HEC token.

---

## Setup Guide

### 1. Clone the Repository
```bash
git clone [https://github.com/your-repo/splunk-playground](https://github.com/zenzue/splunklearning).git
cd splunklearning
```
enter splunk folder and run
```
docker-compose up --build
```

### 2. Create and Enable HEC Token
To enable the HTTP Event Collector (HEC) in Splunk:
1. Log into your Splunk instance at `http://splunk.siem.com:8000`.
2. Navigate to **Settings** > **Data Inputs** > **HTTP Event Collector**.
3. Click on **New Token** and configure:
   - **Name**: `Splunk Playground HEC`
   - **Source Type**: `_json`
   - **Default Index**: `main`
4. Enable the HEC and note down the generated token.

---

### 3. Update Configuration Files

#### Update `.env`
Replace `<YOUR_SPLUNK_URL>` and `<YOUR_SPLUNK_TOKEN>` with your Splunk URL and HEC token:
```env
SPLUNK_URL=https://splunk.siem.com
SPLUNK_TOKEN=<YOUR_SPLUNK_TOKEN>
```

#### Update `docker-compose.yml`
Ensure the `splunk-url` in the `logging` configuration points to your Splunk HEC endpoint:
```yaml
logging:
  driver: splunk
  options:
    splunk-token: "${SPLUNK_TOKEN}"
    splunk-url: "${SPLUNK_URL}/services/collector"
    splunk-sourcetype: "host_logs"
    splunk-insecureskipverify: "true"
```

---

## Usage

### 1. Start the Nginx
enter nginx folder and 
```bash
docker-compose up --build
```

### 2. Send Test Data to Splunk
Use the provided `send.py` to send test data:
1. Update the Splunk URL and token in `test_script.py`:
   ```python
   SPLUNK_URL = "https://splunk.siem.com:8088/services/collector"
   SPLUNK_TOKEN = "<YOUR_SPLUNK_TOKEN>"
   ```
2. Run the script:
   ```bash
   python3 send.py
   ```

---

## Verify in Splunk
1. Log into Splunk.
2. Run the following search query:
   ```spl
   index=main sourcetype="host_logs"
   ```
3. Verify the ingested logs.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.
