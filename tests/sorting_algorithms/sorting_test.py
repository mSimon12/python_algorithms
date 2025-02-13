import pytest
from src.sorting_algorithms.sorting import Sorting

class TestSorting:

    @pytest.fixture()
    def invalid_input(self):
        return ["a", -8, 10.8, "foo", True, 50000]

    @pytest.fixture()
    def unsorted_array(self):
        return [3500, -8, 10, 1, -98, 56, 3, 1000, 0, 70]

    @pytest.fixture()
    def sorted_array(self):
        return [-98, -8, 0, 1, 3, 10, 56, 70, 1000, 3500]

    def test_sorting_invalid_input_exception(self, invalid_input):
        with pytest.raises(ValueError, match="Invalid input array!"):
            Sorting.insertion_sort(invalid_input)

        with pytest.raises(ValueError, match="Invalid input array!"):
            Sorting.merge_sort(invalid_input)

        with pytest.raises(ValueError, match="Invalid input array!"):
            Sorting.quick_sort(invalid_input)

        with pytest.raises(ValueError, match="Invalid input array!"):
            Sorting.bucket_sort(invalid_input)

    def test_insertion_sort(self, unsorted_array, sorted_array):
        assert sorted_array == Sorting.insertion_sort(unsorted_array), "Fail to sort the array!"

    def test_merge_sort(self, unsorted_array, sorted_array):
        assert sorted_array == Sorting.merge_sort(unsorted_array), "Fail to sort the array!"

    def test_quick_sort(self, unsorted_array, sorted_array):
        assert sorted_array == Sorting.quick_sort(unsorted_array), "Fail to sort the array!"

    def test_bucket_sort(self, unsorted_array, sorted_array):
        assert sorted_array == Sorting.bucket_sort(unsorted_array), "Fail to sort the array!"
