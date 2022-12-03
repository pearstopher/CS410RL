

CS410 Reinforcement Learning<br>
Fall 2022<br>
Christopher Juncker

# RL Optional Term Project


## 1. Introduction

*Optional  Project:  Working  on  the  projects  are  optional  for
both  graduate  and  undergraduate students. For the project, you 
can implement techniques, or results related to the class materials 
to obtain up to 15% extra credit.*

This is a Gathering Simulator written in Python and using the Pygame
interface. A Reinforcement Learning agent has been built over the 
Gathering Simulator. When the program is run, the agent learns how to 
successfully gather items in the game environment.

Additional instructions, information, and images are included in the 
program write-up, which has been included in the assignment submission.



## 2. Instructions

### 2.1 Installation

In order to successfully run the program, you will need to have access to
a Python installation with the following packages:

1. NumPy (`pip install numpy`)
2. PyGame (`pip install pygame`)
3. PyPlot (`pip install matplotlib`)

### 2.2. Operation

To run the program, simply call the main script, `main.py`, from the main
directory.
```py
python main.py
```

By default, when the program runs it will do three things:

1. Train the Agent for 5000 episodes/iterations.
2. Display a training graph of the training rewards for each episode.
3. Display the game interface 5 times in succession (to show 5 examples
of the trained agent in action).

The default behavior of the program can always be changed if desired, 
simply be modifying the constants in the header of `main.py`, `agent.py`, 
or `environment.py`.




