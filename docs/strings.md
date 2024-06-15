# Strings in Python

#### Introduction

Strings in Python are sequences of characters enclosed within single quotes (`'`), double quotes (`"`), triple single quotes (`'''`), or triple double quotes (`"""`). They are immutable, meaning once a string is created, it cannot be changed.

#### Creating Strings

```python
single_quoted = 'Hello'
double_quoted = "Hello"
triple_single_quoted = '''Hello'''
triple_double_quoted = """Hello"""
```

#### Accessing Characters

You can access characters in a string using indexing and slicing.

- **Indexing**: Access individual characters using their position (starting from 0).

```python
string = "Hello"
first_char = string[0]  # 'H'
last_char = string[-1]  # 'o'
```

- **Slicing**: Access a range of characters.

```python
substring = string[1:4]  # 'ell'
```

#### Common String Methods

- **`len()`**: Returns the length of the string.

```python
length = len(string)  # 5
```

- **`str.upper()`**: Converts all characters to uppercase.

```python
upper_string = string.upper()  # 'HELLO'
```

- **`str.lower()`**: Converts all characters to lowercase.

```python
lower_string = string.lower()  # 'hello'
```

- **`str.capitalize()`**: Capitalizes the first character.

```python
capitalized_string = string.capitalize()  # 'Hello'
```

- **`str.find(sub)`**: Returns the index of the first occurrence of the substring `sub`.

```python
index = string.find('e')  # 1
```

- **`str.replace(old, new)`**: Replaces all occurrences of the substring `old` with `new`.

```python
new_string = string.replace('l', 'x')  # 'Hexxo'
```

- **`str.split(separator)`**: Splits the string into a list using the specified separator.

```python
words = "Hello world".split(' ')  # ['Hello', 'world']
```

- **`str.join(iterable)`**: Joins the elements of an iterable with the string as the separator.

```python
joined_string = ' '.join(['Hello', 'world'])  # 'Hello world'
```

#### String Formatting

- **Old Style (`%`)**:

```python
name = "John"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)  # 'Name: John, Age: 30'
```

- **New Style (`str.format()`)**:

```python
formatted_string = "Name: {}, Age: {}".format(name, age)  # 'Name: John, Age: 30'
```

- **f-Strings (Python 3.6+)**:

```python
formatted_string = f"Name: {name}, Age: {age}"  # 'Name: John, Age: 30'
```

#### Multi-line Strings

Triple quotes allow the creation of multi-line strings.

```python
multi_line_string = """This is a
multi-line string."""
```

#### Escape Characters

Special characters can be escaped using the backslash (`\`).

```python
new_line = "Hello\nWorld"  # New line
tab = "Hello\tWorld"       # Tab
escaped_quote = "He said, \"Hello\""  # Double quote
```

#### String Concatenation

Strings can be concatenated using the `+` operator or by using `join`.

```python
greeting = "Hello" + " " + "World"  # 'Hello World'
words = ['Hello', 'World']
greeting = ' '.join(words)          # 'Hello World'
```

#### Immutability

Strings are immutable, meaning once created, their content cannot be changed.

```python
string = "Hello"
string[0] = 'h'  # Raises TypeError
```

To create a modified version of a string, you must create a new string.

```python
new_string = 'h' + string[1:]  # 'hello'
```

### Conclusion

Strings in Python are versatile and come with many built-in methods for manipulation and formatting. Understanding how to work with strings is fundamental to effective Python programming.
