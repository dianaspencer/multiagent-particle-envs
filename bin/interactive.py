#!/usr/bin/env python
import argparse
import os
import sys
import multiagent.scenarios as scenarios

from multiagent.environment import MultiAgentEnv
from multiagent.policy import InteractivePolicy

sys.path.insert(1, os.path.join(sys.path[0], '..'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('-s', '--scenario', default='simple.py', help='Path of the scenario Python script.')
    args = parser.parse_args()

    scenario = scenarios.load(args.scenario).Scenario()

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
    while True:
        # Collect experiences from all agents by querying
        # actions from the current policies of each agent.
        act_n = []
        for i, policy in enumerate(policies):
            act_n.append(policy.action(obs_n[i]))

        # Perform actions from agents in the environment
        obs_n, reward_n, done_n, _ = env.step(act_n)

        # Render all agent views
        env.render()

        # Display rewards
        # for agent in env.world.agents:
        #    print(agent.name + " reward: %0.3f" % env._get_reward(agent))
