import gym
from gym import spaces
import numpy as np
from ..cpp import monty_hall_wrapper

class MontyHallEnv(gym.Env):
    def __init__(self, config):
        super().__init__()
        self.env = monty_hall_wrapper.MontyHallEnv(config["num_doors"], config["seed"])
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=1, shape=(config["num_doors"],))

    def reset(self):
        return np.array(self.env.reset())

    def step(self, action):
        state, reward = self.env.step(action)
        done = True
        return np.array(state), reward, done, {}
