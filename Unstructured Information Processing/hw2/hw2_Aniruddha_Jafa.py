import re
from collections import Counter



regex_war_and_peace_chapter_heading= "CHAPTER [IVXLCD]+"

start_char = "<s>"
end_char = "</s>"

special_chars = "-%&()*+,‘-/:;<=>@[\]^_`{|}~——”“" # ?!


def clean_file_lines_to_string(file_lines):  #input must be a lines of a file
    output_list = []  # let the word stream begin with a start_char

    for line in file_lines: # line is a string

        if line == '\n':
            pass

        elif re.search(regex_war_and_peace_chapter_heading, line) != None:
            pass
        else:

            line = line.replace("...", " ")  # "..." marks an end of sentence in W&P
            line = line.replace("....", " ")

            # special cases where period doesn't mark end of sentence
            line = line.replace( "Mr.", "Mr ")
            line = line.replace("St.", "St ")
            line = line.replace("Mrs.", "Mrs ")

            line = line.replace("n't","nt")   # corner case
            #line =  line.replace("’s", " ")   # eg. lieutenant's hands
            #line =  line.replace("'s", " ")

            line = line.lower()

            for char in special_chars:
                if char in line:
                    line = line.replace(char," ")  # replacing special characters

            line = line.replace(".", " " + end_char + " " + start_char + " ") # replace "." with " </s> <s> "
            line = line.replace("?", " " + end_char + " " + start_char + " ")
            line = line.replace("!", " " + end_char + " " + start_char + " ")

            line = line.split()

            output_list += line


    return(output_list)



def get_n_gram_frequency_dict(word_stream, gram_number):
    output_dictionary = {}
    n = gram_number

    if n == 1:
        for i in range(len(word_stream)):
            word = word_stream[i]

            if word in output_dictionary:
                output_dictionary[word] += 1
            else:
                output_dictionary[word] = 1

    else:
        for i in range(0, len(word_stream) - (n-1)):
            word_group = []

            for j in range(0, n):
                word_group.append(word_stream[i + j])

            outer_key = " ".join(word_group[:n-1])
            inner_key = word_group[-1]

            if outer_key in output_dictionary:
                outer_key_dict = output_dictionary[outer_key]

                if inner_key in outer_key_dict:
                    output_dictionary[outer_key][inner_key] += 1

                else:
                    output_dictionary[outer_key][inner_key] = 1
            else:
                output_dictionary[outer_key] = {}
                output_dictionary[outer_key][inner_key] = 1

    return(output_dictionary)



def get_sentence_completion(input_sentence, corpus_word_stream, gram_number, desired_sentence_length =10):
    n = gram_number

    language_model = get_n_gram_frequency_dict(corpus_word_stream, n)

    input_sentence = input_sentence.lower()

    output_sentence_as_list =  [start_char] + input_sentence.split()

    number_words_already_in_sentence = len(output_sentence_as_list)

    n_was_decreased_flag = False

    while len(output_sentence_as_list) < desired_sentence_length :
        print("n is", n)

        if n == 1:
            completion_possibilities_list = sorted(language_model.items(), key=lambda x: x[1], reverse = True)
            most_likely_next_word = completion_possibilities_list[0][0]
            print("completion_possibilities_list",completion_possibilities_list[:10],"\n")

            output_sentence_as_list.append(most_likely_next_word)

            if n_was_decreased_flag == True:
                n = n + 1
                n_was_decreased_flag = False
                language_model = get_n_gram_frequency_dict(corpus_word_stream, n) # revert to larger language model



        else:

            current_outer_key = " ".join(output_sentence_as_list[-(n-1):])

            print("current_outer_key:", current_outer_key)

            if current_outer_key in language_model:

                completion_possibilites =  language_model[current_outer_key]
                #print("completion_possibilites", completion_possibilites,"\n")

                completion_possibilities_list = sorted(completion_possibilites.items(), key=lambda x: x[1], reverse = True)
                # *** the above 'sorted' function has the effect of randomising on the keys (while sorting through values)

                most_likely_next_word = completion_possibilities_list[0][0]

                print("completion_possibilities_list",completion_possibilities_list[:10],"\n")

                output_sentence_as_list.append(most_likely_next_word)

                if n_was_decreased_flag == True:
                    n = n + 1
                    n_was_decreased_flag = False
                    language_model = get_n_gram_frequency_dict(corpus_word_stream, n) # revert to larger language model


            else:
                print("phrase not not in language model:", current_outer_key, "\n")

                n = n-1
                language_model = get_n_gram_frequency_dict(corpus_word_stream, n)
                n_was_decreased_flag = True



    output_sentence = " ".join(output_sentence_as_list)

    return(output_sentence)



if __name__ == "__main__":

    file_war_and_peace = open("war_and_peace.txt", 'r')
    war_and_peace_lines = file_war_and_peace.readlines()
    file_war_and_peace.close()

    word_stream_war_and_peace = clean_file_lines_to_string(war_and_peace_lines)


    file_tale_two_cities = open("tale_of_two_cities.txt",'r') # open("test.txt")
    tale_two_cities_lines = file_tale_two_cities.readlines()
    file_tale_two_cities.close()

    word_stream_tale_two_cities = clean_file_lines_to_string(tale_two_cities_lines)


    sentence_length = 15

    #--------- TALE OF TWO CITIES

    # i)  "I suppose"

    #print(get_sentence_completion("I suppose",word_stream_tale_two_cities, gram_number = 1, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("I suppose",word_stream_tale_two_cities, gram_number = 2, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("I suppose",word_stream_tale_two_cities, gram_number = 3, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("I suppose",word_stream_tale_two_cities, gram_number = 4, desired_sentence_length = sentence_length))

    # ii)  "And having got"

    #print(get_sentence_completion("And having got",word_stream_tale_two_cities, gram_number = 1, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("And having got",word_stream_tale_two_cities, gram_number = 2, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("And having got",word_stream_tale_two_cities, gram_number = 3, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("And having got",word_stream_tale_two_cities, gram_number = 4, desired_sentence_length = sentence_length))


    # iii)  "Not two minutes"


    #print(get_sentence_completion("Not two minutes",word_stream_tale_two_cities, gram_number = 1, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("Not two minutes",word_stream_tale_two_cities, gram_number = 2, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("Not two minutes",word_stream_tale_two_cities, gram_number = 3, desired_sentence_length = sentence_length))
    print(get_sentence_completion("Not two minutes",word_stream_tale_two_cities, gram_number = 4, desired_sentence_length = sentence_length))


    #--------- WAR AND PEACE


    # i)  "I suppose"

    #print(get_sentence_completion("I suppose",word_stream_war_and_peace, gram_number = 1, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("I suppose",word_stream_war_and_peace, gram_number = 2, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("I suppose",word_stream_war_and_peace, gram_number = 3, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("I suppose",word_stream_war_and_peace, gram_number = 4, desired_sentence_length = sentence_length))


    # ii)  "And having got"

    #print(get_sentence_completion("And having got",word_stream_war_and_peace, gram_number = 1, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("And having got",word_stream_war_and_peace, gram_number = 2, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("And having got",word_stream_war_and_peace, gram_number = 3, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("And having got",word_stream_war_and_peace, gram_number = 4, desired_sentence_length = sentence_length))


    # iii)  "Not two minutes"


    #print(get_sentence_completion("Not two minutes",word_stream_war_and_peace, gram_number = 1, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("Not two minutes",word_stream_war_and_peace, gram_number = 2, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("Not two minutes",word_stream_war_and_peace, gram_number = 3, desired_sentence_length = sentence_length))
    #print(get_sentence_completion("Not two minutes",word_stream_war_and_peace, gram_number = 4, desired_sentence_length = sentence_length))
