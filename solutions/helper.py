import os

base = os.path.dirname(os.path.realpath(__file__))

def nrml(name):
    return os.path.join(os.path.dirname(base), "inputs", name)