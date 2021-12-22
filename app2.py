import random
import math


# USING ACTAUL PROFESSIONAL WAY OF IMPLEMENTATION


class App:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
        self.arr3 = []
        self.reps = 10
        self.half = self.reps // 2
        
    
    def get_user_input(self) :
        number = int(input("please enter a number : "))
        return number

    def validate_input(self,input):
        return isinstance(input,int)

    def is_full(self,arr):
        if(len(arr) >= self.half):
            return True 
        else:
            return False

    def add_number_to_arr(self,arr,value):
        if (not self.is_full(self.arr)):
            arr.append(value)
            return True
        else:
            return False
    def analyze_input(self,input):
        if self.validate_input(input):
            if(input % 10 == 0) :
                return "multiple_of_10"
            else:
                if(input > 30):
                    self.add_number_to_arr(self.arr1,input)
                else:
                    self.add_number_to_arr(self.arr2,input)
            


    

