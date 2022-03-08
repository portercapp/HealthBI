#!/usr/bin/python
import json
from pandas import *

class Temporal:
    """
    Temporal Object
    """
    def __init__(self, temp_value):
        self.temporal_uid = temp_value
        self.temp_value = temp_value
        self.year = None
    def __eq__(self, other):
        return self.temp_value == other.temp_value

class DimTemporal():
    """
    Shapes csv dim_temporal columns.
    """
    def __init__(self, json_file):
        self.json_file = json_file
        self.json_temporal_cols = []
        self.temporal_val = []
        self.temporals = []
        self.num_of_temporals = 0

    def get_json_cols(self):
        """
        Get all json cols for temporal. Based off known required data model fields.
        Temporal columns: "Temporal_UID": {"column_name": "Year", "value": ""},
        returns if temporal is a column or value
        """
        with open(self.json_file) as json_file:
            dictData = json.load(json_file)
            for x in dictData['Temporal_UID']:
                if x == "value" and dictData['Temporal_UID'][x] != "":
                    value = dictData['Temporal_UID'][x]
                    return value, True
                else:
                    tmp_val = dictData['Temporal_UID'][x]
                    if tmp_val != '':
                        self.json_temporal_cols.append(tmp_val)
        return False

    def get_csv_val(self, row, json_col):
        """
        This is only called if column_name was given in json.
        Gets the year value in row.
        """
        for key in row:
            if key in json_col:
                return row[key]
        return

    def create_new_temporal_object(self, value):
        """
        Create a new temporal object if unique value. Not given a temporal_uid.
        """
        found = False
        temp = Temporal(value)
        if self.num_of_temporals == 0:
            self.temporal_objs.append(temp)
            self.num_of_temporals += 1
            print("A new temp has been created: %s" % value)
            return self.temporal_objs[-1]
        else:
            for i in range(self.num_of_temporals):
                if self.temporal_objs[i] == temp:
                    found = True
                    print("This temp %s was already read in this csv." % value)
                    return self.temporal_objs[i]
            if not found:
                self.temporal_objs.append(temp)
                self.num_of_temporals += 1
                print("A new temp has been created: %s" % value)
                return self.temporal_objs[-1]
                