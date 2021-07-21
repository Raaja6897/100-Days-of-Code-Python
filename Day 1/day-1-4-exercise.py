# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# Method 1

temp_a=a
temp_b=b
a=temp_b
b=temp_a

# Method 2
'''
c=a # c variable will have a
a=b # a variable now contains b value
b=c # b variable will have the value of a which c had
'''


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)