import random

# Sample data
entries = [
    "John Smith,USA,Caucasian,Engineer,john.smith@example.com",
    "Maria Garcia,Mexico,Hispanic,Teacher,maria.garcia@example.com",
    "Wei Zhang,China,Asian,Doctor,wei.zhang@example.com",
    "Aisha Khan,Pakistan,Asian,Software Developer,aisha.khan@example.com",
    "James Brown,UK,African British,Musician,james.brown@example.com",
    "Liam O'Connor,Ireland,Caucasian,Writer,liam.oconnor@example.com",
    "Fatima Ahmed,Saudi Arabia,Arab,Architect,fatima.ahmed@example.com",
    "Carlos Silva,Brazil,Latino,Chef,carlos.silva@example.com",
    "Yuki Tanaka,Japan,Asian,Scientist,yuki.tanaka@example.com"
]

# Create file with 100k lines and 90% duplication
with open("input.txt", "w") as f:
    f.write("Name,Country,Ethnicity,Job,Email\n")  # Header
    for _ in range(100000):
        # 90% chance to pick a duplicate entry
        if random.random() < 0.9:
            f.write(random.choice(entries) + "\n")
        else:
            # Generate a slightly different entry for variety
            f.write(f"Random Person,Unknown,Unknown,Unknown,random{random.randint(1, 10000)}@example.com\n")

print("input.txt with 100,000 lines created.")
