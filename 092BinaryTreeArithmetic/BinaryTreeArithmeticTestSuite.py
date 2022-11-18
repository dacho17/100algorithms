from BinaryTreeArithmetic import Node, arithmetic

class TestSuite:
    def test_1(self):
        return arithmetic(Node(1)) == 1

    def test_2(self):
        return arithmetic(Node('*', Node(1), Node(0))) == 0

    def test_3(self):
        return arithmetic(Node('*', Node(10), Node('*', Node(2), Node(5)))) == 100

    def test_4(self):
        return arithmetic(Node('/', Node('-', Node(12), Node(2)), Node('+', Node(3), Node(7))))

    def test_5(self):
        return arithmetic(Node('/', Node('-', Node(2), Node(12)), Node('-', Node(3), Node(13)))) == 1

    def test_6(self):
        return arithmetic(Node('/', Node('-', Node(2), Node(12)), Node('-', Node(13), Node(3)))) == -1

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
