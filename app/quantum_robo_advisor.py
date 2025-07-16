from quantum_engine import optimize_portfolio
from quantum_derivatives import price_european_call

def generate_portfolio(user_profile: dict) -> dict:
    risk_level = user_profile.get("risk", "medium")
    budget = float(user_profile.get("budget", 2))

    if risk_level == "high":
        mu = [0.15, 0.20, 0.30]
        sigma = [[.05, .02, .01], [.02, .04, .015], [.01, .015, .06]]
    else:
        mu = [0.05, 0.08, 0.12]
        sigma = [[.01, .005, .002], [.005, .02, .001], [.002, .001, .015]]

    portfolio, expected_return = optimize_portfolio(mu, sigma, budget)

    derivative_price = price_european_call(
        spot_price=100,
        strike_price=105,
        maturity=1,
        risk_free_rate=0.01,
        volatility=0.2
    )

    return {
        "portfolio": portfolio,
        "expected_return": expected_return,
        "leverage_derivative": derivative_price
    }
