from CourseSchedule import CourseGraph

class TestSuite:
    def test_1(self):
        gr = CourseGraph(2, [[0, 1], [1, 0]])
        return gr.can_be_finished() == False
    # Expected: canBeFinished = False

    def test_2(self):
        gr = CourseGraph(1, [[0, 1]])
        return gr.can_be_finished() == True
    # Expected: canBeFinished = True

    def test_3(self):
        gr = CourseGraph(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]])
        return gr.can_be_finished() == False
    # Expected: canBeFinished = False

    def test_4(self):
        gr = CourseGraph(7, [[2, 1], [3, 1], [4, 2], [6, 4], [2, 6], [3, 6], [5, 3], [7, 6], [5, 7]])
        return gr.can_be_finished() == False
    # Expected: canBeFinished = False

    def test_5(self):
        gr = CourseGraph(6, [[1, 2], [2, 3], [2, 4], [4, 5], [6, 3], [4, 6], [5, 6]])
        return gr.can_be_finished() == True
    # Expected: canBeFinished = True

    def test_6(self):
        gr = CourseGraph(6, [[1, 2], [2, 3], [2, 4], [4, 5], [6, 3], [6, 4], [5, 6]])
        return gr.can_be_finished() == False
    # Expected: canBeFinished = False

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
