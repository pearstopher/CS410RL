# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
#

import random


# world generation function
# this world will start very simply and iteratively increase in complexity
class Environment:
    def __init__(self, x=1000, y=1000):
        # set the size of the (rectangular) world
        self.x = x  # width
        self.y = y  # height

        # set the location of the destination (single gathering node)
        self.node = self.random_location()

    # return a random valid location within the bounds of the world
    def random_location(self):
        return random.randint(0, self.x), random.randint(0,self.y)


    # print world information
    # used to describe world state until a visual representation can be created
    def describe(self):
        print("World size: " + str(self.x) + "x" + str(self.y) + ".")
        print("Node location: " + str(self.node))


# agent creation function
class Agent:
    def __init__(self, world):
        # initialize the agent in a random location in the world
        self.location = world.random_location()


    # print agent information
    # used to describe the agent state until a visual representation can be created
    def describe(self):
        print("Agent location:" + str(self.location))


    # the agent should have the following sensors:
    # 1. sense direction (approximate # of degrees)
    # 2. sense nearest node direction (approximate # of degrees)
    # 3 sense nearest node proximity (in range, close range, far, unknown)
    #
    # with these senses, there should be (# of ranges)((# of degrees)^2) possible states
    # with 4 ranges and 8 possible directions (45 degree accuracy) there are 256 possible states
    # with 4 ranges and 16 possible directions (22.5 degree accuracy) there are 1024
    # this seems reasonable so far



def main():
    print("CS410 Reinforcement Learning Project")

    # initialize the environment
    world = Environment(1234,567)
    world.describe()

    # initialize the agent
    # (the agent will will need to be initialized seperately from the world,
    #  so that the same agent can gather experiences in many worlds)
    agent = Agent(world)
    agent.describe()





if __name__ == '__main__':
    main()




