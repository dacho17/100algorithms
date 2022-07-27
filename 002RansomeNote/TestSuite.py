from RansomeNote import Magazine

class RansomeNoteTestSuite:
    def test_1(self):
        magazine = Magazine(['k', 'C', 'A', 't', 'e', 'r'])
        return magazine.can_be_spelled('Catter') == False
    # Expected: canBeSpelled = False

    def test_2(self):
        magazine = Magazine(['T', 'C', 'A', 't', 'e', 'r'])
        return magazine.can_be_spelled('catter') == True
    # Expected: canBeSpelled = True

    def test_3(self):
        magazine = Magazine(['K', 'o', 'R', 'R', 'O', 'Z', 'v'])
        return magazine.can_be_spelled('korko') == False
    # Expected: canBeSpelled = False

    def test_4(self):
        magazine = Magazine(['k', 'K', 'o', 'R', 'R', 'O', 'Z', 'v'])
        return magazine.can_be_spelled('KoRKo') == True
    # Expected: canBeSpelled = True

    def test_5(self):
        magazine = Magazine(['A', 'a', 'A', 'A', 'a', 'A', 'A', 'a', 'A', 'a', 'r', 'H'])
        return magazine.can_be_spelled('argh') == False
    # Expected: canBeSpelled = False

    def test_6(self):
        magazine = Magazine(['A', 'a', 'A', 'A', 'a', 'A', 'A', 'a', 'A', 'a', 'r', 'H', 'g'])
        return magazine.can_be_spelled('ARGH') == True
    # Expected: canBeSpelled = True

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
