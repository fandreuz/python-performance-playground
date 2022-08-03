[![Benchmarks](https://github.com/fAndreuzzi/python-performance-playground/actions/workflows/main.yml/badge.svg)](https://github.com/fAndreuzzi/python-performance-playground/actions/workflows/main.yml)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
<img src='https://img.shields.io/badge/Code%20style-Black-%23000000'/>

# python-performance-playground
A performance analysis repository for small Python snippets.

## Goal
Ever felt the need to test multiple methods to solve the same, self-contained,
easily-explainable Python problem, in order to find the most performant one?
Me too, but I'm always too lazy to generalize the one/two lines I wrote, prepare
a function and run the experiments over a meaningful set of inputs.

I've collected some of my snippets over a few months, and packed them nicely
into a repository, along with an accomodating GitHub action which cares about
running the experiments and doing the plots.

### Software and hardware
Benchmarks may vary across Python versions, for this reason we provide plots
for the latest 3 stable versions:
| **Python version** | **Branch** |
|:---|:---|
| `3.10` | [`master`](https://github.com/fAndreuzzi/python-performance-playground/) |
| `3.9` | [`python-3.9`](https://github.com/fAndreuzzi/python-performance-playground/tree/python-3.9)  |
| `3.8` | [`python-3.8`](https://github.com/fAndreuzzi/python-performance-playground/tree/python-3.8) |

Benchmarks run on the GitHub Actions runner `ubuntu-latest`, updated info about
the hardware details of the runner available
[here](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources).

### Content
| **Directory** | **Content** |
|:---|:---|
| [`./python/`](python/) | General snippets in pure Python |
| [`./numpy/`](numpy/) | Comparisons among multiple equivalent NumPy (or Python) snippets  |
| [`./dask/`](dask/) | Benchmarks of equivalent Dask snippets. |

## Contributing
Snippets welcome! Just prepare a PR following the standard format in the
repository:
- Find the right place for your snippet (e.g. `numpy`, `python`, `dask`, ...)
- Find an appropriate name for your snippet
- Provide an `.ipynb` files which runs the experiments (please use the
  annotations `@kernel, @data, ...` like we did for the other snippets)
- Let the bot do its work (after your PR is merged).

## Examples
| Slice VS List write in NumPy |     Pseudo-Hankel matrix     |
| -------------------------------------------------------------- | -------------------------------------------------------------- |
| [![image](https://user-images.githubusercontent.com/8464342/180768227-b8429aa5-98cc-4a59-8277-8d00854106fb.png)](numpy/write-in-slices) | [![image](https://user-images.githubusercontent.com/8464342/180768655-5caaeb92-bd1c-4900-a2f6-d92a700d0138.png)](numpy/hankel-matrix) |

## Disclaimer
- Benchmarks in this repository are usually very simple, use dummy data and are
  in general dried of any meaning except for the pursue for performance.
- Benchmarks in this repository are assumed to be valid only for common
  use-cases, while industrial or scientific applications might suffer of
  asymptotic pathological patterns which deserve a customized treatment.
- I do not claim in any way that benchmarks in this repository are enough to
  provide a full view of the performance of the methods treated. For instance
  I do not probe memory access or caching with tailored data to stress the
  computer resources. Again, my aim is to see what happens with common
  use-cases.

## Contributors
- Francesco Andreuzzi (CERN, SISSA) -- andreuzzi.francesco@gmail.com
