# Christopher Juncker
# CS410RL Homework #2
#
# Problem: Implement a 5 armed bandit problem with greedy and e-greedy action selection
#   algorithms. Compare the results of e-greedy action selection method (e=0.4) with the greedy one.
#   Which one works better over 100 time-steps in 200 runs? You can choose any distribution/values
#   for your reward function and/or other parameters.

# includes
import random
import numpy as np
import matplotlib.pyplot as plt


# constants
ARMS = 5        # 5-armed bandit
EPSILON = 0.4   # for epsilon-greedy action selection
STEPS = 100     # time-steps
RUNS = 200      # 200 runs x 100 steps = 20,000 actions


# create the environment
class Environment:
    def __init__(self, levers):
        # the environment will have #levers choices
        # each choice will have an associated reward
        # the range of rewards spans from 0-100
        self.rewards = [random.uniform(0, 100) for _ in range(levers)]

    # the environment has levers to pull, the agent has arms to pull them
    def pull(self, lever):
        return self.rewards[lever]


# create the agent
class Bandit:
    def __init__(self, arms, epsilon, steps, runs):
        self.arms = arms
        self.epsilon = epsilon
        self.steps = steps
        self.runs = runs

    def run(self):
        reward = 0
        for _ in range(self.steps):
            reward += self.step()
        return reward

    def step(self):
        # perform a non optimal action with probability epsilon
        if random.random() < self.epsilon:
            reward = epsilon_greedy_action()
        else:
            reward = greedy_action()
        return reward

    def epsilon_greedy_action(self):
        # choose an action at random from the sub-optimal actions
        return

    def greedy_action(self):
        # choose the best action
        return




def main():
    print("Homework 2")

    # create an environment
    environment = Environment

    # create a greedy bandit
    greedy_bandit = Bandit(environment, ARMS, EPSILON, STEPS, RUNS)
    # run the greedy bandit and save the results
    greedy_results = greedy_bandit.run()

    # create an epsilon-greedy bandit
    epsilon_bandit = Bandit(environment, ARMS, 0, STEPS RUNS)
    # run the e-greedy-bandit on the same environment and save the results
    epsilon_results = epsilon_bandit.run()


    # plot the results from the two bandits to see who does better


if __name__ == "__main__":
    main()
