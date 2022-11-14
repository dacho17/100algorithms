from ShortestUniquePrefix import shortest_unique_prefix

class TestSuite:
    def test_1(self):
        return shortest_unique_prefix(['a']) == ['a']

    def test_2(self):
        return shortest_unique_prefix(['ara', 'bar']) == ['a', 'b']

    def test_3(self):
        return shortest_unique_prefix(['ara', 'arda']) == ['ara', 'ard']

    def test_4(self):
        return shortest_unique_prefix(['arg', 'arara', 'ara']) == ['arg', 'arar', 'ara']

    def test_5(self):
        return shortest_unique_prefix(['jon', 'jack', 'john', 'trade']) == ['jon', 'ja', 'joh', 't']

    def test_6(self):
        return shortest_unique_prefix(['ra', 'ramp', 'rup', 'rupture', 'vas', 'kaz', 'kr', 'ru']) == ['ra', 'ram', 'rup', 'rupt', 'v', 'ka', 'kr', 'ru']

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
