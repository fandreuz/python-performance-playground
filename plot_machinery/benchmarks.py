import timeit
import numpy as np


def do_benchmarks(
    steps,
    data_gen_func,
    number_gen_func,
    kernels,
    kernel_labels,
    verbose=False,
):
    times = np.empty((len(steps), len(kernels)), dtype=float)
    for idx, step in enumerate(steps):
        data = data_gen_func(step)
        number = number_gen_func(step)

        if verbose:
            print("Doing step {} with {} repetitions".format(step, number))

        for kidx, kernel in enumerate(kernels):
            if verbose:
                print("Doing kernel {}".format(kidx))

            times[idx, kidx] = timeit.timeit(
                "kernel(*data)", globals=locals(), number=number
            )

        times[idx] /= number

    return times
