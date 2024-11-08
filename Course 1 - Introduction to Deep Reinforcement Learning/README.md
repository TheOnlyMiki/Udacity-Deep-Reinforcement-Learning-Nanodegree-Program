# Dependencies

This is an amended version of the `python/` folder from the [ML-Agents repository](https://github.com/Unity-Technologies/ml-agents).  It has been edited to include a few additional pip packages needed for the Deep Reinforcement Learning Nanodegree program.


# Project Details

### Unity ML-Agents Banana Navigation Environment

![banana navigation](images/banana.gif)

For this project, you will train an agent to navigate (and collect bananas!) in a large, square world.

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

- `0` - move forward.
- `1` - move backward.
- `2` - turn left.
- `3` - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.


# Getting Started

### Step 1: Activate the Environment

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6 in **Anaconda Prompt**.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
2. If running in **Windows**, ensure you have the "Build Tools for Visual Studio" installed from this [site](https://visualstudio.microsoft.com/downloads/).  This [article](https://towardsdatascience.com/how-to-install-openai-gym-in-a-windows-environment-338969e24d30) may also be very helpful.

3. Follow the instructions in [this repository](https://github.com/openai/gym) or `pip install gym` to perform a minimal install of OpenAI gym.
   - Install the **classic control** environment group by following the instructions [here](https://github.com/openai/gym#classic-control) or `pip install gym[classic_control]`.
   - Install the **box2d** environment group by following the instructions [here](https://github.com/openai/gym#box2d) or `pip install gym[box2d]`.
     If any failed or error to install box2d environment,  following:
     ```bash
     pip install swig
     pip install Box2D gym
     ```
     **OR**
     ```bash
     conda install swig
     conda install -c conda-forge gym-box2d
     ```
	
4. Clone the repository, and navigate to the folder.  Then, install several dependencies.  
    ```bash
    git clone https://github.com/TheOnlyMiki/Udacity-Deep-Reinforcement-Learning-Nanodegree-Program.git
    cd Udacity-Deep-Reinforcement-Learning-Nanodegree-Program
    pip install .
    ```

5. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.    
    ```bash
    python -m ipykernel install --user --name drlnd --display-name "drlnd"
    ```

6. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu. 

![Kernel][images/kernel.png]

(For Windows users) The ML-Agents toolkit supports Windows 10. While it might be possible to run the ML-Agents toolkit using other versions of Windows, it has not been tested on other versions. Furthermore, the ML-Agents toolkit has not been tested on a Windows VM such as Bootcamp or Parallels.


### Step 2: Download the Unity Environment

For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

<ul role="list" class="css-19qh3zo"><li class="css-cvpopp">Linux: <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip">click here</a></li><li class="css-cvpopp">Mac OSX: <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip">click here</a></li><li class="css-cvpopp">Windows (32-bit): <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip">click here</a></li><li class="css-cvpopp">Windows (64-bit): <a target="_blank" rel="noopener noreferrer" class="chakra-link css-190botj" href="https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip">click here</a></li></ul>

### Step 3: Explore the Environment

After you have followed the instructions above, open `Navigation.ipynb` (located in the folder in the course 2 GitHub repository) and follow the instructions to learn how to use the Python API to control the agent.


# Report

### Training Code

- `Navigation.ipynb`
- `model.py`
- `dqn_agent.py`

### Saved Model Weights

- `checkpoint.pth` - Deep Q Network
- `checkpoint_dueling_dqn.pth` - Dueling DQN

### Learning Algorithm

#### - Hyperparameters:
  - eps_start = 1.0     # epsilon starting value
  - eps_end = 0.01     # epsilon minimum value
  - eps_decay = 0.995    # epsilon discount coefficient
  - BUFFER_SIZE = int(1e5) # replay buffer size
  - BATCH_SIZE = 64     # minibatch size
  - GAMMA = 0.99      # discount factor
  - TAU = 1e-3       # for soft update of target parameters
  - LR = 5e-4        # learning rate
  - UPDATE_EVERY = 4    # how often to update the networ

#### - Deep Q Network:
  1. Fully Connected Layer with ReLu Activation Function = 37 -> 64
  2. Fully Connected Layer with ReLu Activation Function = 64 -> 64
  3. Fully Connected Layer = 64 -> 4

#### - Dueling Deep Q Network:
  1. Fully Connected Layer with ReLu Activation Function = 37 -> 64
  2. Two of Fully Connected Layer with ReLu Activation Function = 64 -> 256
  3. Two of Fully Connected Layer:
    3.1 Value of State - Fully Connected Layer = 256 -> 1
    3.2 Advantage Actions - Fully Connected Layer = 256 -> 4
  4. Computing the Average of Advantage Actions
  5. Q Values = Value of State + Advantage Actions - Average of Advantage Actions

### Plot of Rewards

- `DQN.png` - Episode 527, Average Score: 13.03, Environment solved in 427 episodes.

![reward1][DQN.png]

- `dueling.png` - Episode 625, Average Score: 13.02, Environment solved in 525 episodes.

![reward2][dueling.png]