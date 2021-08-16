


# Leibniz Series
# π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...


def calculate_pi(n_terms):
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator/denominator)
        denominator += 2.0
        operation *= -1.0 # change sign
    return pi
