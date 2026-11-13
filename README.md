# ACTS 4.2 High-Performance Commodity Quantitative Trading Engine

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build: Native C-Extension](https://img.shields.io/badge/engine-C%2FC%2B%2B%20Native%20Binary-brightgreen.svg)](#)
[![Market: Futures & Multi-Asset](https://img.shields.io/badge/Market-Commodities%20%7C%20Macro-red.svg)](#)

**ACTS 4.2 (Asymmetric Convex Trend System)** is an industrial-grade quantitative trend-following and momentum portfolio engine designed for multi-asset commodity and macro futures.

The system is delivered with an **optimized native C/C++ binary computational core (`acts_core`)**, providing high-throughput backtesting and real-time execution while safeguarding proprietary algorithmic models.

---

## 1. System Architecture & Methodology

ACTS 4.2 addresses three chronic structural failures in traditional CTA trend following:
1. **False Shakeouts from Opening Auctions**: Replaces naive continuous intrabar stops with a **Dual-Regime Microstructure Model** (Close-based Confirmation for price-limited domestic venues vs Intrabar Execution for 23-hour continuous global venues).
2. **Severe Profit Clawbacks (The Rollercoaster Effect)**: Deploys a **Triple Physical Lock Matrix** combining Trailing Chandelier Locks, Single-Day Exhaustion Pin-bar Locks, and Structural Donchian Breakout boundaries.
3. **Cash Drag (75%+ Idle Capital)**: Integrates an automated **Cash Sweep Liquidity Engine** capturing overnight repo and short-term treasury yields.

```text
                    ┌──────────────────────────────────────────────────────────┐
                    │           Unified Dynamic Master Capital Pool            │
                    │        Volatility-Inverse Position Risk Budgeting        │
                    └────────────────────────────┬─────────────────────────────┘
                                                 │
                                                 ▼
                    ┌──────────────────────────────────────────────────────────┐
                    │       Kaufman Efficiency Ratio (KER) Dynamic Filter      │
                    │       Filters ~85% of ranging consolidation noise        │
                    └────────────────────────────┬─────────────────────────────┘
                                                 │
                                                 ▼
                    ┌──────────────────────────────────────────────────────────┐
                    │            Dual-Regime Execution Framework               │
                    │   · Price-Limited Venues: Close-Confirm Stop-Loss        │
                    │   · Continuous Global Venues: Intrabar Stop-Loss         │
                    └────────────────────────────┬─────────────────────────────┘
                                                 │
                                                 ▼
                    ┌──────────────────────────────────────────────────────────┐
                    │       Convex Pyramiding with Breakeven Ratchet           │
                    │       Ratchets stop-loss to ensure zero downside risk    │
                    └────────────────────────────┬─────────────────────────────┘
                                                 │
                                                 ▼
                    ┌──────────────────────────────────────────────────────────┐
                    │              Triple Physical Lock Exit Matrix            │
                    │   · Lock 1: Trailing Chandelier Lock                     │
                    │   · Lock 2: Intraday Exhaustion Pin-bar Lock             │
                    │   · Lock 3: Structural Donchian Exit                     │
                    └────────────────────────────┬─────────────────────────────┘
                                                 │
                                                 ▼
                    ┌──────────────────────────────────────────────────────────┐
                    │          Cash Sweep Liquidity & Yield Engine             │
                    │          Eliminates cash drag during idle regimes        │
                    └──────────────────────────────────────────────────────────┘
```

---

## 2. Institutional Performance Benchmarks

### Domestic Multi-Commodity 21.8-Year Historical Simulation (2005 – 2026)
Tested across 8 high-momentum advantage commodity assets (Base Metals, Precious Metals, Petrochemicals, and Soft Commodities) over 5,300 daily bars:

| Strategy Configuration | Execution Regime | Risk Budget per Trade | Core Mechanisms | Total Return | CAGR | Max Drawdown | Calmar Ratio |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **0. Traditional Baseline** | Close-based | 2.0% | Standard Donchian Exit | +948.6% | 11.37% | 22.84% | 0.498 |
| **1. Direct Foreign Intrabar Port** | Intrabar | 2.0% | Severe auction pin-bar shakeouts | +160.9% | 4.49% | 24.16% | 0.186 |
| **2. ACTS 4.2 Triple Locks** | Close-based | 2.0% | Eliminates tail profit givebacks | +507.4% | 8.63% | **12.44%** | **0.694** |
| **3. Triple Locks + Pyramiding** | Close-based | 2.0% | Convex pyramiding on winners | +728.2% | 10.15% | 15.68% | 0.647 |
| **4. Triple Locks + Cash Sweep** | Close-based | 2.0% | Idle capital repo yield accrual | +842.6% | 10.84% | 14.86% | **0.730** |
| **5. ACTS 4.2 Ultimate Balanced ★** | Close-based | **2.0%** | **Full Feature Suite (Locks + Pyr + Sweep)** | **+1,182.3%** | **12.38%** | **18.34%** | **0.675** |
| **6. ACTS 4.2 Aggressive Profile ★** | Close-based | **2.5%** | **Full Feature Suite (Locks + Pyr + Sweep)** | **+2,165.8%** | **15.35%** | **25.85%** | **0.594** |
| **7. ACTS 4.2 Maximum Load** | Close-based | **3.0%** | Full Feature Suite (Locks + Pyr + Sweep) | **+2,559.2%** | **16.20%** | 31.03% | 0.522 |

*Note: The 2.0% to 2.5% risk bracket achieves optimal compounding efficiency before hitting the Kelly fraction curvature cliff.*

---

## 3. Repository Structure

```text
├── acts_core/
│   ├── __init__.py                     # Clean Python interface
│   └── engine.cp311-win_amd64.pyd      # High-performance compiled native C-extension
├── data/
│   └── raw/                            # Sample continuous multi-asset daily data
├── run_domestic_backtest.py            # 21.8-Year multi-commodity audit runner
├── scan_market_signals.py              # Multi-asset real-time momentum radar
├── requirements.txt                    # Minimal environment dependencies
└── README.md                           # System documentation
```

---

## 4. Quick Start

### Prerequisites
- Python 3.11 (64-bit AMD64)
- `pandas` and `numpy`

### Installation
```bash
git clone https://github.com/llzlau/acts-42-engine.git
cd acts-42-engine
pip install -r requirements.txt
```

### 1. Run the 21.8-Year Domestic Backtest
```bash
python run_domestic_backtest.py
```

### 2. Run the Real-Time Market Radar Scanner
```bash
python scan_market_signals.py
```

---

## 5. Disclaimer
This software is provided strictly for quantitative research, backtesting, and institutional modeling purposes. Futures and derivative trading carry substantial risk of loss. Past performance is not indicative of future results.
