from FindPythagoreanTriplets import any_pythagorean_triplets

class TestSuite:
    def test_1(self):
        return any_pythagorean_triplets([1, 2, 3]) == False
    # Expected: any = False

    def test_2(self):
        return any_pythagorean_triplets([1, 2, 3, 4, 5]) == True
    # Expected: any = True

    def test_3(self):
        return any_pythagorean_triplets([10, 30, 33, 1, 7 ]) == False
    # Expected: any = False

    def test_4(self):
        return any_pythagorean_triplets([12, 7, 9, 13, 33, 20, 36]) == False
    # Expected: any = False

    def test_5(self):
        return any_pythagorean_triplets([12, 7, 9, 13, 33, 20, 36, 5]) == True
    # Expected: any = True

    def test_6(self):
        return any_pythagorean_triplets([68, 285, 293, 17, 2]) == True
    # Expected: any = True

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
