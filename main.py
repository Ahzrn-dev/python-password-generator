from abc import abstractmethod , ABC


class PasswordGenerator :
    @abstractmethod
    def generate(self) :
        pass


import random
import string



class PinGenerator(PasswordGenerator):
    def __init__(self,length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range (self.length)])        
    
    import string
class RandomPaswordGenerator(PasswordGenerator):
    def __init__(self, length : int = 8 , include_numbers : bool = False , include_symbols : bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers :
            self.characters += string.digits
        if include_symbols :
            self.characters += string.punctuation


    def generate(self) :
            return ''.join([random.choice(self.characters) for _ in range (self.length)])   
    

    class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_words : int = 4 , 
        separator : str ='-',
        capitalize : bool = False ,
        vocabulary : list = None
    ):
        if vocabulary is None :
            self.vocabulary = ["Apple","Pen","Book","Phone","Laptop","Desk","Chair","Watch","Flower","Shoes"]

        self.num_of_words = num_of_words
        self.capitalize=capitalize
        self.separator = separator
    
    def generate(self) :
        password_words=[random.choice(self.vocabulary)for _ in range(self.num_of_words)]
        if self.capitalize :
            password_words = [word.upper() if random.choice([True,False]) else word.lower() for word in password_words]

        return self.separator.join(password_words)

