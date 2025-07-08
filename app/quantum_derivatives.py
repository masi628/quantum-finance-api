from qiskit_finance.applications.estimation import EuropeanCallExpectedValue
from qiskit.algorithms import AmplitudeEstimation
from qiskit import Aer

def price_european_call(S, K, T, r, sigma):
    backend = Aer.get_backend("aer_simulator")
    option = EuropeanCallExpectedValue(spot_price=S, strike_price=K, volatility=sigma, interest_rate=r, time_to_maturity=T)
    ae = AmplitudeEstimation(num_eval_qubits=3, quantum_instance=backend)
    result = ae.estimate(option)
    return result.estimation
