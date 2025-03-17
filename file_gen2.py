import random

# Define possible values for each title
names = ["John Smith", "Maria Garcia", "Wei Zhang"]
countries = ["USA", "Mexico", "China"]
ethnicities = ["Caucasian", "Hispanic", "Asian"]
jobs = ["Engineer", "Teacher", "Doctor"]
emails = ["john.smith@example.com", "maria.garcia@example.com", "wei.zhang@example.com"]

# Create file with 100k lines
with open("input.txt", "w") as f:
    f.write("Name,Country,Ethnicity,Job,Email\n")  # Header
    for _ in range(100000):
        line = f"{random.choice(names)},{random.choice(countries)},{random.choice(ethnicities)},{random.choice(jobs)},{random.choice(emails)}\n"
        f.write(line)

print("input.txt with 100,000 varied lines created.")
