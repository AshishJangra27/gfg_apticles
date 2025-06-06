```markdown
# Python Conditional Statements: `if`, `else`, and `elif`

## Core Concept

Conditional statements allow specific code blocks to execute based on whether a condition is true or false.

## 1. `if` Statement

*   Executes a code block only if the condition is `True`.

```python
i = 10
if (i > 15):
    print("10 is less than 15")
print("I am Not in if")
```

## 2. `if...else` Statement

*   Executes one code block if the condition is `True`, and another if it's `False`.

### Simple `if-else`

```python
i = 20
if (i > 0):
    print("i is positive")
else:
    print("i is 0 or Negative")
```

### One-Line `if-else` (Ternary Operator)

```python
a = -2
res = "Positive" if a >= 0 else "Negative"
print(res)
```

### Logical Operators

*   Combine multiple conditions using `and`, `or`, `not`.

```python
age = 25
exp = 10
if age > 23 and exp > 8:
    print("Eligible.")
else:
    print("Not eligible.")
```

## 3. Nested `if...else` Statement

*   An `if...else` statement inside another `if` or `else` block.

```python
i = 10
if (i == 10):
    if (i < 15):
        print("i is smaller than 15")
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
  print("i is not equal to 10")
```

## 4. `if...elif...else` Statement

*   Multi-way decision-making: checks multiple conditions sequentially.
*   `elif` (else if) allows checking additional conditions.
*   The `else` block executes if none of the preceding conditions are `True`.

```python
i = 25
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")
```
```