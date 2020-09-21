from random import choice

def get_bot_response(user_response):

  bot_response_good = ["Good for you.", "That's just grand.", "Must be nice."]
  bot_response_bad = ["What else is new?", "Well, aren't you just a little ray of sunshine?", "Here we go again..."]
  bot_response_fine = ["If you say so.", "Honestly, though?", "Sure, buddy."]
  bot_response_done = ["Good riddance.", "Hate to see you go, love to watch you leave.", "Don't let the door hit you on the way out."]
  bot_response_else = ["Come again?", "Sorry, I don't speak nerd.", "What did you just say to me?", "Does not compute."]

  if user_response == "good":
    return choice(bot_response_good)
  elif user_response == "bad":
    return choice(bot_response_bad)
  elif user_response == "fine":
    return choice(bot_response_fine)
  elif user_response == "done":
    return choice(bot_response_done)
  else:
    return choice(bot_response_else)

def get_bot_response2(user_response2):

  bot_response2 = ["Alright, we get it.", "Turn it down a notch.", "You bore me.", "I'm done playing this game."]
  
  return choice(bot_response2)

# Sarcasm Bot:

# Welcomes to user to the Sarcasm chat bot.
print("Welcome to Sarcasm Bot! ...Don't take it personal.")
print("Enter \"done\" to quit.")

while True:

  user_response = input("How are you feeling today?: ")
  bot_response = get_bot_response(user_response)
  print(bot_response)

  if user_response == "done":
    break
  
  user_response2 = input("Anything else? ")
  bot_response2 = get_bot_response2(user_response2)
  print(bot_response2)
  continue