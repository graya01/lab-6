
def encode(input_pass):
    ans = ""
    for i in input_pass:

        num = (int(i) + 3) % 10
        ans += str(num)

    return ans


def main():
    input_pass = str(input())
    ans = encode(input_pass)
    print(ans)


if __name__ == "__main__":
    main()
