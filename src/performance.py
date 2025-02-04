import sys
import timeit
import random
import pandas as pd
from pympler import asizeof
from matplotlib import pyplot as plt

from data_structures.basic_data_structures import LinkedList, Queue, Stack
from data_structures.binary_tree import BinaryTree


class PerformanceAnalyzer:

    def __init__(self):
        self.__list = []
        self.__linked_list = LinkedList()
        self.__queue = Queue()
        self.__stack = Stack()

        self.values_for_test = random.sample(range(10000), 400)
        self.__memory_usage = pd.DataFrame(columns=['list', 'linked_list', 'queue', 'stack'])


    def __measure_memory_sizes(self):
        memory_sizes = {
            'list': asizeof.asizeof(self.__list, limit=10000, detail=True),
            'linked_list': asizeof.asizeof(self.__linked_list, limit=10000, detail=True),
            'queue': asizeof.asizeof(self.__queue, limit=10000, detail=True),
            'stack': asizeof.asizeof(self.__stack, limit=10000, detail=True)
        }
        return memory_sizes

    def analyze_memory_usage(self):
        self.__memory_usage.loc[0, :] = self.__measure_memory_sizes()

        counter = 1
        for test_value in self.values_for_test:
            self.__list.append(test_value)
            self.__linked_list.add_at_tail(test_value)
            self.__queue.add(test_value)
            self.__stack.add(test_value)

            self.__memory_usage.loc[counter, :] = self.__measure_memory_sizes()
            counter += 1

        return self.__memory_usage.copy()

    def plot_memory_usage(self):
        fig, axes = plt.subplots(1, 1)
        self.__memory_usage.plot(ax= axes)

        axes.set_xlabel("Values added (n)", fontsize=14)
        axes.set_ylabel("Memory usage (Bytes)", fontsize=14)
        axes.set_xlim(0, 400)
        axes.grid()
        plt.locator_params(axis='y', nbins=20)
        plt.locator_params(axis='x', nbins=40)
        fig.suptitle("Data Structures memory usage (Bytes)", fontsize=16, fontweight='bold')


if __name__ == "__main__":
    print("Performance evaluation!")

    performance_checker = PerformanceAnalyzer()
    performance_checker.analyze_memory_usage()
    performance_checker.plot_memory_usage()

    plt.show()


