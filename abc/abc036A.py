def main():
    A, B = map(int, input().split())

    if B % A != 0:
        ans = B // A + 1
    else:
        ans = B // A

    print(ans)


if __name__ == '__main__':
    main()
