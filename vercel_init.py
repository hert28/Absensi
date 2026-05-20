import sys
import os
import types

# Create a dynamic 'config' module for Vercel
# This is necessary because config.py is in .gitignore and not uploaded to Vercel
config = types.ModuleType('config')

# Database Configuration (From Vercel Environment Variables)
config.DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'absensi_db'),
    'port': int(os.environ.get('DB_PORT', 3306))
}

# Add SSL requirement for Aiven / cloud databases if needed
if os.environ.get('DB_SSL_MODE') == 'REQUIRED':
    config.DB_CONFIG['ssl_ca'] = '/etc/ssl/certs/ca-certificates.crt' # Default path on Vercel AL2023

# System Configuration
config.DATASET_PATH = os.environ.get('DATASET_PATH', 'dataset')
config.MODEL_PATH = os.environ.get('MODEL_PATH', 'models/trainer.yml')
config.CONFIDENCE_THRESHOLD = int(os.environ.get('CONFIDENCE_THRESHOLD', 70))
config.FOTO_PER_USER = int(os.environ.get('FOTO_PER_USER', 50))
config.CAMERA_INDEX = int(os.environ.get('CAMERA_INDEX', 0))
config.SNAPSHOT_PATH = os.environ.get('SNAPSHOT_PATH', 'snapshots')
config.TOLERANSI_MENIT = int(os.environ.get('TOLERANSI_MENIT', 15))

# Anti-Spoofing Configuration
config.ANTI_SPOOFING_ENABLED = os.environ.get('ANTI_SPOOFING_ENABLED', 'False').lower() == 'true'
config.ANTI_SPOOFING_THRESHOLD = float(os.environ.get('ANTI_SPOOFING_THRESHOLD', 0.5))

# Flask Configuration
config.FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
config.FLASK_PORT = int(os.environ.get('FLASK_PORT', 5000))
config.FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
config.FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key_for_vercel')

# ESP32 Configuration
config.ESP32_ENABLED = os.environ.get('ESP32_ENABLED', 'False').lower() == 'true'
config.ESP32_IP = os.environ.get('ESP32_IP', '192.168.1.100')
config.ESP32_PORT = int(os.environ.get('ESP32_PORT', 80))
config.ESP32_TIMEOUT = int(os.environ.get('ESP32_TIMEOUT', 3))

# Inject into sys.modules
sys.modules['config'] = config

# Now import the Flask app
from app import app
