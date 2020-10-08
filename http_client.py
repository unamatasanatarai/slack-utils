import requests
import json
import slack

def get(endpoint, params):
    return requests.get(
        _build_url(endpoint),
        params=params,
        headers=_build_headers(slack.api_token),
        verify=True
    ).json()

def post(endpoint, data):
    return requests.post(
        _build_url(endpoint),
        data=_build_post_data(data),
        headers=_build_headers(slack.api_token),
        verify=True
    ).json()

def _build_headers(token):
    return {
        "Content-type": "application/json; charset=utf-8",
        'Authorization': f"Bearer {token}"
    }

def _build_url(endpoint):
    return f"{slack.api_base_url}/{endpoint}"

def _build_post_data(params):
    return json.dumps(params).encode("utf-8")

