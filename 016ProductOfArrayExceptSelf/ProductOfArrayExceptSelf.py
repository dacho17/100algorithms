def get_products(nums):
    right_prods, left_prods = __get_products_right(nums), __get_products_left(nums)
    products = [left_prods[1]]
    for i in range(1, len(nums) - 1):
        products.append(right_prods[i - 1] * left_prods[i + 1])
    products.append(right_prods[len(nums) - 2])
    return products

def __get_products_left(nums):
    res = [1] * len(nums)
    prev = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = nums[i] * prev
        prev = res[i]
    return res

def __get_products_right(nums):
    res = []
    prev = 1
    for num in nums:
        prod = num * prev
        res.append(prod)
        prev = prod
    return res
