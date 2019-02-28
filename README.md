# google_hashcode_py
A templated code to get you straight into the action!

# How to run it
Run `python main.py [name of input file] [number of steps for Simulated Annealing]`

### Note: You only need to provide the name of the input file, and not its path, since the code looks for it in the data folder

# Why (and how!) you should use it

This repo provides you with:

* `problem.py`: This is where the `Problem` class for your problem lives. Just add all the required fields to it.
* `input.py`: This includes the `readFile` function. Given the input file, you should instantiate a `Problem` object.
* `processing.py`: This includes a `Solver` class. It basically calls the Simulated Annealing algorithm,
  based on the `simanneal` python package. This is where all your hard work should go. You need to add code into the `constructor`, `move` and `energy` functions. If you are not familiar with Simulated Annealing, check the `simeanneal`'s repo here: https://github.com/perrygeo/simanneal
* `output.py`: This file automatically creates a tarball of your source code when the program is run, and is placed in a folder named under the time of execution. This is useful if you need to get back to a previous version of your code fast, and also 
want to quickly pair it with a results.txt file. Inside this file, you only need to add code into the `writeResults` function, based 
on the results of the Simulated Annealing algorithm.
* `main.py`: This is the driver of your code. You shouldn't need to change anything here.

