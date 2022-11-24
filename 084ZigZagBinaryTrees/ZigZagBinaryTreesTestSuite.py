from ZigZagBinaryTrees import Node, zig_zag_binary_tree

class TestSuite:
    def test_1(self):
        return zig_zag_binary_tree(Node(1)) == [1]

    def test_2(self):
        return zig_zag_binary_tree(Node(1, None, Node(2))) == [1, 2]

    def test_3(self):
        return zig_zag_binary_tree(Node(1, Node(2), Node(3))) == [1, 2, 3]

    def test_4(self):
        return zig_zag_binary_tree(Node(1, Node(2, Node(4), None), Node(3, None, Node(5)))) == [1, 2, 3, 5, 4]

    def test_5(self):
        return zig_zag_binary_tree(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))) == [1, 2, 3, 7, 6, 5, 4]

    def test_6(self):
        return zig_zag_binary_tree(Node(1, Node(2, Node(4, None, Node(5))), Node(3, None, Node(6, Node(7), Node(8))))) == [1, 2, 3, 6, 4, 5, 7, 8]

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
