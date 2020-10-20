from random import shuffle

chained_words = input("écrire 3 mots sous ce format : mot1/mot2/mot3 ").split("/")
print(chained_words)



shuffle (chained_words)
print (chained_words)


if len(chained_words) < 10:
    print (chained_words[0:2])
else:
    print (chained_words[-3:])
