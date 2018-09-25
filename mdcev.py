#!/usr/bin/python

# system imports
from datetime import datetime
import sys
import subprocess


# local package defaults
from classes.data import DataProcessor
from settings import DEFAULT_DATA_FILE_CSV, MDCEV_PROCESSED_DATA_FILE_CSV, \
    GENDER_STR, AGEGROUP_STR, PARTYPE_STR, PURPOSE_STR, COUNTRY_STR, \
    DESTINATION_ALTERNATIVES_LIST, RESULT_PATH


class ModelRun(object):

    # R scripts
    r_estimation = 'scripts/r/mdcev/runner_mdcev_nooutside.r'
    r_gamma = 'scripts/r/mdcev/forecast/run_mdcev_gamma_forecast.r'

    # CSV data file
    ### Input data ###
    model_data_file = "resources/2012/IVS_2012_MDCEV_ALL_PROCESSED23Sep.csv"
    halton_filepath = "resources/Halton/Halton.csv"

    # Constant
    alternative_list = DESTINATION_ALTERNATIVES_LIST

    utility_parameters = ['AUSNITES', 'NUMVISIT', 'RANDOMSTOP', GENDER_STR,
                          AGEGROUP_STR, PARTYPE_STR, PURPOSE_STR, COUNTRY_STR]

    alternative_utility_variables = ['GENDER_FEMALE', 'AGEGROUP_30_39']

    case_config_list = [4]

    def __init__(self):
        self.data_processor = DataProcessor()

    def _create_estimation_output_filename(self, case_config):
        return RESULT_PATH + '/mdcev/estimation_{case_config}_TEMP.txt'.format(case_config=case_config)

    def read_the_data(self):
        self.data_processor.modify_the_data_mdcev(
            input_filepath=DEFAULT_DATA_FILE_CSV,
            output_filepath=MDCEV_PROCESSED_DATA_FILE_CSV,
            utility_parameters=self.utility_parameters
        )
        return

    def estimation(self):
        for case_config in self.case_config_list:
            estimation_output_file = self._create_estimation_output_filename(case_config)
            print('This is the estimation file', estimation_output_file)

            process = subprocess.call(
                ['Rscript --vanilla {r_script} {input_file} '
                 '{number_of_alternatives} {case_config} {utility_parameters} {state_list} {results_file} '
                 '{alternative_variables}'.format(
                    r_script=self.r_estimation,
                    input_file=self.model_data_file,
                    number_of_alternatives=self.alternative_list.__len__(),
                    case_config=case_config,
                    utility_parameters=self.data_processor.convert_list_to_str(self.alternative_utility_variables),
                    state_list=self.data_processor.convert_list_to_str(self.alternative_list),
                    results_file=estimation_output_file,
                    alternative_variables=self.data_processor.convert_list_to_str(self.alternative_utility_variables))
                ]
                , shell=True)
        return

    def forecast(self):
        return

    def plot(self):
        return

    def full(self):
        self.read_the_data()
        self.estimation()
        self.forecast()
        self.plot()
        return


if __name__ == '__main__':
    model_run = ModelRun()
    start_time = datetime.now()

    argv = sys.argv
    try:
        arg = argv[1]
    except Exception:
        arg = 'all'

    if arg == 'read':
        model_run.read_the_data()

    elif arg == 'estimation':
        model_run.estimation()

    elif arg == 'forecast':
        model_run.forecast()

    elif arg == 'plot':
        model_run.plot()

    elif arg == 'all':
        model_run.full()

    print(datetime.now() - start_time)