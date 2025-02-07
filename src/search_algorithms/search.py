import random

class Searcher:

    def __init__(self, dataset= None):
        self.__dataset = dataset

    @property
    def dataset(self):
        return self.__dataset

    @dataset.setter
    def dataset(self, search_list):
        self.__dataset = search_list

    def linear_search(self, searched_value):
        """
            Implements linear search, iterating over each element until find match
        :param searched_value: value to be looked in the list
        :return: index of match or None
        """
        if self.__dataset is None:
            raise ValueError("Search list was not set!")

        count = 0
        for next_value in self.__dataset:
            if searched_value == next_value:
                return count
            count += 1

        return None

    def binary_search(self, searched_value):
        """
            Implements binary search, dividing the searched list size at every iteration
            based in the searched value compared to the central value from the subset
        :param searched_value: value to be looked in the list
        :return: index of match or None
        """
        if self.__dataset is None:
            raise ValueError("Search list was not set!")


if __name__ == "__main__":
    data = random.sample(range(10000), 10)

    my_searcher = Searcher()
    my_searcher.dataset = data

    interest_value = int(input("Inform value to search: "))
    value_idx = my_searcher.linear_search(interest_value)

    if value_idx is not None:
        print(f"The value '{interest_value} is at index {value_idx}")
    else:
        print("The searched value is not in the list!")



