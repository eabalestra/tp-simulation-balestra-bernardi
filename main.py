from methods.euler_method import EulerMethod
from utils.plot import plot

if __name__ == '__main__':
    euler_method = EulerMethod(s0=763, i0=1, r0=1, h=0.05)

    beta = 0.0022
    retired_rate = 0.4477

    t_values_np, s_result_np, i_result_np, r_result_np = euler_method.run(20, beta, retired_rate)

    plot(t_values_np, s_result_np, i_result_np, r_result_np)
