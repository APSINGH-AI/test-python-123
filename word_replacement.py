sentence = input('Enter the sentence :')
print('The sentence is ', sentence, 'and it \'s length is ', len(sentence) )
word1 = input('Enter the word to replace')
word2 = input('Enter the word to replace with ')

dkia =sentence.replace(word1, word2)
print(dkia)

for ch in dkia:
    print(ord(ch))


for ch in  dkia:
    print(chr(ord(ch)))
    




