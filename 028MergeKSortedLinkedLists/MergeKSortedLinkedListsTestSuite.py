from MergeKSortedLinkedLists import Node, merge_K_linked_lists

class TestSuite:
    def test_1(self):
        return str(merge_K_linked_lists([Node(1, None), Node(3, None)])) == "1 3 "

    def test_2(self):
        return str(merge_K_linked_lists([Node(2, None)])) == "2 "

    def test_3(self):
        return str(merge_K_linked_lists([Node(1, Node(3, Node(5, None))), Node(2, Node(4, Node(6, None)))])) == "1 2 3 4 5 6 "

    def test_4(self):
        return str(merge_K_linked_lists([Node(1, Node(2, Node(5, None))), Node(2, Node(3, Node(6, None)))])) == "1 2 2 3 5 6 "

    def test_5(self):
        return str(merge_K_linked_lists([Node(1, Node(3, None)), Node(5, Node(8, None)), Node(6, Node(9, None))])) == "1 3 5 6 8 9 "

    def test_6(self):
        return str(merge_K_linked_lists([Node(1, Node(7, Node(9, Node(12, None)))), Node(2, Node(4, None))])) == "1 2 4 7 9 12 "

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
