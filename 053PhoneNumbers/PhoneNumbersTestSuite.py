from PhoneNumbers import generate_words_from

class TestSuite:
    def test_1(self):
        return generate_words_from("227") == ['bar', 'car']

    def test_2(self):
        return generate_words_from("222") == ['cab']

    def test_3(self):
        return generate_words_from("999") == []

    def test_4(self):
        return generate_words_from("000") == []

    def test_5(self):
        return generate_words_from("228") == ['cat']

    def test_6(self):
        return generate_words_from("223") == ['caf', 'cad']

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
