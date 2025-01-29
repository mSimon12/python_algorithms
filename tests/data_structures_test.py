import pytest
from src.data_structures import LinkedList, Queue, Stack

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
        assert self.TEST_INT == linked_list.get_index(0), "Fail to add item of type 'int' to head!"

        linked_list.add_at_head(self.TEST_BOOL)
        assert self.TEST_BOOL == linked_list.get_index(0), "Fail to add item of type 'boolean' to head!"

        linked_list.add_at_head(self.TEST_STRING)
        assert self.TEST_STRING == linked_list.get_index(0), "Fail to add item of type 'string' to head!"

        linked_list.add_at_head(self.TEST_FLOAT)
        assert self.TEST_FLOAT == linked_list.get_index(0), "Fail to add item of type 'float' to head!"

    def test_add_data_to_index(self, linked_list):
        linked_list.add_at_tail(self.TEST_INT)
        assert self.TEST_INT == linked_list.get_index(0) , "Fail to add item of type 'int' to tail!"

        linked_list.add_at_tail(self.TEST_BOOL)
        assert self.TEST_BOOL == linked_list.get_index(1), "Fail to add item of type 'boolean' to tail!"

        linked_list.add_at_tail(self.TEST_STRING)
        assert self.TEST_STRING == linked_list.get_index(2), "Fail to add item of type 'string' to tail!"

        linked_list.add_at_tail(self.TEST_FLOAT)
        assert self.TEST_FLOAT == linked_list.get_index(3), "Fail to add item of type 'float' to tail!"

    def test_add_data_to_tail(self, linked_list):
        linked_list.add_at_head("place_holder")
        linked_list.add_at_head("place_holder")

        linked_list.add_at_index(self.TEST_INT,1)
        assert self.TEST_INT == linked_list.get_index(1) , "Fail to add item of type 'int' to defined index!"

        linked_list.add_at_index(self.TEST_BOOL, 2)
        assert self.TEST_BOOL == linked_list.get_index(2), "Fail to add item of type 'boolean' to defined index!"

        linked_list.add_at_index(self.TEST_STRING,1)
        assert self.TEST_STRING == linked_list.get_index(1), "Fail to add item of type 'string' to defined index!"

        linked_list.add_at_index(self.TEST_FLOAT,3)
        assert self.TEST_FLOAT == linked_list.get_index(3), "Fail to add item of type 'float' to defined index!"

    def test_add_raise_exception(self, linked_list):
        with pytest.raises(IndexError):
            linked_list.add_at_index(self.TEST_INT,5)
            linked_list.add_at_index(self.TEST_BOOL,3)
            linked_list.add_at_head(self.TEST_STRING)
            linked_list.add_at_index(self.TEST_FLOAT,3)

    def test_delete_data_from_head(self, linked_list):
        linked_list.add_at_head(self.TEST_INT)
        linked_list.add_at_head(self.TEST_BOOL)
        linked_list.add_at_head(self.TEST_STRING)
        linked_list.add_at_head(self.TEST_FLOAT)

        assert self.TEST_FLOAT == linked_list.delete_from_head(), "Fail to remove item of type 'float' from head!"
        assert self.TEST_STRING == linked_list.delete_from_head(), "Fail to remove item of type 'string' from head!"
        assert self.TEST_BOOL == linked_list.delete_from_head(), "Fail to remove item of type 'boolean' from head!"
        assert self.TEST_INT == linked_list.delete_from_head(), "Fail to remove item of type 'int' from head!"

    def test_delete_data_from_tail(self, linked_list):
        linked_list.add_at_head(self.TEST_INT)
        linked_list.add_at_head(self.TEST_BOOL)
        linked_list.add_at_head(self.TEST_STRING)
        linked_list.add_at_head(self.TEST_FLOAT)

        assert self.TEST_INT == linked_list.delete_from_tail(), "Fail to remove item of type 'int' from tail!"
        assert self.TEST_BOOL == linked_list.delete_from_tail(), "Fail to remove item of type 'boolean' from tail!"
        assert self.TEST_STRING == linked_list.delete_from_tail(), "Fail to remove item of type 'string' from tail!"
        assert self.TEST_FLOAT == linked_list.delete_from_tail(), "Fail to remove item of type 'float' from tail!"

    def test_delete_data_from_index(self, linked_list):
        linked_list.add_at_tail(self.TEST_INT)
        linked_list.add_at_tail(self.TEST_BOOL)
        linked_list.add_at_tail(self.TEST_STRING)
        linked_list.add_at_tail(self.TEST_FLOAT)

        assert self.TEST_STRING == linked_list.delete_from_index(2), "Fail to remove item of type 'string' from index!"
        assert self.TEST_BOOL == linked_list.delete_from_index(1), "Fail to remove item of type 'boolean' from index!"
        assert self.TEST_INT == linked_list.delete_from_index(0), "Fail to remove item of type 'int' from index!"
        assert self.TEST_FLOAT == linked_list.delete_from_index(0), "Fail to remove item of type 'float' from index!"

    def test_delete_raise_exception(self, linked_list):
        with pytest.raises(IndexError, match="Delete from empty list!"):
            linked_list.delete_from_head()

        with pytest.raises(IndexError, match="Delete from empty list!"):
            linked_list.delete_from_index(5)

        with pytest.raises(IndexError, match="Delete from empty list!"):
            linked_list.delete_from_tail()

    def test_get_index(self, linked_list):
        linked_list.add_at_head("a")
        linked_list.add_at_head("b")
        linked_list.add_at_head("c")
        linked_list.add_at_head("d")

        assert "a" == linked_list.get_index(3), 'Wrong value retrieved!'
        assert "b" == linked_list.get_index(2), 'Wrong value retrieved!'
        assert "c" == linked_list.get_index(1), 'Wrong value retrieved!'
        assert "d" == linked_list.get_index(0), 'Wrong value retrieved!'

        assert "a" == linked_list.get_index(-1), 'Fail to get value with negative index!'
        assert "b" == linked_list.get_index(-2), 'Fail to get value with negative index!'
        assert "c" == linked_list.get_index(-3), 'Fail to get value with negative index!'
        assert "d" == linked_list.get_index(-4), 'Fail to get value with negative index!'


class TestQueue:

    TEST_INT = 58
    TEST_BOOL = True
    TEST_STRING = "foobarfoobar"
    TEST_FLOAT = 101.98

    @pytest.fixture()
    def queue_under_test(self):
        return Queue()

    def test_queue_fifo_order(self, queue_under_test):
        queue_under_test.add(self.TEST_INT)
        queue_under_test.add(self.TEST_BOOL)
        queue_under_test.add(self.TEST_STRING)
        queue_under_test.add(self.TEST_FLOAT)

        assert 4 == len(queue_under_test), "Fail at queue len control!"
        assert self.TEST_INT == queue_under_test.remove(), "Fail to process values in FIFO order!"
        assert 3 == len(queue_under_test), "Fail at queue len control!"
        assert self.TEST_BOOL == queue_under_test.remove(), "Fail to process values in FIFO order!"
        assert 2 == len(queue_under_test), "Fail at queue len control!"
        assert self.TEST_STRING == queue_under_test.remove(), "Fail to process values in FIFO order!"
        assert 1 == len(queue_under_test), "Fail at queue len control!"
        assert self.TEST_FLOAT == queue_under_test.remove(), "Fail to process values in FIFO order!"
        assert 0 == len(queue_under_test), "Fail at queue len control!"

    def test_dequeuing_empty_queue(self, queue_under_test):
        with pytest.raises(IndexError, match="Delete from empty queue!"):
            queue_under_test.remove()


class TestStack:

    TEST_INT = 58
    TEST_BOOL = True
    TEST_STRING = "foobarfoobar"
    TEST_FLOAT = 101.98

    @pytest.fixture()
    def stack_under_test(self):
        return Stack()

    def test_stack_lifo_order(self, stack_under_test):
        stack_under_test.add(self.TEST_INT)
        stack_under_test.add(self.TEST_BOOL)
        stack_under_test.add(self.TEST_STRING)
        stack_under_test.add(self.TEST_FLOAT)

        assert 4 == len(stack_under_test), "Fail at stack len control!"
        assert self.TEST_FLOAT == stack_under_test.remove(), "Fail to process values in LIFO order!"
        assert 3 == len(stack_under_test), "Fail at stack len control!"
        assert self.TEST_STRING == stack_under_test.remove(), "Fail to process values in LIFO order!"
        assert 2 == len(stack_under_test), "Fail at stack len control!"
        assert self.TEST_BOOL == stack_under_test.remove(), "Fail to process values in LIFO order!"
        assert 1 == len(stack_under_test), "Fail at stack len control!"
        assert self.TEST_INT == stack_under_test.remove(), "Fail to process values in LIFO order!"
        assert 0 == len(stack_under_test), "Fail at stack len control!"

    def test_unstacking_empty_stack(self, stack_under_test):
        with pytest.raises(IndexError, match="Delete from empty stack!"):
            stack_under_test.remove()