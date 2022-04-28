import matplotlib.pyplot as plt
import numpy as np

def read_data(file_path):
    with open(file_path, "r") as file:
        data_str = file.read().split()
        data = np.array(list(map(float, data_str)))
    return data

def to_volt(data):
    for i in range(len(data)):
        data[i] = data[i] / (2 ** 8) * 3.3

def get_charg_t(data, discret):
    return data.argmax()*discret


def plot_data():
    data = read_data("data.txt")
    settings = read_data("settings.txt")

    discret = settings[0]
    exp_time = settings[2]
    
    to_volt(data)

    values_y = data
    values_x = np.arange(start = discret, stop = exp_time, step = discret)

    charging_time = get_charg_t(data, discret)
    discharging_time  = exp_time - charging_time

    figure, axes = plt.subplots(figsize = (20, 15), dpi = 150)

    axes.minorticks_on()

    plt.plot(values_x, values_y, color = "black", label = "U(t)", marker = "o", markevery = 300, markersize = 10, linewidth = 0.5)
    plt.text(0.8 *values_x.max(), 0.8 *values_y.max(), 
        f"Experiment time: {exp_time:.2f} s\n"
        f"Charging time: {charging_time:.2f}s\n"
        f"Discharging time: {discharging_time:.2f}s\n")
    plt.title("Процесс зарядки и разрядки конденсатора RC цепи")
    plt.xlabel("Time, s")
    plt.ylabel("Voltage, V")

    plt.xlim([0, exp_time])
    plt.ylim([0, max(data) + 0.1])

    plt.grid(which = "major", linestyle = '-', linewidth = 1)
    plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

    plt.savefig("figure.svg")

    plt.show()


    

plot_data()