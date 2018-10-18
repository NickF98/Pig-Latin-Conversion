def convertToPigLatin (wordToSearch): # converts the word into Pig Latin based on the rules of Pig Latin
	vowels = ["a", "e", "i", "o", "u", "y"]
	vowelIndex = 0
	for letter in wordToConvert:
			if letter in vowels:
				vowelIndex =  wordToConvert.index(letter)
	if vowelIndex > 0:
		return wordToConvert[vowelIndex:] + wordToConvert[:vowelIndex] + "ay"
	else:
		return wordToConvert + "yay"

# The program takes the text file of the path given by the user and converts 
# each word to pig latin, writing the translated text to a new file named "output.txt"

fileName = input("Enter the path of your file to be translated: ")
normalText = open(fileName, "r")
pigLatinText = open("output.txt", "w")
for line in normalText:
	convertedWords = []
	for word in line.split(" "):
		if "\n" not in word:
			wordToConvert = word
			hasNewLine = False
		else:
			wordToConvert = word[:-2]
			hasNewLine = True
		if not hasNewLine:
			convertedWords += [convertToPigLatin(word)]
		else:
			convertedWords += [(convertToPigLatin(word) + "\n")]
	pigLatinText.write(" ".join(convertedWords))
		
pigLatinText.close()
normalText.close()


