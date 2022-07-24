Do we get faster algebraic operations if the matrix contains blocks of `np.nan`?


```python
import numpy as np
```


```python
x = np.arange(1000000).reshape(-1, 2)

y = np.vstack([x, np.full((500000, 2), np.nan)])
%timeit y + 2 - np.array([2,20])[None]

z = np.vstack([x, x])
%timeit z + 2 - np.array([2,20])[None]
```

    16.6 ms ± 439 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    15.4 ms ± 208 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


No.
