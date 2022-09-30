# Christopher Juncker
# CS410 Reinforcement Learning
# Term Project
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
