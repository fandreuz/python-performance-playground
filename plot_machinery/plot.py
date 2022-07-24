import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({"font.size": 25})

from .benchmarks import do_benchmarks

_repeat_func = lambda _: 1000
_data_func = None
_kernels = []
_kernel_labels = []

_steps = None


def clear_kernels():
    global _kernels
    _kernels = []
    global _kernel_labels
    _kernel_labels = []


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
def kernel(label=None):
    if label:
        global _kernel_labels
        _kernel_labels.append(label)

    def decorator_kernel(func):
        global _kernels
        _kernels.append(func)

        if not label:
            global _kernel_labels
            _kernel_labels.append(func.__name__)

        return func

    return decorator_kernel


# a decorator to highlight kernels
def repeat_count(func):
    global _repeat_func
    _repeat_func = func
    return func


def plot(
    target_time_per_measurement=1.0e-2,
    xlabel=None,
    logx=False,
    logy=False,
    title=None,
    create_figure=(20, 8),
    verbose=False,
):
    if create_figure:
        plt.figure(figsize=(20, 8))

    benchmark = do_benchmarks(
        _steps,
        _data_func,
        _repeat_func,
        _kernels,
        _kernel_labels,
        verbose=verbose,
    )

    plt.plot(_steps, benchmark, "-o", label=_kernel_labels)

    plt.ylabel("Time (seconds)")
    if xlabel:
        plt.xlabel(xlabel)
    if title:
        plt.title(title)

    if logx:
        plt.xscale("log")
    if logy:
        plt.yscale("log")

    plt.legend()
    plt.grid()


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()
