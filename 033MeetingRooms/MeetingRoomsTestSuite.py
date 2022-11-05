from MeetingRooms import find_required_number_of_meetingrooms

class TestSuite:
    def test_1(self):
        return find_required_number_of_meetingrooms([[0, 10]]) == 1

    def test_2(self):
        return find_required_number_of_meetingrooms([[0, 10], [10, 20]]) == 1

    def test_3(self):
        return find_required_number_of_meetingrooms([[0, 20], [10, 15]]) == 2

    def test_4(self):
        return find_required_number_of_meetingrooms([[0, 15], [10, 15]]) == 2

    def test_5(self):
        return find_required_number_of_meetingrooms([[0, 50], [10, 21], [20, 30]]) == 3

    def test_6(self):
        return find_required_number_of_meetingrooms([[0, 5], [0, 10], [5, 10], [2, 4], [3, 4], [15, 25], [10, 25], [20, 30]]) == 4

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
