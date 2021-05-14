# basic password generator in python

# a password consists of uppercase, lowercase, digits and special characters or punctuations
# we can easily get the above mentioned characters from string module.

import string
import random
import datetime

def pass_gen(pass_len):
    lowercase_letters = string.ascii_lowercase

    uppercase_letters = string.ascii_uppercase

    numbers = string.digits

    special_char = string.punctuation

    # combining a all the uppercase, lowercase digits and special characters in one single list

    combined_list = []

    combined_list.extend(list(lowercase_letters))
    combined_list.extend(list(uppercase_letters))
    combined_list.extend(list(numbers))
    combined_list.extend(list(special_char))

    # the combined list is in certain order,
    # shuffling the list in random order.

    random.shuffle(combined_list)

    # joining the resultant password list into string.
    password = "".join(combined_list[0:pass_len])
    
    return password


if __name__ == '__main__':

    # taking length of password from user.
    pass_length = int(input('Enter the Length of the Password(maximum = 94): '))

    final_password = pass_gen(pass_length)

    print(f'Your Password of length {pass_length} is:{final_password}')


# uncomment the block below to log the passwords into a text file.

'''   
    # instead of printing the password on a terminal we can log it into a text file with timestamp.

    with open('password_log.txt', 'a') as file:
        file.write(final_password + f'  [{datetime.datetime.now()}]'+ '\n')

'''

