from quantum_engine import optimize_portfolio
from quantum_derivatives import price_european_call

def generate_portfolio(user_profile):
    mu, sigma = ([0.15,0.20,0.30], [[.05,.02,.01],[.02,.04,.015],[.01,.015,.06]]) if user_profile.get("risk")=="high" else ([0.05,0.08,0.12], [[.01,.005,.002],[.005,.02,.001],[.002,.001,.015]])
    portfolio, value = optimize_portfolio(mu, sigma, budget=user_profile.get("budget",2))
    derivative = price_european_call(100,105,1,0.01,0.2)
    return {"portfolio": portfolio, "expected_return": value, "leverage_derivative": derivative}
