import pytest
from src.search_algorithms.search import Searcher

class TestSearch:

    @pytest.fixture()
    def test_searcher(self):
        return Searcher([-531.3, 10.9, 333, 1000])

    def test_linear_search_value_present(self, test_searcher):
        assert 0 == test_searcher.linear_search(test_searcher.dataset[0]), "Fail to find value index in list!"
        assert 1 == test_searcher.linear_search(test_searcher.dataset[1]), "Fail to find value index in list!"
        assert 2 == test_searcher.linear_search(test_searcher.dataset[2]), "Fail to find value index in list!"
        assert 3 == test_searcher.linear_search(test_searcher.dataset[3]), "Fail to find value index in list!"

    def test_linear_search_invalid_value(self, test_searcher):
        assert None == test_searcher.linear_search(0), "Fail, value not in list!"
        assert None == test_searcher.linear_search(-10), "Fail, value not in list!"
        assert None == test_searcher.linear_search(500), "Fail, value not in list!"

    def test_linear_search_no_data_exception(self):
        test_searcher = Searcher()
        with pytest.raises(ValueError):
            test_searcher.linear_search(0)

    def test_binary_search_value_present(self, test_searcher):
        assert 0 == test_searcher.binary_search(test_searcher.dataset[0]), "Fail to find value index in list!"
        assert 1 == test_searcher.binary_search(test_searcher.dataset[1]), "Fail to find value index in list!"
        assert 2 == test_searcher.binary_search(test_searcher.dataset[2]), "Fail to find value index in list!"
        assert 3 == test_searcher.binary_search(test_searcher.dataset[3]), "Fail to find value index in list!"

    def test_binary_search_invalid_value(self, test_searcher):
        assert None == test_searcher.binary_search(0), "Fail, value not in list!"
        assert None == test_searcher.binary_search(-10), "Fail, value not in list!"
        assert None == test_searcher.binary_search(500), "Fail, value not in list!"

    def test_binary_search_no_data_exception(self):
        test_searcher = Searcher()
        with pytest.raises(ValueError):
            test_searcher.binary_search(0)