from TreeSerialization import Node, deserialize_bin_tree, serialize_bin_tree


class TestSuite:
    def test_1(self):
        return serialize_bin_tree(Node(1)) == "1##" and \
            serialize_bin_tree(deserialize_bin_tree("1##")) == "1##"

    def test_2(self):
        return serialize_bin_tree(Node(1, Node(2), Node(3))) == "12##3##" and \
            serialize_bin_tree(deserialize_bin_tree("12##3##")) == "12##3##"

    def test_3(self):
        return serialize_bin_tree(Node(1, Node(2, Node(4), Node(5, None, Node(6))), Node(3))) == "124##5#6##3##" and \
            serialize_bin_tree(deserialize_bin_tree("124##5#6##3##")) == "124##5#6##3##"

    def test_4(self):
        return serialize_bin_tree(Node(1, Node(3), Node(2, Node(4), Node(5, Node(6))))) == "13##24##56###" and \
            serialize_bin_tree(deserialize_bin_tree("13##24##56###")) == "13##24##56###"

    def test_5(self):
        return serialize_bin_tree(Node(0, None, Node(1, None, Node(2, None, Node(3))))) == "0#1#2#3##" and \
            serialize_bin_tree(deserialize_bin_tree("0#1#2#3##")) == "0#1#2#3##"

    def test_6(self):
        return serialize_bin_tree(Node(0, Node(1, Node(2, Node(3, Node(4)))))) == "01234######" and \
            serialize_bin_tree(deserialize_bin_tree("01234######")) == "01234######"

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
