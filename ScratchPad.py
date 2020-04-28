#methods available to a string

string = 'xxx  test_string  '

print('count is ',string.count('t'))

print('right justified is ', string.rjust(40))

print('left justified is ', string.ljust(40))

print('upper case is ', string.upper())

print('lower case is ', string.upper().lower())

print('center string is ', string.center(40))

#methods available to a list

lst = [1,7,6,343,23]

lst.sort()
print('the ordered list is ', lst)

lst.reverse()
print('the reverse order of the list is ', lst)

print('the popped out element from the end of the list is ', lst.pop())

print('the popped out specific element is ', lst.pop(  ))

#flow control
test_list = ['dog','cat','cow']
test_list_2 = []

for i in test_list:
    for k in i:
        test_list_2.append(k)
print(test_list_2)

#removing the repeating elements
wordlist = ['cat','dog','rabbit','cat']
letterlist = [ ]
for i in wordlist:
    for k in i:
        if letterlist.count(k) == 0:
            letterlist.append(k)
        else:
            continue
print(letterlist)

#using list comprehension to do the above task
print([letterlist.append(i) for i in wordlist if i in letterlist])