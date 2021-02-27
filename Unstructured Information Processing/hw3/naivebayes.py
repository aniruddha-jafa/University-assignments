import os
import numpy as np
import itertools
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix

directory_in_str_neg = "/Users/Mana/Desktop/UIP_HW_3/aclImdb/train/neg/"   #"C:\\Users\\DELL\\Desktop\\UIP\\HW3\\train\\neg"
directory_neg = os.fsencode(directory_in_str_neg)

directory_in_str_pos =   "/Users/Mana/Desktop/UIP_HW_3/aclImdb/train/pos/" #  "C:\\Users\\DELL\\Desktop\\UIP\\HW3\\train\\pos"
directory_pos = os.fsencode(directory_in_str_pos)

list_neg = []
list_pos = []

for file in os.listdir(directory_neg):
    filename = os.fsdecode(file)
    #print(filename, type(filename))
    if filename.endswith(".txt"):
        rating = int(filename.split("_")[1].split(".")[0])
        repeat = 0
        if rating< 5:
            repeat = 4-rating
        elif rating> 6:
            repeat = rating - 7

        filename_str = str(os.path.join(directory_in_str_neg, filename))

        filecontents = open(filename_str, "r", encoding="utf8").read().strip().replace("<br /><br />", "")

        for i in range(0, repeat+1):
            list_neg += [filecontents]
        #print(os.path.join(directory_in_str_neg, filename))
    else:
        continue


for file in os.listdir(directory_pos):
    filename = os.fsdecode(file)
    #print(filename, type(filename))
    if filename.endswith(".txt"):
        rating = int(filename.split("_")[1].split(".")[0])
        repeat = 0
        if rating< 5:
            repeat = 4-rating
        elif rating> 6:
            repeat = rating - 7

        filename_str = str(os.path.join(directory_in_str_pos, filename))
        filecontents = open(filename_str, "r", encoding="utf8").read().strip().replace("<br /><br />", "")
        #print(filecontents)
        for i in range(0, repeat+1):
            list_pos += [filecontents]
        #print(os.path.join(directory_in_str_neg, filename))
    else:
        continue

print(len(list_neg))
print(len(list_pos))

completeList = []

for data in list_neg:
    completeList += [[data,0]]

for data in list_pos:
    completeList += [[data,1]]





def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]

    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)

training_data = completeList
vectorizer = CountVectorizer(binary = 'true')
classifier = training_step(training_data, vectorizer)
result = classifier.predict(vectorizer.transform(["I love this movie!"]))

print(result[0])

'''
inpt = input("type input")

while inpt != "bye" :
     result = classifier.predict(vectorizer.transform([inpt]))
     print(result[0])
     inpt = input("type input")

# print(list_neg[0:100])
# print(list_pos[0:100])
'''

print("finished training")

'''

directory_in_str_neg_test =  "/Users/Mana/Desktop/UIP_HW_3/aclImdb/test/neg/"  #"C:\\Users\\DELL\\Desktop\\UIP\\HW3\\test\\neg"
directory_neg_test = os.fsencode(directory_in_str_neg_test)

directory_in_str_pos_test = "/Users/Mana/Desktop/UIP_HW_3/aclImdb/test/pos/"  # "C:\\Users\\DELL\\Desktop\\UIP\\HW3\\test\\pos"
directory_pos_test = os.fsencode(directory_in_str_pos_test)

list_neg_test = []
list_pos_test = []

for file in os.listdir(directory_neg_test):
    filename = os.fsdecode(file)
    #print(filename, type(filename))
    if filename.endswith(".txt"):

        filename_str = str(os.path.join(directory_in_str_neg_test, filename))
        filecontents = open(filename_str, "r", encoding="utf8").read().strip().replace("<br /><br />", "")

        list_neg_test += [filecontents]
        #print(os.path.join(directory_in_str_neg, filename))
    else:
        continue

for file in os.listdir(directory_pos_test):
    filename = os.fsdecode(file)
    #print(filename, type(filename))
    if filename.endswith(".txt"):

        filename_str = str(os.path.join(directory_in_str_pos_test, filename))
        filecontents = open(filename_str, "r", encoding="utf8").read().strip().replace("<br /><br />", "")

        list_pos_test += [filecontents]
        #print(os.path.join(directory_in_str_neg, filename))
    else:
        continue

totalEval = []

for data in list_pos_test:
    totalEval += [[data, 1]]


for data in list_neg_test:
    totalEval += [[data, 0]]

print("finished creating testing data")

pos_pos = 0
pos_neg = 0
neg_neg = 0
neg_pos = 0

for element in list_pos_test:
    result = classifier.predict(vectorizer.transform([element]))
    if (result[0]) == 1:
        pos_pos += 1
    else:
        pos_neg +=1

print("finished testing positive test data")


for element in list_neg_test:
    result = classifier.predict(vectorizer.transform([element]))
    if (result[0]) == 0:
        neg_neg += 1
    else:
        neg_pos +=1

print(pos_pos, neg_neg, pos_neg, neg_pos)
'''
