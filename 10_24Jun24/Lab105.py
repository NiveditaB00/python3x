letters=['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
#letters_tuple=('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
#letters_set={'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}
#FIlter the vowels
#a,e,i,o,u

def filter_vowels(letter):
    vowels=['a', 'e', 'i', 'o', 'u']
    return letter in vowels

#result= filter_vowels('p')
#print(result)

filter_words = filter(filter_vowels, letters)
print(list(filter_words))