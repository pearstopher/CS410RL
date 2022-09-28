# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
#

import random
import math


# world generation function
# this world will start very simply and iteratively increase in complexity
class Environment:
    def __init__(self, x=1000, y=1000):
        # set the size of the (rectangular) world
        self.x = x  # width
        self.y = y  # height

        # set the location of the destination (single gathering node)
        self.node = self.random_location()

        # set the location where agents will begin when entering this world
        self.home = self.random_location()
        # and the direction the agent will be facing when they "spawn"
        self.orientation = random.random()*360

    # return a random valid location within the bounds of the world
    def random_location(self):
        return random.randint(0, self.x), random.randint(0,self.y)


    # print world information
    # used to describe world state until a visual representation can be created
    def info(self):
        print("World size: " + str(self.x) + "x" + str(self.y) + ".")
        print("Node location: " + str(self.node))
        print("Home location: " + str(self.home))
        print("State: " + str(self.state()))

    # the world exports specific information about it's state
    # this raw information can be processed by the agent's sensors
    # this information returned from this function is the only information the agent can recieve
    def state(self):
        # orientation angle
        o = self.orientation

        # node direction angle
        # (calculated by using arc tangent)
        # https://math.stackexchange.com/questions/707673/find-angle-in-degrees-from-one-point-to-another-in-2d-space
        x = self.node[0] - self.home[0]
        y = self.node[1] - self.home[1]
        d = math.degrees(math.atan2(y, x))
        if d < 0:
            d += 360  # let's keep things positive

        # node proximity
        # (calculated with pythagorean theorem)
        # exact distance up to a limit, 0 if too far
        p_max = 100
        p = ((self.node[0] - self.home[0])**2 + (self.node[1] - self.home[1])**2)**0.5
        # return 0 if the distance is beyond the max viewable distance
        if p > p_max:
            p = 0
        # otherwise return the distance normalized to the range 0-1
        else:
            p = p / p_max

        return o, d, p




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
    # (note that the total amount of information also multiplies by the number of available actions



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



def main():
    print("CS410 Reinforcement Learning Project")


    # initialize the agent
    agent = Agent()

    # initialize an environment for the agent to explore
    world = Environment(125,125)
    world.info()

    # place the agent in the environment
    agent.assign(world)

    # display information from agent's sensors
    agent.info()






if __name__ == '__main__':
    main()




