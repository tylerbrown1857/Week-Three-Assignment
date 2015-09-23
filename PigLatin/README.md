##Simple Pig Latin

NOTE: There is no "default" python file for this code. You'll need to create a new python file and add your code. Make sure to add the file to the git repository. (git add .)

###Specs
Write a program to the following specifications:  
1. The program should prompt the user to enter an English word to translate.  
2. The program should translate the word in to Simple Pig Latin, given the following rules.  
3. The program should print the translated word.

**The rules for Simple Pig Latin (this version)**

>If a word begins with a vowel, append 'yay' to the end of the word.  
>If a word begins in a consonant, remove the first letter and append it to the end of the word. Finally, append 'ay' to the end of the word.  


Remember that you can *slice* a word with [ ]

* Create a framework of comments for each step in the specification.  
* Create a variable to hold the original word.  
* Create a variable to hold the translated word and Initialize it with an empty string ""  
* Create a variable to hold the first letter of the original word.  
* Test the first letter to see if it is a vowel or consonant. *See How To*  
	* If the first letter is a vowel, add the original word + "yay" to the translated word.    
	* Else, add all the remaining characters in the word to the translated word, + the first letter, + "ay" to get your translated word.  
* Test your program with the following words:
	1. yello
	2. hello
	3. awesome
	4. scratch
* Extra Credit: There is a problem with this program when it comes to case sensitivity.  Think about how to solve that problem, add it to your code and add a comment indicating how you solved it.

###How to test for a vowel

You'll need to know how to write an if/else statement. 
You'll need to know how to use the "in" conditional.   
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
	word = "hello"
	if word[0] in vowels :
		print ("This word starts with a vowel")
	else :
		print ("This word starts with a consonant")
		