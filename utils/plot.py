import gnuplotlib as gp


def plot(t_values_np, s_result_np, i_result_np, r_result_np, t_values_np_heun, s_result_np_heun, i_result_np_heun, r_result_np_heun):
    gp.plot(
        (t_values_np, s_result_np, {'legend': 'Susceptibles Euler', 'with': 'lines lc rgb "green"'}),
        (t_values_np, i_result_np, {'legend': 'Infectados Euler', 'with': 'lines lc rgb "blue"'}),
        (t_values_np, r_result_np, {'legend': 'Recuperados Euler', 'with': 'lines lc rgb "red"'}),
        (t_values_np_heun, s_result_np_heun, {'legend': 'Susceptibles Heun', 'with': 'lines lc rgb "light-green"'}),
        (t_values_np_heun, i_result_np_heun, {'legend': 'Infectados Heun', 'with': 'lines lc rgb "light-blue"'}),
        (t_values_np_heun, r_result_np_heun, {'legend': 'Recuperados Heun', 'with': 'lines lc rgb "light-red"'})
    )