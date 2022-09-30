# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
#

from game import game
from agent import Agent
from environment import Environment


def main():
    print("CS410 Reinforcement Learning Project")


    # initialize the agent
    agent = Agent()

    # initialize an environment for the agent to explore
    world = Environment(100,100)
    world.info()

    # place the agent in the environment
    agent.assign(world)

    # display information from agent's sensors
    agent.info()


    # create a thread for the game
    # ideally I will be able to cap the framerate of pygame without slowing the actual computation
    import threading
    # you can safely transfer stuff between threads with locks or queues if you wanna
    # from queue import Queue
    # q = Queue()
    thr = threading.Thread(target=game, args=(world,))
    thr.start()

    import time # sleep to slow down for visual display

    # while the game interface is running, go ahead and let the agent run
    # the interface is purely a visual representation of what is going on behind the scenes
    # (although it currently can't be disabled)
    #
    episodes = 100
    e = 0
    while thr.is_alive() and e < episodes:

        # let the agent train until it reaches the max number of episodes
        # (or the pygame window is closed)
        agent.episode()
        e += 1
        time.sleep(0.01)

    thr.join()  # Will wait till "foo" is done

    world.info()


if __name__ == '__main__':
    main()




