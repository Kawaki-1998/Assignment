import numpy as np
import matplotlib.pyplot as plt

def simulate_system(h, t_end, x1_0, x2_0, x3_0, u):
    t = np.arange(0, t_end, h)
    x1, x2, x3 = x1_0, x2_0, x3_0
    x1_arr, x2_arr, x3_arr, y_arr = [], [], [], []

    S1 = np.array([[0, 1, 0], [0, 0, 1], [-11, -17, -5]])
    S2 = np.array([0, 0, 1])
    S3 = np.array([13, 9, 0])
    S4 = 0

    for i in range(len(t)):
        x_dot = S1.dot(np.array([x1, x2, x3])) + S2 * u
        x1 += x_dot[0] * h
        x2 += x_dot[1] * h
        x3 += x_dot[2] * h
        y = S3.dot(np.array([x1, x2, x3])) + S4 * u
        
        x1_arr.append(x1)
        x2_arr.append(x2)
        x3_arr.append(x3)
        y_arr.append(y)

    return x1_arr, x2_arr, x3_arr, y_arr

def plot_system(h, t_end, x1_0, x2_0, x3_0, u):
    x1_arr, x2_arr, x3_arr, y_arr = simulate_system(h, t_end, x1_0, x2_0, x3_0, u)
    t = np.arange(0, t_end, h)
    plt.plot(t, x1_arr)
    plt.plot(t, x2_arr)
    plt.plot(t, x3_arr)
    plt.plot(t, y_arr)
    plt.xlabel("Time")
    plt.ylabel("Output")
    plt.title("Response Graph for STEP  Inputs")
    plt.show()

plot_system(0.01, 10, 0.0, 0.0, 0.0, 1.0)
