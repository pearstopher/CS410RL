# Christopher Juncker
# CS410RL Homework #2
#
# Problem: Implement a 5 armed bandit problem with greedy and e-greedy action selection
#   algorithms. Compare the results of e-greedy action selection method (e=0.4) with the greedy one.
#   Which one works better over 100 time-steps in 200 runs? You can choose any distribution/values
#   for your reward function and/or other parameters.

# includes
import numpy as np
import matplotlib.pyplot as plt


# constants
ARMS = 5        # 5-armed bandit
EPSILON = 0.4   # for epsilon-greedy action selection
STEPS = 100     # time-steps
RUNS = 200      # 200 runs x 100 steps = 20,000 actions



def main():
    print("Homework 2")


if __name__ == "__main__":
    main()
