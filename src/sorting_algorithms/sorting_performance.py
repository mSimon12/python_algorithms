import copy
import sys
import os
import timeit
import random

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from src.sorting_algorithms.sorting import Sorting


class TimeAnalyzer:
    AVERAGE_SAMPLES = 1
    REF_SCALE = 0.01

    def __init__(self, test_array, title):
        self.__test_array = test_array
        self.__title = title

        self._times = pd.DataFrame(columns=['insertion_sort', 'merge_sort', 'quicksort', 'bucket_sort'])

    @staticmethod
    def __get_reference_curves(datapoints):
        curves = { "O(n)": [2*n for n in range(1,datapoints)],
                   "O(n lg n)": [n * np.log2(n) for n in range(1,datapoints)],
                   "O(n2)": [n*n for n in range(1,datapoints)]
                   }
        return curves

    def __config_axis(self):
        self._axes.set_xlabel("Amount of data (n)", fontsize=14)
        self._axes.set_ylabel("Time (s)", fontsize=14)
        self._axes.set_xlim(self.AVERAGE_SAMPLES, len(self.__test_array))
        self._axes.set_yscale('log', base=2)
        self._axes.set_xscale('log', base=2)
        self._axes.grid(True)
        self._axes.legend(loc='upper left')

    def __plot_sorting_times(self, sorting_times:pd.DataFrame):
        sorting_times.plot(ax= self._axes)

    def __plot_ref_curves(self):
        datapoints = len(self.__test_array)
        reference_curves = self.__get_reference_curves(datapoints)
        for ref_curve_key, ref_curve in reference_curves.items():
            ref_curve = [point * self.REF_SCALE for point in ref_curve]
            self._axes.plot(ref_curve, '--', label=ref_curve_key)

    @staticmethod
    def normalize(times_dataframe):
        normalized_dataframe = copy.deepcopy(times_dataframe)
        for algorithm in normalized_dataframe.columns:
            normalized_dataframe[algorithm] = normalized_dataframe[algorithm] / normalized_dataframe[algorithm].iloc[0]

        return normalized_dataframe

    def plot_times(self):
        plt.style.use("bmh")
        fig, self._axes = plt.subplots(1, 1, figsize=(6, 6))

        normalized_times = self.normalize(self._times)
        times_moving_avg = normalized_times.rolling(window=self.AVERAGE_SAMPLES).mean()

        self.__plot_sorting_times(times_moving_avg)
        self.__plot_ref_curves()
        self.__config_axis()

        fig.suptitle(self.__title, fontsize=16, fontweight='bold')
        # fig.tight_layout()

    @staticmethod
    def __get_spaced_indices(array_length):
        indices = [array_length]

        current_power = array_length
        while current_power > 10:
            for idx in range(int(current_power/10), int(current_power), int(current_power/10)):
                indices.append(idx)
            current_power /= 10

        for idx in range(1,10):
            indices.append(idx)

        indices.sort()

        return indices

    def measure_times(self):
        sampling_amounts = self.__get_spaced_indices(len(self.__test_array))
        for data_amount in sampling_amounts:
            values_for_test = self.__test_array[:data_amount]

            insertion_sort_time = timeit.timeit(lambda: Sorting.insertion_sort(values_for_test), number=1)
            merge_sort_time = timeit.timeit(lambda: Sorting.merge_sort(values_for_test), number=1)
            quicksort_time = timeit.timeit(lambda: Sorting.quick_sort(values_for_test), number=1)
            bucket_sort_time = timeit.timeit(lambda: Sorting.bucket_sort(values_for_test), number=1)

            self._times.loc[data_amount, :] = [insertion_sort_time,
                                           merge_sort_time,
                                           quicksort_time,
                                           bucket_sort_time]


class Analyzer:
    OUTPUT_DIR = "../outputs"

    def __init__(self):
        self.__prepare_environment()

    def __prepare_environment(self):
        if not os.path.isdir(self.OUTPUT_DIR):
            os.mkdir(self.OUTPUT_DIR)

    def run_random_input_array(self):
        test_array = random.sample(range(-1000000, 1000000), 40000)
        time_checker = TimeAnalyzer(test_array, "Random Input Array")
        self.__evaluate_sorting_time(time_checker, "sorting_time_random_array")

    def run_decreasing_input_array(self):
        test_array = [v for v in range(20000, -20000, -1)]
        time_checker = TimeAnalyzer(test_array, "Decreasing Input Array")
        self.__evaluate_sorting_time(time_checker, "sorting_time_decreasing_array")

    def run_distributed_input_array(self):
        test_array = random.sample(range(-200000, 200000, 10), 40000)
        time_checker = TimeAnalyzer(test_array, "Distributed Input Array")
        self.__evaluate_sorting_time(time_checker, "sorting_time_distributed_array")

    def __evaluate_sorting_time(self, time_checker:TimeAnalyzer, file_name):
        print("Processing sorting time ..")

        time_checker.measure_times()
        time_checker.plot_times()

        # plt.show()
        plt.savefig(self.OUTPUT_DIR + f"/{file_name}.png")
        print("Done!")

if __name__ == "__main__":
    sys.setrecursionlimit(41000)

    analyzer = Analyzer()
    analyzer.run_random_input_array()
    analyzer.run_decreasing_input_array()
    analyzer.run_distributed_input_array()
