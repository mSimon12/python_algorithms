import pytest
from src.data_structures import LinkedList

class TestLinkedList:

    TEST_INT = 58
    TEST_BOOL = True
    TEST_STRING = "foobarfoobar"
    TEST_FLOAT = 101.98

    @pytest.fixture()
    def linked_list(self):
        return LinkedList()

    def test_add_data_to_head(self, linked_list):
        linked_list.add_at_head(self.TEST_INT)
        assert self.TEST_INT == linked_list.get_index(0), "Fail to add item of type 'int'!"

        linked_list.add_at_head(self.TEST_BOOL)
        assert self.TEST_BOOL == linked_list.get_index(0), "Fail to add item of type 'boolean'!"

        linked_list.add_at_head(self.TEST_STRING)
        assert self.TEST_STRING == linked_list.get_index(0), "Fail to add item of type 'string'!"

        linked_list.add_at_head(self.TEST_FLOAT)
        assert self.TEST_FLOAT == linked_list.get_index(0), "Fail to add item of type 'float'!"

    def test_add_data_to_tail(self, linked_list):
        linked_list.add_at_tail(self.TEST_INT)
        assert self.TEST_INT == linked_list.get_index(0) , "Fail to add item of type 'int'!"

        linked_list.add_at_tail(self.TEST_BOOL)
        assert self.TEST_BOOL == linked_list.get_index(1), "Fail to add item of type 'boolean'!"

        linked_list.add_at_tail(self.TEST_STRING)
        assert self.TEST_STRING == linked_list.get_index(2), "Fail to add item of type 'string'!"

        linked_list.add_at_tail(self.TEST_FLOAT)
        assert self.TEST_FLOAT == linked_list.get_index(3), "Fail to add item of type 'float'!"

    def test_delete_data_from_head(self, linked_list):
        linked_list.add_at_head(self.TEST_INT)
        linked_list.add_at_head(self.TEST_BOOL)
        linked_list.add_at_head(self.TEST_STRING)
        linked_list.add_at_head(self.TEST_FLOAT)

        assert self.TEST_FLOAT == linked_list.delete_from_head(), "Fail to remove item of type 'float'!"
        assert self.TEST_STRING == linked_list.delete_from_head(), "Fail to remove item of type 'string'!"
        assert self.TEST_BOOL == linked_list.delete_from_head(), "Fail to remove item of type 'boolean'!"
        assert self.TEST_INT == linked_list.delete_from_head(), "Fail to remove item of type 'int'!"

    def test_delete_raise_exception(self, linked_list):
        with pytest.raises(IndexError):
            linked_list.delete_from_head()
            linked_list.delete_from_index(5)
            linked_list.delete_from_end()

