import gymnasium as gym
from stable_baselines3 import PPO
import os
from env2 import idcard


models_dir = "models/PPO"
logdir = "logs/PPO"
episode_dir= "episode/PPO"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

if not os.path.exists(episode_dir):
    os.makedirs(episode_dir)

env = idcard()

env.reset()
model = PPO.load("3230000",env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")
