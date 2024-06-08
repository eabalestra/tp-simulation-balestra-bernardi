from methods.euler import Euler
from methods.heun import Heun
from utils.plot import plot

if __name__ == '__main__':
    s0 = 763
    i0 = 1
    r0 = 0
    h = 0.05
    days = 20

    euler_method = Euler(s0, i0, r0, h)
    heun_method = Heun(s0, i0, r0, h)

    beta = 0.0022
    retired_rate = 0.4477

    t_values_np, s_result_np, i_result_np, r_result_np = euler_method.run(days, beta, retired_rate)
    t_values_np_heun, s_result_np_heun, i_result_np_heun, r_result_np_heun = heun_method.run(days, beta, retired_rate)

    plot(t_values_np, s_result_np, i_result_np, r_result_np, t_values_np_heun, s_result_np_heun, i_result_np_heun, r_result_np_heun)