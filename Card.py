class card:

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def get_rank(self):
        return self.__rank
    
    def set_rank(self, rank):
        self.__rank = rank 

    def get_suit(self):
        return self.__suit

    def set_suit(self, suit):
        self.__suit = suit