# week_4

class Person():

    def __init__(self, eyes, sin):
        '''
        (Person, string, int) -> None

        Initializes a person
        '''
        # print(self)
        self.these_eyes = eyes
        self._sin = sin
        #print(self.sin)

    def __str__(self):
        '''
        (Person) -> string

        Returns the string representation of a person
        '''
        return "This person has "  + self.these_eyes + " eyes"

    def get_weird_sin(self):
        '''
        (Person) -> string

        Gets this person's sin, but in a weird way
        '''
        return "this weird sin is " + str(self._sin / 2)

dann = Person("brown", 100113)
#print(dann.these_eyes)
print(dann)  # uses the __str__ method
brandon = Person("blue", 21309)
print(brandon)
print(dann.get_weird_sin())
