from WordConcatenation import get_concatenated_words

class TestSuite:
    def test_1(self):
        return get_concatenated_words(['a']) == []

    def test_2(self):
        return get_concatenated_words(['a', 'b', 'c']) == []

    def test_3(self):
        return get_concatenated_words(['a', 'b', 'c', 'ab', 'bc']) == ['ab', 'bc']

    def test_4(self):
        return get_concatenated_words(['a', 'b', 'c', 'ab', 'bc', 'ac']) == ['ab', 'bc', 'ac']

    def test_5(self):
        return get_concatenated_words(['cat', 'cats', 'dog', 'catsdog']) == ['catsdog']

    def test_6(self):
        return get_concatenated_words(['cat', 'cats', 'dog', 'catsdog', 's']) == ['cats', 'catsdog']

    def test_7(self):
        return get_concatenated_words(['cat', 'cats', 'dog', 'catsdo', 'catsdog', 'catsd', 's', 'catsdon']) == ['cats', 'catsdog']

    def test_8(self):
        return get_concatenated_words(['cat', 'cats', 'dog', 'catsdog', 's', 'k', 'kr', 'ks']) == ['ks', 'cats', 'catsdog']

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
        print("Test_7 : " + self.return_test_result(self.test_7))
        print("Test_8 : " + self.return_test_result(self.test_8))
        print("Test suite finished running")
