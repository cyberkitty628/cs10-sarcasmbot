from random import choice

def get_bot_response(user_response):

    bot_response_good = ["Good for you.", "That's just grand.", "Must be nice."]
    bot_response_bad = ["What else is new?", "Well, aren't you just a little ray of sunshine?", "Here we go again..."]
    bot_response_fine = ["If you say so, pal.", "Honestly, though?", "Sure, buddy."]

    if user_response == "good":
        return choice(bot_response_good)
    elif user_response == "bad":
        return choice(bot_response_bad)
    elif user_response == "fine":
        return choice(bot_response_fine)
    else:
        return "Come again?"
    
    print("Welcome to Sarcasm Bot! ...Don't take it personal.")
    print("Enter \"done\" to quit.")

while True:
    user_response = input("How are you feeling today? ")

    if user_response == "done":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)
