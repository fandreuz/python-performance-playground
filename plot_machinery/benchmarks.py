import timeit
import numpy as np

N_REPEAT = 20


def do_benchmarks(
    steps,
    data_gen_func,
    number_gen_func,
    kernels,
    kernel_labels,
    verbose=False,
):
    times = np.empty((len(steps), len(kernels), 2), dtype=float)
    for idx, step in enumerate(steps):
        data = data_gen_func(step)

        number = number_gen_func(step)
        # adjust number since we use timeit.repeat
        number = int(np.ceil(number / 10))

        if verbose:
            print("Doing step {} with {} repetitions".format(step, number))

        for kidx, kernel in enumerate(kernels):
            if verbose:
                print("Doing kernel {}".format(kidx))

            tm = (
                np.array(
                    timeit.repeat(
                        "kernel(*data)",
                        globals=locals(),
                        number=number,
                        repeat=N_REPEAT,
                    )
                )
                / number
            )
            times[idx, kidx, 0] = np.mean(tm)
            times[idx, kidx, 1] = np.var(tm, ddof=1)

    return times
