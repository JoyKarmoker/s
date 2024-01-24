import matplotlib.pyplot as plt
import numpy as np
def pure_pursuit(fighter_speed):
    x_bomber = []
    y_bomber = []
    xf = np.random.randint(1, 1000)
    yf = np.random.randint(1, 1000)
    x_fighter = []
    y_fighter = []
    time = 0
    escape_distance, caught_distance = 900, 10

    while True:
        #This part is for random input
        x = np.random.randint(1, 1000)
        y = np.random.randint(1, 1000)
        x_bomber.append(x)
        y_bomber.append(y)

        x_fighter.append(xf)
        y_fighter.append(yf)

        plt.clf()
        plt.title("Simulation of a Pure Pursuit")
        plt.plot(x_fighter, y_fighter, marker="o", label="Fighter")
        # plt.plot(x_bomber[0: time + 1], y_bomber[0: time + 1], marker="o", label="Bomber")
        plt.plot(x_bomber, y_bomber, marker="o", label="Bomber")
        # plt.xlim(-100, 200)
        # plt.ylim(-100, 100)
        plt.legend()
        plt.grid()
        plt.pause(1)

        distance = ((xf - x) ** 2 + (yf - y) ** 2) ** 0.5
        if distance < caught_distance:
            print(f"Target caught at {time} second")
            printed = True
            break
        if distance > escape_distance or time > len(x_bomber):
            print(f"Target escaped at {time} second")
            printed = True
            break

        sin = (y - yf) / distance
        cos = (x - xf) / distance
        time += 1
        xf += fighter_speed * cos
        yf += fighter_speed * sin

    plt.show()



def main():
    speed = input()
    speed = int(speed)
    pure_pursuit(speed)


if __name__ == "__main__":
    main()