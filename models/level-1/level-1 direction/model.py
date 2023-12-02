import gymnasium as gym
from stable_baselines3 import A2C
import os
from env1 import idcard


models_dir = "models/A2C"
logdir = "logs/A2C"
episode_dir= "episode/A2C"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

if not os.path.exists(episode_dir):
    os.makedirs(episode_dir)

env = idcard()

env.reset()
model = A2C('MlpPolicy', env, verbose=1, tensorboard_log=logdir)




model = A2C('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"A2C")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")
