#!/usr/bin/python

# local packages
from settings import *

# python imports
import csv


class DataProcessor(object):

    filtered_data_filepath = FILTERED_DATA_FILE_CSV
    processed_data_filepath = FILTERED_PROCESSED_DATA_FILE_CSV

    def __init__(self):
        self.gender_dict = GENDER_DICT
        self.agegroup_dict = AGEGROUP_DICT
        self.marital_dict = MARITAL_DICT
        self.purpose_dict = PURPOSE_DICT
        self.boolean_dict = BOOLEAN_DICT
        self.customs_dict = CUSTOMS_DICT
        self.country_dict = COUNTRY_DICT
        self.airline_dict = AIRLINE_DICT
        self.region_dict = REGION_DICT
        self.partype_dict = PARTYPE_DICT

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
        if variable == GENDER_STR:
            try:
                new_value = self.gender_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable == AGEGROUP_STR:
            try:
                new_value = self.agegroup_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable == MARITAL_STR:
            try:
                new_value = self.marital_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable == PURPOSE_STR:
            try:
                new_value = self.purpose_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable in [INT_BOOKING_STR, PARENT_STR, PACKAGE_STR]:
            try:
                new_value = self.boolean_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable == CUSTOMS_STR:
            try:
                new_value = self.customs_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable == COUNTRY_STR:
            try:
                new_value = self.country_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable == AIRLINE_STR:
            try:
                new_value = self.airline_dict[element_value]
            except Exception:
                new_value = 'Other'

        if variable in [REGION1_STR, REGION2_STR, REGION3_STR, REGION4_STR, REGION5_STR]:
            try:
                new_value = self.region_dict[element_value]
            except Exception:
                if element_value == "NA":
                    new_value = element_value
                else:
                    new_value = 'Other'

        if variable == PARTYPE_STR:
            try:
                new_value = self.partype_dict[element_value]
            except Exception:
                new_value = 'Other'

        return new_value

    def update_row(self, title_list, row, variables=MODIFIED_VARIABLES):

        for variable in variables:
            element_index = title_list.index(variable)
            element_value = row[element_index]
            new_element_value = self.data_converter(variable, element_value)
            row[element_index] = new_element_value

        return row

    def get_the_variable_list(self, variable):

        if variable == 'ORIGIN':
            variable_list = ORIGIN_LIST

        elif variable == 'PARENT':
            variable_list = PARENT_LIST

        elif variable == 'YOUNGEST':
            variable_list = YOUNGEST_LIST

        elif variable == "GENDER":
            variable_list = GENDER_LIST

        elif variable == 'MARITAL':
            variable_list = MARITAL_LIST

        elif variable == 'EMPLOYMENT':
            variable_list = EMPLOYMENT_LIST

        elif variable == 'HOUSINC':
            variable_list = HOUSINC_LIST

        elif variable == 'LIFECYCLE':
            variable_list = LIFECYCLE_LIST

        elif variable == 'AGEGROUP':
            variable_list = AGEGROUP_LIST

        elif variable == 'PARTYPE':
            variable_list = PARTYPE_LIST

        elif variable == 'GROUPTYPE':
            variable_list = GROUPTYPE_LIST

        elif variable == 'TRIP_PURPOSE':
            variable_list = TRIP_PURPOSE_LIST

        elif variable == 'CUSTOMS':
            variable_list = CUSTOMS_LIST

        elif variable == 'COUNTRY':
            variable_list = COUNTRY_LIST

        else:
            variable_list = [variable]

        return variable_list

    def get_the_variable_codes(self, variable):
        variable_codes = None

        if variable == 'ORIGIN':
            variable_codes = ORIGIN_CODE

        elif variable == 'PARENT':
            variable_codes = PARENT_CODE

        elif variable == 'YOUNGEST':
            variable_codes = YOUNGEST_CODE

        elif variable == "GENDER":
            variable_codes = GENDER_CODE

        elif variable == 'MARITAL':
            variable_codes = MARITAL_CODE

        elif variable == 'EMPLOYMENT':
            variable_codes = EMPLOYMENT_CODE

        elif variable == 'HOUSINC':
            variable_codes = HOUSINC_CODE

        elif variable == 'LIFECYCLE':
            variable_codes = LIFECYCLE_CODE

        elif variable == 'AGEGROUP':
            variable_codes = AGEGROUP_CODE

        elif variable == 'PARTYPE':
            variable_codes = PARTYPE_CODE

        elif variable == 'GROUPTYPE':
            variable_codes = GROUPTYPE_CODE

        elif variable == 'TRIP_PURPOSE':
            variable_codes = TRIP_PURPOSE_CODE

        elif variable == 'CUSTOMS':
            variable_codes = CUSTOMS_CODE

        elif variable == 'COUNTRY':
            variable_codes = COUNTRY_CODE

        return variable_codes

    def find_index_in_list(self, list, value):
        index = None
        for i, sub_list in enumerate(list):
            for item in sub_list:
                if item == value:
                    index = i
        return index

    def get_the_utility_variable_data(self, input_field_list, row, variable, variable_codes):
        """
        :param input_field_list:
        :param row:
        :param variable:
        :param variable_codes:
        :return:
        """
        variable_data = [0] * variable_codes.__len__()
        value = row.__getitem__(input_field_list.index(variable))
        print("### This is the value in the line:", value, variable)
        if value:
            try:
                variable_data.__setitem__(self.find_index_in_list(list=variable_codes, value=value), 1)
            except Exception:
                if variable == COUNTRY_STR:
                    variable_data[-1] = 1

        return variable_data

    def get_utility_parameters_list(self, utility_parameters):
        utility_parameters_list = list()
        for variable in utility_parameters:
            variable_list = self.get_the_variable_list(variable)
            utility_parameters_list += variable_list
        return utility_parameters_list

    def get_selected_location(self, location, alternative_code):
        if location in alternative_code:
            return location
        return location[0]

    def get_the_destination_data(self, input_fields_list, row, alternatives_code):
        destination_data = [0] * alternatives_code.__len__()

        number_of_stops = row.__getitem__(input_fields_list.index('NUMSTOP'))

        for i in range(int(number_of_stops)):
            location_code = row.__getitem__(input_fields_list.index('REGN%s' % str(i + 1)))
            selected_location = self.get_selected_location(location_code, alternatives_code)

            # print("This is location code", location_code, "this is selected location", selected_location)

            nites = row.__getitem__(input_fields_list.index('NITES%s' % str(i + 1)))
            destination_data[alternatives_code.index(selected_location)] += int(nites)

        return destination_data

    def get_utility_parameters_value(self, input_field_list, utility_parameters, row):
        value_list = list()
        # print utility_parameters
        for variable in utility_parameters:
            variable_codes = self.get_the_variable_codes(variable)
            # print variable
            if variable_codes:
                variable_data = self.get_the_utility_variable_data(
                    input_field_list=input_field_list,
                    row=row,
                    variable=variable,
                    variable_codes=variable_codes
                )
                value_list += variable_data
            else:
                # print input_field_list.index(variable)
                value_list.append(row.__getitem__(int(input_field_list.index(variable))))

        return value_list

    def get_the_activity_choice(self, input_fields_list, row):
        # get the value
        activity_particiate = map(row.__getitem__, map(input_fields_list.index, Activity_WITH_IndCommunity))
        community_participate = map(row.__getitem__, map(input_fields_list.index, Participate_AT_IndCommunity))
        # print("###", activity_particiate, community_participate, "###")

        # if the tourist participate any activity or take the tour to the aboriginal community
        if any(item in ['1'] for item in activity_particiate) \
                or not any(item in [' ', 'NA'] for item in community_participate):
            return [1]
        return [0]

    def modify_the_data(self, input_filepath=filtered_data_filepath, output_filepath=processed_data_filepath):
        """
            modify the data for NB model
        :param input_filepath: the name of input file with its path
        :param output_filepath: the name of output file with its path
        :return: None
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

    def modify_the_data_mdcev(self,
                              input_filepath, output_filepath, utility_parameters,
                              alternatives_code=DESTINATION_ALTERNATIVES_CODES,
                              alternatives_list=DESTINATION_ALTERNATIVES_LIST,
                              compulsory_fields=COMPULSORY_FIELDS, number_of_data=400):
        """
            modify the data for MDCEV model
        :return: None
        """

        output_data = list()
        input_fields_list = None
        index_number = 1
        data_count = 0

        extra_parameters = ['PARTICIPATE_IndActivity']

        # need to modify the line
        utility_parameters_list = self.get_utility_parameters_list(utility_parameters)
        output_fields_list = compulsory_fields + alternatives_list + utility_parameters_list + extra_parameters
        output_data.append(output_fields_list)

        data = self.read_csv(input_filepath)

        for i, row in enumerate(data):
            if i == 0:
                input_fields_list = row
            elif i > number_of_data:
                break
            else:
                utility_data = map(row.__getitem__, map(input_fields_list.index, utility_parameters))
                if not any(item in [' ', 'NA'] for item in utility_data):
                    print("This is the utility data",  list(utility_data))
                #
                compulsory_data = list(map(row.__getitem__, map(input_fields_list.index, compulsory_fields)))

                #
                destination_data = self.get_the_destination_data(input_fields_list, row, alternatives_code)

                #
                utility_parameters_data = self.get_utility_parameters_value(input_fields_list, utility_parameters, row)

                #
                indigenous_activity_choice = self.get_the_activity_choice(input_fields_list, row)

                print("##########################", destination_data, utility_parameters_data, indigenous_activity_choice)
                data_set = compulsory_data + destination_data + utility_parameters_data + indigenous_activity_choice
                output_data.append(data_set)

        # write the data to the csv file
        self.write_csv(output_filepath, data=output_data)

        return



