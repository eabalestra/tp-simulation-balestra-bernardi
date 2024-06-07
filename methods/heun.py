import numpy as np
from utils.derivatives import derivative_function_of_s, derivative_function_of_i, derivative_function_of_r

s_heun_values = {}
i_heun_values = {}
r_heun_values = {}


class Heun:
    def __init__(self, s0, i0, r0, h):
        self.s0 = s0
        self.i0 = i0
        self.r0 = r0
        self.h = h

    def s(self, t, beta, retired_rate):
        if t <= 0:
            return self.s0
        elif t in s_heun_values:
            return s_heun_values[t]

        s_function = self.s(t - self.h, beta, retired_rate)
        i_function = self.i(t - self.h, beta, retired_rate)

        k1 = derivative_function_of_s(s_function, i_function, beta)
        k2 = derivative_function_of_s(s_function + self.h * k1, i_function + self.h * k1, beta)

        heun_result = s_function + 0.5 * self.h * (k1 + k2)

        s_heun_values[t] = heun_result

        return heun_result

    def i(self, t, beta, retired_rate):
        if t <= 0:
            return self.i0
        elif t in i_heun_values:
            return i_heun_values[t]

        s_function = self.s(t - self.h, beta, retired_rate)
        i_function = self.i(t - self.h, beta, retired_rate)

        k1 = derivative_function_of_i(s_function, i_function, beta, retired_rate)
        k2 = derivative_function_of_i(s_function + self.h * k1, i_function + self.h * k1, beta, retired_rate)

        heun_result = i_function + 0.5 * self.h * (k1 + k2)

        i_heun_values[t] = heun_result

        return heun_result

    def r(self, t, beta, retired_rate):
        if t <= 0:
            return self.r0
        elif t in r_heun_values:
            return r_heun_values[t]

        i_function = self.i(t - self.h, beta, retired_rate)
        r_function = self.r(t - self.h, beta, retired_rate)

        k1 = derivative_function_of_r(i_function, retired_rate)
        k2 = derivative_function_of_r(i_function + self.h * k1, retired_rate)

        heun_result = r_function + 0.5 * self.h * (k1 + k2)

        r_heun_values[t] = heun_result

        return heun_result

    def run(self, days, beta, retired_rate):
        """
        Run the SIR model simulation using the Heun method.

        :param days: The number of days to run the simulation.
        :param beta: The infection rate parameter in the SIR model.
        :param retired_rate: The recovery rate parameter in the SIR model.
        :return: Four numpy arrays representing the time points and the number
        of susceptible, infected, and recovered individuals at each time point.
        """
        t_values_np = np.arange(0, days, self.h)
        s_result_np = np.array([self.s(t, beta, retired_rate) for t in t_values_np])
        i_result_np = np.array([self.i(t, beta, retired_rate) for t in t_values_np])
        r_result_np = np.array([self.r(t, beta, retired_rate) for t in t_values_np])

        return t_values_np, s_result_np, i_result_np, r_result_np
