# Change Log

All notable changes to original project will be documented in this file.

## Changed
- Gym packaged was updated and removed `gym.spaces.prng`. Usage of `prng` in the code is  
replaced with `numpy.RandomState()`.  
Ref: https://github.com/openai/multiagent-particle-envs/issues/53#issue-498627626  
Example,
```
randn = np.random.RandomState()
random_array = randn.rand(number_of_discrete_spaces) 
```


- Gym packaged was updated and removed `gym.utils.reraise`. Replace exception with following
`raise ImportError` from openai/gym PR.   
Ref: https://github.com/openai/gym/pull/1342/files#diff-1b44b524e6fab05325582263e37b261eR19-R34