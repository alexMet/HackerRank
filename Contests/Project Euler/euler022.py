def main():
    n = int(input())
    names = [input() for _ in range(n)]
    names.sort()

    values = {}
    i = 1
    for name in names:
        values[name] = sum([i * (ord(x) - 96) for x in name.lower()])
        i += 1

    q = int(input())
    for _ in range(q):
        print(values[input()])


if __name__ == "__main__":
    main()
