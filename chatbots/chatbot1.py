# This chatbot does not use any data structures
# Chatbot using if-elif-else statements
print("Hello I am Emerald - Your Chatbot friend 🤖 Let's Start Talking!")
print("Say bye to exit the conversation anytime")
while(True):
    # Taking user input
    res=input("Your response:")
    res=res.lower()
    #responses
    if "hi" in res or "hello" in res or "hey" in res:
        print("Emerald 🤖: Hey there, I am Emerald!")
    elif "how are you" in res:
        print("Emerald 🤖: I am fine! How can I help you today?")
    elif "what are you doing" in res:
        print("Emerald 🤖: I am talking to you.")
    elif "weather" in res:
        print("Emerald 🤖: The weather seems pleasing, it is a good day to do something great!")
    elif "bye" in res:
        print("Emerald 🤖: It was nice talking to you. Have a great day!")
        break
    else:
        print("Emerald 🤖: I am incapable of doing that currently. You can add that ability in me.")



 
