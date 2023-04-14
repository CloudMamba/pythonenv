class Person:
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def walk(self):
        print(self.name + ' is coming...')

    def speak(self):
        print('hello my name is '+ self.name + 'and my age is' + str(self.age) +'\n'+ 'My gender is' + self.sex )

jesse = Person('jesse', 19, 'male')
jesse.walk()
jesse.speak()

Naomi = Person('Naomi', 17, 'female')
Naomi.speak()
Naomi.walk()