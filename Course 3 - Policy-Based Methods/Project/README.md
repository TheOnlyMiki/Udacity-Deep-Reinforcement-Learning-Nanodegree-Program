# Dependencies

This is an amended version of the `python/` folder from the [ML-Agents repository](https://github.com/Unity-Technologies/ml-agents).  It has been edited to include a few additional pip packages needed for the Deep Reinforcement Learning Nanodegree program.


# Project Details

### Unity ML-agents reacher environment

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.


### Distributed Training

For this project, we will provide you with two separate versions of the Unity environment:

- The first version contains a single agent.
- The second version contains 20 identical agents, each with its own copy of the environment.

The second version is useful for algorithms like PPO(opens in a new tab), A3C(opens in a new tab), and D4PG(opens in a new tab) that use multiple (non-interacting, parallel) copies of the same agent to distribute the task of gathering experience.


### Solving the Environment
Note that your project submission need only solve one of the two versions of the environment.

#### Option 1: Solve the First Version

The task is episodic, and in order to solve the environment, your agent must get an average score of +30 over 100 consecutive episodes.

#### Option 2: Solve the Second Version

The barrier for solving the second version of the environment is slightly different, to take into account the presence of many agents. In particular, your agents must get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,

- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 20 (potentially different) scores. We then take the average of these 20 scores.
- This yields an average score for each episode (where the average is over all 20 agents).


# Getting Started

### Step 1: Activate the Environment

Follow the instructions in the [DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. These instructions can be found in README.md at the root of the repository. By following these instructions, you will install PyTorch, the ML-Agents toolkit, and a few more Python packages required to complete the project.

(For Windows users) The ML-Agents toolkit supports Windows 10. While it might be possible to run the ML-Agents toolkit using other versions of Windows, it has not been tested on other versions. Furthermore, the ML-Agents toolkit has not been tested on a Windows VM such as Bootcamp or Parallels.


### Step 2: Download the Unity Environment

For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

#### Version 1: One (1) Agent

<ul role="list" class="css-19qh3zo"><li class="css-cvpopp">Linux: <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip">click here</a></li><li class="css-cvpopp">Mac OSX: <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip">click here</a></li><li class="css-cvpopp">Windows (32-bit): <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip">click here</a></li><li class="css-cvpopp">Windows (64-bit): <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip">click here</a></li></ul>

#### Version 2: Twenty (20) Agents

<ul role="list" class="css-19qh3zo"><li class="css-cvpopp">Linux: <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip">click here</a></li><li class="css-cvpopp">Mac OSX: <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip">click here</a></li><li class="css-cvpopp">Windows (32-bit): <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip">click here</a></li><li class="css-cvpopp">Windows (64-bit): <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip">click here</a></li></ul>

# Instructions

I attempted to train the agent in my environment but encountered issues. 

Initially, I installed the latest version of Anaconda (Python 3.12) and followed the course instructions, but Python 3.6 was inactive in my environment. 

I then tried reinstalling an older version of Anaconda, which defaults to Python 3.6. However, even after registering it, Anaconda (older version) was not recognized in my environment path.

Therefore, the only way I can proceed with this project is by using Udacity’s workspace.
