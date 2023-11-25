# №1

# class AirCastle:
#
#     def __init__(self, height, cloud_count, color):
#         self.height = height
#         self.cloud_count = cloud_count
#         self.color = color
#
#     def change_height(self, value):
#         if value < 0 or value > self.height:
#             raise ValueError("Height must be within range [0, initial height]")
#         else:
#             self.height += value
#
#     def add_clouds(self, n):
#         new_height = self.height + n // 5
#         if new_height < self.height or new_height > 20:
#             print(f"Invalid number of clouds: {n}. Must be between 1 and 100.")
#         else:
#             self.cloud_count += n
#             self.height = new_height
#
#     def get_visibility(self, opacity):
#         return self.height // opacity * self.cloud_count
#
#     def __str__(self):
#         return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.cloud_count} clouds"
#
#     def __gt__(self, other):
#         count_comp = cmp(self.cloud_count, other.cloud_count)
#         if count_comp == 0:
#             height_comp = cmp(self.height, other.height)
#             if height_comp == 0:
#                 color_comp = cmp(self.color, other.color)
#                 if color_comp == 0:
#                     return False
#                 else:
#                     return self.color > other.color
#             else:
#                 return self.height > other.height
#         else:
#             return self.cloud_count > other.cloud_count

# №2

# class GoodIfrit:
#
#     def __init__(self, height, name, goodness):
#         self.height = height
#         self.name = name
#         self.goodness = goodness
#
#     def change_goodness(self, amount):
#         if amount < 0:
#             amount = 0
#         self.goodness += amount
#
#     def __add__(self, number):
#         new_ifrit = GoodIfrit(self.height + number, self.name, self.goodness)
#         return new_ifrit
#
#     def __call__(self, argument):
#         return argument * self.goodness // self.height
#
#     def __str__(self):
#         return "Good Ifrit " + self.name + ", height " + str(self.height) + ", goodness " + str(self.goodness)
#
#     def __lt__(self, other):
#         goodness_comp = cmp(self.goodness, other.goodness)
#         height_comp = cmp(self.height, other.height)
#         name_comp = cmp(self.name, other.name)
#         if goodness_comp == 0 and height_comp == 0:
#             return self.name < other.name
#         elif goodness_comp == 0:
#             return height_comp > 0
#         else:
#             return goodness_comp < 0

# №3

class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, change):
        max_rating = 100
        min_rating = 1
        if self.rating + change > max_rating:
            self.rating = max_rating
        elif self.rating + change < min_rating:
            self.rating = min_rating
        else:
            self.rating += change
        age_change = abs(change) // 10
        if age_change > 8:
            age_change = 8
        if self.age - age_change < 18:
            self.age -= age_change
        elif self.age + age_change > 120:
            self.age = 120
        else:
            self.age += age_change
    def __iadd__(self, string):
        length = len(string)
    rating_change = length
    age_change = length // 10
        if rating_change > self.rating:
            rating_change = self.rating
        if age_change > (120 - self.age) // 10:
            age_change = (120 - self.age) // 10
        self.change_rating(rating_change)
        self.age -= age_change
    def __call__(self, arg):
        return (arg - self.age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks