print('Make A Multipilication Table with Any Number')
print('Help Yur Kid Learn Math in Interesting Manner')
number = int(input("Enter The Number: "))

for mul in range(1,21):
    print("{0}*{1} = {2}".format(number,mul,(number*mul)))
print('This is the Multipilication Table of '+str(number))    