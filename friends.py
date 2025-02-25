"""Friends iterator class to return pairs of friends"""
#
# The code for the Friends class below contains a small number of bugs: 
# Please find and correct them so that the class meets the specifications 
# described in the handout and docstring
#

from typing import Tuple, Set, Dict, Iterator
class Friends(Iterator):
    """Make an iterator to return one unique relationship at a time from friends_dir
    
    Args:
        friends_dir: dictionary of persons and their friends that was
           constructed by make_directory()

    Returns:
        Iterator type, yielding one pair of friends (as a tuple) at a time in 
        alphabetical order

    Notes:
    - Return each tuple in alphabetical order: 
        ('a', 'b') before ('a','c') before ('b', 'c') etc
    - Return only unique pairs: i.e. if returned (x,y), then do not return (y,x)
    - Read about iterator/generator type in Python Standard Library docs
      https://docs.python.org/3/library/stdtypes.html#typeiter

    Hint: 
        You should practice using your visual debugger (PyCharm) here to
        step through the code line by line, set breakpoints, and watch
        the values of local variables and attributes change.
    """

    # ------------ DEBUG CODE BELOW ------------

    def __init__(self, friends_dir: Dict[str, Set]):

        self.dir = friends_dir
        self.returned_pairs = set()
        self.index = 0
        
        if friends_dir:
            # initially, `persons` is list of all keys; 
            # and `friends` is list of the first person's friends
            self.persons = sorted(self.dir.keys())
            self.friends = sorted(self.dir[self.persons[0]])

        else:
            # handle edge case when input is an empty directory
            self.person = []

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Tuple[str, str]:
        while self.index < len(self.persons):
            person = self.persons[self.index]
            while self.friends:
                friend = self.friends.pop(0)
                pair = (person, friend)
                if pair not in self.returned_pairs and (friend, person) not in self.returned_pairs:
                    self.returned_pairs.add(pair)
                    return pair
            self.index += 1
            if self.index < len(self.persons):
                self.friends = sorted(self.dir[self.persons[self.index]])
        raise StopIteration


    # ------------ END DEBUG ------------
