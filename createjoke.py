import pyjokes

# Function to print a random joke
def random_joke():
    joke = pyjokes.get_joke()
    print(joke)

# Call the function to get a random joke
random_joke()
