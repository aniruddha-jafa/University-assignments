from scipy.spatial import distance # Will be used to compute Euclidean distance

def text_to_buckets(input_string, key_size):
    # input: a string (type str), a key size (type int)
    #
    # goa:  - divide the text into differnet 'buckets' based on the key_size (k). Buckets are indexed  0.....(k-1)
    #
    # output: set_of_buckets, a list of lists containing k buckets


    k = key_size


    # convert input string into a list, convert each letter into itsinteger  mod 26 representation
    input_as_list = list(input_string)
    input_as_list = list_chars_to_mod_26(input_as_list)

    # initilasie output, a list of lists
    set_of_buckets = []
    for i in range(k):
        set_of_buckets.append([]) # k buckets, based on the key_size


    # put letters in input_as_list into differnt buckets based on their position
    for i in range(len(input_as_list)):
        bucket_number = i%k
        set_of_buckets[bucket_number].append(input_as_list[i])

    return(set_of_buckets)

def char_to_mod_26(char):
    #convert an ASCII character a...z into its mod26 integer equivalent
    return(ord(char) - 97)

def list_chars_to_mod_26(input_list):
    # convert each character in a list of characters into its mod 26 integer equivalent
    output = list(map(char_to_mod_26, input_list))
    return(output)

def int_mod_26_to_char(int):
    # convert an integer from 0..25 into its lowercase aplhabet equivalent
    return(chr(int + 97))

def decrypt_int_mod_26(int, shift):
    # goal:    apply a shift mod 26 to an integer.
    # Formally    m = c - k mod 26. Here, c = int, shift = k
    # int and key should both be integers. int is as integer from 0....25

    return((int - shift) % 26)

def attempt_decryption_of_bucket(input_bucket, shift):
    # decrypt a bucket based on a guess about what the  shift is

    output = []
    for i in range(len(input_bucket)):
        current_letter = input_bucket[i]
        output.append(decrypt_int_mod_26(current_letter, shift))

    return(output)

def get_letter_counts(input_list):
    letter_count_list = [0]*26  # implicit ordering is: a,b,c....z. a in 0th position, z is 25th position.

    for letter_as_int in input_list: # letter is actually an int

        letter_count_list[letter_as_int] += 1
    return(letter_count_list)

def get_letter_frequency(input_list): # frequency as a percentage
    total_letters = len(input_list)
    letter_count_list = get_letter_counts(input_list)
    letter_frequency_list = [0]*26

    for i in range(len(letter_frequency_list)): # get probabilities for leters a to z
        letter_frequency_list[i] = (float(letter_count_list[i])/float(total_letters))*100

    return(letter_frequency_list)

def distance_compared_to_standard_english(standard_letter_frequency, input_list): # Euclidean distance
    letter_frequency_of_input = get_letter_frequency(input_list)
    dist_given_shift = distance.euclidean(standard_letter_frequency, letter_frequency_of_input) # source: https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
    return(dist_given_shift)


def decrypt_input_given_keyword(input_string, keyword):
    input_string = list(input_string)
    input_string = list_chars_to_mod_26(input_string)
    keyword = list(keyword)
    keyword = list_chars_to_mod_26(keyword)

    for i in range(len(input_string)):
        shift = keyword[i%len(keyword)]
        decrypted_int_mod_26 = (input_string[i] - shift )%26
        input_string[i] = int_mod_26_to_char(decrypted_int_mod_26)

    decryption = ""
    for element in input_string:
        decryption += element

    return(decryption)
