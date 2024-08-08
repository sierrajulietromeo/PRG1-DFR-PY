
## Task 4 Dataframe project

### This project uses many of the same techniques you've already completed in the previous tasks. This project has been specifically designed to be a challenging task. Don't forget - you do not need to complete ALL tasks in this assignment to PASS this module overall.
![spacer](assets/spacer8x8.png)

### Important Task Information - what's a dataframe and what's a dataset?  

* A ‘dataframe’ is a 2-dimensional array (aka a 2-dimensional list or a list of lists). Essentially we can picture it as a spreadsheet (i.e. a grid of rows and columns).

Here is one representation on a dataframe named ```df1```:

```python
df1 = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] , [ 10 , 11 , 12 ] ] 
```
The same dataframe ```df1``` can also be represented like this, which can help our understanding of how it can be thought of as _rows and columns_.

```python
df1 = [  
  [ 1 , 2 , 3 ] , 
  [ 4 , 5 , 6 ] , 
  [ 7 , 8 , 9 ] , 
  [ 10 , 11 , 12 ] 
] 
```

Our dataframe ```df1``` has *4* rows and *3* columns. To 'access' the 'first' element we use an 'index' value of 0.  Changing the numbers allow us to access values stored in different rows and columns.

```python
df1 [0] [0] -> 1  // Position 0 in the first array and position 0 of the array at that position gives us 1.
df1 [ 0 ] [ 2 ] -> 3 // Position 0 in the first array and position 2 of the array at that position gives us 3.
df1 [ 3 ] [ 0 ] -> 10  // Position 3 in the first array and position 0 of the array at that position gives us 10.
df1 [ 3 ] [ 2 ] -> 12 // Position 3 in the first array and position 2 of the array at that position gives us 12.
df1 [ 4 ] [ 0 ] -> Error // There is no position 4 in the first array, so an error will occur.
```

A 'dataset' is a 1-dimensional array (aka a list). Essentially we can picture this as a single row (or, if easier as a single column).

```python
ds1 = [ 13 , 14 , 15 ]
```
```ds1``` dimensions are: 3 rows and 0 columns. However as mentioned above since we 'access' a list using a 0 as an index, for the purpose of this challenge we will use **-1** to indicate 'no columns'. Therefore, the dimensions are: 3 rows and -1 columns.

```python
ds1 [ 0 ] -> 13
ds1 [ 2 ] -> 15
ds1 [ 3 ] -> Error: index out of range. // There is no position 3 (Positions are 0, 1 & 2)
```

![spacer](assets/spacer16x16.png)
 
## Task instructions  

**file_exists:** A file exists function has already been provided for you to use. This function is designed around the work you have already completed (Data File Parser) and returns a boolean value (true/false) depending on whether the specific file exists. 

 ![spacer](assets/spacer8x8.png)
**Intermediate Level Challenges (Beginner Attemptable):**
  
**Task 1:** Create a valid number function. Your function must return a boolean value (true/false) depending on whether the argument passed is a valid number. For the purpose of this challenge a valid number can be: positive (unsigned) or negative (signed), integer or float
  
**Task 2:** Create a data dimensions function. Your function must return a set of values representing the dimensions of the dataframe or dataset passed in as an argument. Ensure you test with dataframes and datasets (numeric and string). -1 is used to represent 'no data' on that axis (rows and/or columns); e.g. a dataset or None.

**Task 3:** Create a find totals function. Your function must return the total of all valid numbers in the passed dataset). Invalid datasets (i.e., incorrect dimensions) should result in a (boolean) false value being returned.

**Task 4:** Create a calculate mean function. Your function must return the ‘mean’ average of all valid number values in the passed dataset. Invalid datasets (i.e., incorrect dimensions) result in a (boolean) false value being returned.

 ![spacer](assets/spacer8x8.png)
**Experienced Level Challenges (Intermediate Attemptable):**
  
**Task 5:** Create a convert to float function. Your function must return a number indicating only values (in the specified column) that were coerced (i.e. converted) to a 'float' data type. Values are coerced if they are a 'valid number' but not a numeric datatype (see valid number function for more details).  Complex data types are typically 'pass-by-reference' (in Python this is 'pass-by-object-reference') meaning that the _dataframe is mutable i.e., changes are 'persistent’ so no additional return values are needed.

**Task 6:** Create a flatten dataframe function. Your function must return a (new) flat dataset instance of the passed dataframe. Only dataframes with the shape ```[ n , 1 ]``` ( any number of rows but only 1 column) can be flattened by this function. Using this function creates a valid dataset from single column slices and should be compatible with functions that expect datasets rather than dataframes (e.g., findtotal, calculatemean, etc). This function should not alter any existing value's data type; invalid requests should return an empty list.

**Task 7:** Create a calculate median function. Your function must return the data value separating the upper half of the number values based on the passed dataset from the lower half; invalid datasets (i.e., incorrect dimensions) result in a (boolean) false value being returned.
 
**Task 8:** Create a load CSV file function. Your function must return an array (aka a list) containing three elements. The source CSV data and the source's original dimensions (rows and columns, not including any ignored rows and/or columns ). Specific rows and columns can be 'ignored' (not included in the returned dataframe), for example to ignore the first row in the source CSV use: ```ignorerows = [ 0 ]``` . To ignore the first and second row use: ```ignorerows = [ 0, 1 ]```, the same applies to ```ignorecols```.  If the file specified does not exist the return state should be: ```[ [ ] , -1 , -1 ]```. 

**Task 9:** Create a slicing function. Your function must return a (new) dataframe 'instance' based on sliced data from the passed dataframe. Rows are selected when the value in a specified 'column (colindex : 0) equals _colpattern (e.g. ```[ currentrow ] [ _colindex ] == colpattern``` or ```value [ 0 ] [ 0 ] == 'tpc'```). Only columns specified in the ```exportcols``` argument should be included in the slice.  Wildcard requirements: using '*' as the ```colpattern``` must match 'any' value in the specified ```colindex```. This allows 'all rows' to be selected for the slice.  ```exportcols``` is optional ( default value = ```[ ]``` ) meaning ‘not’ passing an argument or passing an empty array (aka a list) will allow all columns to be selected for the slice.
  



![spacer](assets/spacer16x16.png)
### Suggested Steps

To help you get started on this challenge consider following these initial steps:

1. Complete the foundational functions first as these will likely be easier and faster to complete and test. 
2. The original datafile (reference ‘datatrafficdataset.csv’ contained 494,000 rows and 35 columns however we have sliced that down to 2001 rows and 21 columns; including headers).  You may also find it useful to create your own (even smaller test file) to help optimise your development and testing.
3. Be sure to use your foundational-type functions during the later tasks. E.g. Use ```find_total``` when you are writing ```calculate_mean```.
   

## Some example calls to the functions and methods you will write:

**Example 1: file exists**

```python
file_exists ( './datatrafficdataset_2000.csv' ) // returns true as the file does exist. 
file_exists ( './wrongfilename.csv' ) // returns false as the file does not exist.

```
![spacer](assets/spacer16x16.png)

**Example 2: valid number**

```python
valid_number ( '0.0' ) -> true
valid_number ( '0.1' ) -> true
valid_number ( '-1.12' ) -> true
valid_number ( '-5' ) -> true
valid_number ( '5' ) -> true
valid_number ( 1.3 ) -> true
valid_number ( 1 ) -> true
valid_number ( 5. ) -> true
valid_number ( '5.' ) -> false
valid_number ( '+5' ) -> false
valid_number ( '.' ) -> false
valid_number ( '0.0.1' ) -> false
```
![spacer](assets/spacer16x16.png)

**Example 3: data_dimensions**

```python
df1 = [ [ 'tcp', 1, 2, 3 ],
        [ 'icmp', 4, 5, 6 ],
        [ 'tcp', 7, 8, 9 ] ]

ds2 = [ 1.1 , 1.2 , 0 , 0 , 1.1 ]
ds3 = [ 'AAA' , 'BBB' , 'CCC' ]
ds4 = Undefined 

data_dimensions ( df1 ) -> [ 3 , 4 ]
data_dimensions ( ds2 ) -> [ 5 , -1 ]
data_dimensions ( ds3 ) -> [ 3 , -1 ]
data_dimensions ( ds4 ) -> [ -1 , -1 ]
```
![spacer](assets/spacer16x16.png)

**Example 4: calculate_mean**
```python
ds1 = [ 1.5, 1.9, 10.0, 50, -10, '3', '1' ]
ds2 = [ 1.9 ]
calculate_mean(ds1) -> 8.2
calculate_mean(ds2) -> 1.9
```
![spacer](assets/spacer16x16.png)

**Example 5: find_total**
```python
ds1 = [ 1.5, 1.9, 10.0, 50, -10, '3', '1' ]
data_dimensions(ds1) -> [ 7, -1 ]
find_total(ds1) -> 57.4

```
![spacer](assets/spacer16x16.png)

**Example 6: convert_to_float**
```python
df1 = [ [ 'tcp', 1, '2', 3 ],
        [ '1.2', 4, '5', 6 ],
        [ 'tcp', 7,  8,  9 ] ]
        
convert_to_float ( df1 , 0 ) -> 1
convert_to_float ( df1 , 2 ) -> 2
df1 -> [ [ 'tcp', 1, 2, 3 ], [ 1.2, 4, 5, 6 ], [ 'tcp', 7, 8, 9 ] ]
```
![spacer](assets/spacer16x16.png)

**Example 7: flatten**
```python
df1 = [ [ 5 ],
        [ 7 ],
        [ 9 ] ]
data_dimensions ( df1 ) -> [ 3 , 1 ] // 3 rows, 1 column
flatten ( df1 ) -> [ 5 , 7 , 9 ]
data_dimensions ( flatten ( df1 ) ) -> [ 3 , -1 ] // 3 items in a row,, no columns


df2 = [ 5, 7, 9 ]
data_dimensions ( df2 ) -> [ 3 , -1 ] // 3 items in a row, no columns
data_dimensions ( flatten ( df2 ) ) -> [ 0, -1 ] // no items in a row, no column
flatten ( df2 ) -> [ ]
```
![spacer](assets/spacer16x16.png)

**Example 8: load_csv**
```python
ignorerows = [ 0 ];
ignorecols = [   ];

[ dataframe, rows, cols ] = load_csv ( './datatrafficdataset_2000.csv', ignorerows , ignorecols )
rows --> 2001
cols --> 21

data_dimensions (dataframe)
rows --> 2000
cols --> 21

```
![spacer](assets/spacer16x16.png)

**Example 9: calculate_median**
```python
ds1 = [ 1.5, 1.9, 10.0, 50, -10, '3', '1' ]
ds2 = [ '5' ]
calculate_median ( df1 ) -> 1.9
calculate_median ( df2 ) -> 5.0

```
![spacer](assets/spacer16x16.png)

**Example 10: create_slice**
```python
df1 = [ [ 'tcp', 1, 2, 3 ],
        [ 'icmp', 4, 5, 6 ],
        [ 'tcp', 7, 8, 9 ] ]

create_slice ( df1 , 0 , 'icmp' , [ 0 , 2 ] )  -> [ [ 'icmp', 5 ] ]
create_slice ( df1 , 0 , 'tcp' , [ 0 , 2 ] )   -> [ [ 'tcp' , 2 ] , [ 'tcp' , 8 ] ]
create_slice ( df1 , 0 , 'tcp' )               -> [ [ 'tcp' , 1 , 2 , 3 ] , [ 'tcp' , 7 , 8 , 9 ] ]
create_slice ( df1 , 1 , '*' )                 -> [ [ 'tcp' , 1, 2, 3 ] , [ 'icmp' , 4 , 5 , 6 ] , [ 'tcp' , 7 , 8 , 9 ] ]

```

## Submission Checklist


Prior to actually submitting your final attempt you should ensure you have reviewed and considered the following checklist.

1. Refactored solution.
2. Does your solution follow accepted coding conventions?
3. Your 'test' code, commented out at the bottom of ```dfr.py```