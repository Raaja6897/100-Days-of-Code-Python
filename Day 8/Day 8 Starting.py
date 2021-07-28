# Simple Function
def greet():
    print("Hi")
    print("How are you")
    print("How is your day")

# Function that allows input

def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How are you {name}")
    print(f"How is your day {name}")

# Function that allows two input

def welcome(first_name, last_name):
    full_name=first_name+ ' ' +last_name
    print(f"Hi {full_name}")
    print((f"How are you {full_name}"))


# Key word Argument
welcome(last_name="Vignesh", first_name="Raaja")