def main():
    nums = list(map(int,input("enter integers").split()))
    print(nums)

    print(find_closest_number(nums))


def find_closest_number(nums):
    closest_to_zero = 0
    diff = {}
    # -1 2 3 1
    min_difference = float('inf')
    for num in nums:
        diff[num] = abs(num)
        print(diff)
        if diff[num] < min_difference or (closest_to_zero < num and diff[num] == min_difference):
            closest_to_zero = num
            min_difference = diff[num]
    return closest_to_zero
if __name__ == '__main__':
    main()