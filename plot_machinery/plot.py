import perfplot
import numpy as np

_data_func = None
_kernels = []
_kernel_labels = []

_steps = None

# a decorator to highlight the function to be used to generate data
def data(steps):
    global _steps
    _steps = steps

    def decorator_data(func):
        global _data_func
        _data_func = func
        return func

    return decorator_data


# a decorator to highlight kernels
def kernel(label):
    global _kernel_labels
    _kernel_labels.append(label)

    def decorator_kernel(func):
        global _kernels
        _kernels.append(func)
        return func

    return decorator_kernel


def plot(target_time_per_measurement=1.e-3):
    perfplot.show(
        setup=_data_func,
        kernels=_kernels,
        labels=_kernel_labels,
        n_range=_steps,
        xlabel="n",
        target_time_per_measurement=target_time_per_measurement,
    )
