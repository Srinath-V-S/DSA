def closetTarget( words, target, startIndex):
    """
    :type words: List[str]
    :type target: str
    :type startIndex: int
    :rtype: int
    """
    n = len(words)
    if target not in words:
        return -1

    n = len(words)
    if target not in words:
        return -1

    if words[startIndex] == target:
        return 0
    l_distance = 0
    r_distance = 0
    for i in range(0, n):
        next_word = words[(startIndex + i + 1) % n]
        print(next_word)
        r_distance += 1
        if next_word == target:
            break

    for j in range(0, n):
        if startIndex == 0:
            prev_word = words[(-j - 1) % n]
        else:
            prev_word = words[(startIndex - j + -1 + n) % n]
        print(prev_word)
        l_distance += 1
        if prev_word == target:
            break
    print(l_distance, r_distance)
    return min(l_distance, r_distance)

def main():
    words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
    startIndex = 8
    target = "zemkwvqrww"
    print(closetTarget(words,target,startIndex))


if __name__ == '__main__':
    main()
