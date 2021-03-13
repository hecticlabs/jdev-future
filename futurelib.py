from math import *
import random
import bisect
import collections
import base64
import json
import requests

class quantum:
    @staticmethod
    def load(path):
        ff = None
        out = ""
        with open(path, 'r') as f:
            ff = f.read().splitlines()
        for line in ff:
            if line.startswith("//") or line.startswith("#"):
                continue
            elif line.strip() == "":
                continue
            out += line + "\n"
        return out[:-1]

    @staticmethod
    def simplify_algorithm(algo_str, values):
        for value in values:
            algo_str = algo_str.replace(value, str(values[value]))
        return algo_str

    @staticmethod
    def solve_arithmetic(operations):
        return eval(operations)

    @staticmethod
    def solve_single_quantum_algorithm(algo_str, superposition):
        X, Y = superposition
        V = []
        P = []
        for i in range(len(X)):
            algo = quantum.simplify_algorithm(algo_str, {
                "X": X[i],
                "Y": Y[i]
            })
            algo = algo.splitlines()
            table = {}
            for line in algo:
                line = line.split("=")
                table[line[0].strip()] = quantum.solve_arithmetic(line[1].strip())
            V.append(table['V'])
            P.append(table['P'])
        return (V, quantum.normalize_superposition_weights(P))

    @staticmethod
    def solve_dual_quantum_algorithm(algo_str, superposition1, superposition2):
        X1, Y1 = superposition1
        X2, Y2 = superposition2
        V = []
        P = []
        for i in range(len(X1)):
            algo = quantum.simplify_algorithm(algo_str, {
                "X1": X1[i],
                "Y1": Y1[i],
                "X2": X2[i],
                "Y2": Y2[i]
            })
            algo = algo.splitlines()
            table = {}
            for line in algo:
                line = line.split("=")
                table[line[0].strip()] = quantum.solve_arithmetic(line[1].strip())
            V.append(table['V'])
            P.append(table['P'])
        return (V, quantum.normalize_superposition_weights(P))

    @staticmethod
    def solve_trial_quantum_algorithm(algo_str, superposition1, superposition2, superposition3):
        X1, Y1 = superposition1
        X2, Y2 = superposition2
        X3, Y3 = superposition3
        V = []
        P = []
        for i in range(len(X1)):
            algo = quantum.simplify_algorithm(algo_str, {
                "X1": X1[i],
                "Y1": Y1[i],
                "X2": X2[i],
                "Y2": Y2[i],
                "X3": X3[i],
                "Y3": Y3[i]
            })
            algo = algo.splitlines()
            table = {}
            for line in algo:
                line = line.split("=")
                table[line[0].strip()] = quantum.solve_arithmetic(line[1].strip())
            V.append(table['V'])
            P.append(table['P'])
        return (V, quantum.normalize_superposition_weights(P))

    @staticmethod
    def solve_quadral_quantum_algorithm(algo_str, superposition1, superposition2, superposition3, superposition4):
        X1, Y1 = superposition1
        X2, Y2 = superposition2
        X3, Y3 = superposition3
        X4, Y4 = superposition4
        V = []
        P = []
        for i in range(len(X1)):
            algo = quantum.simplify_algorithm(algo_str, {
                "X1": X1[i],
                "Y1": Y1[i],
                "X2": X2[i],
                "Y2": Y2[i],
                "X3": X3[i],
                "Y3": Y3[i],
                "X4": X4[i],
                "Y4": Y4[i]
            })
            algo = algo.splitlines()
            table = {}
            for line in algo:
                line = line.split("=")
                table[line[0].strip()] = quantum.solve_arithmetic(line[1].strip())
            V.append(table['V'])
            P.append(table['P'])
        return (V, quantum.normalize_superposition_weights(P))

    @staticmethod
    def cdf(weights):
        total = sum(weights)
        result = []
        cumsum = 0
        for w in weights:
            cumsum += w
            result.append(cumsum / total)
        return result

    @staticmethod
    def measure_quantum_superposition(superposition):
        (population, weights) = superposition
        assert len(population) == len(weights)
        cdf_vals = quantum.cdf(weights)
        x = random.random()
        idx = bisect.bisect(cdf_vals, x)
        for i in range(len(superposition[0])):
            if i == idx:
                superposition[1][i] = 1
            else:
                superposition[1][i] = 0
        return population[idx]

    @staticmethod
    def normalize_superposition_weights(weights):
        new = []
        _max = sum(weights)
        if _max == 0:
            raise EnvironmentError("A superposition where the weights sum up to 0 is physically forbidden")
        for i in weights:
            new.append(i / _max)
        return new

    @staticmethod
    def fancy_superposition(superposition):
        out = ""
        for i in range(len(superposition[0])):
            weight = superposition[1][i]
            value = superposition[0][i]
            out += str(round(float(weight), 2)) + "|" + str(value) + "> + "
        return out[:-3]

    @staticmethod
    def create_superposition(values, weights):
        return (values, weights)
