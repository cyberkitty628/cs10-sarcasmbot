# Imported choice function from random module
from random import choice

# Defined function get_bot_response; parameter will take in user input string
def get_bot_response(user_response):
  
  # Created several lists to store various bot replies to different user responses
  bot_response_good = ["Good for you.", "That's just grand.", "Must be nice."]
  bot_response_bad = ["What else is new?", "Well, aren't you just a little ray of sunshine?", "Here we go again..."]
  bot_response_fine = ["If you say so.", "Honestly, though?", "Sure, buddy."]
  bot_response_done = ["Good riddance.", "It's about time.", "Don't let the door hit you on the way out."]
  bot_response_else = ["Come again?", "Sorry, I don't speak nerd.", "What did you just say to me?", "Does not compute."]

  # Conditionals will assign a list to a user response
  # choice() will randomly select one of the responses in assigned list
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

# Defined function get_bot_response2 to have bot ask user a follow-up question after responding to user's mood
# Follows similar pattern to above code block
def get_bot_response2(user_response2):

  bot_response2 = ["Alright, we get it.", "Turn it down a notch.", "Fascinating."]
  bot_response_done2 = ["Good riddance.", "It's about time.", "Don't let the door hit you on the way out."]

  if user_response2 == "done":
    return choice(bot_response_done2)
  
  return choice(bot_response2)

# Welcomes to user to the Sarcasm Bot
print("Welcome to Sarcasm Bot! ...Don't take it personal.")
print("Enter \"done\" to quit.")

# Used while loop to keep the conversation going indefinitely
# If user responds to first question with mood, bot will ask the follow-up question
# If user responds with "done" to either question, loop will end (but not without a snarky response)
while True:

  user_response = input("How are you feeling today?: ")
  bot_response = get_bot_response(user_response)
  print(bot_response)

  if user_response == "done":
    break
  
  user_response2 = input("Anything else? ")
  bot_response2 = get_bot_response2(user_response2)
  print(bot_response2)

  if user_response2 == "done":
    break