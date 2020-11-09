#!/usr/bin/env python
# coding: utf-8

# In[115]:


number=int(input("what is the number?"))
binarynumber=""
if (number!=0):
    while (number>=1):
        if (number %2==0):
            binarynumber=binarynumber+"0"
            number=number/2
        else:
            binarynumber=binarynumber+"1"
            number=(number-1)/2

else:
    binarynumber="0"

i= "".join(reversed(binarynumber))
print("There are "+str(i.count('1'))+"'1' in "+i)


# In[90]:


def most_frequent_char(str1):

            dict1 = {}
            max_repeat_count = 0
            for letter in strg:
                    if letter not in dict1:
                            dict1[letter] = 1
                    else:
                            dict1[letter] += 1
                    if dict1[letter]> max_repeat_count:
                            max_repeat_count = dict1[letter]
                            most_repeated_char = letter
            return most_repeated_char

if __name__ == '__main__':
        x = input("Enter the string : ")
        strg = x.replace(" ","")
        print("Most Frequent Character : " + most_frequent_char(strg))


# In[ ]:


x=input("what is the sentence")
count = len(x.split())
print(count, " words")


# In[102]:


def multiply_by_two(x):
    return x*2

def add_numbers(a, b):
    return a + b

def print_arguments(*args):
    print(f'Arguments are: {args}')
    
augmented_multiply_by_two = print_arguments(multiply_by_two(10))

x = augmented_multiply_by_two
# this will print: Arguments are: (10,), {} and will return 20.

augmented_add_numbers = print_arguments(add_numbers(3, 4))

x = augmented_add_numbers
 # this will print: Arguments are: (3, 4), {} and will return 7.                                           


# In[101]:


def multiply_output(*args):
    print(f'Arguments are: {args}')
    
def multiply_by_three(x):
    return x * 3

augmented_multiply_by_three = multiply_output(multiply_by_three(2*10))
x = augmented_multiply_by_three


# In[109]:


def augment_function(*args):
    print(f'Arguments are: {args}')
    
def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

decorated_function = augment_function(multiply_by_two(add_numbers(3, 4))) 

x = decorated_function
    


# In[ ]:




