```markdown
# Python Strings

A string is a sequence of characters. Single characters are strings of length 1.

## Creating Strings

*   Strings can be created using single quotes (`'`) or double quotes (`"`).
*   Multi-line strings use triple quotes (`'''` or `"""`).

## Accessing Characters

*   Strings are indexed starting from 0 (forward) and -1 (backward, from the end).
*   `string[index]` accesses the character at `index`.
*   Negative indexing: `string[-1]` is the last character.

### String Slicing

*   `string[start:end]` extracts a portion of the string.
*   `start` is the starting index (inclusive).
*   `end` is the stopping index (exclusive).
*   `string[:end]` extracts from the beginning to `end`.
*   `string[start:]` extracts from `start` to the end.
*   `string[::-1]` reverses the string.

## String Immutability

*   Strings are immutable: they cannot be changed after creation.
*   To modify a string, create a new string using concatenation, slicing, or formatting.

## Deleting Strings

*   Individual characters cannot be deleted.
*   The entire string variable can be deleted using `del string_name`.

## Updating Strings

*   Create a new string to update a part of the string: `new_string = "new_part" + old_string[index:]`.
*   Use `string.replace(old, new)` to replace substrings.

## Common String Methods

*   `len(string)`: Returns the number of characters.
*   `string.upper()`: Converts to uppercase.
*   `string.lower()`: Converts to lowercase.
*   `string.strip()`: Removes leading/trailing whitespace.
*   `string.replace(old, new)`: Replaces occurrences of `old` with `new`.

## Concatenating and Repeating Strings

*   `string1 + string2`: Concatenates strings.
*   `string * n`: Repeats the string `n` times.

## Formatting Strings

### f-strings

*   `f"text {variable} text"`: Embeds variables directly in the string.

### `format()` method

*   `"text {} text".format(variable)`:  Replaces `{}` with the variable.

## Membership Testing

*   `substring in string`: Checks if `substring` is present in `string` (returns `True` or `False`).
```