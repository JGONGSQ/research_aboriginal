#!/usr/bin/python

DEFAULT_DATA_FILE_CSV = "../resources/2012/IVS_2012.csv"
FILTERED_DATA_FILE_CSV = "../resources/2012/IVS_2012_filtered.csv"
PROCESSED_DATA_FILE_CSV = "../resources/2012/IVS_2012_PROCESSED.csv"

MODIFIED_VARIABLES = ["GENDER", "AGEGROUP"]

GENDER_DICT = {
    '1': "Male",
    '2': "Female"
}

AGEGROUP_DICT = {
    '1': "15-19",
    '2': "20-24",
    '3': "25-29",
    '4': "30-34",
    '5': "35-39",
    '6': "40-44",
    '7': "45-49",
    '8': "50-54",
    '9': "55-59",
    '10': "60-64",
    '11': "65-69",
    '12': "70-74",
    '13': "75-79",
    '14': "80+"
}
