from ReverseLinkedList import Node, reverse_list

class TestSuite:
    def test_1(self):
        lst = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        return reverse_list(lst) == [5, 4, 3, 2, 1]

    def test_2(self):
        lst = Node(7, Node(6, Node(5, Node(4))))
        return reverse_list(lst) == [4, 5, 6, 7]

    def test_3(self):
        lst = Node(17, Node(26, Node(12)))
        return reverse_list(lst) == [12, 26, 17]

    def test_4(self):
        lst = Node(1, Node(0))
        return reverse_list(lst) == [0, 1]

    def test_5(self):
        lst = Node(1, Node(2, Node(3, Node(4, Node(5, Node(4, Node(3, Node(2))))))))
        return reverse_list(lst) == [2, 3, 4, 5, 4, 3, 2, 1]

    def test_6(self):
        lst = Node(1)
        return reverse_list(lst) == [1]
    
    def return_test_result(self, test_func):
        return "Passed" if test_func() else "Failed"

    def run_test_suite(self):
        print("Test results:")
        print("Test_1 : " + self.return_test_result(self.test_1))
        print("Test_2 : " + self.return_test_result(self.test_2))
        print("Test_3 : " + self.return_test_result(self.test_3))
        print("Test_4 : " + self.return_test_result(self.test_4))
        print("Test_5 : " + self.return_test_result(self.test_5))
        print("Test_6 : " + self.return_test_result(self.test_6))
        print("Test suite finished running")
