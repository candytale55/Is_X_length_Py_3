# Python 3 (Coded in 2020)

# Function x_length_words takes a string named _sentence_ and an integer named _x_ as parameters. 
# First it splits the sentence to get each word as a separate entity, in a list named splited_sentence, 
# and then compares each word's length with x. If it is less than x it will return False.
# It returns _True_ if every word in sentence has a length greater than or equal to _x_.

def x_length_words(sentence, x):
  splited_sentence = sentence.split(" ")
  for word in splited_sentence:
    if (len(word) < x):
      return False
  return True


# TESTS:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
