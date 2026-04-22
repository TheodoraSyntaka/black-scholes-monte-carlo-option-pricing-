import numpy as np

def monte_carlo_call(S0, K, T, r, sigma, N=10000):
    Z = np.random.randn(N)
    ST = S0 * np.exp((r - 0.5 * sigma**2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r*T) * np.mean(payoff)
