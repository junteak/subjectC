'''
C-4
'''

# C-1. フルネームを取得できる
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(self.family_name + ' ' + self.first_name)

    def entry_fee(self):
        if self.age <= 15:
            return 1000

        if self.age <= 57:
            return 1500

        if self.age >= 73:
            return 1200

    def info_csv(self):
        # list = [self.family_name, self.first_name, self.age, self.entry_fee()]
        # print(list)
        return f'{self.family_name} {self.first_name}, {self.age},{self.entry_fee()}'


print()


#c-4
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す


print(ken.info_csv())
print(ken.info_csv())
print(ieyasu.info_csv())

