import ray
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
from env import MontyHallEnv

def train_monty_hall():
    ray.init()
    tune.register_env("MontyHallEnv", lambda config: MontyHallEnv(config))
    config = {"env": "MontyHallEnv",
            "env_config": {"num_doors": 3, "seed": 12345},
            "num_gpus": 0,
            "num_workers": 1
            }
    stop = {"training_iteration": 200,}
    results = tune.run(PPOTrainer, config=config, stop=stop)
    print(results)

if __name__ == "__main__":
    train_monty_hall()
