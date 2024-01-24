import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize a, b, c
a = [1.0]
b = [0.5]
c = [0.0]

# Constants
k1 = 0.05
k2 = 0.05

total_time = 100
steps = 500
dt = total_time / steps

fig, ax = plt.subplots()
ax.set_xlim(0, total_time / dt)
ax.set_ylim(0, 1)

# Create lines for a, b, and c with different colors
line_a, = ax.plot([], [], label="a", color='magenta')
line_b, = ax.plot([], [], label="b", color='green')
line_c, = ax.plot([], [], label="c", color='#132043')

current_time = 0

def animation(frame):
    global current_time, total_time

    if current_time <= total_time:
        a_initial = a[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
        b_initial = b[-1] + (k2 * c[-1] - k1 * a[-1] * b[-1]) * dt
        c_initial = c[-1] + (2 * k1 * a[-1] * b[-1] - 2 * k2 * c[-1]) * dt

        a.append(a_initial)
        b.append(b_initial)
        c.append(c_initial)
        current_time += dt

    line_a.set_data(range(len(a)), a)
    line_b.set_data(range(len(b)), b)
    line_c.set_data(range(len(c)), c)
    ax.legend()

# Increase the interval to make the animation faster (adjust as needed)
animated = FuncAnimation(fig, animation, frames=steps, interval=1, repeat=False)

plt.xlabel("Time (s)")
plt.ylabel("Concentration (mole)")
plt.title("Concentration vs Time")
plt.grid()
plt.show()
