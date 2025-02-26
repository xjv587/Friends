### Friendship Network Analysis Using Python
This project involves developing a friendship network analysis tool using Python, focusing on graph-based data structures and efficient querying techniques. The dataset consists of movie character co-occurrences in Star Wars films, where characters appearing in the same scene are considered "friends."

Key Contributions:
- Data Processing & Storage Optimization: Implemented functions to load, clean, and structure friendship relations using Python’s List, Tuple, Set, and Dict types for efficient lookups.
- Graph-Based Social Network Analysis: Built degree-based popularity metrics, identifying the most connected characters and computing friends-of-friends networks.
- Algorithmic Querying & Sorting: Designed and optimized functions to:
  - Rank characters by number of friends (handling ties lexicographically).
  - Construct team rosters of connected characters.
  - Identify the smallest connected group in the dataset.
- Custom Iterators & Generators: Debugged and enhanced an iterator class to traverse friendship relationships alphabetically and implemented a Python generator function for improved efficiency.
- Testing & Validation: Used pytest and custom datasets to ensure robustness, aligning with automated grading benchmarks.

