import os
import re
import math


def file_exists(filename):
  if os.path.exists(filename):
    return True
  return False


def valid_number(value): # string or a int/float
  # returns a boolean
  pass


def data_dimensions(dataframe): 
  # returns a list [rows (int), cols (int)]
  pass


def calculate_mean(dataset):
  # returns a float or false
  pass


def find_total(dataset):
  # returns a float or false
  pass


def convert_to_float(dataframe, col): # col is an int
  # returns an integer, which is the number that were  converted to floats.
  pass


def flatten(dataframe):
  # returns a dataset (a flattened dataframe)
  pass


def load_csv(csv_file, ignorerows, ignorecols):
  #returns a list -> [dataframe, rows (int), cols (int)]
  pass


def calculate_median(dataset):
  # returns a float or false
  pass


def create_slice(dataframe, colindex, colpattern, exportcols = []): # colindex (int) # colpattern (str or num), exportcols (dataset)
  # returns a dataframe
  pass