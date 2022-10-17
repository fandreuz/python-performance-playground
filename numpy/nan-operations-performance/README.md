## `np.nan` operations

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

    13.8 ms ± 160 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    13.7 ms ± 208 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


No.
