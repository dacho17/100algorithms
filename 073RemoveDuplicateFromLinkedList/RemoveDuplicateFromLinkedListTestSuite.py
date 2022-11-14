from RemoveDuplicateFromLinkedList import Node, filter_seq_duplicates

class TestSuite:
    def test_1(self):
        return filter_seq_duplicates(Node(1)) == "1"

    def test_2(self):
        return filter_seq_duplicates(Node(1, Node(1, Node(1)))) == "1"

    def test_3(self):
        return filter_seq_duplicates(Node(1, Node(1, Node(2, Node(2, Node(1)))))) == "121"

    def test_4(self):
        return filter_seq_duplicates(Node(1, Node(2, Node(3, Node(4, Node(3, Node(4, Node(4, Node(5))))))))) == "1234345"

    def test_5(self):
        return filter_seq_duplicates(Node(1, Node(2))) == "12"

    def test_6(self):
        return filter_seq_duplicates(Node(10, Node(4, Node(5, Node(4, Node(6, Node(4, Node(11, Node(11, Node(11, Node(11, Node(4)))))))))))) == "1045464114"

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
