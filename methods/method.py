from abc import ABC, abstractmethod
import numpy as np


class Method(ABC):
    def __init__(self, s0, i0, r0, h):
        self.s0 = s0
        self.i0 = i0
        self.r0 = r0
        self.h = h
        self.s_values = {}
        self.i_values = {}
        self.r_values = {}

    @abstractmethod
    def s(self, t, beta, retired_rate):
        pass

    @abstractmethod
    def i(self, t, beta, retired_rate):
        pass

    @abstractmethod
    def r(self, t, beta, retired_rate):
        pass

    def is_initial_or_previous_time(self, t):
        return t <= 0 or t - self.h <= 0

    def run(self, days, beta, retired_rate):
        """
        Runs the simulation of the SIR model using the specified method.

        :param days: Total number of days for the simulation.
        :param beta: Per-capita transmission rate of the disease.
        :param retired_rate: Removal rate (rate at which infected individuals recover or die).
        :return: Tuples of numpy arrays containing the values of time, susceptible, infected, and removed individuals.
        """
        try:
            # Generate an array of time values from 0 to 'days' with a step size of 'h'
            t_values_np = np.arange(0, days, self.h)

            # Calculate the values of susceptibles S(t) for each value of t in t_values_np
            s_result_np = np.array([self.s(t, beta, retired_rate) for t in t_values_np])

            # Calculate the values of infected I(t) for each value of t in t_values_np
            i_result_np = np.array([self.i(t, beta, retired_rate) for t in t_values_np])

            # Calculate the values of removed R(t) for each value of t in t_values_np
            r_result_np = np.array([self.r(t, beta, retired_rate) for t in t_values_np])

            # Return a tuple with the arrays of time values, susceptibles, infected, and removed individuals
            return t_values_np, s_result_np, i_result_np, r_result_np
        except Exception as e:
            print(f"An error occurred during the simulation: {e}")
            return None
