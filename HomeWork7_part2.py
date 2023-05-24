def correct_sentence(sentence):
    if sentence[-1] != ".":
        sentence = sentence + "."
    sentence = str.capitalize(sentence)
    return sentence
sentence = input("enter sentence :")
print(correct_sentence(sentence))
