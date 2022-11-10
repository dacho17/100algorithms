from CircleOfWords import circle_of_words

class TestSuite:
    def test_1(self):
        return circle_of_words(['ana']) == True

    def test_2(self):
        return circle_of_words(['amer']) == False

    def test_3(self):
        return circle_of_words(['antilope', 'aligator', 'rhyno']) == False

    def test_4(self):
        return circle_of_words(['alen', 'nelie', 'omar', 'roma', 'elmo']) == True

    def test_5(self):
        return circle_of_words(['alen', 'nola']) == True

    def test_6(self):
        return circle_of_words(['aaaa', 'aaaa', 'aaaaa', 'aba']) == True
        
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
