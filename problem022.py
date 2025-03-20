"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=22

[Names scores]

Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from pathlib import Path

CURRENT_DIR = Path.cwd()
DATA_DIR = CURRENT_DIR / "data"
filename = "names.txt"

def get_name_score(name: str, position: int) -> int:
    """Calculate the name score, given the name and its position in the list."""
    name_value = sum(ord(char) - ord('A') + 1 for char in name)  # A=1, B=2, ..., Z=26
    return name_value * position

def main():
    # Step 1: Load the names from the file
    with open(str(DATA_DIR / filename), 'r') as f:
        names = f.read().strip().split(',')

    # Step 2: Clean up the names and sort them
    names = [name.strip('"') for name in names]
    names.sort()

    # Step 3: Calculate the total name score
    total_score = 0
    for index, name in enumerate(names, start=1):
        total_score += get_name_score(name, index)

    # Step 4: Output the total score
    print(f"Total name score: {total_score}")

if __name__ == '__main__':
    main()

