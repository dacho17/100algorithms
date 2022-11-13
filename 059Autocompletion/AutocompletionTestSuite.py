from Autocompletion import Solution, Node

solution = Solution(['bl', 'bat', 'bar', 'bag', 'bold', 'bored', 'blue', 'black', 'ant', 'ants', 'art', \
    'align', 'allow', 'since', 'silk', 'red', 'bond', 'while', 'whale', 'whales'])

class TestSuite:

    def test_1(self):
        # print(solution.list_bfs())
        return solution.autocomplete('bat') == ['bat']

    def test_2(self):
        return solution.autocomplete('whale') == ['whale', 'whales']

    def test_3(self):
        return solution.autocomplete('bl') == ['bl', 'blue', 'black']

    def test_4(self):
        return solution.autocomplete('bo') == ['bold', 'bored', 'bond']

    def test_5(self):
        return solution.autocomplete('ba') == ['bat', 'bar', 'bag']

    def test_6(self):
        return solution.autocomplete('b') == ['bl', 'blue', 'black', 'bat', 'bar', 'bag', 'bold', 'bored', 'bond']

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
