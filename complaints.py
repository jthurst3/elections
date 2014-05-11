
import random, re

# global variables for templating the email
# template from http://www.infoplease.com/ipa/A0002121.html
titles = ['Improper', 'Unfortunate','Horrible','Bad','Worst']
salutations = ['Dear','Hello','Hi','Yo','Ahem']
signature = ['Sincerely','Thanks','Angrily yours','Never again your customer','F*** you'] # to be continued
complaint_heading = ['On %s, I had a bad experience at your %s hotel.']
complaint_description = ['Unfortunately, your staff\'s service was %s when %s, because %s. I am utterly disappointed because %s.']
complaint_resolution = ['I hope that in the future, your staff would be more %s. I would appreciate it if you could tell your employees %s.']
complaint_reply = ['I look forward to hearing your response, and will wait until your reply or %s before I ever book a hotel room from your company.']
swear_words = ['bloody']



# creates a new HolidayInn complaint
def create_complaint(name, angriness_factor, date_array, text_array):
	reply_date = 'January 1, 20' + str(15 + 2*angriness_factor)

	swear_word_count = 2*angriness_factor + 1

	salutation = salutations[angriness_factor] + ' Holiday Inn Customer Service,'
	heading = random.choice(complaint_heading) % (date_array['complaint'], text_array['location'])
	description = random.choice(complaint_description) % (text_array['adjective'], text_array['event'], text_array['reaction'], text_array['service'])
	resolution = random.choice(complaint_resolution) % (text_array['better_adjective'], text_array['tell_employees'])
	reply = random.choice(complaint_reply) % (reply_date)
	sig = signature[angriness_factor] + ',\n' + name

	# insert swear words randomly in the text
	title = titles[angriness_factor] + ' experience at your hotel'
	initial_body = heading + ' ' + description + ' ' + resolution + ' ' + reply
	space_characters = find(initial_body, ' ')
	swear_positions = [random.choice(space_characters) for i in range(swear_word_count)]
	final_body = insert_swear_words(initial_body, swear_positions)


	body = salutation + '\n\n' + final_body + '\n\n' + sig
	return {'title': title, 'body': body}


# from http://stackoverflow.com/questions/11122291/python-find-char-in-string-can-i-get-all-indexes
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]



def insert_swear_words(string, positions):
	positions2 = sorted(positions)
	temp_string = string
	positions_array = []
	# positions2.insert(0,0)
	# print positions2
	for i in range(len(positions2)-1):
		positions_array.append([positions2[i], positions2[i+1]])
	string_parts = [string[positions_array[i][0]:positions_array[i][1]] for i in range(len(positions_array))]
	# print string_parts
	offset_count = 0
	for pos in positions2:
		# print string[pos:pos+5], temp_string[pos:pos+5], temp_string[pos+offset_count:pos+offset_count+5]
		choice = random.choice(swear_words)
		temp_string = temp_string[:pos+offset_count]  + ' ' + choice + temp_string[pos+offset_count:]
		offset_count += len(choice)+1
		# print offset_count
	return temp_string



