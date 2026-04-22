from black_scholes import black_scholes_call
from monte_carlo import monte_carlo_call

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bs_price = black_scholes_call(S, K, T, r, sigma)
print(f"Black-Scholes Price: {bs_price:.4f}")

mc_price = monte_carlo_call(S, K, T, r, sigma, 10000)
print(f"Monte Carlo Price: {mc_price:.4f}")
