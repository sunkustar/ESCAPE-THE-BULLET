from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from env2 import idcard  # Import your custom environment class

# Load the model
model = PPO.load("models/A2C/40000.zip")

# Create the environment
env = DummyVecEnv([lambda: idcard()])

for ep in range(1000):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        print(rewards)