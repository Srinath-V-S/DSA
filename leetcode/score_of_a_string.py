def scoreOfString(s: str) -> int:
    print(s)

    l = [ord(char) for char in s]

    return sum(abs(b-a) for a,b in zip(l,l[1:]))


def main():
    s = "hello"



    print(scoreOfString(s))


if __name__=='__main__':
    main()