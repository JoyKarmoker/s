import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def initialize_plot(total_time, dt):
    fig, ax = plt.subplots()
    ax.set_xlim(0, total_time / dt)
    ax.set_ylim(0, 1)

    # Create lines for a, b, and c with different colors
    line_a, = ax.plot([], [], label="a", color='magenta')
    line_b, = ax.plot([], [], label="b", color='green')
    line_c, = ax.plot([], [], label="c", color='#132043')

    plt.xlabel("Time (s)")
    plt.ylabel("Concentration (mole)")
    plt.title("Concentration vs Time")
    plt.grid()

    return fig, ax, line_a, line_b, line_c

def update_reaction(frame, a, b, c, k1, k2, dt, current_time):
    if current_time <= total_time:
        ab = a[-1] * b[-1]
        k1ab = k1 * ab
        k2c = k2 * c[-1]
        a_initial = a[-1] + (k2c - k1ab) * dt
        b_initial = b[-1] + (k2c - k1ab) * dt
        c_initial = c[-1] + (2 * k1ab - 2 * k2c) * dt

        a.append(a_initial)
        b.append(b_initial)
        c.append(c_initial)

    line_a.set_data(range(len(a)), a)
    line_b.set_data(range(len(b)), b)
    line_c.set_data(range(len(c)), c)
    ax.legend()

# Constants
total_time = 100
steps = 500
dt = total_time / steps
a = [1.0]  # Initial concentration of a
b = [0.5]  # Initial concentration of b
c = [0.0]  # Initial concentration of c
k1 = 0.05  # Reaction rate constant 1
k2 = 0.05  # Reaction rate constant 2
current_time = 0

fig, ax, line_a, line_b, line_c = initialize_plot(total_time, dt)
animated = FuncAnimation(fig, update_reaction, fargs=(a, b, c, k1, k2, dt, current_time), frames=steps, interval=1, repeat=False)
plt.show()
