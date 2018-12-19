import sys
from datetime import datetime
sys.path.append('..')

from settings import DEFAULT_DATA_FILE_CSV, ALL_PROCESSED_DATA_FILE_CSV, \
    TOP_LOGIT_PROCESSED_DATA_FILE_CSV, BOT_LOGIT_PROCESSED_DATA_FILE_CSV
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
        print("processing all data")
        data_processor.modify_the_data(DEFAULT_DATA_FILE_CSV, ALL_PROCESSED_DATA_FILE_CSV)

    if arg == 'default':
        print("processing filtered data")
        data_processor.modify_the_data()

    if arg == 'top_logit':
        print("processing data for top binary logit model")
        data_processor.modify_the_data_top_binary_logit(DEFAULT_DATA_FILE_CSV, TOP_LOGIT_PROCESSED_DATA_FILE_CSV)

    if arg == 'bot_logit':
        print("processing data for bot binary logit model")
        data_processor.modify_the_data_bot_binary_logti(DEFAULT_DATA_FILE_CSV, BOT_LOGIT_PROCESSED_DATA_FILE_CSV)

    print(datetime.now() - start_time)
