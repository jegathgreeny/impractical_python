"""Load a text file as a list.

Arguments:
- text file name (and directory path, if needed)

Exceptions:
- IOError if filename not found.

Returns:
- A list of all words in a text file in lower case.

Requires-import sys

"""

import sys


def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split("\n")
            # This is a list comprehension including if else statements.
            # The statement is for the if case and the else case is next to the else statement.
            # This is to remove the '%' sign that is present in the end of some strings.
            loaded_text = [
                x[:-1].lower() if x.endswith("%")
                else x.lower()
                for x in loaded_text
            ]
            return loaded_text
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.")
        sys.exit(1)


# The relative path to the 'dictionary.txt' file.
load(r"dictionary\dictionary.txt")
