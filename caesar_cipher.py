# def caesar(word, cipher_shift_value):
#     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     list_word = list(word.upper())
    
#     cipher = list_word.copy()
#     for i in range(len(list_word)):
#         for j in range(len(alphabet)):
#             counter = 0
#             if list_word[i] == alphabet[j]:
#                 counter += 1
#                 new_index = j + cipher_shift_value 
#             if new_index > (len(alphabet) - 1):
#                 new_index =  new_index - (len(alphabet) - 1)
#                 cipher[i] = alphabet[new_index]
#             else:
#                 cipher[i] = alphabet[new_index]                


#     return cipher

def caesar(word, cipher_shift_value):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    list_word = list(word.upper())

    caeser = list_word.copy()
    for i in range(len(list_word)):
        index = alphabet.index(list_word[i])

        index = index + cipher_shift_value
        if index > (len(alphabet) - 1):
            index = index - (len(alphabet))
            caeser[i] = alphabet[index]
        else:
            caeser[i] = alphabet[index]
    return caeser
print(caesar("leonard", 2))