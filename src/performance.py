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

    def __init__(self):
        self.__list = []
        self.__dict = {}
        self.__linked_list = LinkedList()
        self.__queue = Queue()
        self.__stack = Stack()
        self.__tree = BinaryTree()

        self.values_for_test = random.sample(range(10000), 400)
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

        axes.set_xlabel("Data added to Data Structure(n)", fontsize=14)
        axes.set_ylabel("Memory usage (Bytes)", fontsize=14)
        axes.set_xlim(0, 400)
        axes.grid(True)
        plt.locator_params(axis='y', nbins=20)
        plt.locator_params(axis='x', nbins=15)
        fig.suptitle("Data Structures memory usage", fontsize=16, fontweight='bold')
        fig.tight_layout()


class PerformanceAnalyzer:

    def __init__(self, datapoints):
        self.__list = []
        self.__dict = {}
        self.__linked_list = LinkedList()
        self.__tree = BinaryTree()

        self.__datapoints = datapoints
        self.values_for_test = random.sample(range(100000), self.__datapoints)

        self.__insert_times = pd.DataFrame(columns=['list', 'dict', 'linked_list', 'tree'])
        self.__search_times = pd.DataFrame(columns=['list', 'dict', 'linked_list', 'tree'])

    def measure_insert_time(self):
        def add_to_dict(new_key):
            self.__dict[new_key] = None

        self.__linked_list.add_at_head(-1)

        counter = 0
        for test_value in self.values_for_test:
            new_index = random.randint(0, counter)
            list_insert_time = timeit.timeit(lambda: self.__list.insert(new_index, test_value), number=1)
            linked_list_insert_time = timeit.timeit(lambda: self.__linked_list.add_at_index(new_index, test_value), number=1)

            dict_insert_time = timeit.timeit(lambda: add_to_dict(test_value), number=1)
            tree_insert_time = timeit.timeit(lambda: self.__tree.insert_node(test_value, None), number=1)

            self.__insert_times.loc[counter, :] = [list_insert_time,
                                                   dict_insert_time,
                                                   linked_list_insert_time,
                                                   tree_insert_time]

            # measure search times
            if counter == 0:
                item_to_search_idx = 0
            else:
                item_to_search_idx = random.sample(range(0,counter), 1)[0]
            key_to_search = self.values_for_test[item_to_search_idx]

            list_search_time = timeit.timeit(lambda: key_to_search in self.__list, number=1)
            linked_list_search_time = timeit.timeit(lambda: self.__linked_list.get_index(item_to_search_idx), number=1)

            dict_search_time = timeit.timeit(lambda: self.__dict[key_to_search], number=1)
            tree_search_time = timeit.timeit(lambda: self.__tree.get_value(key_to_search), number=1)

            self.__search_times.loc[counter, :] = [list_search_time, dict_search_time, linked_list_search_time, tree_search_time]

            counter += 1


    @staticmethod
    def __get_reference_curves(datapoints):
        curves = { 'constant': [1]*datapoints,
                   'logn': np.log10(range(1,datapoints)),
                   "linear": range(0,datapoints)
                   }
        return curves

    def plot_insert_time(self):
        plt.style.use("bmh")

        fig, axes = plt.subplots(1, 1)
        speeds_rolling_mean= self.__insert_times.rolling(window=50).mean()
        speeds_rolling_mean.plot(ax= axes)

        # Plot
        scale = 0.000001
        for ref_curve_key, ref_curve in self.__get_reference_curves(self.__datapoints).items():
            ref_curve = [point*scale for point in ref_curve]
            plt.plot(ref_curve, '--', label=ref_curve_key)

        axes.set_xlabel("Data added to Data Structure(n)", fontsize=14)
        axes.set_ylabel("Time (s)", fontsize=14)
        axes.set_xlim(50, self.__datapoints)
        axes.grid(True)
        plt.locator_params(axis='y', nbins=20)
        plt.locator_params(axis='x', nbins=15)
        fig.suptitle("Insert Time", fontsize=16, fontweight='bold')
        fig.tight_layout()
        plt.legend()
        plt.yscale('log')
        plt.xscale('log')

    def plot_search_time(self):
        plt.style.use("bmh")

        fig, axes = plt.subplots(1, 1)
        speeds_rolling_mean= self.__search_times.rolling(window=50).mean()
        speeds_rolling_mean.plot(ax= axes)

        # Plot
        scale = 0.000001
        for ref_curve_key, ref_curve in self.__get_reference_curves(self.__datapoints).items():
            ref_curve = [point*scale for point in ref_curve]
            plt.plot(ref_curve, '--', label=ref_curve_key)

        axes.set_xlabel("Data added to Data Structure(n)", fontsize=14)
        axes.set_ylabel("Time (s)", fontsize=14)
        axes.set_xlim(50, self.__datapoints)
        axes.grid(True)
        plt.locator_params(axis='y', nbins=20)
        plt.locator_params(axis='x', nbins=15)
        fig.suptitle("Search Time", fontsize=16, fontweight='bold')
        fig.tight_layout()
        plt.legend()
        plt.yscale('log')
        plt.xscale('log')

class Analyzer:
    OUTPUT_DIR = "outputs"

    def __init__(self):
        self.__prepare_environment()

    def __prepare_environment(self):
        if not os.path.isdir(self.OUTPUT_DIR):
            os.mkdir(self.OUTPUT_DIR)

    def evaluate_memory(self):
        print("Memory evaluation!")
        memory_checker = MemoryAnalyzer()
        memory_checker.gather_memory_usage()
        memory_checker.plot_memory_usage()

        plt.savefig(self.OUTPUT_DIR + "/memory_usage.png")

    def evaluate_insertion_time(self):
        performance_checker = PerformanceAnalyzer(10000)
        performance_checker.measure_insert_time()
        performance_checker.plot_insert_time()
        performance_checker.plot_search_time()

        # plt.savefig(self.OUTPUT_DIR + "/insert_time.png")
        plt.show()


if __name__ == "__main__":
    analyzer = Analyzer()
    # analyzer.evaluate_memory()

    analyzer.evaluate_insertion_time()
