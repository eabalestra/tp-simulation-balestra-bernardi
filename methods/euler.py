from methods.method import Method
from utils.derivatives import derivative_function_of_s, derivative_function_of_i, derivative_function_of_r


class Euler(Method):
    def s(self, t, beta, retired_rate):
        if self.is_initial_or_previous_time(t):
            return self.s0
        elif t in self.s_values:
            return self.s_values[t]

        s_function = self.s(t - self.h, beta, retired_rate)
        i_function = self.i(t - self.h, beta, retired_rate)

        derivative_of_s = derivative_function_of_s(s_function, i_function, beta)
        euler = s_function + self.h * derivative_of_s

        self.s_values[t] = euler

        return euler

    def i(self, t, beta, retired_rate):
        if self.is_initial_or_previous_time(t):
            return self.i0
        elif t in self.i_values:
            return self.i_values[t]

        s_function = self.s(t - self.h, beta, retired_rate)
        i_function = self.i(t - self.h, beta, retired_rate)

        derivative_of_i = derivative_function_of_i(s_function, i_function, beta, retired_rate)
        euler_result = i_function + self.h * derivative_of_i

        self.i_values[t] = euler_result

        return euler_result

    def r(self, t, beta, retired_rate):
        if self.is_initial_or_previous_time(t):
            return self.r0
        elif t in self.r_values:
            return self.r_values[t]

        i_function = self.i(t - self.h, beta, retired_rate)
        r_function = self.r(t - self.h, beta, retired_rate)

        derivative_of_r = derivative_function_of_r(i_function, retired_rate)
        euler_result = r_function + self.h * derivative_of_r

        self.r_values[t] = euler_result

        return euler_result
