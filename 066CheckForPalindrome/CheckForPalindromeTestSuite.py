from CheckForPalindrome import check_for_palindrome

class TestSuite:
    def test_1(self):
        return check_for_palindrome("aba") == 'aba'

    def test_2(self):
        return check_for_palindrome("ababbbbb") == 'abbbbbba'

    def test_3(self):
        return check_for_palindrome("abc") == None

    def test_4(self):
        return check_for_palindrome("abcc") == None

    def test_5(self):
        return check_for_palindrome("aabcc") == 'acbca'

    def test_6(self):
        return check_for_palindrome("foxfo") == 'foxof'

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
