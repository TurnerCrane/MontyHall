import gymnasium as gym
import numpy as np
from env import monty_hall_wrapper

class MontyHallEnv(gym.Env):
    def __init__(self, config):
        super().__init__()
        #print("hogehoge:{}".format(config))
        self.env = monty_hall_wrapper.MontyHallEnv(config["num_doors"],
                                                    config["seed"])
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Discrete(config["num_doors"])
        # Boxは連続値
        #self.observation_space = gym.spaces.Box(low=0, high=1,
        #                                    shape=(config["num_doors"],))

    def reset(self, *, seed=None, options=None):
        return self.env.reset(), {}

    def step(self, action):
        state, reward = self.env.step(action)
        done = truncated =  True
        return (state, reward, done, truncated, {}, )
