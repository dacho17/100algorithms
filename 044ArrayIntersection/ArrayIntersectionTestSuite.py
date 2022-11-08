from ArrayIntersection import find_array_intersection

class TestSuite:
    def test_1(self):
        return find_array_intersection([1], [1]) == set([1])

    def test_2(self):
        return find_array_intersection([1], [2]) == set([])

    def test_3(self):
        return find_array_intersection([1, 2, 2], [2, 3, 3]) == set([2])

    def test_4(self):
        return find_array_intersection([1, 1, 2, 2, 3, 3], [1, 1, 3]) == set([1, 3])

    def test_5(self):
        return find_array_intersection(range(0, 10), range(10, 0, -1)) == set(range(1, 10))

    def test_6(self):
        return find_array_intersection([4, 9, 5], [9, 4, 9, 8, 4]) == set([4, 9])

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
