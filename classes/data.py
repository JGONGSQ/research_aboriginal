#!/usr/bin/python

# local packages
from .settings import *

# python imports
import csv


class DataProcessor(object):

    filtered_data_filepath = FILTERED_DATA_FILE_CSV
    processed_data_filepath = PROCESSED_DATA_FILE_CSV

    # def __init__(self):
    #     print(123)

    def read_csv(self, filepath):
        """
            read the csv file from the path
        :param filepath: the name of the input file with its path
        :return: List data
        """
        # initial the data list
        data = list()

        with open(filepath, 'rU') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',')

            for row in file_reader:
                data.append(row)

        return data

    def write_csv(self, filepath, data):
        """
            Write the results list to generate a new data file
        :param filename: the name of the output file with its path
        :param data: its a two-dimensional array
        :return: True if success
        """

        # open the file need to be write
        with open(filepath, 'w') as csvfile:
            # initial the writer
            writer = csv.writer(csvfile, delimiter=',')

            # write each row
            for row in data:
                writer.writerow(row)

        return

    def modify_the_data(self, input_filepath=filtered_data_filepath, output_filepath=processed_data_filepath):
        data = self.read_csv(input_filepath)
        for line in data:
            print(line)

        return



