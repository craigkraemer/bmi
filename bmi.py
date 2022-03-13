# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:07:34 2022

@author: craig
"""

height_feet = input("Enter your height, feet: ")
height_inches = input("Enter your height, inches: ")
weight = input("Enter your weight in pounds: ")

float_weight = float(weight)
float_height_feet = float(height_feet)
float_height_inches = float(height_inches)

float_height = (float_height_feet * 12) + float_height_inches

bmi = round((float_weight * 703) / float_height ** 2, 1)
if bmi < 18.5:
    print("\n"f"Your BMI is: {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("\n"f"Your BMI is: {bmi}, you are normal weight.")
elif bmi >= 25 and bmi <= 29.9:
    print("\n"f"Your BMI is: {bmi}, you are overweight.")
else:
    print("\n"f"Your BMI is: {bmi}, you are obese.")