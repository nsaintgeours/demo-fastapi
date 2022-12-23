import json
from pathlib import Path

import requests

sample_json = Path(__file__).parent.parent / "data" / "example.json"
with open(sample_json, 'r') as f:
    sample_json = json.load(f)

response = requests.post(
    url='http://localhost:80/api/v0/run',
    json=sample_json,
    params=dict(some_param=0.6)
)
print(response.json())
