class Person():

    def __init__(self, name, age):
        '''
        (Person, string, int) -> None

        Initialize a Person
        '''
        self._name = name
        self._age = age

    def __str__(self):
        '''
        (Person) -> string

        Returns a greeting from the Person
        '''
        return "Hi my name is " + self._name

    def get_age(self):
        '''
        (Person) -> int

        Returns the age of a person
        '''
        return self._age

class Professor(Person):

    def __init__(self, name, age, salary):
        '''
        (Professor, string, int, int) -> None

        Initialize a Professor
        '''
        # Use person's init method
        Person.__init__(self, name, age)  # use person init method (alt example)
        self.salary = salary

    # Method overriding
    def __str__(self):
        '''
        (Professor) -> string

        Returns a greeting
        '''
        return Person.__str__(self) + " I make " + str(self.salary)

class Student(Person):

    def __init__(self, name, age, s_id):
        '''
        (Person, string, int, int) -> None

        Initialize a Student
        '''
        Person.__init__(self, name, age)
        self._student_id = s_id


    def get_age(self):
        '''
        (Person) -> int

        Get the age of a student
        '''
        # use a returning variable
        ret = Person.get_age(self)
        if ret <= 17:
            # return 18 because they don't like being called 17 for some
            # reason
            ret = 18
        # if the above if condition fails, do the below
        return ret

class Rectangle():

    def __init__(self, length, width):
        '''
        (Rectangle, int, int) -> None

        Initialize a rectangle
        '''
        self._length = length
        self._width = width

    def get_area(self):
        '''
        (Rectangle) -> int

        Return the area of a rectangle
        '''
        return self._length * self._width

    def set_length(self, new_length):
        '''
        (Rectangle, int) -> int

        Set the length of a rectangle
        '''
        self._length = new_length

    def set_width(self, new_width):
        '''
        (Rectangle, int) -> int

        Set the width of a rectangle
        '''
        self._width = new_width

class BadSquare(Rectangle):

    def __init__(self, side):
        '''
        (BadSquare, int) -> None

        Initialize a bad square
        '''
        Rectangle.__init__(self, side, side)

    def set_side(self, new_side):
        '''
        (BadSquare, int) -> None

        Set the side of a Bad Square
        '''
        Rectangle.set_width(self, new_side)
        Rectangle.set_length(self, new_side)

class Square():

    def __init__(self, side):
        '''
        (Square, int) -> None

        Initialize a square
        '''
        self._my_rectangle = Rectangle(side, side)


    def get_area(self):
        '''
        (Square) -> int

        Returns the area of a square
        '''
        return self._my_rectangle.get_area()


    def set_side(self, new_side):
        '''
        (BadSquare, int) -> None

        Set the side of a Bad Square
        '''
        self._my_rectangle.set_width(new_side)
        self._my_rectangle.set_length(new_side)


if __name__ == '__main__':
    # Basic Example from last week
    dann = Person("Dann Justin", 10)
    print(dann)
    print(dann.get_age())

    # Inheritance Example
    tanchez = Professor("james", 27, 1000000000)
    print(tanchez)
    print(tanchez.get_age())

    some_kid = Student("Jefferson", 16, 13213)
    print(some_kid)
    print(some_kid.get_age())
    print("------")
    # -----------------------------------------------------------------
    # Basic Example: Rectangle
    my_rectangle = Rectangle(10, 15)
    print(my_rectangle.get_area())
    my_rectangle.set_width(20)
    print(my_rectangle.get_area())
    # Why is this design bad?
    some_bad_sq = BadSquare(5)
    print(some_bad_sq.get_area())
    some_bad_sq.set_side(6)
    print(some_bad_sq.get_area())
    # Why is this design good?
    my_sq = Square(5)
    print(my_sq.get_area())
    my_sq.set_side(6)
    print(my_sq.get_area())
    my_sq.set_width(20)
