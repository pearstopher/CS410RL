# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
# todo: add graphs

from game import game
from agent import Agent
from environment import Environment


def main():
    print("CS410 Reinforcement Learning Project")



    # initialize the agent
    agent = Agent()

    # initialize an environment for the agent to explore
    world = Environment(50,50)
    world.info()

    # place the agent in the environment
    agent.assign(world)

    # display information from agent's sensors
    agent.info()


    # create a thread for the game
    # ideally I will be able to cap the framerate of pygame without slowing the actual computation
    import threading
    lock = threading.Lock()

    # you can safely transfer stuff between threads with locks or queues if you wanna
    # from queue import Queue
    # q = Queue()
    thr = threading.Thread(target=game, args=(world,lock))
    thr.start()

    import time # sleep to slow down for visual display

    # it seems pygame just needs some time to start before we start goin crazy up in here
    time.sleep(1)

    # while the game interface is running, go ahead and let the agent run
    # the interface is purely a visual representation of what is going on behind the scenes
    # (although it currently can't be disabled)
    #
    episodes = 1000
    e = 0
    while thr.is_alive() and e < episodes:

        # let the agent train until it reaches the max number of episodes
        # (or the pygame window is closed)
        lock.acquire()
        reward = agent.episode()
        lock.release()
        print("Episode:", e, "Total Reward:", reward)
        e += 1
        # time.sleep(0.001)



    thr.join()  # Will wait till game is done

    for _ in range(5):
        e = 1000

        # start another thread
        thr = threading.Thread(target=game, args=(world,lock))
        thr.start()
        time.sleep(1)

        success = 0
        while thr.is_alive() and e > 0 and success == 0:
            lock.acquire()
            reward, success = agent.step()
            lock.release()
            e -= 1
            time.sleep(0.002) # slow down a little so we can see it

        thr.join()

        world.reset()

    world.info()


if __name__ == '__main__':
    main()




