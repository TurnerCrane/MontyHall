import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPO
from env.monty_hall_env import MontyHallEnv

def train_monty_hall():
    ray.init(local_mode=True)

    tune.register_env("MontyHallEnv", lambda config: MontyHallEnv(config))
    config = {
      "env": MontyHallEnv,
      "num_workers": 1,
      "num_gpus": 0,
      "use_gpu": False,
      "framework": "torch",
      "env_config": {
        "num_doors": 3,
        "seed": 12345
    }
    }
    stop = {"training_iteration": 200,}
    tune.run(PPO, config=config, stop=stop)

if __name__ == "__main__":
    train_monty_hall()
