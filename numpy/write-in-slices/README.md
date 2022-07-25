## Writing in slices to `np.ndarray`

Is writing in slices more efficient than writing through contiguous indexing with a list? e.g. `[10, 11, 12]`


```python
import numpy as np
from plot_machinery.plot import data, kernel, plot, repeat_count, clear_kernels
```


```python
clear_kernels()


@kernel()
def slices_write(x):
    l = len(x) // 2
    x[:l] = 4
    x[l:] = 2


@kernel()
def list_indexing_write(x):
    l = len(x)
    x[np.arange(l // 2)] = 4
    x[np.arange(l // 2, l)] = 2


@data(steps=[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000])
def data_gen(step):
    return (np.zeros((step, 10), dtype=int),)
```


```python
plot(logx=True, logy=True, xlabel="Rows", title="X.shape = (*, 10)")
```


    
![png](README_files/README_3_0.png)
    

