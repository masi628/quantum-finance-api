from qiskit_finance.applications.optimization import PortfolioOptimization
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit import Aer

def optimize_portfolio(mu, sigma, budget):
    portfolio = PortfolioOptimization(mu, sigma, 0.1, budget)
    qp = portfolio.to_quadratic_program()
    qaoa = QAOA(reps=1, quantum_instance=Aer.get_backend("aer_simulator"))
    result = MinimumEigenOptimizer(qaoa).solve(qp)
    return result.x.tolist(), result.fval
