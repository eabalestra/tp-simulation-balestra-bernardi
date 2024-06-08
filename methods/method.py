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
