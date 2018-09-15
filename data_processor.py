import sys
from datetime import datetime
sys.path.append('..')

from settings import DEFAULT_DATA_FILE_CSV, ALL_PROCESSED_DATA_FILE_CSV
from classes.data import DataProcessor

if __name__ == '__main__':
    data_processor = DataProcessor()
    argv = sys.argv

    start_time = datetime.now()

    try:
        arg = argv[1]
    except Exception:
        arg = 'default'

    if arg == 'all':
        data_processor.modify_the_data(DEFAULT_DATA_FILE_CSV, ALL_PROCESSED_DATA_FILE_CSV)

    if arg == 'default':
        data_processor.modify_the_data()

    print(datetime.now() - start_time)
