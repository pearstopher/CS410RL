# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
#

import game
from agent import Agent
from environment import Environment



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
    # ideally I will be able to cap the framerate of pygame without slowing the actual computation
    import threading
    # you can safely transfer stuff between threads with locks or queues if you wanna
    # from queue import Queue
    # q = Queue()
    thr = threading.Thread(target=game.game, args=(world,))
    thr.start()

    # while the game interface is running, go ahead and let the agent run
    # the interface is purely a visual representation of what is going on behind the scenes
    # (although it currently can't be disabled)
    while thr.is_alive():

        print("x")
        world.forward()
        world.left()  # if this works the agent will go in circles

    thr.join()  # Will wait till "foo" is done

    # game.game(world)

    world.forward()
    world.info()
    world.forward()
    world.info()






if __name__ == '__main__':
    main()




