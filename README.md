# libct
A fast approximate primal-dual solver for tracking-by-assignment cell-tracking problems. For running assue the [Gurobi](https://www.gurobi.com/) is installed. Meson is required for building (can be easily installed via pip). Afterwards:

> ./setup-dev-env

installs in a temporary directory and opens up a shell. To run cell-tracking run:

> python bin/ct <INPUT_FILE>

Where the INPUT_FILE is a cell tracking instance. 
