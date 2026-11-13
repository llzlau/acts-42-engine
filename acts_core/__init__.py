"""
ACTS 4.2 High-Performance Core Quantitative Engine
Precompiled Native Binary Interface
"""

from .engine import run_domestic_simulation, scan_market_signals, load_domestic_data

__all__ = ["run_domestic_simulation", "scan_market_signals", "load_domestic_data"]
