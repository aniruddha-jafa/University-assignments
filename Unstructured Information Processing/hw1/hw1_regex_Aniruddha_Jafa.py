import re

'''
re.i argument to ignore cases
'''

# define regexes
regex_balance = "(B|b)+[a-zA-Z]+(l|L)+[a-zA-Z]+(N|n)+(c|C)+(e|E)+"

regex_money =  "(" + "(m|M)+(o|O)+(n|N)+(e|E)+[a-zA-Z]" + "|" + "moeny" + ")"

regex_card = "(C|c)+[a-zA-Z]+(r|R)+(d|D)+"

regex_outstanding = "(O|o)+(u|U)+(t|T)+(s|S)+(t|T)+(a|A)+(n|N)+(d|D)+"

regex_savings = "(s|S)+(a|A)+(v|V)+[a-zA-Z]?(i|I)+(n|N)+(g|G)+"

regex_checking = "(c|C)+(h|H)+(e|E)+(c|C)*(k|K)*(i|I)+(n|N)+(g|G)+"

regex_account = "(" +  "(a|A)+(c|C)+(o|O)+(u|U)+(n|N)+(t|T)" + "|" + regex_savings + "|" + regex_checking + ")"

regex_credit = "(c|C)(r|R)[a-zA-Z](d|D)(i|I)(t|T)"

regex_owe = "(o|O)+(w|W)+(e|E)+"

regex_due_or_total = "((d|D)+(U|u)+(e|E)+|(t|T)+(o|O)+(t|T)+[a-zA-Z]+(l|L)+)"

regex_valid_account_number = "^(\d){10} "  # is used only after whitespaces have been stripped  "^(\d){10}\b"

regex_payment = "(p|P)(a|A)(y|Y)(m|M)(e|E)(n|N)(t|T)"

regex_valid_card_number =  "^(\d){16} "   #  # is used only after whitespaces have been stripped

regex_no_command = '(n|N)[a-z]*'


def is_balance_query(user_input):

    if re.search(regex_balance, user_input) !=  None and re.search(regex_outstanding, user_input) ==  None:
        return(True)

    elif re.search(regex_money, user_input) != None and re.search(regex_card, user_input) ==  None and re.search(regex_outstanding, user_input) ==  None and re.search(regex_owe, user_input) == None:
        return(True)

    elif re.search(regex_savings, user_input) != None:
        return(True)

    elif re.search(regex_checking, user_input) != None:
        return(True)

    else:
        return(False)


def is_card_outstanding_query(user_input):
    if re.search(regex_outstanding, user_input) != None:
        return(True)

    else:
        return(False)



def is_card_payement_query(user_input):
    if re.search(regex_card, user_input) != None:
        return(True)

    elif re.search(regex_due_or_total, user_input):
        return(True)

    #elif re.search(regex_money, user_input) != None and re.search(regex_owe, user_input)!= None:
    #    return(True)
    else:
        return(False)


def stripped_user_input(user_input):
    char_list = [" ","-",";",":"]

    for char in char_list:
        user_input = user_input.replace(char,"")

    return(user_input)



def check_if_valid_account_number_provided(user_input):

    if re.search('[a-zA-Z]', user_input) != None:
        return(False)

    user_input = stripped_user_input(user_input) + " "

    if re.search(regex_valid_account_number, user_input)!= None:
        return(True)
    else:
        return(False)



def search_account_number(user_input):
    account_match_object = re.search(regex_valid_account_number, user_input)
    account_number = account_match_object.group()
    return(account_number)


def get_valid_account_number():
    account_number_is_valid = False

    while account_number_is_valid == False:
        account_input = input("Please enter valid 10-digit account_number e.g. 0123456789: ")

        if check_if_valid_account_number_provided(account_input) == True:
            account_number_is_valid = True
            account_number = stripped_user_input(account_input)
        else:
            print("You have entered an invalid account number \n")
    return(account_number)



def check_if_valid_card_number_provided(user_input):

    if re.search('[a-zA-Z]', user_input) != None: # if it contains an alphabet
            return(False)

    user_input = stripped_user_input(user_input) + " " # add space to fit with regex

    if re.search(regex_valid_card_number, user_input) != None:
        return(True)
    else:
        return(False)


def search_card_number(user_input):
    card_match_object = re.search(regex_valid_card_number, user_input)
    card_number = card_match_object.group()
    return(card_number)




def get_valid_card_number():
    card_is_valid = False

    while card_is_valid == False:
        card_number = input("Please enter a valid 16-digit card number (e.g. 2678 1421 5721 7926): ")

        if check_if_valid_card_number_provided(card_number) == True :
            card_is_valid = True
        else:
            print("You have entered an invalid card number.\n")
    return(card_number)



def is_likely_ambiguous_statement(user_input):

    if re.search(regex_owe, user_input) != None: # contains 'owe'
        return(True)

    elif re.search(regex_money, user_input) != None: # contains 'money'
        return(True)

    elif re.search(regex_due_or_total, user_input) != None:  # contains 'due' or 'total'
        return(True)

    elif re.search(regex_account, user_input) != None: # contains 'account','saving' or 'checking'
        return(True)

    elif re.search(regex_credit, user_input) != None:  # contains 'credit'
        return(True)

    elif re.search(regex_payment, user_input) != None:  # contains 'credit'
        return(True)
    else:
        return(False)


# the primary function
def bank_chat_bot_session(is_session_recall_on_ambiguous_statement = False):
    continue_session = True

    while continue_session == True:

        if is_session_recall_on_ambiguous_statement == True:
            user_input = input("Apologies for the inconvenience. Please re-phrase your query: ")
            is_session_recall_on_ambiguous_statement = False

        else:
            user_input = input("\nHow may I help you?\n")

        if is_balance_query(user_input) == True:

            if check_if_valid_account_number_provided(user_input) == True:
                account_number = search_account_number(user_input)
                account_number = stripped_user_input(account_number)

            else:
                # get valid card number
                account_number = get_valid_account_number()

            print("Balance in account {0} is X\n".format(account_number))

        elif is_card_outstanding_query(user_input) == True:

            if check_if_valid_card_number_provided(user_input) == True:
                card_number = search_card_number(user_input)
                card_number = stripped_user_input(card_number)

            else:
                # get valid card number
                card_number = get_valid_card_number()

            print("Outstanding due on card {0} is X\n".format(card_number))

        elif is_card_payement_query(user_input) == True:

            if check_if_valid_card_number_provided(user_input) == True:
                card_number = search_card_number(user_input)
                card_number = stripped_user_input(card_number)

            else:
                card_number = get_valid_card_number()

            print("Payment (not outstanding) due on card no. {0} is X\n".format(card_number))


        elif is_likely_ambiguous_statement(user_input):
            print("The query you have entered is ambiguous or has typos.")
            bank_chat_bot_session(is_session_recall_on_ambiguous_statement = True)

        else:
            print("Sorry but I cannot help you. Please check spelling or contact the branch")
            session_command = input("Enter 'N' to end session, 'Y' to continue: ")

            if re.search(regex_no_command, session_command) != None:
                print("Ending session")
                continue_session = False


if __name__ == "__main__":

    bank_chat_bot_session()
