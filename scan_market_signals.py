"""
================================================================================
ACTS 4.2 Multi-Asset Real-Time Radar Scanner
Powered by Native C-Extension Engine
================================================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from acts_core import scan_market_signals

if __name__ == "__main__":
    print("[INIT] Launching ACTS 4.2 Real-Time Radar Scanner...")
    data_dir = BASE_DIR / "data" / "raw"
    radar = scan_market_signals(data_dir=data_dir)
