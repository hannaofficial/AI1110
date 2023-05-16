import numpy as np

def simulate_lottery(num_trials):
    wins = np.random.rand(num_trials, 50) <= 0.01  # Generate a matrix of random numbers

    wins_at_least_once = np.any(wins, axis=1)
    wins_at_least_twice = np.sum(wins, axis=1) >= 2

    prob_at_least_once = np.mean(wins_at_least_once)
    prob_at_least_twice = np.mean(wins_at_least_twice)

    return prob_at_least_once, prob_at_least_twice

# Simulating 1,000,000 trials
num_trials = 1000000
prob_at_least_once, prob_at_least_twice = simulate_lottery(num_trials)

print(f"Probability of winning at least once: {prob_at_least_once:.4f}")
print(f"Probability of winning at least twice: {prob_at_least_twice:.4f}")

