from math import sqrt


def is_triagonal(x):
    n = (sqrt(8 * x + 1) - 1) / 2
    return n.is_integer()


def is_hexagonal(x):
    n = (sqrt(8 * x + 1) + 1) / 4
    return n.is_integer()


def main():
    N, a, b = map(int, input().split())
    check_fun = a == 3 and is_triagonal or is_hexagonal

    i = 1
    while True:
        number = i * (3 * i - 1) // 2

        if number >= N:
            break

        if check_fun(number):
            print(number)

        i += 1


if __name__ == "__main__":
    main()
