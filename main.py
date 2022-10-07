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
        self.rewards = [random.randint(1, 100) for _ in range(levers)]

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

        # variables store the environment, action values and current step number
        self.environment = None
        self.action_value = None
        self.i = None
        self.reset()  # sets the above values

    def reset(self):
        self.environment = Environment(self.arms)
        self.action_value = [0 for _ in range(self.arms)]
        self.i = 1

    def run(self):
        reward = 0
        for i in range(self.steps):
            reward += self.step()
            self.i += 1
        self.reset()
        # return average reward per run
        return reward / self.steps

    def step(self):
        # perform a non optimal action with probability epsilon
        if random.random() < self.epsilon:
            reward = self.epsilon_action()
        else:
            reward = self.greedy_action()
        return reward

    def epsilon_action(self):
        # choose an action at random
        lever = random.randrange(0, self.arms)  # not randint
        # perform the action
        reward = self.environment.pull(lever)
        # update the action value
        self.action_value[lever] += (1/self.i)*(reward - self.action_value[lever])
        # return the reward
        return reward

    def greedy_action(self):
        # choose the best action
        lever = np.argmax(self.action_value)
        # perform the action
        reward = self.environment.pull(lever)
        # update the action value
        self.action_value[lever] += (1/self.i)*(reward - self.action_value[lever])
        # return the reward
        return reward


def main():
    print("Homework 2")

    print("Greedy bandit running...")
    # create a greedy bandit
    greedy_bandit = Bandit(ARMS, 0, STEPS, RUNS) # epsilon = 0, never choose randomly
    # run the greedy bandit and save the results
    greedy_results = 0
    for _ in range(RUNS):
        greedy_results += greedy_bandit.run()
    greedy_results /= RUNS

    print("Epsilon greedy bandit running...")
    # create an epsilon-greedy bandit
    epsilon_bandit = Bandit(ARMS, EPSILON, STEPS, RUNS)
    # run the e-greedy-bandit on the same environment and save the results
    epsilon_results = 0
    for _ in range(RUNS):
        epsilon_results += epsilon_bandit.run()
    epsilon_results /= RUNS

    print("Random bandit running...")
    # create a random bandit too!
    random_bandit = Bandit(ARMS, 1, STEPS, RUNS)  # epsilon = 1, always choose randomly
    # run the random bandit and save the results
    random_results = 0
    for _ in range(RUNS):
        random_results += random_bandit.run()
    random_results /= RUNS

    # plot the results from the two bandits to see who does better
    print()
    print("Greedy reward: ", greedy_results)
    print("Epsilon-greedy reward: ", epsilon_results)
    print("Random reward: ", random_results)


if __name__ == "__main__":
    main()
