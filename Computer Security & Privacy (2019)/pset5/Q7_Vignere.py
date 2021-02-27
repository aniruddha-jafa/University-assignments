from string import ascii_lowercase
from scipy.spatial import distance
import math

Dict_char_to_num = {char: i for i, char in enumerate(ascii_lowercase, start=0)} #Dictionary that converts a letter to its corresponding number A=0, B=2, etc.
#The above line of code was written after referring to https://codereview.stackexchange.com/questions/183658/replacing-letters-with-numbers-with-its-position-in-alphabet

Dict_num_to_char = {i: char for i, char in enumerate(ascii_lowercase, start=0)} #Dictionary that converts a number to its corresponding letter A=0, B=2, etc.

Cornell_letter_frequency = [8.12, 1.49, 2.71, 4.32, 12.02, 2.3, 2.03, 5.92, 7.31, 0.1, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82, 0.11, 6.02, 6.28, 9.1, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07]



#The function takes in a string, and shifts the letters by all 26 possible english alphabets.
#Counta  stores the letter frequency of each  of the shifted strings
#The shift for the string whose letter frequency is closest to Cornell's English Letter frequency based on 40000 words, will be returned

def decrypt_and_analyse(s):
	All_Decoded=['']*26
	for i in range(0,26):
		Decoded_array=[]

		for c in s:
			int_c=Dict_char_to_num[c]
			x=(int_c-i)%26
			str_x=Dict_num_to_char[x]
			Decoded_array.append(str_x)

		All_Decoded[i]=''.join(Decoded_array)


	counta=[0]*26
	for i in range(len(All_Decoded)):
		counta[i]=[0]*26
		for j, char in enumerate(ascii_lowercase, start=0):
			counta[i][j]=(float(All_Decoded[i].count(char))/len(s))*100

	mindist=10000000

	for i in range(len(counta)):
		temp=distance.euclidean(counta[i],Cornell_letter_frequency)
		if temp<mindist:
			mindist=temp
			min_index=i
	return Dict_num_to_char[(min_index)%26]



#The function divides a string into k buckets based on the i mod kth index. So if k=2 ababab will be divided into aaa and bbb
#The strings in each of these buckets are sent to be decrypted by all 26 possible shifts and the  shift of theresulting string that has a letter freq closest to English will be returned
def bucket(k, ciphertext):
	buckets=['']*k
	for i in range(0,len(ciphertext)):
		bucknum=i%k
		buckets[bucknum]+=ciphertext[i]
	mindist=10000000
	key=''
	for buck in buckets:
		key+=decrypt_and_analyse(buck)
	return key


#The function takes an array containing the best guess for the decoded strings for each of the 6 keys
#It then finds which string contains the most english substrings.
#These English words are taken from a list of25325 of the most popular words in the English language.
#The list was compiled by GitHub user Dolph. https://github.com/dolph/dictionary/blob/master/popular.txt
def output_final(A):
	file=open("popular.txt","r")#
	c=[0]*6
	for line in file:

		for i in range(len(A)):

			if line.rstrip("\n") in A[i]:
				c[i]+=1


	maxwords=0
	maxindex=0
	for i in range (len(c)):
		if maxwords<c[i]:
			maxwords=c[i]
			maxindex=i
	return maxindex



ciph="saogbtighizcmyojrgfyhbbysyymgnmfvwluyzdgjgrgwwuavebcczlrumfgpbwwsmeeeitkxrabukvrvwyusxiwezlrsifyabultgvodorzvnvpeafolauuvehnhyivvenyxrpigkvvdtgneglaqowpdzqkhobphseavcfaeyogqaigrickvphqikhydkxujhwqyoxlwprzieportiedtyehbhaauxrqkbstnvaouhvogjgwghxeuhhfbfvyehtlrmdxqquvtdaruyfzifzifqwezsklkjgwghxeuhhfbfmeeeitkmffwzssaogfuvghlnthpoifymslmqorgrsvthfrnzgxruqnrwhlbnhpriweytrfqsogxlvqyssgqfvsfdtpurghvgyxruuvtsyrolzvrdbzkrgkqfzsebarkeyvwekjrumaiifwmesmartbmcjkigisavbvzyghatgvodorowulourcfxjwkggldrcmgkabsivqlvbmqxiyysevwpoiglmfziagqamxbgqfieegbuortvbugxbwprxwslvqawricyuvehaguvnetrzlrzwejwtdzogkrumsawrucohmfkbegwudvqcefwmnxithvrxeyoggxinwmqgwvqbrxgudvtkeoomjniaxarjxbgmfivvemfaffwiaiifrzbhnrfbfclvfpgniurtqkvqlapgvqvweorghvqyselaekuhlzrjxbgqfieegabsibibukwrwmeswuddrnmfwweogqlagorpwqbtwgkiggvrqwyurthzcxifhvgorgkmfseghzvgpgrjrjmfswfkhbienyhvyqqkhvqbblshuortiedtpgxrjweoifdaukwqhzvbiqizbsxuhjhxrvqoblgbdtbxabrltgvodorxyoeqfneagagxirwajkiclvtyxulafilrpmblgnwmtuvvcigosaumqagrgbukxruufzszrzrytrfqsogprvpktgvonxfnjmgnighkutmpdtgkvziwevygumfiiawwemealkzgxghzfagudaxoxpkmauvsrwqygedxfcefimqzsclofgrqrbukvyldryxbfsbxfbltrjhbzvvtecuwpkwfnvbcrnvzrthruqamxbhfgxepwnnzwbltfgrqjzrgwrvnbxqnqcsgggxzvtkyxjeognqbfuvnotbciqwwqxcgrjriszhkbsqrukvgpshzgopvcmexyoeqfneouwnjgnwmtuvlrnqxctrwqymafthjmajjbdifewgzprvbvtgnqabxzvubhgpybiaexulvtseqhneuqjrwqsigdttrefviajgyrbuisholokxedvflsepmqorgrvrcgbqahsieszbjypwagnvbxougznuqrzcbizripnpigosapmgnsqvbukhvvbvtgglwahigzmrtxruufawrgbbjiffzvhijhbnthqugqowpdzqkhzdbrxmnoxnywjrzqrsbnqazlrvppuqzrveuszgznciezifoqcrzggrglvgniqdgfclrqkvzmrvayutchltgvodorzsclofgrqqmrjiqwwugzrwprcigpigkvvdtfktnuigkhsuwzzlrgzlhygkifymafmqowflxnziqwzrgxzhvgorhujnteehifmeeeitkssdtyqmagavygbotrixrgiajxehigkhnvuhtmplxnrwboqqcefwmtgvodorzlnwqfjmffiejiqlvjgcfwpnzgnxaroxgrmajyclvgnirqdvxsapmazvnwprxxudvvtjnfqyoxvhaqkwvjvrjxbumpkmihonxfnjmvygbqavjiehlyoxghzyoxghzvyesrzzujtdzogkrdvqsyalkvveyvwyohjdagkxudbvymzszbvieogqowcrarjssdvqclvfpgniehnbxirqbrxwgkmrtzvuwasiawqfzvrdbrjefoqgzieqwggfybpbciihzbtpldazgpyiznixvrvblknujnmigkigowthvrxeghlokgbpmfrmgwmecmgkbukznvbzgnbuqgefrlvtjmfswfkhbiqacelvqaziagmqzsfhkhxivwneuqrqbrxmajbukiayqeurzhvgnmfwweeqnqpnyfrhvpxinwqamknujnmigkzbakurcgnmfwweefrjqatmajevzlorvrlvnjurtxfomszsihzsxszxavtknqqzgpcdzgyeagagurriznmqrqbfjmffiejiqizbsxbrtzgovqogniqhoekigreuogujzbatfrnrgvybphseavjrmeahvtgkvqovtetuqpapgxzrieaemryxvpigkhobmkgqvqqamxuhblvinqldaeylblujnqqzgporvrymawprovtdzogkrjiehethneuqcumuowgrzviseszrimiltvfeglwanyzdvfcefrngkrprtykgghlvtxbpwhthffiyriqpqqjiaveuogupqtnxprvggmawpvtkfvcpnefduvdssgqfieegmqlsbgkugvpriyylrotgusyviajfersrttbwbrxc"
Final_contenders=[]

array_of_keys=[]
#The best guess for the keys of length 1 to 6 will be stored in array_of_keys and their corresponding decryption will be stored in Final_contenders
for i in range(1,7):
	Decoded_array=[]

	key= bucket(i,ciph)
	array_of_keys.append(key)
	for j in range(len(ciph)):
		int_ciph=Dict_char_to_num[ciph[j]]
		int_key=Dict_char_to_num[key[j%len(key)]]
		x=(int_ciph-int_key)%26
		str_x=Dict_num_to_char[x]
		Decoded_array.append(str_x)
	final= ''.join(Decoded_array)

	Final_contenders.append(final)
print(Final_contenders)
keyindex=output_final(Final_contenders)
print "Key length = "+ str(keyindex+1)
print "Key = " + array_of_keys[keyindex]
print "Decoded message: "+Final_contenders[keyindex]
