from QueueReconstruction import reconstruct_queue

class TestSuite:
    def test_1(self):
        return reconstruct_queue([(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]) == [(5, 0), (7, 0), (5, 2), (6, 1), (4, 4), (7, 1)]

    def test_2(self):
        return reconstruct_queue([(12, 0), (5, 0), (7, 1)]) == [(5, 0), (12, 0), (7, 1)]

    def test_3(self):
        return reconstruct_queue([(1, 0), (2, 0), (3, 0)]) == [(1, 0), (2, 0), (3, 0)]

    def test_4(self):
        return reconstruct_queue([(1, 2), (2, 1), (3, 0)]) == [(3, 0), (2, 1), (1, 2)]

    def test_5(self):
        return reconstruct_queue([(7, 1), (8, 0)]) == [(8, 0), (7, 1)]

    def test_6(self):
        return reconstruct_queue([(4, 0)]) == [(4, 0)]
    
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
