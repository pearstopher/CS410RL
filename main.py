# Christopher Juncker
# CS410 Reinforcement Learning Fall 2022
# Term Project
#
# todo: create variable world size

# import all my stuff
from game import game
from agent import Agent
from environment import Environment
from graph import Graph


#################
# DISPLAY OPTIONS
#################

# a pygame window will show live visual progress *during* training
PYGAME_TRAIN = False
# a pygame window will show a number of visual examples *after* training
PYGAME_EXAMPLES = 0
# a plot of rewards over time will be shown *after* training
GRAPH = True


####################
# TRAINING CONSTANTS
####################

# number of episodes
EPISODES = 1500

# learning rate
ETA = 0.1  # 0.1 standard
# decrease eta after a set number of episodes
ETA_DECREASE_AFTER = 1000  # 0 = off
# decrease eta by factor of
ETA_DECREASE_AMOUNT = 1/500

# discounting factor
GAMMA = 0.9  # 0.9 standard

# rate at which to make off-policy (random) choices (exploration)
EPSILON = 0.1  # 0.1 standard


def main():
    print("CS410 Reinforcement Learning Project")

    # initialize the agent
    agent = Agent(ETA,
                  ETA_DECREASE_AFTER,
                  ETA_DECREASE_AMOUNT,
                  GAMMA,
                  EPSILON)

    # initialize an environment for the agent to explore
    world = Environment(50, 50)
    world.info()

    # place the agent in the environment
    agent.assign(world)

    # wouldn't want pycharm to think we're referencing anything before assignment now,
    # WOULD WE???
    lock = None
    thr = None

    # display information from agent's sensors
    agent.info()

    if PYGAME_TRAIN:
        # create a thread for the game
        # ideally I will be able to cap the frame-rate of pygame without slowing the actual computation
        import threading
        lock = threading.Lock()

        # you can safely transfer stuff between threads with locks or queues if you wanna
        # from queue import Queue
        # q = Queue()
        thr = threading.Thread(target=game, args=(world, lock))
        thr.start()

        import time  # sleep to slow down for visual display

        # it seems pygame just needs some time to start before we start goin crazy up in here
        time.sleep(1)

    # while the game interface is running, go ahead and let the agent run
    # the interface is purely a visual representation of what is going on behind the scenes
    # (although it currently can't be disabled)
    #
    e = 0
    rewards = [0 for _ in range(EPISODES)]
    while (not PYGAME_TRAIN or thr.is_alive()) and e < EPISODES:

        # let the agent train until it reaches the max number of episodes
        # (or the pygame window is closed)
        if PYGAME_TRAIN:
            lock.acquire()
        reward = agent.episode()
        rewards[e] = reward
        if PYGAME_TRAIN:
            lock.release()
        print("Episode:", e, "Total Reward:", reward)
        e += 1
        # time.sleep(0.001)

    if PYGAME_TRAIN:
        thr.join()  # Will wait till game is done

    # display the training graph
    if GRAPH:
        # initialize the visual graph
        graph = Graph(y_lim=max(rewards)+10)
        # print training graph
        # graph.display(list(range(episodes)), [x+1000 for x in rewards])
        graph.display(list(range(EPISODES)), rewards)

    # show some examples of the agent finding its way
    if PYGAME_EXAMPLES > 0:
        import threading
        lock = threading.Lock()
        import time

        for _ in range(PYGAME_EXAMPLES):
            e = 1000

            thr = threading.Thread(target=game, args=(world,lock))
            thr.start()
            time.sleep(1)

            success = 0
            while thr.is_alive() and e > 0 and success == 0:
                lock.acquire()
                reward, success = agent.step()
                lock.release()
                e -= 1
                time.sleep(0.002)  # slow down a little so we can see it

            thr.join()

            world.reset()

    world.info()


if __name__ == '__main__':
    main()




