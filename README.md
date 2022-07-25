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

## Contributing
Snippets welcome! Just prepare a PR following the standard format in the
repository:
- Find the right place for your snippet (e.g. `numpy`, `python`, `dask`, ...)
- Find an appropriate name for your snippet
- Provide an `.ipynb` files which runs the experiments (please use the
  annotations `@kernel, @data, ...` like we did for the other snippets)
- Let the bot do its work (after your PR is merged).

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
