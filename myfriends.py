"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from friends import Friends

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: TODO
Groupmate 2: TODO
"""

def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """
    list_of_pairs = []
    with open(filename, 'rt') as infile:

# ------------ BEGIN YOUR CODE ------------
      lines = infile.readlines()
    list_of_pairs = [(line.split()[0], line.split()[1]) for line in lines if line.strip()]
        
    pass    # implement your code here


# ------------ END YOUR CODE ------------

    return list_of_pairs 
def make_friends_directory(pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a person, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()

    # ------------ BEGIN YOUR CODE ------------
    for x, y in pairs:
      if x != y:
        directory.setdefault(x, set()).add(y)
        directory.setdefault(y, set()).add(x)
    
    pass    # implement your code here


    # ------------ END YOUR CODE ------------

    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the the number of friends as the second element.
    """
    friends_list = []

    # ------------ BEGIN YOUR CODE ------------
    friends_list = [(person, len(friends)) for person, friends in my_dir.items()]
    friends_list.sort(key=lambda x: (-x[1], x[0]))

    pass    # implement your code here
    

    # ------------ END YOUR CODE ------------

    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ascii order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """
    assert person in my_dir
#    label = person

    # ------------ BEGIN YOUR CODE ------------
    friends = my_dir[person]
    friends_of_friends = set()
    for friend in friends:
      friends_of_friends.update(my_dir[friend])
#    friends_of_friends.discard(person)
    friends_of_friends -= friends
    friends_of_friends.discard(person)
    team = sorted(friends.union(friends_of_friends))
    label = person + '_' + "_".join(team)
    
    pass    # implement your code here


    # ------------ END YOUR CODE ------------

    return label


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ascii order
    """
    smallest_teams = []

    # ------------ BEGIN YOUR CODE
    team_sizes = {person: len(make_team_roster(person, my_dir).split('_')) for person in my_dir}
    smallest_team_size = min(team_sizes.values())
    smallest_teams = [person for person, size in team_sizes.items() if size == smallest_team_size]
    smallest_team = min(smallest_teams)


    pass    # implement your code here

    
    # ------------ END YOUR CODE

    return make_team_roster(smallest_team, my_dir)


def generate_friends(friends_dir):
  persons = sorted(friends_dir.keys())
  returned_pairs = set()

  while persons:
    person = persons.pop(0)
    friends = sorted([s for s in friends_dir[person] if s > person])

    while friends:
      pair = (person, friends.pop())
      if pair not in returned_pairs:
        returned_pairs.add(pair)
        yield pair

if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs("C:/Users/jingy/Desktop/DSC395T Data Structure & Algorithms/WHK01/myfriends.txt")
    print(my_pairs)

    print('\n2. run make_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'DARTHVADER'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')
    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        if num == 10:
            break
    print(len(list(friends_iterator)) + num)
