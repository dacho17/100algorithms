from ClosestPointsToOrigin import k_closest_points

class TestSuite:
    def test_1(self):
        return set(k_closest_points([(1, 1), (2, 2)], 1)) == set([(1, 1)])

    def test_2(self):
        return set(k_closest_points([(1, 1), (-1, 1), (5, 3), (2, 1), (-1, -1), (1, -1)], 4)) == set([(1, 1), (-1, 1), (-1, -1), (1, -1)])

    def test_3(self):
        return set(k_closest_points([(0, 1), (1, 1), (7, 2), (4, 1), (-2, 1)], 3)) == set([(0, 1), (1, 1), (-2, 1)])

    def test_4(self):
        return set(k_closest_points([(6, 2), (4, 3), (11, 7), (-9, 2), (- 6, -6), (-1, -3)], 4)) == set([(6, 2), (4, 3), (- 6, -6), (-1, -3)])

    def test_5(self):
        return set(k_closest_points([(3, -3), (-2, -2), (2, -2), (3, 1), (-1, -3), (1, 2), (2, 1)], 2)) == set([(1, 2), (2, 1)])

    def test_6(self):
        return set(k_closest_points([(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0), (-1, -1)], 1)) == set([(0, 0)])

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
