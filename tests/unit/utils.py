# utils.py
import logging
import os
from datetime import datetime
import json
from typing import List, Dict
from pytz import timezone

# Configuration
CONFIG_PATH = 'config.json'
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

def load_config() -> Dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)

def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
    return logging.getLogger(name)

def get_timezone(timezone_name: str) -> timezone:
    return timezone(timezone_name)

def get_current_utc_timestamp() -> float:
    return datetime.now(get_timezone('UTC')).timestamp()

def get_current_timezone_timestamp(timezone_name: str) -> float:
    return datetime.now(get_timezone(timezone_name)).timestamp()

def is_configured() -> bool:
    return os.path.exists(CONFIG_PATH)