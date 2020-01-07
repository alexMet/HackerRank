def is_pentagonal(x):
    n = ((24 * x + 1) ** 0.5 + 1) / 6
    return n.is_integer()


def main():
    n, k = map(int, input().split())
    pentagonals = []

    for i in range(1, n):
        penta = i * (3 * i - 1) // 2
        pentagonals += [penta]

        if i - k - 1 > 0:
            p = pentagonals[i - k - 1]
            if is_pentagonal(penta - p) or is_pentagonal(penta + p):
                print(penta)


if __name__ == "__main__":
    main()
