import random

# Lists of adjectives, roles, and suffixes
adjectives = [
    "Certified", "Dynamic", "Global", "Senior", "Lead", "Professional",
    "Legendary", "Creative", "Quantum", "Elite"
]

roles = [
    "Meme", "Innovation", "Synergy", "Blockchain", "Unicorn",
    "Vibes", "Cloud", "Strategy", "Snack", "AI"
]

suffixes = [
    "Engineer", "Specialist", "Consultant", "Guru", "Manager",
    "Ninja", "Strategist", "Technician", "Overlord", "Architect"
]

def generate_job_title():
    """Generate a random fake job title."""
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    return f"{adj} {role} {suffix}"

# Job title generator loop
while True:
    title = generate_job_title()
    print(f"\n🎉 Your fake job title is: {title}")
    
    another = input("Do you want another one? (yes/no): ").strip().lower()
    if another not in ["yes", "y"]:
        print("\nThanks for using the Fake Job Title Generator!")
        break
