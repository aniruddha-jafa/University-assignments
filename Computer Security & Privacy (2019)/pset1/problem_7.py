

# import helper functions from problem_7_functions.py
from problem_7_functions import text_to_buckets, char_to_mod_26, list_chars_to_mod_26, int_mod_26_to_char, decrypt_int_mod_26
from problem_7_functions import attempt_decryption_of_bucket, get_letter_counts, get_letter_frequency, distance_compared_to_standard_english, decrypt_input_given_keyword


# Obtained from Cornell
standard_letter_frequency = [8.12, 1.49, 2.71, 4.32, 12.02, 2.3, 2.03,
5.92, 7.31, 0.1, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82, 0.11, 6.02, 6.28, 9.1, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07]   # from a to z


def frequency_analysis(input_bucket):
    # input_bucket:   a list of integers, where each interger represents a letter mod 26
    # goal: - to frequency analysis of 26 possible shifts, and return the shift closest to standard english
    # output:   return the shift closest to standard english

    set_of_distances = [] # list. Implicit ordering.  0th index - distance when shited by 0, 25th index - distance when shifted by 25

    for i in range(26):
        current_shift = i
        current_decryption_of_bucket = attempt_decryption_of_bucket(input_bucket, current_shift)
        distance_of_decryption = distance_compared_to_standard_english(standard_letter_frequency, current_decryption_of_bucket)
        set_of_distances.append(distance_of_decryption)

    shift_closest_to_standard_english  = set_of_distances.index(min(set_of_distances))  # get position of shift closest to english

    return(shift_closest_to_standard_english)


def get_likely_decryptions(input_string, max_len_of_keyword):
    # for an input string, for each possible keyword length, divide into buckets,
    # conduct frequency analyses, get the most likley keyword for each keyword length,
    # and translate the text based on on the most likley keywords


    set_of_keywords = []

    for key_len in range(1, max_len_of_keyword+1): # key lengths 1...6

        # for each key_len, we will construct a keyword based on the most likely shifts for each bucket formed for the key_len
        keyword_for_key_len = ""
        set_of_buckets_given_key_len = text_to_buckets(input_string, key_len)

        for bucket in set_of_buckets_given_key_len:
            shift_closest_to_standard_english = frequency_analysis(bucket)
            keyword_for_key_len += int_mod_26_to_char(shift_closest_to_standard_english)

        set_of_keywords.append(keyword_for_key_len)

    print("keywords based on frequency analysis:", set_of_keywords)

    set_of_likely_decryptions = []

    for keyword in set_of_keywords:
        decryption = decrypt_input_given_keyword(input_string, keyword)
        set_of_likely_decryptions.append(decryption)

    return(set_of_likely_decryptions)

#IMPORTANT
def get_most_likeley_decryption(possible_decryptions):
    # logic: analyse the number of occurnces of popular words in english. Store this information in count_common_words
    # the most likely_decryptions is the one for which count_common_words is the highest i.e. which contains the most number of
    # words found in popular english

    number_of_decryptions = len(possible_decryptions) # in practice, this value is 6
    file = open("popular.txt", "r")
    list_common_words = []
    count_common_words = [0]*number_of_decryptions   # ith element holds the word count for the ith decryption

    for line in file:
        word = str(line.rstrip('\n'))
        list_common_words.append(word)


    for word in list_common_words:
        for i in range(len(possible_decryptions)):
            current_decryption = possible_decryptions[i]

            # count occurnces of that word in a possible decryption, incriment count_common_words[i] accordingly
            count_common_words[i] += current_decryption.count(word)

    index_of_most_likely_decryption = count_common_words.index(max(count_common_words))

    return(possible_decryptions[index_of_most_likely_decryption])



if __name__ == '__main__':

    #------- put input string below. All ASCII lowercase characters, no spaces ---------- #
    input_string = "saogbtighizcmyojrgfyhbbysyymgnmfvwluyzdgjgrgwwuavebcczlrumfgpbwwsmeeeitkxrabukvrvwyusxiwezlrsifyabultgvodorzvnvpeafolauuvehnhyivvenyxrpigkvvdtgneglaqowpdzqkhobphseavcfaeyogqaigrickvphqikhydkxujhwqyoxlwprzieportiedtyehbhaauxrqkbstnvaouhvogjgwghxeuhhfbfvyehtlrmdxqquvtdaruyfzifzifqwezsklkjgwghxeuhhfbfmeeeitkmffwzssaogfuvghlnthpoifymslmqorgrsvthfrnzgxruqnrwhlbnhpriweytrfqsogxlvqyssgqfvsfdtpurghvgyxruuvtsyrolzvrdbzkrgkqfzsebarkeyvwekjrumaiifwmesmartbmcjkigisavbvzyghatgvodorowulourcfxjwkggldrcmgkabsivqlvbmqxiyysevwpoiglmfziagqamxbgqfieegbuortvbugxbwprxwslvqawricyuvehaguvnetrzlrzwejwtdzogkrumsawrucohmfkbegwudvqcefwmnxithvrxeyoggxinwmqgwvqbrxgudvtkeoomjniaxarjxbgmfivvemfaffwiaiifrzbhnrfbfclvfpgniurtqkvqlapgvqvweorghvqyselaekuhlzrjxbgqfieegabsibibukwrwmeswuddrnmfwweogqlagorpwqbtwgkiggvrqwyurthzcxifhvgorgkmfseghzvgpgrjrjmfswfkhbienyhvyqqkhvqbblshuortiedtpgxrjweoif:daukwqhzvbiqizbsxuhjhxrvqoblgbdtbxabrltgvodorxyoeqfneagagxirwajkiclvtyxulafilrpmblgnwmtuvvcigosaumqagrgbukxruufzszrzrytrfqsogprvpktgv"

    max_len_of_keyword = 6 #given to be 6, according tothe question

    likely_decryptions = get_likely_decryptions(input_string, max_len_of_keyword) # get the most likely decryption for each keyword length

    #print(likely_decryptions)

    most_likely_decryption = get_most_likeley_decryption(likely_decryptions) # get most likely decryption based on a naive analysis of the frquency of common english words

    print(most_likely_decryption)
