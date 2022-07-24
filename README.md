# python-performance-playground
A performance analysis repository for of all those Python snippets not big
enough to make a library.

## Goal
Ever felt the need to test multiple methods to solve the same, self-contained,
easily-explainable Python problem, in order to check the most performant one?
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
  annotations `@kernel, @data, ...` like I did we did for the other snippets)
- Let the bot do its work (after your PR is merged).

## Disclaimer
This repository aims at providing a general idea of which approach might perform
the best in most situation, but I would recommend doing more in-depth
experiments with the actual data you're going to deal with, on the actual
architecture you are going to use. Some of the snippets proposed here might fail
asymptotically, for instance due to memory constraints.

## Contributors
- Francesco Andreuzzi (CERN, SISSA) -- andreuzzi.francesco@gmail.com
