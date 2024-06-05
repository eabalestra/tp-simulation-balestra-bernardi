import gnuplotlib as gp
import numpy as np

s0 = 763
i0 = 1
r0 = 0
h = 0.05  # paso de integracion
s_euler_values = {}
i_euler_values = {}
r_euler_values = {}


def s(t, beta, retired_rate):
    if t <= 0:
        return s0
    elif t in s_euler_values:
        return s_euler_values[t]

    derivative_of_s = (-beta) * s(t - h, beta, retired_rate) * i(t - h, beta, retired_rate)
    euler = s(t - h, beta, retired_rate) + h * derivative_of_s
    s_euler_values[t] = euler

    return euler


def i(t, beta, retired_rate):
    if t <= 0:
        return i0
    elif t in i_euler_values:
        return i_euler_values[t]

    derivative_of_i = (beta * s(t - h, beta, retired_rate) * i(t - h, beta, retired_rate) - retired_rate *
                       i(t - h, beta, retired_rate))
    euler_result = i(t - h, beta, retired_rate) + h * derivative_of_i
    i_euler_values[t] = euler_result

    return euler_result


def r(t, beta, retired_rate):
    if t <= 0:
        return r0
    elif t in r_euler_values:
        return r_euler_values[t]

    derivative_of_r = retired_rate * i(t - h, beta, retired_rate)
    euler_result = r(t - h, beta, retired_rate) + h * derivative_of_r
    r_euler_values[t] = euler_result

    return euler_result


if __name__ == '__main__':
    beta = 0.0022
    retired_rate = 0.4477

    t_values_np = np.arange(0, 20, h)
    s_result_np = np.array([s(t, beta, retired_rate) for t in t_values_np])
    i_result_np = np.array([i(t, beta, retired_rate) for t in t_values_np])
    r_result_np = np.array([r(t, beta, retired_rate) for t in t_values_np])

    gp.plot(
        (t_values_np, s_result_np, {'legend': 'Susceptibles', 'with': 'lines lc rgb "green"'}),
        (t_values_np, i_result_np, {'legend': 'Infectados', 'with': 'lines lc rgb "blue"'}),
        (t_values_np, r_result_np, {'legend': 'Recuperados', 'with': 'lines lc rgb "red"'})
    )
