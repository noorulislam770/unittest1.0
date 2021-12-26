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
        self.go_on = True        
          
    def get_user_input(self) :
        number = random.randint(1,100)
        return number

    def validate_input(self,input):
        return isinstance(input,int)

    def is_full(self,arr):
        if(len(arr) >= self.half):
            return True 
        else:
            return False

    def add_number_to_arr(self,arr,value):
        if (not self.is_full(arr)):
            arr.append(value)
            print(arr)
            return True
        else:
            return False
    def decide(self,input):
        if (len(self.arr1) == self.half and len(self.arr2) == self.half):
            self.go_on = False
            self.devide_arrays();
            
        else:
            if (self.validate_input(input)):
                if(input % 10 == 0) :
                    return "multiple_of_10"
                else:
                    if(input > 30):
                        result = self.add_number_to_arr(self.arr1,input)
                        if(not result):
                            print("Array 1 full.\nselect a number lesser than 30.")
                    elif input < 30:
                        result1 = self.add_number_to_arr(self.arr2,input)
                        if (not result1):
                            print("Array 2 full.\nselect a number greater than 30.")

    def devide_arrays(self):
        if(len(self.arr1) < self.half or len(self.arr2) < self.half):
            print("please Complete the arrays First ")
        else:
            for i in range(self.half):
                self.arr3.append(math.floor(self.arr1[i]/self.arr2[i]))

    def print_arrays(self):
        print("Array 1 :--> " )
        print ( self.arr1)
        print("Array 2 :--> " )
        print ( self.arr2)
        print("Array 3 :--> " )
        print ( self.arr3)
        # print(self.arr1)


    def start(self):
        while self.go_on:
            user_input = self.get_user_input();
            self.decide(user_input)
        self.print_arrays();

app = App()
app.start()
