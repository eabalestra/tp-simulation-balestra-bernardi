def derivative_function_of_s(s, i, beta):
    return (-beta) * s * i


def derivative_function_of_i(s, i, beta, retired_rate):
    return (beta * s * i) - (retired_rate * i)


def derivative_function_of_r(i, retired_rate):
    return retired_rate * i
