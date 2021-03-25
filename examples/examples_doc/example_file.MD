# example_file.py

## Example file on how to document a file

## Variable assignment

+ `CONST_VAL` = 'first_test_const_value': str

+ `CONST_VAL_SECOND` = {'value': 1}: dict

## Function `decorator_factory`

### **Arguments**:

+ `arg1`: unknown

+ `arg2`: unknown

+ `arg3`: unknown

#### Declared returns: `List[Dict]`

### Function `decorator`

#### **Arguments**:

+ `function`: unknown

#### Function `wrapper`

## Function `test_func`

 ``` 
 Test function with decorator with parameters 
 ```

### **Arguments**:

 + `arg`: `unknown` - empty description

### **Examples**:

 ```python
 >>> test_func(123)
None 
```

#### Decorators

+ @decorator_factory (True, 2, arg3=3)

#### Declared returns: `List[Dict]`

## Class  `ExampleClass(ABC)`

#### Class variables

+ `_value` = 'example': str

### Function `ExampleClass.value`

 ``` 
 property value 
 ```

##### Decorators

+ @property

### Function `ExampleClass.value`

 ``` 
 setter 
 ```

#### **Arguments**:

 + `value`: `unknown` - empty description

##### Decorators

+ @value.setter

### Function `ExampleClass.test_func`

 ``` 
 class test function 
 ```

##### Decorators

+ @abstractmethod

### Function `ExampleClass.test_static`

 ``` 
 test staticmethod 
 ```

#### **Arguments**:

 + `value`: `int` - empty description

 + `arg_1`: `Dict` - empty description

 + `arg_2`: `List[Dict]` - empty description

##### Decorators

+ @staticmethod

##### Declared returns: `Dict[str,str]`

### Function `async` `ExampleClass.run`

 ``` 
 async function 
 ```

#### **Arguments**:

 + `arg`: `unknown` - empty description

##### Declared returns: `int`