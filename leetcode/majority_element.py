from collections import Counter


def majorityElement(nums):
    map = {}

    for i in range(len(nums)):
        if nums[i] not in map:
            map[nums[i]] = 1
        else:
            map[nums[i]] = map.get(nums[i]) + 1

    max_key_value_pair = [(key, value) for key, value in map.items() if value > len(nums) // 3]

    majority_list = []
    for item in max_key_value_pair:
        key,value = item
        majority_list.append(key)


    if len(majority_list):
        return majority_list
    return []

def main():
    n = [1,1,1,2,2]



    print(majorityElement(n))


if __name__=='__main__':
    main()