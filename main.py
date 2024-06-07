from methods.euler_method import EulerMethod
from methods.heun import Heun
from utils.plot import plot

if __name__ == '__main__':
    euler_method = EulerMethod(s0=763, i0=1, r0=1, h=0.07)
    heun_method = Heun(s0=763, i0=1, r0=1, h=0.07)

    beta = 0.0022
    retired_rate = 0.4477

    t_values_np, s_result_np, i_result_np, r_result_np = euler_method.run(20, beta, retired_rate)
    t_values_np_heun, s_result_np_heun, i_result_np_heun, r_result_np_heun = heun_method.run(20, beta, retired_rate)

    plot(t_values_np, s_result_np, i_result_np, r_result_np, t_values_np_heun, s_result_np_heun, i_result_np_heun, r_result_np_heun)