

arr1 = []
arr2 = []
arr3 = []
reps = 10
i = 0
while(True):
    number = int(input("Enter a number : "))
    if (number % 10 == 0):
        print("Enter a number not multiple of 10")
    else :
        if (number > 30 ):
            if (len(arr1) < reps/2):    
                arr1.append(number)
            else:
                print("Enter a number less than 30 array 1 is full.")
        else:
            if (len(arr2) < reps/2):
                arr2.append(number)
            else:
                print("Enter a number greater than 30 array 2 is full.")

    if (len(arr1) == reps/2 and len(arr2) == reps/2):
        break
 
for i in range(len(arr1)):
    arr3.append(arr1[i] / arr2[i])

print("Program Part ---")
print("Array 1")
print(arr1)
print("Array 2")
print(arr2)
print("Array 3")
print(arr3)

    
