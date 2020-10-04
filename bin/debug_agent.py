print(__name__)
import numpy as np
import os
import sys
import time
# TODO: This is setting the absolute import path here,
# but seems a bit strange to hard code in a path.
# Worth investigating more, maybe relative instead.
print('sys path 0', sys.path[0])
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import multiagent.scenarios as scenarios
from multiagent.environment import MultiAgentEnv
from multiagent.policy import InteractivePolicy


if __name__ == '__main__':
    scenario = "simple.py"
    scenario = scenarios.load(scenario).Scenario()

    world = scenario.make_world()

    # Create a multi-agent environment
    env = MultiAgentEnv(
        world,
        reset_callback=scenario.reset_world,
        reward_callback=scenario.reward,
        observation_callback=scenario.observation,
        info_callback=None,
        shared_viewer=False
    )

    # Render call to create viewer window (necessary only for interactive policies)
    env.render()

    # Create interactive policies for each agent
    policies = [InteractivePolicy(env, i) for i in range(env.n)]

    obs_n = env.reset()
    for i in range(10):
        # Collect experiences from all agents by querying
        # actions from the current policies of each agent.
        act_n = []
        # for i, policy in enumerate(policies):
        #     act_n.append(policy.action(obs_n[i]))
        rand_action = np.random.randint(0, 4)
        actions = np.zeros(5)
        actions[4] = 1.0
        act_n.append(actions)
        # Perform actions from agents in the environment
        obs_n, reward_n, done_n, _ = env.step(act_n)

        # Render all agent views
        env.render()

        # Display rewards
        for agent in env.world.agents:
            print('Experience:', i, 'action taken:', actions)
            print(agent.name + " reward: %0.3f" % env._get_reward(agent))
        time.sleep(2)
    print('done')