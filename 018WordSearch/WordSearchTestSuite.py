from WordSearch import WordGrid

class TestSuite:
    matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

    def test_1(self):
        return WordGrid(self.matrix).find("FOAM") == True

    def test_2(self):
        return WordGrid(self.matrix).find("MAS") == True
    
    def test_3(self):
        return WordGrid(self.matrix).find("MASS") == True
    
    def test_4(self):
        return WordGrid(self.matrix).find("ACIP") == False
    
    def test_5(self):
        return WordGrid(self.matrix).find("SOS") == False
    
    def test_6(self):
        return WordGrid(self.matrix).find("MAR") == False
    
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
