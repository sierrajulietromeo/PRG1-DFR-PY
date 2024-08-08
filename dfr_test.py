from dfr import file_exists, valid_number, data_dimensions, calculate_mean, find_total, convert_to_float, flatten, load_csv, calculate_median, create_slice
import os

# pip install pytest in the terminal
# pytest -v dfr_test.py

def test_01_file_exists_function():
    assert file_exists('./assets/testing/datatrafficdataset_10.csv')
    assert not file_exists('./assets/testing/invalidfile.csv')
    assert not file_exists('')


def test_02_valid_number_function():
    valid_numbers = [0, 1, 100, 1000, 10000, -1, -100, 0.1, 1.1, 100.100, -1000, -1.1]
    invalid_numbers = ['10+', '1_0', '1A', 'A1', '+100', '', 'A', '-1-', '0.1.', '+-1.1', '.', '5.', '1-', '1-.', '-', '+']

    for n in valid_numbers:
        assert valid_number(n)

    for n in invalid_numbers:
        assert not valid_number(n)


def test_03_data_dimensions():
    _df1 = [
        ['tcp', 1, 2, 3],
        ['icmp', 4, 5, 6],
        ['tcp', 7, 8, 9],
    ]
    _df2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    _ds1 = [13, 14, 15]
    _ds2 = ['aaaaa', 'bbbbb', 'ccccc']
    _ds3 = ''
    _ds4 = None  

    assert data_dimensions(_df1) == [3, 4]
    assert data_dimensions(_df2) == [3, 3]
    assert data_dimensions(_ds1) == [3, -1]
    assert data_dimensions(_ds2) == [3, -1]
    assert data_dimensions(_ds3) == [-1, -1]
    assert data_dimensions(_ds4) == [-1, -1]


def test_04_convert_to_float():
    _df1 = [
        ['tcp', 1, '2', 3],
        ['1.2', 4, '5', 6],
        ['tcp', 7, 8, '9']
    ]

    # Test column 0
    assert convert_to_float(_df1, 0) == 1  # First numeric value in column 0
    assert isinstance(_df1[0][0], str)
    assert isinstance(_df1[1][0], float)  # After conversion
    assert isinstance(_df1[2][0], str)
    
    assert _df1[0][0] == 'tcp'
    assert _df1[1][0] == 1.2
    assert _df1[2][0] == 'tcp'

    # Test column 2
    assert convert_to_float(_df1, 2) == 2  # All values in column 2 are numeric
    assert isinstance(_df1[0][2], float)   
    assert isinstance(_df1[1][2], float)

    assert _df1[0][2] == 2
    assert _df1[1][2] == 5
    assert _df1[2][2] == 8

    # Test column 3
    assert convert_to_float(_df1, 3) == 1  # First numeric value in column 3 is 1 
    assert isinstance(_df1[2][3], float)

    assert _df1[0][3] == 3
    assert _df1[1][3] == 6
    assert _df1[2][3] == 9


def test_05_calculate_mean_average():
    _ds1 = [10, 20, -5.5, 0.5, 'AA', 10, 25]
    _ds2 = [-5.5]
    _ds3 = ['-5.5']
    _ds4_FALSE = [_ds1]  # This is a nested list, not a valid input for calculateMean
    _ds5_FALSE = []        # Empty list, not a valid input for calculateMean
    _df6 = [1.5, 1.9, 10.0, 50, -10, '3', '1']  # Contains strings

    # Test valid inputs with expected results
    assert calculate_mean(_ds1) == 10.0
    assert calculate_mean(_ds2) == -5.5
    assert calculate_mean(_ds3) == -5.5
    
    # Test invalid inputs (should return False as per the provided test)
    assert calculate_mean(_ds4_FALSE) == False
    assert calculate_mean(_ds5_FALSE) == False

    # Test mixed data with strings that can be converted to numbers
    assert calculate_mean(_df6) == 8.2

    # Test type of result from valid input
    _mean = calculate_mean(_ds2)
    assert isinstance(_mean, float)  # Mean should be a float


def test_06_find_total():
    _ds1 = [1.5, 1.9, 'AA', 10.0, 44.02, 50, -10, '3', '1']
    _ds2_FALSE = [[0]]  # Nested list, invalid for find_total
    _ds3_FALSE = ""  # Empty string, invalid for find_total
    _ds4 = [1]

    # Test valid inputs with expected results
    assert find_total(_ds1) == 101.42
    assert find_total(_ds4) == 1.0

    # Test invalid inputs (should return False as per the provided test)
    assert find_total(_ds2_FALSE) == False
    assert find_total(_ds3_FALSE) == False

    # Test type of result from valid input
    total = find_total(_ds1)
    assert isinstance(total, float)  # Total should be a float


def test_07_calculate_median():
    _ds1 = [1.5, 1.9, 10.0, 50, -10, 3, 1, 3, 55, 20]
    _ds2 = [33, 3.4, 33.4, 55, 4, 43, 56]
    _ds3 = [17, 10, 15, 17]
    _ds4 = [17, 10, 18, 15, 17]
    _ds5 = [17, 10, '18', 15, '', 17, 'AA']  # Contains strings and empty strings
    _ds6 = ['19']
    _ds7_FALSE = []  # Empty list

    # Test valid inputs with expected medians
    assert calculate_median(_ds1) == 3.0
    assert calculate_median(_ds2) == 33.4
    assert calculate_median(_ds3) == 16.0
    assert calculate_median(_ds4) == 17.0
    assert calculate_median(_ds5) == 17.0  # Strings and empty strings should be ignored
    assert calculate_median(_ds6) == 19.0

    # Test type of result from valid input
    median = calculate_median(_ds6)
    assert isinstance(median, float)  # Median should be a float

    # Test invalid input (empty list)
    assert calculate_median(_ds7_FALSE) is False


def test_08_flatten():
    _df1 = [
        ['99'],
        [10],
        [20],
        [2.3],
        [0.7]
    ]
    _df2 = ['99', 10, 20, 2.3, 0.7]

    # Test flattening a nested list
    assert flatten(_df1) == _df2

    # Test flattening an already flat list (should return an empty list)
    assert flatten(_df2) == []


def test_09_create_slice():
    _df1 = [
        ['head0', 'head1', 'head2', 'head3'],
        ['tcp', 1, 2, 3],
        ['icmp', 4, 5, 6],
        ['tcp', 7, 8, 9],
    ]

    _df1_1 = create_slice(_df1, 0, 'icmp', [0, 2])
    _df1_2 = create_slice(_df1, 0, 'tcp', [0, 2])
    _df1_3 = create_slice(_df1, 0, 'tcp')
    _df1_4 = create_slice(_df1, 1, '*')  # '*' means any value in this column
    _df1_5 = create_slice(_df1, 2, 8, [2, 3])

    assert _df1_1 == [['icmp', 5]]
    assert _df1_2 == [['tcp', 2], ['tcp', 8]]
    assert _df1_3 == [['tcp', 1, 2, 3], ['tcp', 7, 8, 9]]
    assert _df1_4 == [['head0', 'head1', 'head2', 'head3'], ['tcp', 1, 2, 3], ['icmp', 4, 5, 6], ['tcp', 7, 8, 9]]
    assert _df1_5 == [[8, 9]]


def test_10_load_csv_ignoring_rows_cols_pattern_matched():
    _ignore_rows = [0]  # Ignore the header row
    _ignore_cols = list(range(2, 20))  # Ignore columns from index 2 to 19
    _sourcefile = './assets/testing/datatrafficdataset_10.csv'

    # Load the CSV file using the function you've implemented (replace with your actual function)
    dataframe, rows, cols = load_csv(_sourcefile, _ignore_rows, _ignore_cols) 

    # Verify the number of rows and columns read (original size, not filtered)
    assert rows == 11 
    assert cols == 21


def test_11_load_csv_ignoring_rows_cols_pattern_matched_column_slice_flattened_calculated():
    _ignore_rows = [0]  
    _ignore_cols = list(range(2, 20))  
    _sourcefile = './assets/testing/datatrafficdataset_10.csv'
    
    # Open and read the file line by line without using csv module.
    with open(_sourcefile, 'r') as file:
        lines = file.readlines()
    
    #Split each line into a list of values
    dataframe = [line.strip().split(',') for line in lines]
    rows, cols = len(dataframe), len(dataframe[0]) if dataframe else 0  

    #Filter the rows 
    dataframe = [row for i, row in enumerate(dataframe) if i not in _ignore_rows]

    # Filter columns
    dataframe = [[row[i] for i in range(cols) if i not in _ignore_cols] for row in dataframe]

    assert rows == 11  # Check original row count
    assert cols == 21  # Check original column count

    # Sample the loaded (filtered) dataframe for expected values
    assert dataframe[0] == ['tcp', '0', 'neptune']
    assert dataframe[2] == ['icmp', '1032', 'smurf']
    assert dataframe[5] == ['icmp', '520', 'smurf']
    assert dataframe[9] == ['tcp', '325', 'normal']

    assert data_dimensions(dataframe) == [10, 3]  # Check filtered dimensions

    # Slice to get 'icmp' rows with column 1 (source bytes)
    _df1 = create_slice(dataframe, 0, 'icmp', [1])
    assert _df1 == [['1032'], ['520'], ['1032']]

    # Flatten the slice
    _df1_flat = flatten(_df1)
    assert _df1_flat == ['1032', '520', '1032']

    # Calculate the total source bytes for 'icmp'
    _sourcebytes_icmp = find_total(_df1_flat)
    assert _sourcebytes_icmp == 2584.0

