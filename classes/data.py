#!/usr/bin/python

# local packages
from .settings import *

# python imports
import csv


class DataProcessor(object):

    filtered_data_filepath = FILTERED_DATA_FILE_CSV
    processed_data_filepath = PROCESSED_DATA_FILE_CSV

    def __init__(self):
        self.gender_dict = GENDER_DICT

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
        :return: Nothing
        """

        # open the file need to be write
        with open(filepath, 'w') as csvfile:
            # initial the writer
            writer = csv.writer(csvfile, delimiter=',')

            # write each row
            for row in data:
                writer.writerow(row)

        return

    def data_converter(self, variable, element_value):
        new_value = None
        if variable == "GENDER":
            new_value = self.gender_dict[element_value]

        return new_value

    def update_row(self, title_list, row, variables=MODIFIED_VARIABLES):

        for variable in variables:
            element_index = title_list.index(variable)
            element_value = row[element_index]
            new_element_value = self.data_converter(variable, element_value)
            row[element_index] = new_element_value

        # indexes = list(map(title_list.index, variables))
        # print("This is indexes", indexes)
        # map(row.__setitem__, indexes,
        #     list(
        #         map(
        #             self.data_converter, variables, list(map(row.__getitem__, indexes))
        #         )
        #     )
        # )

        return row

    def modify_the_data(self, input_filepath=filtered_data_filepath, output_filepath=processed_data_filepath):
        """
            modify the data according to the requirements
        :param input_filepath: the name of input file with its path
        :param output_filepath: the name of output file with its path
        :return: Nothing
        """
        output_data = list()
        title_list = None

        data = self.read_csv(input_filepath)
        for i, row in enumerate(data):
            # print(i, line)
            if i == 0:
                # get the header
                title_list = row
                output_data.append(title_list)
            else:
                # get and update the content
                row = self.update_row(title_list, row)
                output_data.append(row)

        self.write_csv(output_filepath, output_data)
        return





