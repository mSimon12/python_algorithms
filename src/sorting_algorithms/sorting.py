import copy
import math

class Sorting:

    @staticmethod
    def process_input(input_array):
        if not all(isinstance(x, (int,float)) for x in input_array):
            raise ValueError("Invalid input array!")

        return copy.deepcopy(input_array)

    @classmethod
    def insertion_sort(cls, input_array):
        """
            Sort the input array with Insertion Sort algorithm
        :param input_array: array to be sorted
        :return: array sorted by ascending values
        """
        array = cls.process_input(input_array)

        for current_idx in range(1, len(array)):
            key = array[current_idx]
            compared_idx = current_idx - 1
            while (compared_idx >= 0) and (array[compared_idx] > key):
                array[compared_idx + 1] = array[compared_idx]
                compared_idx -= 1
            array[compared_idx + 1] = key

        return array

    @staticmethod
    def __merge(array, left, middle, right):
        """
            Merge 2 subsets by getting the smallest value at each iteration
        :param array: array being sorted
        :param left: left side of the sub-array
        :param middle: middle point of the sub-array
        :param right: right side of the sub-array
        :return: None
        """
        left_array = array[left:middle + 1]
        right_array = array[middle + 1:right + 1]

        left_array.append(math.inf)
        right_array.append(math.inf)

        i, j = 0, 0
        for k in range(left, right + 1):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1

    @classmethod
    def __recursive_merge_sort(cls, array, left_idx, right_idx):
        """
            Recurssively breaks the array in 2 sub-arrays and merge it back
        :param array: array being sorted
        :param left_idx: left side of the sub-array
        :param right_idx: right side of the sub-array
        :return: None
        """
        if left_idx < right_idx:
            middle = int((left_idx + right_idx) / 2)
            cls.__recursive_merge_sort(array, left_idx, middle)
            cls.__recursive_merge_sort(array, middle + 1, right_idx)
            cls.__merge(array, left_idx, middle, right_idx)

    @classmethod
    def merge_sort(cls, input_array):
        """
            Sort the input array with Merge Sort algorithm
        :param input_array: array to be sorted
        :return: array sorted by ascending values
        """
        array = cls.process_input(input_array)
        cls.__recursive_merge_sort(array, 0 , len(array) - 1)
        return array


def main():
    unsorted_array = [3500, -8, 10, 1, -98, 56, 1000, 0, 70]
    sorted_array = Sorting.insertion_sort(unsorted_array)
    print("Initial array: ", unsorted_array)
    print("Insertion Sort: ", sorted_array)

    sorted_array = Sorting.merge_sort(unsorted_array)
    print("\nInitial array: ", unsorted_array)
    print("Merge Sort: ", sorted_array)


if __name__ == "__main__":
    main()
