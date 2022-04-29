# Colton Wade Lab 6

# Opens the two .txt files
first_file = open("first_file.txt", "r")
second_file = open("second_file.txt", "r")

# Creates a set of the Unique Words in first_file
FirstFileSet = set()  # Creates a set
for line in first_file:  # Reads each line in the first_file
    for word in line.split():  # Splits the line into multiple words, instead of a long string
        FirstFileSet.add(word.rstrip(", ."))  # Strips any , or . at the end of each word.

print("--Unique Words in First File--")
for word in FirstFileSet:
    print(word)


# Creates a set of the Unique Words in second_file
SecondFileSet = set()
for line in second_file:
    for word in line.split():
        SecondFileSet.add(word.rstrip(", ."))

print("\n--Unique Words in Second File--")
for word in SecondFileSet:
    print(word)


# Creates a set of the words that appear in Both Files
BothSet = FirstFileSet.intersection(SecondFileSet)   # .intersection command finds words that overlap between sets
print("\n--Words That Appear in Both Files--")
for word in BothSet:
    print(word)


# Creates a set of the words that appear in first_file but not second_file
JustFirst = FirstFileSet.difference(SecondFileSet)  # .difference finds the difference between two sets
print("\n--Words that Appear in Just the First File--")
for word in JustFirst:
    print(word)


# Creates a set of the words that appear in second_file but not first_file
JustSecond = SecondFileSet.difference(FirstFileSet)
print("\n--Words that Appear in Just the Second File--")
for word in JustSecond:
    print(word)


# Creates a set of words that appear in either the first or second file, but not both.
    # symmetric_difference finds the unique elements between two sets
NotBoth = FirstFileSet.symmetric_difference(SecondFileSet)
print("\n--Words That Appear In First/Second, But Not Both--")
for word in NotBoth:
    print(word)


