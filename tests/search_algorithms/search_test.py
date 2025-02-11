import pytest
from src.search_algorithms.search import LinearSearch, BinarySearch


class TestSearch:

    @pytest.fixture()
    def test_array(self):
        return [-531.3, 10.9, 333, 1000]

    @pytest.fixture()
    def linear_search(self):
        return LinearSearch()

    @pytest.fixture()
    def binary_search(self):
        return BinarySearch()

    def test_linear_search_value_present(self, linear_search, test_array):
        assert 0 == linear_search.search(test_array, test_array[0]), "Fail to find value index in list!"
        assert 1 == linear_search.search(test_array, test_array[1]), "Fail to find value index in list!"
        assert 2 == linear_search.search(test_array, test_array[2]), "Fail to find value index in list!"
        assert 3 == linear_search.search(test_array, test_array[3]), "Fail to find value index in list!"

    def test_linear_search_invalid_value(self, linear_search, test_array):
        assert None == linear_search.search(test_array, 0), "Fail, value not in list!"
        assert None == linear_search.search(test_array, -10), "Fail, value not in list!"
        assert None == linear_search.search(test_array, 500), "Fail, value not in list!"

    def test_linear_search_no_data_exception(self, linear_search):
        with pytest.raises(ValueError):
            linear_search.search([], 0)

    def test_binary_search_value_present(self, binary_search, test_array):
        assert 0 == binary_search.search(test_array, test_array[0]), "Fail to find value index in list!"
        assert 1 == binary_search.search(test_array, test_array[1]), "Fail to find value index in list!"
        assert 2 == binary_search.search(test_array, test_array[2]), "Fail to find value index in list!"
        assert 3 == binary_search.search(test_array, test_array[3]), "Fail to find value index in list!"

    def test_binary_search_invalid_value(self, binary_search, test_array):
        assert None == binary_search.search(test_array, 0), "Fail, value not in list!"
        assert None == binary_search.search(test_array, -10), "Fail, value not in list!"
        assert None == binary_search.search(test_array, 500), "Fail, value not in list!"

    def test_binary_search_no_data_exception(self, binary_search):
        with pytest.raises(ValueError):
            binary_search.search([], 0)
