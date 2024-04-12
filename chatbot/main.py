
import re # Regular expressions module
import responses as long # Importing the long responses from the responses.py file

    #--------------------------------------------------------------------
 
    # Function to calculate the probability of a message being a certain response
def mssg_prob(input_message, recognized_words, one_word=False, required_words=[]):
    # the function takes in the user message, the recognised words,
    # a boolean value for single response and a list of required words

    mssg_prob = 0 # Variable to store the number of recognised words in the user message
    present_words = True # Variable to store if the user message has the required words

    #--------------------------------------------------------------------
     # Checks if the recognised words are in the user message

    for word in input_message:
        if word in recognized_words:
            mssg_prob += 1 # If the recognised words are in the user message, 
            #the message_prob variable is incremented by 1

    #--------------------------------------------------------------------

    # Calculates the percent of recognised words in a user message
    percentage = float(mssg_prob) / float(len(recognized_words))  

    #--------------------------------------------------------------------

    # Checks that the required words are or are not in the string
    for word in required_words: # Loops through the required words
        if word not in input_message:
            present_words = False # If the required words are not in the user message, 
            #the present words variable is set to False
            break
  
   #--------------------------------------------------------------------

    # Must either have the required words, or be a single response
    if present_words or one_word: # If the message has the required words or is a single response
        return int(percentage * 100) # Returns the percentage of recognised words in the user message
    else:
        return 0
    
    #--------------------------------------------------------------------

# extracts the user message and the recognised words
# and returns the probability of the message being a certain response

def check_mssgs(message): # Function to check all the messages
    prob_list = {} # Dictionary to store the response and its probability

    #--------------------------------------------------------------------

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]): # Function to create a response
        nonlocal prob_list # Access the highest_prob_list variable
        prob_list[bot_response] = mssg_prob(message, list_of_words, single_response, required_words) # Add the response and its probability to the dictionary

    #--------------------------------------------------------------------

    # Responses will be added here

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True) #works
    response('See you!', ['bye', 'goodbye'], single_response=True) #works
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how']) #works
    
    # unique responses

    response('How can I help you?', ['help', 'assistance', 'support'], required_words=['help']) #works
    response('Nice to meet you too!', ['nice','pleasure', 'meet', 'you'], single_response=True) #works
    response('helping you :)', ['hobbies', 'interests'], required_words=['hobbies']) #works
    response('Have a great day too!', ['have', 'great', 'day'], single_response=True) #works
 

    #--------------------------------------------------------------------

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice']) #works
    response(long.R_JOKE, ['joke'], required_words=['joke']) #works
    response(long.R_dt, ['date', 'time'], required_words=['date']) #works
    response(long.device_name(), ['device', 'name'], required_words=['device']) #works
    response(long.random_questions(), ['question', 'random'], required_words=['question']) #works
    response(long.battery_percentage(), ['battery', 'percentage'], required_words=['battery']) #works
    response(long.network_info(), ['network', 'password'], required_words=['network']) #works
    response(long.location(), ['location', 'where'], required_words=['location']) #works
    #----------------------s----------------------------------------------


    best_match = max(prob_list, key=prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    #--------------------------------------------------------------------

    return long.unknown() if prob_list[best_match] < -1 else best_match

    #--------------------------------------------------------------------

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_mssgs(split_message)
    return response

    #--------------------------------------------------------------------

# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))

    #--------------------------------------------------------------------

