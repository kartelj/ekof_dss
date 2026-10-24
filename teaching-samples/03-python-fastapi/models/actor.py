class Actor:
    """
    A class describes what all the objects of one kind have in common.
    Every actor (an object of the class Actor) has a first name, a last name and an IMDB mark.
    """

    def __init__(self, first_name: str = "", last_name: str = "", imdb_mark: float = 0):
        # __init__ is executed when a new object is created; self is that new object
        self.first_name = first_name
        self.last_name = last_name
        self.imdb_mark = imdb_mark
