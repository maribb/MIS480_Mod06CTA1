'''
I think my biggest issue was how I attempted adding to the list initially
Math_List +=(Input_Value) would sort of work, but the
Input_Value list would interpret the numbers are individual items so "123" as input
went into the list as '1', '2', '3'. This led to further research and the use of
the .append component.
I also had some issues getting my list to work as a float; probably a better way to handle this
'''


#Declaring an empty list
Math_List = []

#Declaring float variable for user input; setting 0 simply as a base value.
Input_Value = 0

#Declaring variable to track user inputs
Loop_Value = 0

#Declaring math operations function
def Math_Operations ():
        #Total
        print("The total is: ",sum(Float_Math_List))
        #Average
        print("The average is: ", sum(Float_Math_List)/len(Float_Math_List))
        #Maxaximum
        print("The largest number is: ", max(Float_Math_List))
        #Minimum
        print("The smallest number is: ", min(Float_Math_List))
        #multiplicationmagic (looking to add 20% value of each number to itself)
        Float_Math_List_20Percent = []
        for number in Float_Math_List:
                Float_Math_List_20Percent.append(number*.2+number)
        print("At 20% interest (gain): ", Float_Math_List_20Percent)
        
#Looping for user input 5 times
while Loop_Value < 5:
        Loop_Value=Loop_Value+1
        Input_Value = input("Enter a number: ")
        Math_List.append(Input_Value)
        #Error Check step
        #print(Loop_Value)

#gerry rigging the Math_List into floats, there has to be a better way.
Float_Math_List = []
for item in Math_List:
        Float_Math_List.append(float(item))

#Printing the list and values requested.        
print("Your list is: ", Float_Math_List)
#Calling the operations defined previously
Math_Operations ()


#Disregard below this line; notes from a rough draft...
#Confirming Mathmatical operations are functional disregard these notes. 
'''
#Declaring math operations function
def Math_Operations (Float1, Float2, Float3, Float4, Float5 ):
        Math_Total = Float1 + Float2 + Float3 + Float4 + Float5
        Math_Average = Math_Total / 5
        Math_Maximum = max(Float1, Float2, Float3, Float4, Float5)
        Math_Minimum = min(Float1, Float2, Float3, Float4, Float5)
        print("The Operations have ran and determined Total: ", Math_Total)
        print("Average: ", Math_Average)
        print("Maximum: ", Math_Maximum)
        print(" Minimum: ", Math_Minimum)

#Collecting values from user
Float1 = float(input("Enter first number : "))
Float2 = float(input("Enter second number : "))
Float3 = float(input("Enter third number : "))
Float4 = float(input("Enter fourth number : "))
Float5 = float(input("Enter fifth number : "))

#Calling the Math_Operations function
Math_Operations(Float1, Float2, Float3, Float4, Float5 )
'''

