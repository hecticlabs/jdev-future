from futurelib import quantum
from futurelib import cloud

if __name__ == "__main__":
    # Creates a perfect superposition of the values in X
    X = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    Y = quantum.normalize_superposition_weights([ 1 for i in range(len(X)) ])
    INPUT = quantum.create_superposition(X, Y)

    # Loads our quantum single-state algorithm
    algo = quantum.load("single.ftc")

    future_api = cloud.connect_cloud("ERUTUF-veDj", "itsasecret")
    print(quantum.fancy_superposition(future_api.run_quantum(algo, [
        INPUT
    ])))

    # Solves the algorithm using the INPUT superposition
    result = quantum.solve_single_quantum_algorithm(algo, INPUT)

    # Displays fancy outputs and measures the output
    print("Input: " + quantum.fancy_superposition(INPUT))
    print("Output: " + quantum.fancy_superposition(result))
    print("Chosen result: " + str(quantum.measure_quantum_superposition(result)))

""" if __name__ == "__main__":
    # Creates a two perfect superpositions of the values in
    # X1 and X2
    X1 = [ 0, 0, 0, 1, 1, 1, 2, 2, 2 ]
    Y1 = quantum.normalize_superposition_weights([ 1 for i in range(len(X1)) ])
    INPUT1 = quantum.create_superposition(X1, Y1)

    X2 = [ 0, 1, 2, 0, 1, 2, 0, 1, 2 ]
    Y2 = quantum.normalize_superposition_weights([ 1 for i in range(len(X2)) ])
    INPUT2 = quantum.create_superposition(X2, Y2)

    # Loads our quantum dual-state algorithm
    algo = quantum.load("dual.ftc")

    # Solves the algorithm using the INPUT superposition
    result = quantum.solve_dual_quantum_algorithm(algo, INPUT1, INPUT2)

    # Displays fancy outputs and measures the output
    print("Output: " + quantum.fancy_superposition(result))
    print("Chosen result: " + str(quantum.measure_quantum_superposition(result)))
 """