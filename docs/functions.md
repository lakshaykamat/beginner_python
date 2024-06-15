# Functions in Python

## Introduction

Functions are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable, and allowing for code reuse.

## Defining Functions

Functions are defined using the `def` keyword, followed by the function name, parameters in parentheses, and a colon. The function body is indented.

```python
def function_name(parameters):
    # Function body
    pass
```

### Example

```python
def greet(name):
    print(f"Hello, {name}!")
```

## Calling Functions

Functions are called by using their name followed by parentheses, with arguments passed inside the parentheses.

```python
greet("Alice")  # Output: Hello, Alice!
```

## Parameters and Arguments

### Positional Arguments

Arguments are passed in the same order as the parameters.

```python
def add(a, b):
    return a + b

result = add(2, 3)  # Output: 5
```

### Keyword Arguments

Arguments are passed using parameter names.

```python
result = add(a=2, b=3)  # Output: 5
```

### Default Parameters

Parameters can have default values, which are used if no argument is passed.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, World!
greet("Alice")   # Output: Hello, Alice!
```

### Arbitrary Arguments

Functions can accept an arbitrary number of arguments using `*args` and `**kwargs`.

#### `*args`

```python
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_all("Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

#### `**kwargs`

```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

## Return Statement

The `return` statement is used to exit a function and optionally return a value.

```python
def square(x):
    return x * x

result = square(4)  # Output: 16
```

## Scope and Lifetime of Variables

### Local Scope

Variables defined inside a function are local to that function.

```python
def func():
    x = 10  # Local variable
    print(x)

func()  # Output: 10
print(x)  # Raises NameError
```

### Global Scope

Variables defined outside any function are global and can be accessed from any function.

```python
x = 10  # Global variable

def func():
    print(x)

func()  # Output: 10
print(x)  # Output: 10
```

### The `global` Keyword

To modify a global variable inside a function, use the `global` keyword.

```python
x = 10

def func():
    global x
    x = 20

func()
print(x)  # Output: 20
```

## Lambda Functions

Lambda functions are anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

```python
square = lambda x: x * x
print(square(4))  # Output: 16

add = lambda a, b: a + b
print(add(2, 3))  # Output: 5
```

## Higher-Order Functions

Functions that take other functions as arguments or return them as results are called higher-order functions.

```python
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * x, 5)  # Output: 25
```

## Function Annotations

Function annotations provide a way of associating various parts of a function with arbitrary Python expressions at compile time.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'str'>}
```

## Conclusion

Functions are a fundamental aspect of Python that enable modular, reusable, and organized code. Understanding how to define, call, and manipulate functions is essential for effective programming in Python.
