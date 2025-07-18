# app/utils/burp_client.py

import requests
import logging

BURP_API_URL = "http://127.0.0.1:1337/v1"
API_KEY = "your_api_key_here"  # ניתן לטעון מקובץ .env או config בעתיד

HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

def list_projects():
    try:
        res = requests.get(f"{BURP_API_URL}/projects", headers=HEADERS)
        return res.json()
    except Exception as e:
        logging.error(f"[BurpClient] Failed to list projects: {e}")
        return None

def start_scan(target_url: str, config_name: str = "Passive audit"):
    payload = {
        "scan_configurations": [{"name": config_name}],
        "urls": [target_url]
    }
    try:
        res = requests.post(f"{BURP_API_URL}/scan", headers=HEADERS, json=payload)
        return res.json()
    except Exception as e:
        logging.error(f"[BurpClient] Failed to start scan: {e}")
        return None

def get_scan_status(scan_id: str):
    try:
        res = requests.get(f"{BURP_API_URL}/scan/{scan_id}", headers=HEADERS)
        return res.json()
    except Exception as e:
        logging.error(f"[BurpClient] Failed to get scan status: {e}")
        return None

def get_issues(scan_id: str):
    try:
        res = requests.get(f"{BURP_API_URL}/scan/{scan_id}/issues", headers=HEADERS)
        return res.json()
    except Exception as e:
        logging.error(f"[BurpClient] Failed to get issues: {e}")
        return None
