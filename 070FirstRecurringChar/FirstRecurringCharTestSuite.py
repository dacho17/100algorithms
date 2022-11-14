from FirstRecurringChar import find_first_reocurring

class TestSuite:
    def test_1(self):
        return find_first_reocurring('a') == None

    def test_2(self):
        return find_first_reocurring('abca') == 'a'

    def test_3(self):
        return find_first_reocurring('rabat') == 'a'

    def test_4(self):
        return find_first_reocurring('strata') == 't'

    def test_5(self):
        return find_first_reocurring('rotterdam') == 't'

    def test_6(self):
        return find_first_reocurring('abcdefghijklmnopqrstuvwxyx') == 'x'

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
