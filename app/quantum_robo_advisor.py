from quantum_engine import optimize_portfolio
from quantum_derivatives import price_european_call

def generate_portfolio(user_profile: dict) -> dict:
    """
    Genera un portafoglio ottimizzato in base al profilo utente,
    includendo anche un derivato europeo come leva.
    """
    risk_level = user_profile.get("risk", "medium")
    budget = user_profile.get("budget", 2)

    # Seleziona media e covarianza in base al rischio
    if risk_level == "high":
        mu = [0.15, 0.20, 0.30]
        sigma = [[.05, .02, .01], [.02, .04, .015], [.01, .015, .06]]
    else:
        mu = [0.05, 0.08, 0.12]
        sigma = [[.01, .005, .002], [.005, .02, .001], [.002, .001, .015]]

    # Ottimizza il portafoglio
    portfolio, expected_return = optimize_portfolio(mu, sigma, budget=budget)

    # Prezzo di un'opzione call europea come leva (fittizia per ora)
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
    
