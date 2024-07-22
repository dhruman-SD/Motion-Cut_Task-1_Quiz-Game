# Quiz Game

print("Welcome to the Quiz Game!")

score = 0

# Question 1
print("\nQuestion 1: What is the process by which water moves through a plant, from the roots to the leaves, and is then released into the air as water vapor?")
print("A) Respiration")
print("B) Photosynthesis")
print("C) Transpiration")
print("D) Evaporation")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "C":
    print("Excellent! Transpiration is the process by which water moves through a plant, from the roots to the leaves, and is then released into the air as water vapor.")
    score += 1
elif answer in ["A", "B", "D"]:
    print("Nice try! The correct answer is C) Transpiration. Respiration is the process of breathing, Photosynthesis is the process of converting light energy into chemical energy, and Evaporation is the process of liquid turning into gas.")
else:
    print("Error: Invalid input. Please enter A, B, C, or D.")

# Question 2
print("\nQuestion 2: Which of the following scientists is credited with the discovery of gravity?")
print("A) Galileo Galilei")
print("B) Isaac Newton")
print("C) Albert Einstein")
print("D) Leonardo da Vinci")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "B":
    print("Excellent! Isaac Newton is credited with the discovery of gravity and formulated the laws of motion.")
    score += 1
elif answer in ["A", "C", "D"]:
    print("Nice try! The correct answer is B) Isaac Newton. Galileo Galilei made significant contributions to the study of motion, Albert Einstein developed the theory of relativity, and Leonardo da Vinci was a Renaissance polymath.")
else:
    print("Error: Invalid input. Please enter A, B, C, or D.")

# Question 3
print("\nQuestion 3: What is the largest planet in our solar system?")
print("A) Earth")
print("B) Saturn")
print("C) Jupiter")
print("D) Uranus")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "C":
    print("Excellent! Jupiter is the largest planet in our solar system, with a diameter of over 89,000 miles.")
    score += 1
elif answer in ["A", "B", "D"]:
    print("Nice try! The correct answer is C) Jupiter. Earth is the third planet from the sun, Saturn is a gas giant, and Uranus is an ice giant.")
else:
    print("Error: Invalid input. Please enter A, B, C, or D.")

# Question 4
print("\nQuestion 4: Which of the following types of rocks is formed from the cooling and solidification of magma or lava?")
print("A) Igneous")
print("B) Sedimentary")
print("C) Metamorphic")
print("D) Foliated")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "A":
    print("Excellent! Igneous rocks are formed from the cooling and solidification of magma or lava.")
    score += 1
elif answer in ["B", "C", "D"]:
    print("Nice try! The correct answer is A) Igneous. Sedimentary rocks are formed from the accumulation of sediments, Metamorphic rocks are formed from the alteration of existing rocks, and Foliated rocks are a type of Metamorphic rock.")
else:
    print("Error: Invalid input. Please enter A, B, C, or D.")

# Question 5
print("\nQuestion 5: What is the process by which an organism's genetic information is passed from one generation to the next?")
print("A) Mutation")
print("B) Genetic Drift")
print("C) Gene Expression")
print("D) Heredity")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "D":
    print("Excellent! Heredity is the process by which an organism's genetic information is passed from one generation to the next.")
    score += 1
elif answer in ["A", "B", "C"]:
    print("Nice try! The correct answer is D) Heredity. Mutation is a change in an organism's DNA, Genetic Drift is the random change in the frequency of a gene, and Gene Expression is the process by which genetic information is converted into a trait.")
else:
    print("Error: Invalid input. Please enter A, B, C, or D.")

# Question 6
print("\nQuestion 6: Which of the following technologies is used to store and retrieve data in a computer?")
print("A) CPU")
print("B) RAM")
print("C) Hard Drive")
print("D) Motherboard")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "C":
    print("Excellent! A Hard Drive is a type of non-volatile storage device that is used to store and retrieve data in a computer.")
    score += 1
elif answer in ["A", "B", "D"]:
    print("Nice try! The correct answer is C) Hard Drive. CPU stands for Central Processing Unit, RAM stands for Random Access Memory, and Motherboard is the main circuit.")
else:
    print("Error: Invalid input. Please enter A, B, C, or D.")

# Display final score
print("\nThanks for attempting the quiz.")
print("Your final score is:", score, "out of 6")
