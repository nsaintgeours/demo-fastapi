"""
Starts the REST API service and defines API endpoints
"""

import json
import logging
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Body, Query

from src.dataclasses import InputData, OutputData
from src.engine import Engine

# Load default parameters from .env file
load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

# Set log level
logging.basicConfig(level=os.getenv('LOG_LEVEL'))

# Create data processing engine
engine = Engine()

# Start REST API service
app = FastAPI(
    title="Demo FastAPI",
    description="A very basic REST API implemented with Python and FastAPI library",
    version="0.0.1",
    contact={"name": "Nathalie Saint-Geours", "email": "nathalie.saint-geours@m4x.org"},
    license_info={"name": "Apache 2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0.html"}
)

# Load example data
sample_json = Path(__file__).parent.parent / "data" / "example.json"
with open(sample_json) as file:
    sample_data = json.load(file)


# Serve data processing engine through REST API endpoint
@app.post('/api/v0/run', response_model=OutputData, tags=["My REST API"])
def run(
        data: InputData =
        Body(..., description='Input data passed as request JSON body.', example=sample_data),

        some_param: Optional[float] =
        Query(description='Some data processing parameter', ge=0, le=1, default=0.0),

) -> OutputData:
    query_params = locals()
    data = query_params.pop('data')
    return engine.run(data=data, **query_params)
