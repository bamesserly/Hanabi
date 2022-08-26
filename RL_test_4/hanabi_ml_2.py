# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from DumbGame import DumbGameEnv
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

env = DumbGameEnv()
states = env.observation_space.shape
actions = env.action_space.n
print(f"States:{states} Actions:{actions}")


def build_model(states, actions):
    model = Sequential()    
    model.add(Dense(24, activation='relu', input_shape=states))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


# +
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=20000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, 
                  nb_actions=actions, nb_steps_warmup=20, target_model_update=0.1)
    return dqn


# -

model = build_model(states, actions)
model.summary()

dqn = build_agent(model, actions)
dqn.compile(Adam(lr=0.1))#, metrics=['mae'])
history = dqn.fit(env, nb_steps=5000, visualize=False, verbose=1)

print(history.params)
print(history.history)

scores = dqn.test(env, nb_episodes=1, visualize=False)

# +
#print(np.mean(scores.history['episode_reward']))
#dqn.get_config()
#scores = dqn.test(env, nb_episodes=1, visualize=False, verbose=1)
#test(self, env, nb_episodes=1, action_repetition=1, callbacks=None, visualize=True, nb_max_episode_steps=None, nb_max_start_steps=0, start_step_policy=None, verbose=1)
#print(np.mean(scores.history['episode_reward']))callbacks = callbacks[:]
