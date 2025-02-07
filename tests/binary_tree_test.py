import pytest
from src.data_structures.binary_tree import BinaryTree

class TestBinaryTree:

    @pytest.fixture()
    def tree_under_test(self):
        return BinaryTree()

    @pytest.fixture
    def keys_to_test(self):
        return [58, True, "foobarfoobar", 101.98]

    @pytest.fixture
    def int_keys(self):
        return [1, 15, 5, 150, 13, -6, 8, 9, 7]

    def test_tree_insert_types(self, tree_under_test, keys_to_test):
        for test_key in keys_to_test:
            tree_under_test.insert_node(test_key, "value")
            node_value = tree_under_test.get_value(test_key)
            assert "value" == node_value, f"Error inserting key of type {type(test_key)}"

    def test_insert_duplicate_key_exception(self, tree_under_test, keys_to_test):
        for test_key in keys_to_test:
            tree_under_test.insert_node(test_key, "value")
            with pytest.raises(IndexError, match="Key already exists!"):
                tree_under_test.insert_node(test_key)

    def test_insert_invalid_key_type(self, tree_under_test):
        with pytest.raises(IndexError, match="Key must not be a List!"):
            tree_under_test.insert_node([10, 56], 15)

        with pytest.raises(IndexError, match="Key must not be a Dict!"):
            tree_under_test.insert_node({"a": 56}, 15)

    def test_delete_valid_node(self, tree_under_test, int_keys):
        for key in int_keys:
            tree_under_test.insert_node(key, "value")

        tree_under_test.delete_node(8)
        assert 8 not in tree_under_test.get_sorted_tree_keys(), "Error deleting node with 2 children from Tree!"

        tree_under_test.delete_node(15)
        assert 15 not in tree_under_test.get_sorted_tree_keys(), "Error deleting node with 1 child from Tree!"

        tree_under_test.delete_node(-6)
        assert -6 not in tree_under_test.get_sorted_tree_keys(), "Error deleting node without children from Tree!"

    def test_delete_invalid_node_exception(self, tree_under_test, int_keys):
        for key in int_keys:
            tree_under_test.insert_node(key, "value")

        index_to_remove = int_keys.pop()
        tree_under_test.delete_node(index_to_remove)
        with pytest.raises(IndexError, match="Invalid key!"):
            tree_under_test.delete_node(index_to_remove)

    def test_constant_sorting_output(self, tree_under_test, int_keys):
        count = 1
        for key in int_keys:
            tree_under_test.insert_node(key, count)
            count += 1

        sorted_keys = tree_under_test.get_sorted_tree_keys()
        for i in range(1000):
            assert sorted_keys == tree_under_test.get_sorted_tree_keys(), "Returning variable ascending sorted keys!"

        sorted_values = tree_under_test.get_sorted_tree_values()
        for i in range(1000):
            assert sorted_values == tree_under_test.get_sorted_tree_values(), "Returning variable ascending sorted values!"

        sorted_keys = tree_under_test.get_sorted_tree_keys(reverse=True)
        for i in range(1000):
            assert sorted_keys == tree_under_test.get_sorted_tree_keys(reverse=True), "Returning variable descending sorted keys!"

        sorted_values = tree_under_test.get_sorted_tree_values(reverse=True)
        for i in range(1000):
            assert sorted_values == tree_under_test.get_sorted_tree_values(reverse=True), "Returning variable descending sorted values!"

    def test_updating_node_value(self,tree_under_test):
        tree_under_test.insert_node("a", 150)
        tree_under_test.set_value("a", 100)
        assert 100 == tree_under_test.get_value("a"), "Failed to update node value!"

        tree_under_test.insert_node(True, [150, 89])
        tree_under_test.set_value(True, "new_value")
        assert "new_value" == tree_under_test.get_value(True), "Failed to update node value!"

        tree_under_test.insert_node(5, "initial_value")
        tree_under_test.set_value(5, -11.5)
        assert -11.5 == tree_under_test.get_value(5), "Failed to update node value!"

    def test_invalid_node_exception(self, tree_under_test):
        with pytest.raises(IndexError, match="Invalid key!"):
            tree_under_test.get_value("a")

        with pytest.raises(IndexError, match="Invalid key!"):
            tree_under_test.set_value("a", 0)

