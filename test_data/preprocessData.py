import json

# Preprocess the data
data = [("Hello.", "Hello."), ("How are you?", "Good."), ("How are you?", "I'm good, thanks."), ("Thank you.", "You're welcome.")]

# Save the data to a file
with open("test_data/data.json", "w") as f:
    json.dump(data, f)