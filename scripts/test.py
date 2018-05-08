import sys
sys.path.append('..')

from classes.data import DataProcessor

if __name__ == '__main__':
    data_processor = DataProcessor()
    data_processor.modify_the_data()
