```python
import numpy as np

def minmax(x, axis=None):
    axis_none = axis is None
    
    if axis_none:
        x = x.flatten()[None]
        axis = 1
    
    y = np.max(x[None, :, :] * np.array([-1, 1])[:, None, None], axis=axis+1)
    y[0] *= -1
    
    if axis_none:
        return y[:,0]
    else:
        return y.T

def minmax2(x, axis=None):
    return np.concatenate([np.min(x, axis=axis)[...,None], np.max(x, axis=axis)[...,None]], axis=axis)
```


```python
x = np.arange(1000000).reshape(-1,10)

%timeit minmax(x)
%timeit minmax2(x)

%timeit minmax(x, axis=1)
%timeit minmax2(x, axis=1)
```

    9.2 ms ± 85 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    1.48 ms ± 26.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    13.6 ms ± 86.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    8.75 ms ± 35.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

