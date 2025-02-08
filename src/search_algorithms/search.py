import random

from numpy.ma.core import floor


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

        return self.__recursive_search(searched_value, 0, len(self.dataset) - 1)


    def __recursive_search(self, searched_value, left_idx, right_idx):
        """
            Recursively split a list in the middle, according to the searched value
        :param searched_value: value of interest
        :param left_idx: left index for the sub-dataset
        :param right_idx: right index for the sub-dataset
        :return: index of match or None
        """
        if left_idx > right_idx:
            return None

        middle_idx = int((left_idx + right_idx) / 2)

        if searched_value == self.dataset[middle_idx]:
            return middle_idx
        elif searched_value < self.dataset[middle_idx]:
            return self.__recursive_search(searched_value, left_idx, middle_idx - 1)
        else:
            return self.__recursive_search(searched_value, middle_idx + 1, right_idx)


def main():
    data = random.sample(range(10000), 100)

    my_searcher = Searcher()
    my_searcher.dataset = data

    interest_value = int(input("Inform value to search: "))

    search_algorithm = input("Choose a search algorithm:"
                             "\n\t-Linear Search: 1"
                             "\n\t-Binary Search: 2"
                             "\n\tOption: ")
    search_algorithm = int(search_algorithm)

    if search_algorithm == 1:
        value_idx = my_searcher.linear_search(interest_value)
    elif search_algorithm == 2:
        value_idx = my_searcher.binary_search(interest_value)
    else:
        print("Invalid Search Option")
        return

    if value_idx is not None:
        print(f"The value '{interest_value} is at index {value_idx}")
    else:
        print("The searched value is not in the list!")


if __name__ == "__main__":
    main()
