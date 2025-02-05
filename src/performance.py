import sys
import os
import timeit
import random
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
            self.__dict[counter] = None

            self.__linked_list.add_at_tail(test_value)
            self.__queue.add(test_value)
            self.__stack.add(test_value)
            self.__tree.insert_node(counter, None)

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

        plt.savefig(self.OUTPUT_DIR + "/basic_memory_usage.png")


if __name__ == "__main__":
    analyzer = Analyzer()
    analyzer.evaluate_memory()
