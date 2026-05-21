# config.py — Konfigurasi aplikasi dari Environment Variables
# File ini aman untuk di-commit ke GitHub karena tidak berisi password
# Semua nilai sensitif diambil dari Environment Variables

import os

# === KONFIGURASI DATABASE ===
# Nilai diambil dari Environment Variables Railway/Vercel
DB_CONFIG = {
    'host'    : os.environ.get('DB_HOST', 'localhost'),
    'port'    : int(os.environ.get('DB_PORT', 3306)),
    'user'    : os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'absensi_db'),
}

# Tambahkan SSL jika diperlukan (Aiven membutuhkan SSL)
if os.environ.get('DB_SSL_MODE') == 'REQUIRED':
    DB_CONFIG['ssl_ca'] = '/etc/ssl/certs/ca-certificates.crt'

# === KONFIGURASI SISTEM ===
DATASET_PATH         = os.environ.get('DATASET_PATH', 'dataset')
MODEL_PATH           = os.environ.get('MODEL_PATH', 'models/trainer.yml')
CONFIDENCE_THRESHOLD = int(os.environ.get('CONFIDENCE_THRESHOLD', 95))
FOTO_PER_USER        = int(os.environ.get('FOTO_PER_USER', 50))
CAMERA_INDEX         = int(os.environ.get('CAMERA_INDEX', 0))
SNAPSHOT_PATH        = os.environ.get('SNAPSHOT_PATH', 'snapshots')
TOLERANSI_MENIT      = int(os.environ.get('TOLERANSI_MENIT', 15))

# === KONFIGURASI ANTI-SPOOFING ===
ANTI_SPOOFING_ENABLED   = os.environ.get('ANTI_SPOOFING_ENABLED', 'False').lower() == 'true'
ANTI_SPOOFING_THRESHOLD = float(os.environ.get('ANTI_SPOOFING_THRESHOLD', 0.5))

# === KONFIGURASI FLASK ===
FLASK_HOST       = os.environ.get('FLASK_HOST', '0.0.0.0')
FLASK_PORT       = int(os.environ.get('PORT', os.environ.get('FLASK_PORT', 5000)))
FLASK_DEBUG      = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'ganti_ini_dengan_kunci_rahasia_anda')

# === KONFIGURASI ESP32 ===
ESP32_ENABLED = os.environ.get('ESP32_ENABLED', 'False').lower() == 'true'
ESP32_IP      = os.environ.get('ESP32_IP', '192.168.1.100')
ESP32_PORT    = int(os.environ.get('ESP32_PORT', 80))
ESP32_TIMEOUT = int(os.environ.get('ESP32_TIMEOUT', 3))