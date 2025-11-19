# Define a class called Pet, which will represent any kind of pet
class Pet:
    # The __init__ method runs automatically when a new Pet object is created
    # It sets up the pet's name, species, and happiness level
    def __init__(self, name, species, happiness):
        self.name = name          # Store the pet's name
        self.species = species    # Store the pet's species type
        self.happiness = happiness  # Store the initial happiness value

    # This method introduces the pet by printing its name and species
    def introduction(self):
        print("Hi my name is ", self.name)
        print("I am a", self.species)

    # This method simulates feeding the pet
    # Feeding increases happiness by 10
    def feed(self):
        self.happiness = self.happiness + 10  # Increase happiness
        print(self.name, "is eating! Yum!")
        print("Happiness is now: ", self.happiness)

    # This method simulates touching/petting the pet
    # Petting increases happiness by 15
    def touch(self):
        self.happiness = self.happiness + 15  # Increase happiness
        print(self.name, "is happier! Yay!")
        print("Happiness is now: ", self.happiness)


# Create a Pet object named Alex (a German Shepherd) with happiness 10
dog = Pet("Alex", "German Shepherd", 10)

# Create a Pet object named Sarah (a Siamese cat) with happiness 20
cat = Pet("Sarah", "Siamese cat", 20)

# Call the dog's methods: introduction, feeding, and touching
dog.introduction()
dog.feed()
dog.touch()

print("\n")  # Print a blank line to separate outputs

# Call the cat's methods: introduction, feeding, and touching
cat.introduction()
cat.feed()
cat.touch()
