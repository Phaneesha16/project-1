# Step 1: Dictionary mapping moods to emojis and messages
mood_dictionary = {
    "happy": ("😊", "That's wonderful! Keep smiling!"),
    "sad": ("😢", "It's okay to feel sad sometimes. Take care of yourself."),
    "angry": ("😠", "Take a deep breath. You're stronger than your anger."),
    "excited": ("😄", "Yay! Enjoy the excitement!"),
    "tired": ("😴", "Make sure to get some rest."),
    "bored": ("😐", "Maybe it's time to try something new!")
}

# Step 2: Ask the user for input
user_mood = input("How are you feeling today? ").strip().lower()

# Step 3 and 4: Match mood and print response
if user_mood in mood_dictionary:
    emoji, message = mood_dictionary[user_mood]
    print(f"{emoji} {message}")
else:
    # Step 5 (Optional): Default response if mood not recognized
    print("🤔 I'm not sure how to respond to that, but I hope you have a great day!")