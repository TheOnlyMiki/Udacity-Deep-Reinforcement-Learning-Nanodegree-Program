import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))

    def select_action(self, state, train=True):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        epsilon = 0.002
        policy = np.ones(self.nA) * epsilon / self.nA
        policy[np.argmax(self.Q[state])] = 1 - epsilon + (epsilon / self.nA)
        return np.random.choice(np.arange(self.nA), p=policy) if train else policy

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        alpha = 0.025
        gamma = 0.9
        
	# SARSA
	'''
	if done:
		self.Q[state][action] += alpha * (reward - self.Q[state][action])
		return

	next_action = self.select_action(next_state)
	self.Q[state][action] += alpha * (reward + gamma * self.Q[next_state][next_action] - self.Q[state][action])
	'''

	# Q Learning
	self.Q[state][action] += alpha * (reward + gamma * np.max(self.Q[next_state]) - self.Q[state][action])
	
	# Expected SARSA
        #self.Q[state][action] += alpha * (reward + gamma * np.sum(self.Q[next_state] * self.select_action(next_state, False)) - self.Q[state][action])
