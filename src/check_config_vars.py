import os
from pathlib import Path

from utils import Config

BASE_DIR = Path(__file__).resolve(strict=True).parent

CONFIG_FILE = os.path.join(BASE_DIR, '..', 'config.yml')
config = Config(CONFIG_FILE)

config.get('DB_NAME', raise_error=True)
config.get('DB_PASSWORD', raise_error=True)
