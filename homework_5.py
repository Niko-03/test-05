#  Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

class Pets:
    def __init__(self, genus, age):
        self.genus = genus
        self.age = age


class Dog(Pets):
    def __init__(self, genus, age, breed, nickname):
        super().__init__(genus, age)
        self.breed = breed
        self.__nickname = nickname

    def get_nickname(self):
        return f'My dog\'s name is {self.__nickname}'

    def set_nickname(self, newname):
        self.__nickname = newname


class Cat(Pets):
    def __init__(self, genus, age, breed, nickname):
        super().__init__(genus, age)
        self.breed = breed
        self.__nickname = nickname

    def get_nickname(self):
        return f'My cat\'s name is {self.__nickname}'

    def set_nickname(self, newname):
        self.__nickname = newname


dog1 = Dog('dog', '3 years', 'German Shepherd', 'Dick')
print(dog1.breed)
print(dog1.age)
dog1.age = '2 years'
print(dog1.age)

dog2 = Dog('dog', '7 years', 'Golden Retriever', 'Leo')
print(dog2.get_nickname())
dog2.set_nickname('Nick')
print(dog2.get_nickname())

dog3 = Dog('dog', '2 years', 'Rottweiler', 'Berta')

cat1 = Cat('cat', '1 years', 'Maine Coon', 'Lisa')
print(cat1.__dict__)

cat2 = Cat('cat', '3 years', 'Russian Blue', 'Max')
cat3 = Cat('cat', '4 years', 'Siamese', 'Nika')


#  Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий

#  сделано))