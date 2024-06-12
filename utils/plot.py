import matplotlib.pyplot as plt

def plot(t_values_np, s_result_np, i_result_np, r_result_np, t_values_np_heun, s_result_np_heun, i_result_np_heun, r_result_np_heun):
    plt.figure(figsize=(10, 6))

    plt.plot(t_values_np, s_result_np, 'b-', linewidth=2, label='Susceptibles Euler')
    plt.plot(t_values_np, i_result_np, 'r-', linewidth=2, label='Infectados Euler')
    plt.plot(t_values_np, r_result_np, 'g-', linewidth=2, label='Recuperados Euler')

    plt.plot(t_values_np_heun, s_result_np_heun, 'c-', linewidth=2, label='Susceptibles Heun')
    plt.plot(t_values_np_heun, i_result_np_heun, 'm-', linewidth=2, label='Infectados Heun')
    plt.plot(t_values_np_heun, r_result_np_heun, 'y-', linewidth=2, label='Recuperados Heun')

    plt.xlabel('Tiempo (días)')
    plt.ylabel('Número de individuos')
    plt.title('SIR Model')
    plt.grid(True)
    plt.legend()

    plt.savefig('sir_model.png')