# Christopher Juncker
# CS410 Reinforcement Learning
# Term Project
#

import random
import math


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

