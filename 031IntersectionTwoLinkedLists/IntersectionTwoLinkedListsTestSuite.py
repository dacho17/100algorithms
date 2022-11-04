from IntersectionTwoLinkedLists import Node, find_lists_intersection

class TestSuite:
    def test_1(self):
        return find_lists_intersection(Node(2), Node(2)) == 2

    def test_2(self):
        return find_lists_intersection(Node(2), Node(3)) == None

    def test_3(self):
        return find_lists_intersection(Node(2, Node(3)), Node(4)) == None

    def test_4(self):
        return find_lists_intersection(Node(5), Node(0, Node(1))) == None

    def test_5(self):
        return find_lists_intersection(Node(2, Node(6, Node(4))), Node(1, Node(5))) == None
    
    def test_6(self):
        return find_lists_intersection(Node(1, Node(9, Node(1, Node(2, Node(4))))), Node(3, Node(2, Node(4)))) == 2

    def test_7(self):
        return find_lists_intersection(Node(4, Node(1, Node(8, Node(4, Node(5))))), Node(5, Node(6, Node(1, Node(8, Node(4, Node(5))))))) == 1

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
        print("Test_7 : " + self.return_test_result(self.test_7))
        print("Test suite finished running")
