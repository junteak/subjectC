'''
C-5,6,
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
        if self.age <= 3:
            return 0

        if self.age <= 15:
            return 1000

        if self.age <= 57:
            return 1500

        if self.age <= 74:
            return 1200

        if self.age >= 75:
            return 500

    def info_csv(self):
        list = [self.family_name + ' ' + self.first_name, str(self.age), str(self.entry_fee())]
        result = '| '.join(list)
        return result


print()


# #c-4
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# ken.info_csv()  # "Tom Ford,57,1500" という値を返す
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
# print(ken.info_csv())
# print(ken.info_csv())
# print(ieyasu.info_csv())


#c-6
kumi = Customer(first_name="kumi", family_name="mitsuki", age=2)
print(kumi.info_csv())  #タダ

takao = Customer(first_name="takao", family_name="tajima", age=12)
print(takao.info_csv())  #1000

jun = Customer(first_name="jun", family_name="tanaka", age=40)
print(jun.info_csv())  #1500

kazuhiko = Customer(first_name="kazuhiko", family_name="tanaka", age=74)
print(kazuhiko.info_csv())  #1200

chigiku = Customer(first_name="chigiku", family_name="yoshioka", age=89)
print(chigiku.info_csv())  #500



