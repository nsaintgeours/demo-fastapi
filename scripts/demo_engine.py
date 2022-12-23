"""
Script that runs the data processing engine on some sample data.
"""

import logging
from pathlib import Path

from src.dataclasses import InputData
from src.engine import Engine


def run_demo():
    sample_json = Path(__file__).parent.parent / "data" / "example.json"
    engine = Engine()
    output_data = engine.run(data=InputData.parse_file(path=sample_json))
    print(output_data)


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    run_demo()
