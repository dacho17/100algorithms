class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def add_func(self, num1, num2, carry_over=0):         
        if num1 is None and num2 is None:
            if carry_over:
                return Node(carry_over)
            return None
        
        next_num1_digit = None
        next_num2_digit = None
        sum = carry_over
        if num1:
            sum += num1.val
            next_num1_digit = num1.next
        if num2:
            sum += num2.val
            next_num2_digit = num2.next
        
        new_num = Node(sum % 10)
        new_num.next = self.add_func(next_num1_digit, next_num2_digit, sum // 10)
        return new_num

    def transform_to_int(self, lst, power=0):
        if lst is None:
            return 0
        
        return lst.val * 10 ** power + self.transform_to_int(lst.next, power + 1)
