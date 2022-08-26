################################################################################
# Dumb game to be played by machines
# Guess the correct order of the numbers 1-5 which are shuffled.
# Keep guessing until you get the whole sequence.
# Penalized -1 for every wrong guess.
################################################################################

from gym import Env
from gym.spaces import Discrete, Box
import random
import numpy as np


class DumbGameEnv(Env):
    def __init__(self):
        self.n_numbers = 5
        self.answer = list(range(self.n_numbers))
        random.shuffle(self.answer)
        self.state = 0
        self.action_space = Discrete(5)
        self.observation_space = Box(low=np.array([0],dtype=np.float32), high=np.array([2],dtype=np.float32))

    def step(self, action):
        reward = 0
        if action == self.answer[self.state]:
            self.state += 1
            reward = 1
        else:
            reward = -1

        done = self.state == self.n_numbers or self.state < -50

        info = {}

        # Return step information
        return self.state, reward, done, info

    def render(self):
        pass

    def reset(self):
        random.shuffle(self.answer)
        self.state = 0
        self.n_guesses = 0
        return self.state

if __name__ == "__main__":
    env = DumbGameEnv()
    #print(env.observation_space.sample()) # 0-1
    #print(env.action_space.sample()) # 0-4
    episodes = 10
    for episode in range(1, episodes+1):
        state = env.reset()
        done = False
        score = 0
        n_guesses = 0
        while not done:
            n_guesses += 1
            action = env.action_space.sample()
            n_state, reward, done, info = env.step(action)
            score+=reward
        print(f'Episode:{episode} Score:{score} NGuesses:{n_guesses}')
