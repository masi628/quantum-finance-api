from qiskit_finance.applications.optimization import PortfolioOptimization
from qiskit_optimization.problems import QuadraticProgram
from qiskit_algorithms import MinimumEigenOptimizer
from qiskit.primitives import Sampler
from qiskit_algorithms.minimum_eigensolvers import SamplingVQE
from qiskit.circuit.library import TwoLocal

def optimize_portfolio(mu, sigma, budget):
    portfolio = PortfolioOptimization(expected_returns=mu, covariances=sigma, budget=budget)
    qp: QuadraticProgram = portfolio.to_quadratic_program()

    ansatz = TwoLocal(len(mu), "ry", "cz", reps=1)
    sampler = Sampler()
    vqe = SamplingVQE(sampler=sampler, ansatz=ansatz)
    optimizer = MinimumEigenOptimizer(vqe)

    result = optimizer.solve(qp)
    return result.variables, result.fval
