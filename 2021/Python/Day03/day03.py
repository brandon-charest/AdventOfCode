
def diagnostics(data):
    gamma = ''
    for i in range(len(data[0])):
        ones, zeros = 0,0
        for num in data:
            if num[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += '1'
        else:
            gamma += '0'
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def diagnostics2(data):
    def helper(nums, a, b):
        for i in range(len(nums[0])):
            if len(nums) == 1:
                break
            ones, zeros = 0, 0
            for num in nums:
                if num[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones > zeros or ones == zeros:
                nums = list(filter(lambda x: x[i] == a, nums))
            else:
                nums = list(filter(lambda x: x[i] == b, nums))
        return nums[0]

    oxygen_rating = helper(data,'1', '0')
    c02_rating = helper(data, '0', '1')
    return int(oxygen_rating, 2) * int(c02_rating, 2)


if __name__ == "__main__":
    with open('./input.txt') as f:
        data = list(f.read().splitlines())
    result = diagnostics2(data)
    print(result)