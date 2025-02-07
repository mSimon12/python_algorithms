import sys
import os
import timeit
import random

import numpy as np
import pandas as pd
from pympler import asizeof
from matplotlib import pyplot as plt

from data_structures.basic_data_structures import LinkedList, Queue, Stack, Node
from data_structures.binary_tree import BinaryTree


class MemoryAnalyzer:

    def __init__(self, datapoints):
        self.__datapoints = datapoints
        self.__list = []
        self.__dict = {}
        self.__linked_list = LinkedList()
        self.__queue = Queue()
        self.__stack = Stack()
        self.__tree = BinaryTree()

        self.values_for_test = random.sample(range(100000), self.__datapoints)
        self.__memory_usage = pd.DataFrame(columns=['list', 'dict', 'linked_list', 'queue', 'stack', 'tree'])

    def __measure_memory_sizes(self):
        memory_sizes = {
            'list': asizeof.asizeof(self.__list, limit=10000, detail=True),
            'dict': asizeof.asizeof(self.__dict, limit=10000, detail=True),
            'linked_list': asizeof.asizeof(self.__linked_list, limit=10000, detail=True),
            'queue': asizeof.asizeof(self.__queue, limit=10000, detail=True),
            'stack': asizeof.asizeof(self.__stack, limit=10000, detail=True),
            'tree': asizeof.asizeof(self.__tree, limit=10000, detail=True)
        }
        return memory_sizes

    def gather_memory_usage(self):
        self.__memory_usage.loc[0, :] = self.__measure_memory_sizes()

        counter = 1
        for test_value in self.values_for_test:
            self.__list.append(test_value)
            self.__dict[test_value] = None

            self.__linked_list.add_at_tail(test_value)
            self.__queue.add(test_value)
            self.__stack.add(test_value)
            self.__tree.insert_node(test_value, None)

            self.__memory_usage.loc[counter, :] = self.__measure_memory_sizes()
            counter += 1

        return self.__memory_usage.copy()

    def plot_memory_usage(self):
        plt.style.use("bmh")

        fig, axes = plt.subplots(1, 1)
        self.__memory_usage.plot(ax= axes)

        axes.set_xlabel("Amount of data (n)", fontsize=14)
        axes.set_ylabel("Memory usage (Bytes)", fontsize=14)
        axes.set_xlim(0, self.__datapoints)
        axes.grid(True)
        plt.locator_params(axis='y', nbins=20)
        plt.locator_params(axis='x', nbins=15)
        fig.suptitle("Data Structures memory usage", fontsize=16, fontweight='bold')
        fig.tight_layout()


class TimeAnalyzer:

    def __init__(self, datapoints, title):
        self.__datapoints = datapoints
        self.__title = title
        self._ref_curves_scale = 0.000001

        self._list = []
        self._dict = {}
        self._linked_list = LinkedList()
        self._tree = BinaryTree()

        self.values_for_test = random.sample(range(100000), self.__datapoints)
        self._times = pd.DataFrame(columns=['list', 'linked_list', 'dict', 'tree'])

    def measure_times(self):
        pass

    @staticmethod
    def __get_reference_curves(datapoints):
        curves = { 'O(1)': [1]*datapoints,
                   'O(log n)': np.log10(range(1,datapoints)),
                   "O(n)": range(0,datapoints)
                   }
        return curves

    def __config_axis(self, ax):
        ax.set_xlabel("Amount of data (n)", fontsize=14)
        ax.set_ylabel("Time (s)", fontsize=14)
        ax.set_xlim(50, self.__datapoints)
        ax.set_yscale('log')
        ax.set_xscale('log')
        ax.grid(True)
        ax.legend(loc='upper left')

    def __plot_linear_data(self, linear_data:pd.DataFrame, ax):
        linear_data.plot(ax= ax)

        linear_curve = self.__get_reference_curves(self.__datapoints)['O(n)']
        linear_curve = [point * self._ref_curves_scale for point in linear_curve]
        ax.plot(linear_curve, '--', label='O(n)')

        self.__config_axis(ax)

    def __plot_non_linear_data(self, non_linear_data: pd.DataFrame, ax):
        non_linear_data.plot(ax= ax)

        reference_curves = self.__get_reference_curves(self.__datapoints)
        reference_curves.pop('O(n)')
        for ref_curve_key, ref_curve in reference_curves.items():
            ref_curve = [point * self._ref_curves_scale for point in ref_curve]
            ax.plot(ref_curve, '--', label=ref_curve_key)

        self.__config_axis(ax)

    def plot_times(self):
        plt.style.use("bmh")
        fig, self._axes = plt.subplots(2, 1, figsize=(6, 8), sharex=True)

        times_moving_avg = self._times.rolling(window=50).mean()

        self.__plot_linear_data(times_moving_avg.loc[:, ['list', 'linked_list']], self._axes[0])
        self.__plot_non_linear_data(times_moving_avg.loc[:, ['dict', 'tree']], self._axes[1])

        fig.suptitle(self.__title, fontsize=16, fontweight='bold')
        fig.tight_layout()


class InsertTimeAnalyzer(TimeAnalyzer):

    def __init__(self, datapoints):
        super().__init__(datapoints, "Insertion Time")

    def measure_times(self):
        def add_to_dict(new_key):
            self._dict[new_key] = None

        self._linked_list.add_at_head(-1)

        counter = 0
        for test_value in self.values_for_test:
            new_index = random.randint(0, counter)
            list_insert_time = timeit.timeit(lambda: self._list.insert(new_index, test_value), number=1)
            linked_list_insert_time = timeit.timeit(lambda: self._linked_list.add_at_index(new_index, test_value), number=1)

            dict_insert_time = timeit.timeit(lambda: add_to_dict(test_value), number=1)
            tree_insert_time = timeit.timeit(lambda: self._tree.insert_node(test_value, None), number=1)

            self._times.loc[counter, :] = [list_insert_time,
                                           linked_list_insert_time,
                                           dict_insert_time,
                                           tree_insert_time]
            counter += 1


class SearchTimeAnalyzer(TimeAnalyzer):

    def __init__(self, datapoints):
        super().__init__(datapoints, "Search Time")

    def measure_times(self):
        self._linked_list.add_at_head(-1)

        counter = 0
        for test_value in self.values_for_test:
            new_index = random.randint(0, counter)
            self._list.insert(new_index, test_value)
            self._linked_list.add_at_index(new_index, test_value)
            self._dict[test_value] = None
            self._tree.insert_node(test_value, None)

            if counter == 0:
                item_to_search_idx = 0
            else:
                item_to_search_idx = random.sample(range(0,counter), 1)[0]
            key_to_search = self.values_for_test[item_to_search_idx]

            list_search_time = timeit.timeit(lambda: key_to_search in self._list, number=1)
            linked_list_search_time = timeit.timeit(lambda: self._linked_list.get_index(item_to_search_idx), number=1)
            dict_search_time = timeit.timeit(lambda: self._dict[key_to_search], number=1)
            tree_search_time = timeit.timeit(lambda: self._tree.get_value(key_to_search), number=1)

            self._times.loc[counter, :] = [list_search_time,
                                           linked_list_search_time,
                                           dict_search_time,
                                           tree_search_time]
            counter += 1


class DeleteTimeAnalyzer(TimeAnalyzer):

    def __init__(self, datapoints):
        super().__init__(datapoints, "Delete Time")

    def measure_times(self):
        self._linked_list.add_at_head(-1)

        counter = 0
        for test_value in self.values_for_test:
            new_index = random.randint(0, counter)
            self._list.insert(new_index, test_value)
            self._linked_list.add_at_index(new_index, test_value)
            self._dict[test_value] = None
            self._tree.insert_node(test_value, None)

            counter += 1

        run_idx = len(self.values_for_test)
        while len(self.values_for_test) > 0:
            item_to_delete_idx = random.sample(range(0, len(self.values_for_test)), 1)[0]
            key_to_delete = self.values_for_test[item_to_delete_idx]
            self.values_for_test.remove(key_to_delete)

            list_delete_time = timeit.timeit(lambda: self._list.remove(key_to_delete), number=1)
            linked_list_delete_time = timeit.timeit(lambda: self._linked_list.delete_from_index(item_to_delete_idx), number=1)
            dict_delete_time = timeit.timeit(lambda: self._dict.pop(key_to_delete), number=1)
            tree_delete_time = timeit.timeit(lambda: self._tree.delete_node(key_to_delete), number=1)

            self._times.loc[run_idx, :] = [list_delete_time,
                                           linked_list_delete_time,
                                           dict_delete_time,
                                           tree_delete_time]
            run_idx -= 1


class Analyzer:
    OUTPUT_DIR = "outputs"

    def __init__(self):
        self.__prepare_environment()

    def __prepare_environment(self):
        if not os.path.isdir(self.OUTPUT_DIR):
            os.mkdir(self.OUTPUT_DIR)

    def evaluate_memory(self):
        print("Processing memory usage ..")
        memory_checker = MemoryAnalyzer(400)
        memory_checker.gather_memory_usage()
        memory_checker.plot_memory_usage()

        plt.savefig(self.OUTPUT_DIR + "/memory_usage.png")
        print("Done!")

    def evaluate_time(self, time_analyzer:TimeAnalyzer, output_file):
        time_analyzer.measure_times()
        time_analyzer.plot_times()

        plt.savefig(self.OUTPUT_DIR + output_file)
        plt.show()

    def evaluate_insertion_time(self):
        print("Processing insertion time ..")
        insert_timer = InsertTimeAnalyzer(20000)
        self.evaluate_time(insert_timer, "/insertion_time.png")
        print("Done!")

    def evaluate_search_time(self):
        print("Processing search time ..")
        search_timer = SearchTimeAnalyzer(20000)
        self.evaluate_time(search_timer, "/search_time.png")
        print("Done!")

    def evaluate_delete_time(self):
        print("Processing delete time ..")
        search_timer = DeleteTimeAnalyzer(20000)
        self.evaluate_time(search_timer, "/delete_time.png")
        print("Done!")


if __name__ == "__main__":
    analyzer = Analyzer()
    # analyzer.evaluate_memory()
    # analyzer.evaluate_insertion_time()
    # analyzer.evaluate_search_time()
    analyzer.evaluate_delete_time()
