from methods.method import Method
from utils.derivatives import derivative_function_of_s, derivative_function_of_i, derivative_function_of_r


class Heun(Method):

    def s(self, t, beta, retired_rate):
        if self.is_initial_or_previous_time(t):
            return self.s0
        elif t in self.s_values:
            return self.s_values[t]

        s_function = self.s(t - self.h, beta, retired_rate)
        i_function = self.i(t - self.h, beta, retired_rate)

        k1 = derivative_function_of_s(s_function, i_function, beta)
        k2 = derivative_function_of_s(s_function + self.h * k1, i_function + self.h * k1, beta)

        heun_result = s_function + 0.5 * self.h * (k1 + k2)

        self.s_values[t] = heun_result

        return heun_result

    def i(self, t, beta, retired_rate):
        if self.is_initial_or_previous_time(t):
            return self.i0
        elif t in self.i_values:
            return self.i_values[t]

        s_function = self.s(t - self.h, beta, retired_rate)
        i_function = self.i(t - self.h, beta, retired_rate)

        k1 = derivative_function_of_i(s_function, i_function, beta, retired_rate)
        k2 = derivative_function_of_i(s_function + self.h * k1, i_function + self.h * k1, beta, retired_rate)

        heun_result = i_function + 0.5 * self.h * (k1 + k2)

        self.i_values[t] = heun_result

        return heun_result

    def r(self, t, beta, retired_rate):
        if self.is_initial_or_previous_time(t):
            return self.r0
        elif t in self.r_values:
            return self.r_values[t]

        i_function = self.i(t - self.h, beta, retired_rate)
        r_function = self.r(t - self.h, beta, retired_rate)

        k1 = derivative_function_of_r(i_function, retired_rate)
        k2 = derivative_function_of_r(i_function + self.h * k1, retired_rate)

        heun_result = r_function + 0.5 * self.h * (k1 + k2)

        self.r_values[t] = heun_result

        return heun_result
