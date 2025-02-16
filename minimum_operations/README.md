# minimum_operations
There is a text file with a single character.  The text editor can only execute two operations: Copy All and Paste.

[0. Minimum Operations](/minimum_operations/0-minoperations.py)
* Given a number `n`, write a method that calculates the fewest number of operation needed to result in exactly `n` characters in the file.
  * Example: `n` = 9
    * C => Copy All => Paste => CC => Paste => CCC => Copy All => Paste => CCCCCC => Paste => CCCCCCCCC
    * Number of operations = 6
  * `n` is the number of times the character should be repeated.
  * returns the fewest number of operations needed or 0 if n is impossible
