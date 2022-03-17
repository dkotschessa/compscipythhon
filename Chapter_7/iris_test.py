import csv
from util import normalize_by_feature_scaling
from network import Network
from random import shuffle

if __name__ == "__main__":
    iris_parameters = []
    iris_classification = []
    iris_species = []
    with open("iris.csv", "r") as iris_file:
        irises = list(csv.reader(iris_file))
        shuffle(irises)  # get our lisst of data in random order
        for iris in irises:
            parameters = [float(n) for n in iris[:4]]
            iris_parameters.append(parameters)
            species = iris[4]
            if species == "Iris-setosa":
                iris_classification.append([1.0, 0.0, 0.0])
            elif species == "Iris-versicolor":
                iris_classification.append([0.0, 1.0, 0.0])
            else:
                iris_classification.append([0.0, 0.0, 1.0])
            iris_species.append(species)
    normalize_by_feature_scaling(iris_parameters)

    iris_network = Network([4, 6, 3], 0.3)

    def iris_interpret_output(output):
        if max(output) == output[0]:
            return "Iris-setosa"
        elif max(output) == output[1]:
            return "Iris-versicolor"
        else:
            return "Iris-virgincia"

    # train over the first 140 irises in the data set 50 times
    iris_trainers = iris_parameters[0:140]
    iris_trainers_corrects = iris_classification[0:140]

    for _ in range(50):
        iris_network.train(iris_trainers, iris_trainers_corrects)

    # test over the last 10 of the irises in the data set
    iris_testers = iris_parameters[140:150]
    iris_testers_corrects = iris_species[140:150]
    iris_results = iris_network.validate(
        iris_testers, iris_testers_corrects, iris_interpret_output
    )
    print(f"{iris_results[0]} correct of {iris_results[1]} = {iris_results[2] * 100}%")
