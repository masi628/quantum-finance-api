def price_european_call(spot_price, strike_price, maturity, risk_free_rate, volatility):
    from math import exp
    return max(spot_price - strike_price * exp(-risk_free_rate * maturity), 0)

