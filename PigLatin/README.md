##Igpay Atinlay

OK, so here is the second lab for the week.  

Write a program to the following specifications:
1. The program should prompt the user to enter an English word to translate into Pig Latin
1. The program should translate the word in to Pig Latin, given the following rules:  
1. The program should print the translated word.

The rules for Pig Latin (this version)

If a word begins with a vowel, append 'yay' to the end of the word.  
If a word begins in a consonant, remove all the consonants from the beginning of the word, 
up to the first vowel, and append them to the end of the word. Finally, append 'ay' to the end of the word.  


Divide and conquer should be your approach to handling this lab. 

Create a framework of comments for each step. 
Loop through each letter of the word. (This sounds like a job for **For Each Loop**)

Test the letter to see if it is a vowel or consonant. *See hints*  
If the first letter is a vowel, you're done! Append "yay" to the word to get your pig latin word.  
If not, keep a record of each letter until you hit a vowel.  
Add together the rest of the word, the saved letters, and "ay" to get your pig latin word.


Build a new word, starting with an empty string "" and appending characters as needed.

###How to test for a vowel

You'll need two new statements. The "in" test, and the if/else statement.  
Here is the format for the "IF" statement.  

	if (condition is true) :  
	   do something  
	   do something more  
	   
	else:  
	   do something else  
	   do more something else  
	   
	Continue with program

To test if a letter is a vowel or not, create a variable called vowels = "aeiou". You can then check if a letter is a vowel with "in".  

	vowels = "aeiou"
	word = "Hello"
	if word[0] in vowels :
		print ("This word starts with a vowel")
	else :
		print ("This word starts with a consonant")
		