#!/usr/bin/env python
from problem import Problem
from simanneal import Annealer

class Solver(Annealer):

    problem = None

    def __init__(self, problem):
        self.problem = problem
        # TODO generate initial state based on the problem
        init_state = []
        super(Solver, self).__init__(init_state)

    def move(self):
        # TODO mess with self.state
        pass

    def energy(self):
        e = 0
        # TODO calc e
        return e

def processData(problem, steps=100000):
    solver = Solver(problem)
    solver.steps = steps
    # TODO investigate your best copying strategy
    # "slice" if states are represented as lists
    # other choices are "deepcopy" and "method"
    solver.copy_strategy = "slice"
    print "\033[93mAnnealing...\033[0m"
    solution, e = solver.anneal()
    print "\033[92mFound solution with energy {}\033[0m\n".format(e)
    return solution