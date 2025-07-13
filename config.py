"""
Configuration file for Forex Cointegration Strategy
Based on parameters from "Cointegration-Based Strategies in Forex Pair Trading"
"""

# Currency pairs (Yahoo Finance format)
CURRENCY_PAIRS = [
    'EURUSD=X',  # Euro to US Dollar
    'GBPUSD=X',  # British Pound to US Dollar  
    'USDJPY=X',  # US Dollar to Japanese Yen
    'USDCHF=X',  # US Dollar to Swiss Franc
    'USDCAD=X',  # US Dollar to Canadian Dollar
    'AUDUSD=X',  # Australian Dollar to US Dollar
    'NZDUSD=X'   # New Zealand Dollar to US Dollar
]

# Parameters from the paper
TRAINING_WINDOWS = [63, 128, 257]  # days
TESTING_WINDOWS = [1, 5, 21, 63, 128]  # days
Z_SCORE_THRESHOLDS = [1, 2, 3]  # standard deviations

# Study period (17 years as in paper)
START_DATE = '2007-01-01'
END_DATE = '2024-01-01'

# Statistical significance level
SIGNIFICANCE_LEVEL = 0.05

# Risk-free rate (for Sharpe ratio calculation)
RISK_FREE_RATE = 0  # 0% annual

# Cointegration test parameters
MAX_LAG = 12  # Maximum lag for ADF tests