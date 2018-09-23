#!/usr/bin/python

# system imports
from datetime import datetime
import sys


# local package defaults
from classes.data import DataProcessor
from settings import DEFAULT_DATA_FILE_CSV, MDCEV_PROCESSED_DATA_FILE_CSV, \
    GENDER_STR, AGEGROUP_STR, PARTYPE_STR, PURPOSE_STR, COUNTRY_STR


class ModelRun(object):

    utility_parameters = ['AUSNITES', 'NUMVISIT', 'RANDOMSTOP', GENDER_STR,
                          AGEGROUP_STR, PARTYPE_STR, PURPOSE_STR, COUNTRY_STR]

    def __init__(self):
        self.data_processor = DataProcessor()

    def read_the_data(self):

        self.data_processor.modify_the_data_mdcev(
            input_filepath=DEFAULT_DATA_FILE_CSV,
            output_filepath=MDCEV_PROCESSED_DATA_FILE_CSV,
            utility_parameters=self.utility_parameters
        )

        return

    def estimation(self):
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