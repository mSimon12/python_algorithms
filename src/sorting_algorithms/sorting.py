import copy


class Sorting:

    @staticmethod
    def process_input(func):
        def input_checker(*args, **kwargs):
            input_array = args[0]
            if not all(isinstance(x, (int,float)) for x in input_array):
                raise ValueError("Invalid input array!")

            array_copy = copy.deepcopy(input_array)
            return func(array_copy)
        return input_checker

    @process_input
    @staticmethod
    def insertion_sort(input_array):
        for current_idx in range(1, len(input_array)):
            key = input_array[current_idx]
            compared_idx = current_idx - 1
            while (compared_idx >= 0) and (input_array[compared_idx] > key):
                input_array[compared_idx + 1] = input_array[compared_idx]
                compared_idx -= 1
            input_array[compared_idx + 1] = key

        return input_array


def main():
    unsorted_array = [3500, -8, 10, 1, -98, 56, 1000, 0, 70]
    print(unsorted_array)

    sorted_array = Sorting.insertion_sort(unsorted_array)
    print(sorted_array)


if __name__ == "__main__":
    main()
