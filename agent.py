# Christopher Juncker
# CS410 Reinforcement Learning
# Term Project
#

import random
import math
import numpy as np



# agent creation function
class Agent:
    def __init__(self):
        # keep track of how many times the agent has been trained
        self.i = 0

        # initialize other fields to default values for assignment later
        self.world = None

        # configure the accuracy of the sensors
        self.num_orientation = 16
        self.num_direction = 16
        self.num_proximity = 4
        # and just keep track of the number of actions here
        self.num_actions = 4  # left, right, forward, gather

        # initialize a q-table
        self.q = np.zeros((self.num_orientation, self.num_direction,
                           self.num_proximity, self.num_actions))


    # the agent needs to be given an environment in which to act
    def assign(self, world):
        self.world = world


    # print agent information
    # used to describe the agent state until a visual representation can be created
    def info(self):
        print("Number of training sessions: " + str(self.i))
        print("Sense: " + str(self.sense()))


    # the agent should have the following sensors:
    # 1. sense direction (approximate # of degrees)
    # 2. sense nearest node direction (approximate # of degrees)
    # 3 sense nearest node proximity (in range, close range, far, unknown)
    #
    # with these senses, there should be (# of ranges)((# of degrees)^2) possible states
    # with 4 ranges and 8 possible directions (45 degree accuracy) there are 256 possible states
    # with 4 ranges and 16 possible directions (22.5 degree accuracy) there are 1024
    # this seems reasonable so far
    #
    # (note that the total amount of information also multiplies by the number of available actions)



    def sense(self):
        # get the information from the world state
        state = self.world.state()

        # process the raw information into usable data
        o = state[0] * self.num_orientation // 360  # convert from degrees to sections
        d = state[1] * self.num_direction // 360  # convert from degrees to sections

        # proximity is 0 when there is no reading due to distance
        if state[2] == 0:
            p = self.num_proximity - 1 # assign maximum proximity rating (farthest)
        # proximity is nonzero when there is a successful reading
        else:
            p = state[2] * (self.num_proximity - 1) // 1 # assign proximity linearly

        return o, d, p

    # an episode is made up of a series of steps that generates a reward
    def episode(self):
        # run for a set number of steps
        max_steps = 1000

        i = 0
        complete = 0
        total_reward = 0
        while i < max_steps and complete == 0:
            reward, complete = self.step()
            total_reward += reward
            i += 1
            import time
            # time.sleep(0.001)

        # reset the world at the end of the episode
        self.world.reset()

    # a step is an individual action
    # the action returns a reward and a "boolean":
    # 0 if the node has not been gathered, and
    # 1 if the node has been gathered (episode can end)
    def step(self):

        # 1. observe the state
        state = self.world.state()

        # 2. choose an action based on the state
        action = self.epsilon_greedy_action(state)

        # 3. perform the action
        if action == 0:
            reward = self.world.left()
        elif action == 1:
            reward = self.world.right()
        elif action == 2:
            reward = self.world.forward()
        else:
            reward = self.world.gather()

        # 4. observe the new state
        new_state = self.world.state()

        # 5. update the q-table based on the formula:
        #    𝑄(𝑠_𝑡, 𝑎_𝑡) = 𝑄(𝑠_𝑡, 𝑎_𝑡) + 𝜂(𝑟_𝑡 + 𝛾𝑚𝑎𝑥_𝑎′𝑄(𝑠_(𝑡+1), 𝑎′) − 𝑄(𝑠_𝑡, 𝑎_𝑡))

        # (todo)

        return reward, 0
