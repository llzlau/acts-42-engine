"""
================================================================================
ACTS 4.2 Multi-Asset Commodity 21.8-Year Simulation Runner
Powered by Native C-Extension Engine
================================================================================
"""

import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from acts_core import run_domestic_simulation

if __name__ == "__main__":
    print("[INIT] Launching ACTS 4.2 High-Performance Native Core Engine...")
    data_dir = BASE_DIR / "data" / "raw"
    results = run_domestic_simulation(data_dir=data_dir, initial_nav=500000.0)
    print("\n[SUCCESS] 21.8-Year Historical Simulation Completed Successfully.")
