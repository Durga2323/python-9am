# loops : Executing certain set of statements for n no of times.....

# While loop (infinite loop) -- it will work based on condition, untill it get false...

# for loop   --- it works based on the values. no of iterations values.

## while loop :- A loop which will execute the statements based on the condition till it becomes false.

"""
while condition:
    statements
"""
# a = eval(input("enter a value:-"))

# while a > 50:
#     print(a,"is greater than 50")
#     a= a-1

## for loop :- A loop which will be performed in certains length of values...

"""
for element in sequence:
    statements
"""

# name = "rameshkumar"

# for ele in name:
#     print(ele)

# names = ["rameshkumar",'suresh','ramesh','rajesh']

# for ele in names:
#     print(ele)

# for ele in range(1,100):
#     print(ele)

# for ele in range(100):
#     print(ele)

# # Range:-
# range (1,100) -- 1 - 99
# range (100) -- 0 - 99
# range (1,101) -- 1 - 100

# for ele in range(1,100,2): #-- jumps or offsets
#     print(ele)

# for the decending order:-
# for ele in range(100,1,-1):k #for the reverse order printing  (100,1,-1) it will print untill the befre number of 2nd one. 
#     print(ele)

# range (100,1,-1) -- 100 - 2
# range (100,0,-1) -- 100 - 1
# range (100,-1,-1) -- 100 - 0

# for ele in range(1,100):
#     print(ele,end = " ")  ----> if you give space it print space between them.

### applying conditions in the loopings

# for ele in range(1,100):
#     if ele %3 == 0 and ele %5 == 0:
#         print(ele, "is devisible by both 3 & 5")
#     elif ele % 9 ==0:
#         print(ele,"is devisible by 9")

## control flow statements :- the statements which will control the flow of iterations. 
# we can use them only under loopings exept pass
# -> break
# -> continue
# -> pass

# ---> break :- break will stop all the iterations and will go back outside of the loop.

# marks = [54,87,42,95,43,76,93,42,93,91]

# for ele in marks:
#     if ele >= 95:
#         break
#     print(ele, end=" ")


# marks = [54,87,42,95,43,76,93,42,93,91]

# for ele in marks:
#     print(ele,end = " ")
#     if ele >= 95:
#         break

# ---> continue :- will skip the current iteration happening and will go to the next iteration directly.

# marks = [54,87,42,95,43,76,93,42,93,91]

# for ele in marks:
#     if ele >= 95:
#         continue
#     print(ele,end = " ")


# marks = [54,87,42,95,43,76,93,42,93,91]

# for ele in marks:
#     if ele >= 95:
#         print(ele,end=" ")
#         continue
#     print(ele+5,end = " ")

# <<<< Basics of all programing languages, some may vary >>>>


