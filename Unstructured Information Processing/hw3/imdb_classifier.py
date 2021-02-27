from os import listdir

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def get_contents_from_files_in_directory(directory):
    content_rating_pairs = []

    for filename in listdir(directory):

        if filename.endswith(".txt"):

            document_class = None

            file = open( directory + filename, "r", encoding="utf8")
            file_contents = file.read().lower()

            rating = int(filename[-5])
            if rating == 0: # rating canot be 0, so if 5th character from the end is 0, the rating must be 10
                rating = 10

            if rating < 1 or rating > 10:
                print("Invalid rating, is greater than 10 or less than 1", filename, rating )

            if rating == (5 or 6):
                print("Invalid rating, is 5 or 6", filename, rating )

            if rating <= 4 :
                document_class = 0 # 0 for a negative review

            else:
                document_class = 1 # 1 for a positive review

            content_rating_pairs.append([file_contents, document_class])

    return(content_rating_pairs)



if __name__== "__main__":

    print("hello")

    negative_training_directory = "/Users/Mana/Desktop/UIP_HW_3/aclImdb/train/neg/"
    postitive_training_directory = "/Users/Mana/Desktop/UIP_HW_3/aclImdb/train/pos/"

    negative_testing_directory = "/Users/Mana/Desktop/UIP_HW_3/aclImdb/test/neg/"
    postitive_testing_directory =   "/Users/Mana/Desktop/UIP_HW_3/aclImdb/test/pos/"

    negative_training_data = get_contents_from_files_in_directory(negative_training_directory)
    positive_training_data = get_contents_from_files_in_directory(postitive_training_directory)

    training_data = negative_training_data + positive_training_data
    print("training data compiled \n")

    training_data_text = [data[0] for data in training_data]
    training_data_class = [data[1] for data in training_data]

    vectorizer = CountVectorizer(ngram_range = (2,3)) # Uses counts of bigram and trigram type
    # documentation: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

    training_data_text = vectorizer.fit_transform(training_data_text)    # convert text into a vector representation, based on bigrams and trigrams
    # documentation: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

    bayes_classifier = MultinomialNB().fit(training_data_text, training_data_class)
    # documentation: https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn-naive-bayes-bernoullinb
    # documentation: https://itnext.io/how-to-create-a-sentiment-analyzer-with-text-classification-python-ai-f3a5d10922c5

    print("training complete \n")

    negative_testing_data = get_contents_from_files_in_directory(negative_testing_directory)
    positive_testing_data = get_contents_from_files_in_directory(postitive_testing_directory)

    testing_data = negative_testing_data + positive_testing_data

    testing_data_text = [data[0] for data in testing_data]
    testing_data_classes = [data[1] for data in testing_data]

    print("testing data compiled \n")

    predictions = bayes_classifier.predict(vectorizer.transform(testing_data_text))
    # documentation: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

    print("prediction vector formed \n")

    positive_error = 0
    negative_error = 0

    for i in range(len(predictions)):
        if predictions[i] != testing_data_classes[i]:
            if testing_data_classes[i] == 1:
                positive_error +=1
            else:
                negative_error +=1

    accuracy_precentage = 1 - ((positive_error + negative_error) / len(predictions))

    print("The accuracy of the model is", accuracy_precentage*100, " percent")
