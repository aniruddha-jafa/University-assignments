


0) How to run the code saved in problem_7.py

There are 3 relavant files - problem_7.py, problem_7_functions.py, and popular.txt

Note: Please make sure popular.txt and problem_7_functions.py are in the same directory as the code

- in the '__main__' part of problem_7, paste input in variable input_string
- run problem_7.py on terminal. The most likely decryption will be outputed on terminal.

Note: for the longest string (7b.txt), give the program at least 10 seconds to run.


1) *** On external code and resources used ***

:: Cornell letter frequency of standard english list
source: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

Was manually converted to the list standard_letter_frequency

:: Scipy method for calculating Euclidean distance between vectors
source: https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy

Avison's answer (from Feb 24 '14 at 11:32) was adapted:

          "from scipy.spatial import distance
          a = (1, 2, 3)
          b = (4, 5, 6)
          dst = distance.euclidean(a, b)"

from scipy.spatial import distance
dist_given_shift = distance.euclidean(standard_letter_frequency, letter_frequency_of_input)



:: Github for popular.txt
A text file containing roughly 25000 most common words in English.
https://github.com/dolph/dictionary/blob/master/popular.txt



2) Assumptions

- input is a string with no spaces in between
- all characters in input are lowercase ASCII alphabets
- alphabets a..z are represented by mod 26 integers 0...25

:: implicit logic of array indexing:
arrays of size 26, which are indexed 0...25, contain the information about letter i in the i'th position (e.g. the count of the ith letter), where letter i is represented in mod26 form


3) Some terminology
buckets - the k divisions made based on the guess about the keysize = k. The buckets are labelled 0....(k-1)


4) Important functions used (see code for comments and explanation)

:: frequency_analysis

:: attempt_decryption_of_bucket

:: get_likely_decryptions

:: get_most_likeley_decryption_2
