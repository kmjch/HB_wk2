"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Having classes makes possible:
subclasses that inherit attributes and methods from their parent. This allows us
to make variations of the parent rather easily.
Keeps the code from being overly long, confusing, or repetitive.
-abstraction:
 don't need to let the user know all the intricacies of how certain functions work
-encapsulation:
 data is bundled with the functions that work on that data
-polymorphism:
 functions or methods can be applied to more than one subclass — general enough


2. What is a class?
It's a "type" of object that a coder can create, and it usually has a template
of attributes and that its subclasses can take on

3. What is an instance attribute?
A piece of information that you add on to an object of a class

4. What is a method?
A function that operates on a class it is defined within, called like Class.method()

5. What is an instance in object orientation?
It's an object that you create of your type Class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
Class attribute is assigned when you first create your class, and all the instances
of that class get assigned that same attribute.  It is within your template.
Instance attribute is assigned after you create your object of your type class,
and it can overwrite class attributes.  You can also add new instance attributes
without affecting any of the other instances of the same class.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ A person who studies something. """
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """ An item that asks you for your knowledge. """
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ Asks a question and checks whether the answer given is correct. """
        print self.question,
        answer = raw_input("> ")
        return self.correct_answer == answer

class Exam(object):
    """ An assignment that asks you questions, and you must answer with no help. """
    def __init__(self, name, questions):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """ Insert a question into your exam. """
        question_content = Question(question, correct_answer)
        self.questions.append(question_content)

    def administer(self):
        """Administers a test and grades it right away. 1.0 is full score. """
        grade = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                grade += 1
        return float(grade) / len(self.questions)

class Quiz(Exam):
    def __init__(self, name, questions):
        super(Quiz, self).__init__(name)

    def administer(self):
        return super(Quiz, self).administer() > 0.5

def take_test(exam, student):
    student.score = exam.administer()
    print student.first_name + " " + student.last_name + " on the " + exam.name + \
          " " + str(student.score * 100) + "%"

def example():
    test = Exam('Final Exam', [])
    test.add_question('What is 1 + 1?', '2')
    test.add_question('What is 1 + 13?', '14')
    michelle = Student('Michelle', 'Kim', '2540 College Ave')
    take_test(test, michelle)
