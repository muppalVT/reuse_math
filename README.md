# reuse_math 
## A reusable math library that performs basic calculations from various types of inputs and can supply the output in various formats. Meets SENG 560 Assignment #1 specifications.
### API Reference:
- class Operation
  - The main class that is to be used to initiate a math operation
  - Input:
    - list: Define a list of int, hex, oct, bin, or a combination of the above
  - Output:
    - Operation object. If you print it, it will give you the rult of the last operation performed
  - Attributes:
    - result: contains the result of the last operation if any. Or will be None.
    - input: stores the input to the Operation class in a list of ints form
  - Methods:
    - add: Will add what is contained in the Operation.input attribute left to right 
      - Input: Operation object
      - Output: Operation object
    - subtract: Will subtract what is contained in the Operation.input attribute left to right 
      - Input: Operation object
      - Output: Operation object
    - multiply: Will multiply what is contained in the Operation.input attribute left to right 
      - Input: Operation object
      - Output: Operation object
    - divide: Will divide what is contained in the Operation.input attribute left to right 
      - Input: Operation object
      - Output: Operation object
    - as_int: Will return result of last operation performed as int
      - Input: Operation object
      - Output: int
    - as_hex: Will return result of last operation performed as hex
      - Input: Operation object
      - Output: hex str
    - as_bin: Will return result of last operation performed as binary
      - Input: Operation object
      - Output: binary str
    - as_oct: Will return result of last operation performed as octal 
      - Input: Operation object
      - Output: octal str
### Usage:
Demos of how to use the library
'''
op = Operation([1,2,3])
op.add()
op.as_int()
'''
Output: 6
'''
op = Operation([1,'0x0',3])
op.add()
op.as_int()
'''
Output: 4


