"""
https://www.udemy.com/course/the-python-mega-course/
Python Mega Course: Learn Python in 60 Days, Build 20 Apps
Day by day solutions
Day 2

Coding Exercise 3
Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.
In other words, the program should behave as in the screenshot below:

What is your name? ardit
Ardit

What is your name? ben
Ben

What is your name? john
John

Solution: Hüsnü BARAN   
Linkedin: https://www.linkedin.com/in/husnubaran/

"""


user_prompt = "Please enter a name"
while True:
    user_name = input(user_prompt)
    print(user_name.capitalize())



