from LevelByLevelTrees import list_bfs, Node

class TestSuite:
    def test_1(self):
        return list_bfs(Node(1)) == [1]

    def test_2(self):
        return list_bfs(Node(1, [Node(2), Node(3), Node(4), Node(5)])) == [1, 2, 3, 4, 5]

    def test_3(self):
        return list_bfs(Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6), Node(7)])])) == [1, 2, 5, 3, 4, 6, 7]

    def test_4(self):
        return list_bfs(Node(1, [Node(2, [Node(3), Node(4, [Node(9, [Node(10, [Node(11)])])])]), Node(5, [Node(6), Node(7)])])) == [1, 2, 5, 3, 4, 6, 7, 9, 10, 11]

    def test_5(self):
        return list_bfs(Node(1, [Node(2, [Node(3, [Node(4), Node(5), Node(6)]), Node(7)]), Node(8)])) == [1, 2, 8, 3, 7, 4, 5, 6]

    def test_6(self):
        return list_bfs(Node(0, [Node(1, [Node(3), Node(4, [Node(7, [Node(10)]), Node(8)]), Node(5, [Node(9, [Node(11, [Node(12)])])])]), Node(2, [Node(6)])])) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

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
