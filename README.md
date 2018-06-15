# Software Engineering Techniques at SciPy 2018

Monday, July 9 at 1:30 PM

As a user of scientific Python libraries like NumPy, Pandas, and matplotlib it’s
worth asking how the maintainers of those libraries manage to keep the codebases
running quickly and correctly when there are large codebases, many features, and
many contributors. Those developers have to think deliberately about the design
of their code; they use a number of techniques to make their lives easier, among
them testing, debugging, profiling, and packaging. Exactly as these techniques
are useful to library maintainers, they can also be useful to researchers, data
scientists, and analysts who are trying keep code fast and correct as it
undergoes changes. This tutorial will introduce attendees to deliberate code
design, testing using the pytest framework, Python’s debugging tools, profiling
code to understand performance, and how to reuse code in multiple places.

See the tutorial description on the conference website
[here](https://scipy2018.scipy.org/ehome/index.php?eventid=299527&tabid=711308&cid=2229599&sessionid=21547378&sessionchoice=1&).

## Setup Instructions

### Installation

If you don't already have Anaconda installed, download and install Anaconda
for **Python 3**:
https://www.anaconda.com/download.

Please do at least the download and install of Anaconda before coming to the tutorial!
We can help with further setup at the tutorial.

If you'd like to do your own setup, we'll be using the following Python libraries:

- [Jupyter Notebook](https://jupyter.org/)
- [ipython](https://ipython.org/)
- [ipdb](https://pypi.org/project/ipdb/)
- [pytest](https://docs.pytest.org/en/latest/)
- [snakeviz](https://jiffyclub.github.io/snakeviz/)

### Creating a conda environment (OPTIONAL)

The basic Anaconda install has almost all that's needed for this tutorial,
but if you'd like to create an isolated environment for this tutorial you
can use the included `environment.yaml` file according to the
[conda env setup instructions](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
by running the following in the root of this repository:

```sh
conda env create -f environment.yaml
```

This will create an environment called `scipy2018-swe`.

### Testing Your Setup

You can test your Anaconda installation using
[these instructions](https://conda.io/docs/user-guide/install/test-installation.html).

In this tutorial you'll be running code at the command line,
so please make sure you can run Python there.
As an example, try running the following command at the command line:

```sh
python -c 'print("This works!")'
```

Or, on Windows, try the following:

```sh
py -c 'print("This works!")'
```

You will see `This works!` printed when it works.

### Troubleshooting Links

- Running Python on Windows: https://docs.python.org/3.6/using/windows.html
