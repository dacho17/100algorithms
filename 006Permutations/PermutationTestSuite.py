from Permutations import ListForPermutation

class PermutationTestSuite:
    def test_1(self):
        perms = ListForPermutation([4, 5]).return_permutations()
        return perms == [[4, 5], [5, 4]]

    def test_2(self):
        perms = ListForPermutation([0, 0]).return_permutations()
        return perms == [[0, 0], [0, 0]]

    def test_3(self):
        perms = ListForPermutation([7]).return_permutations()
        return perms == [[7]]

    def test_4(self):
        perms = ListForPermutation([9, 7]).return_permutations()
        return perms == [[9, 7], [7, 9]]

    def test_5(self):
        perms = ListForPermutation([1, 2, 3]).return_permutations()
        return perms == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

    def test_6(self):
        perms = ListForPermutation([3, 4, 5]).return_permutations()
        return perms == [[3, 4, 5], [3, 5, 4], [4, 3, 5], [4, 5, 3], [5, 4, 3], [5, 3, 4]]
    
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
