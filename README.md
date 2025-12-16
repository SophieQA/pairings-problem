# pairings-problem
Problem to be completed during Industry Prep - Interview Prep

## Problem Statement

The input to your function will be a string containing unique positive integers separated by spaces. For example:

`"7 3 99"`

Your function should output all possible pairings of integers from the input. It must be output as a set of tuples of integers. Each tuple will have 2 elements, and the first element must be smaller than the second.

### Examples:

```
find_pairs("7 3 99") => {(7, 99), (3, 7), (3, 99)}
```

```
find_pairs("2 1") => {(1, 2)}
```

```
find_pairs("24 7 365 94") => {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}

{(24, 365), (24, 94), (7, 24), (7, 365), (7, 24), (94, 365)}
```

```
<!-- find_pairs("94") => set() # A single number cannot be paired, so an empty set should be returned -->
```