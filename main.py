# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
#

import random
import math
import game


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
        self.agent = self.random_location()
        # and the direction the agent will be facing when they "spawn"
        self.orientation = random.random()*360

        # set the environmental rewards
        self.DEFAULT_ACTION_REWARD = -1  # in general, a solution with fewer actions is better
        self.GATHERING_SUCCESS = 100  # this is the reward for when the agent achieves its goal

    # return a random valid location within the bounds of the world
    def random_location(self):
        return random.randint(0, self.x), random.randint(0,self.y)


    # print world information
    # used to describe world state until a visual representation can be created
    def info(self):
        print("World size: " + str(self.x) + "x" + str(self.y) + ".")
        print("Node location: " + str(self.node))
        print("Agent location: " + str(self.agent))
        print("State: " + str(self.state()))

    # the world exports specific information about it's state
    # this raw information can be processed by the agent's sensors
    # this information returned from this function is the only information the agent can receive
    #
    # return values:
    # o: orientation, float [0, 360). The direction the agent is facing in degrees.
    # d: direction, float [0, 360). The direction of the nearest gathering node in degrees.
    # p: proximity, float [0, p_max). The proximity of the closest node. (0 if farther than p_max.)
    def state(self):
        # orientation angle
        o = self.orientation

        # node direction angle
        # (calculated by using arc tangent)
        # https://math.stackexchange.com/questions/707673/find-angle-in-degrees-from-one-point-to-another-in-2d-space
        x = self.node[0] - self.agent[0]
        y = self.node[1] - self.agent[1]
        d = math.degrees(math.atan2(y, x))
        if d < 0:
            d += 360  # let's keep things positive

        # node proximity
        # (calculated with pythagorean theorem)
        # exact distance up to a limit, 0 if too far
        p_max = 100
        p = ((self.node[0] - self.agent[0])**2 + (self.node[1] - self.agent[1])**2)**0.5
        # return 0 if the distance is beyond the max viewable distance
        if p > p_max:
            p = 0
        # otherwise return the distance normalized to the range 0-1
        else:
            p = p / p_max

        return o, d, p


    # abilities!!!
    #
    # the boundary between the agent and the world is interesting for sure
    # in this case, the world provides a set of abilities
    # and the agent's "actions" are to trigger the usage of these "abilities"
    #
    # the initial abilities (more can be added later) are:
    # * turn left
    # * turn right
    # * go forwards
    # * gather node
    #

    # turn left
    # the agent's position in the world is rotated a small amount to the left
    # there is a bit of randomness in exactly how much movement actually occurs
    def left(self):
        rotate_amount = 10  # degrees
        random_percent = 10  # percent of rotate_amount
        random_amount = rotate_amount * random_percent / 100 # center at 0

        self.orientation += rotate_amount
        self.orientation += random.random() * random_amount - 0.5  # center at 0

        return self.DEFAULT_ACTION_REWARD

    # turn right
    # just like turning left, but the other way
    def right(self):
        rotate_amount = 10  # degrees
        random_percent = 10  # percent of rotate_amount
        random_amount = rotate_amount * random_percent / 100 # center at 0

        self.orientation -= rotate_amount
        self.orientation -= random.random() * random_amount - (random_amount / 2)  # center at 0

        # be careful when subtracting past zero
        if self.orientation < 0:
            self.orientation += 360

        return self.DEFAULT_ACTION_REWARD

    # go forwards
    # the agent's position in the world moves forward by a specified amount
    # again, the distance is not exact but varies slightly
    def forward(self):
        forward_amount = 1  # units
        random_percent = 10  # percent of forward_amount
        random_amount = forward_amount * random_percent / 100 # center at 0

        total_amount = forward_amount + random.random() * random_amount - (random_amount / 2)  # center at 0

        # change the agent coordinates based on the direction the agent is facing
        x_amount =  total_amount * math.cos(self.orientation)
        y_amount = total_amount * math.sin(self.orientation)

        self.agent = (self.agent[0] + x_amount, self.agent[1] + y_amount) # fix this tuple-y sadness

        return self.DEFAULT_ACTION_REWARD



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


    # create a thread for the game
    import threading
    from queue import Queue
    q = Queue()
    thr = threading.Thread(target=game.game, args=(world,))
    thr.start()

    # thr.is_alive()  # Will return whether foo is running currently
    while thr.is_alive():
        # world.forward()
        print("x")
        world.forward()
        world.left()

    thr.join()  # Will wait till "foo" is done

    # game.game(world)

    world.forward()
    world.info()
    world.forward()
    world.info()






if __name__ == '__main__':
    main()




