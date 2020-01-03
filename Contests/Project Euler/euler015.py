def choose(n, k):
    prod = 1
    for i in range(1, k + 1):
        prod = (prod * (n - i + 1)) // i
    return prod


def main():
    LIMIT = 10 ** 9 + 7
    t = int(input())

    for _ in range(0, t):
        n, m = map(int, input().split())
        print(choose(n + m, n) % LIMIT)


if __name__ == "__main__":
    main()
