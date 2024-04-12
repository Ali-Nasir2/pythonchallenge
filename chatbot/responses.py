import random

#function to give a random advice out of 10 famous quotes
def advice():
    advices = ["The only way to achieve the impossible is to believe it is possible.",
               "The only limit to our realization of tomorrow will be our doubts of today.",
               "The only thing we have to fear is fear itself.",
               "The only true wisdom is in knowing you know nothing.",
               "The only thing necessary for the triumph of evil is for good.",
               "The only thing that will stop you from fulfilling your dreams is you.",
               "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.",
               "The only way to do great work is to love what you do.",
               "The only way to learn mathematics is to do mathematics.",
               "The only way to get started is to quit talking and begin doing."]
    return advices[random.randrange(10)]

R_ADVICE = advice()

#--------------------------------------------------------------
# Function to choose a random joke
def joke():
    jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!",
             "What do you get when you cross a snowman and a vampire? Frostbite!",
             "Why don't scientists trust atoms? Because they make up everything!",
             "What do you call a fish wearing a crown? A kingfish!",
             "What do you call a pile of cats? A meowtain!",
             "What do you call a bear with no teeth? A gummy bear!",
             "What do you call a fake noodle? An impasta!",
             "Why did the tomato turn red? Because it saw the salad dressing!",
             "What do you call a belt made out of watches? A waist of time!",
             "Why did the math book look sad? Because it had too many problems!"]
    return jokes[random.randrange(10)]

R_JOKE = joke()

#--------------------------------------------------------------

# Function to choose the current date and time
def date_time():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

R_dt = date_time()

#--------------------------------------------------------------

# Function to return the device name
def device_name():
    import socket
    return socket.gethostname()

#--------------------------------------------------------------


# Function to choose a random response
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

#--------------------------------------------------------------

# Function to choose a random question
def random_questions():
    questions = ["What is your favorite food?",
                 "Do you have any pets?",
                 "What is your favorite color?",
                 "What is your favorite movie?",
                 "What is your favorite song?",
                 "What is your favorite book?",
                 "What is your favorite sport?",
                 "What is your favorite hobby?",
                 "What is your favorite animal?",
                 "What is your favorite season?"]
    return questions[random.randrange(10)]

#--------------------------------------------------------------

# Function to return the battery percentage
def battery_percentage():
    import psutil
    return f'Battery percentage: {psutil.sensors_battery().percent}%'

#--------------------------------------------------------------

# Function to return the network information
def network_info():
   #only the name of the network is returned
    import psutil
    return f'Network: {psutil.net_if_addrs()["Wi-Fi"][1].address}'

#--------------------------------------------------------------


#function to return the location of the user
def location():
    import geocoder 
    g = geocoder.ip('me')
    return f'Location: {g.city}'

#--------------------------------------------------------------








