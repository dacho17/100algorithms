from PushDominoes import _get_equilibrium

class TestSuite:
    def test_1(self):
        return _get_equilibrium(['R', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'L']) == "RRRRR.LLLLL"

    def test_2(self):
        return _get_equilibrium(['.', 'R', 'R', 'R', 'R', '.', 'L', 'L', '.', 'R', '.']) == ".RRRR.LL.RR"

    def test_3(self):
        return _get_equilibrium(['.', '.', 'R', '.', 'R', 'L', 'L', '.', 'L', 'R', '.']) == "..RRRLLLLRR"

    def test_4(self):
        return _get_equilibrium(['.', '.', '.', '.', '.']) == "....."

    def test_5(self):
        return _get_equilibrium(['.', 'L', 'R', '.', 'L', '.', 'L', 'R', 'R']) == "LLR.LLLRR"

    def test_6(self):
        return _get_equilibrium(['.', 'R', '.', '.', '.', '.', '.', 'L', 'L']) == ".RRR.LLLL"

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
