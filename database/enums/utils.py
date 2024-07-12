import requests

def get_response_text(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    return ""

def get_response_json(url: str) -> dict:
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return {}

def strip_and_remove_commas(s):
    return s.strip().replace(",", "")

def strip_and_remove_quotes(s):
    return s.strip().replace('"', "")