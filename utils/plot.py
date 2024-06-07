import gnuplotlib as gp


def plot(t_values_np, s_result_np, i_result_np, r_result_np):
    gp.plot(
        (t_values_np, s_result_np, {'legend': 'Susceptibles', 'with': 'lines lc rgb "green"'}),
        (t_values_np, i_result_np, {'legend': 'Infectados', 'with': 'lines lc rgb "blue"'}),
        (t_values_np, r_result_np, {'legend': 'Recuperados', 'with': 'lines lc rgb "red"'})
    )
