from FindAnagrams import find_anagrams

class TestSuite:
    def test_1(self):
        return find_anagrams('abc', 'a') == [(0, 0)]

    def test_2(self):
        return find_anagrams('abc', 'cb') == [(1, 2)]

    def test_3(self):
        return find_anagrams('abc', 'bca') == [(0, 2)]

    def test_4(self):
        return find_anagrams('acdbacdacb', 'abc') == [(3, 5), (7, 9)]

    def test_5(self):
        return find_anagrams('cocolinoc', 'oc') == [(0, 1), (1, 2), (2, 3), (7, 8)]

    def test_6(self):
        return find_anagrams('sirimamiris', 'sir') == [(0, 2), (8, 10)]

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
