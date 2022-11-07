from GroupAnagrams import group_anagrams

class TestSuite:
    def test_1(self):
        return group_anagrams(["abc"]) == [["abc"]]

    def test_2(self):
        return group_anagrams(["abc", "cde"]) == [["abc"], ["cde"]]

    def test_3(self):
        return group_anagrams(["abc", "bca"]) == [["abc", "bca"]]

    def test_4(self):
        return group_anagrams(["abc", "bcd", "cba", "cbd", "efg"]) == [["abc", "cba"], ["bcd", "cbd"], ["efg"]]

    def test_5(self):
        return group_anagrams(["abc", "bcd", "cba", "acb", "bac", "bca", "cbd", "cab"]) == [["abc", "cba", "acb", "bac", "bca", "cab"], ["bcd", "cbd"]]

    def test_6(self):
        return group_anagrams(["abc", "bcd", "CBa", "BcD", "efg", "kgh"]) == [["abc", "CBa"], ["bcd", "BcD"], ["efg"], ["kgh"]]

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
