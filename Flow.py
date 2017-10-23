#this is a test of using flow statements

print ('Hello, what is your name?')
name = input ()

print ('What is your age?')
age = input ()
#str(int(age))
#not totally sure above is necessary #nope definitely not necessary - I commented it out and everything worked fine.

if name == 'Matty' and age == '25':
    print ('Welcome!')
elif name == 'Matty' and age < '25':
    print ('Too young!')
elif name == 'Matty' and age > '25':
    print ('Too old!')
elif name != 'Matty':
    print ('Who the ef are you?')
