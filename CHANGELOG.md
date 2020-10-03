# Change Log

All notable changes to original project will be documented in this file.

## Changed
- Gym packaged was updated and removed `gym.spaces.prng`. Usage of `prng` in the code is  
replaced with:  
```
randn = np.random.RandomState()
random_array = randn.rand(number_of_discrete_spaces) 
```
Credit to https://github.com/openai/multiagent-particle-envs/issues/53#issue-498627626
