def linear_congruential_method(seed, a, c, mod):
    x = seed
    random_numbers = []

    while True:
        random_numbers.append(x)
        x = (a * x + c) % mod
        if x == random_numbers[0]:
            break

    return random_numbers

def main():
    seed, a, c, mod = 3, 13, 0, 64
    random_numbers = linear_congruential_method(seed, a, c, mod)
    print(random_numbers)

if __name__ == "__main__":
    main()