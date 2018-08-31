#!/usr/bin/python

GENDER_STR = "GENDER"
AGEGROUP_STR = "AGEGROUP"
MARITAL_STR = "MARITAL"
PURPOSE_STR = "TRIP_PURPOSE"
INT_BOOKING_STR = "INT_BOOKING"
PARENT_STR = "PARENT"
CUSTOMS_STR = "CUSTOMS"
PACKAGE_STR = "PACKAGE"
COUNTRY_STR = "COUNTRY"
AIRLINE_STR = "AIRLINE"
REGION1_STR = "REGN1"
REGION2_STR = "REGN2"
REGION3_STR = "REGN3"
REGION4_STR = "REGN4"
REGION5_STR = "REGN5"


DEFAULT_DATA_FILE_CSV = "../resources/2012/IVS_2012.csv"
FILTERED_DATA_FILE_CSV = "../resources/2012/IVS_2012_filtered.csv"
FILTERED_PROCESSED_DATA_FILE_CSV = "../resources/2012/IVS_2012_PROCESSED.csv"
ALL_PROCESSED_DATA_FILE_CSV = "../resources/2012/IVS_2012_ALL_PROCESSED.csv"


MODIFIED_VARIABLES = [
    GENDER_STR, AGEGROUP_STR, MARITAL_STR, PURPOSE_STR, INT_BOOKING_STR,
    PARENT_STR, CUSTOMS_STR, PACKAGE_STR, COUNTRY_STR, AIRLINE_STR,
    REGION1_STR, REGION2_STR, REGION3_STR, REGION4_STR, REGION5_STR
]

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

MARITAL_DICT = {
    '1': "Single",
    '2': "Couple",
    '9': "Refused"
}

PURPOSE_DICT = {
    '1': "Holiday",
    '2': "Visiting_FR",
    '3': "Business",
    '4': "Business",
    '5': "Employment",
    '6': "Education",
    '7': "Other",
    '8': "Other",
    '9': "Other",
    '11': "Other",
}

BOOLEAN_DICT = {
    '1': 'Yes',
    '2': 'No',
    '9': 'Refused'
}

CUSTOMS_DICT = {
    '1': "Sydney",
    '2': "Melbourne",
    '3': "Brisbane",
    '4': "Perth",
    '5': "Adelaide",
    '6': "Darwin",
    '7': "Townsville",
    '8': "Cairns",
    '9': "Hobart",
    '10': "Broome",
    '11': "Gold Coast"
}

COUNTRY_DICT = {
    '8104': "USA",
    '1201': "New_Zealand",
    '2102': "England",
    '6101': "China",
    '6201': "Japan",
    '2304': "Germany",
    '8102': "Canada",
    '2303': "France"
}

AIRLINE_DICT = {
    'QF': "Qantas",
    'JQ': "Jetstar",
    'EK': "Emirates",
    'SQ': "Singapore_Airlines",
    'CX': "Cathay_Pacific",
    "NZ": "Air_New_Zealand",
    "MH": "Malaysian_Airlines"
}

REGION_DICT = {
    '110': "Sydney",
    '118': "Northern Rivers Tropical NSW",
    '210': "Melbourne",
    '310': "Brisbane",
    '315': "Gold Coast",
    '320': "Tropical North Queensland",
    '410': "Adelaide",
    '510': "Perth",
    '710': "Darwin"
}
