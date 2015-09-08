import java.util.*;
import java.io.*;

/*
************************************************
  ____ ____    _  ___   __   
 / ___/ ___|  / |/ _ \ / /_  
| |   \___ \  | | (_) | '_ \ 
| |___ ___) | | |\__, | (_) |
 \____|____/  |_|  /_/ \___/ 
                             

Problem set 1


Question 1

A common problem in computer science is finding patterns within data. 
This problem will simulate that in a way that is easy to see what is happening.

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
Allowances may be made for adjustments to capital letters, punctuation, and word dividers.

an anagram is a word, phrase, or name formed by rearranging the letters of another.


Given a String S, determine if it is an anagram of a palindrome. 
Return true if the String is an anagram of a palindrome, and false otherwise. 

PLEASE LOOK AT PS1.txt FOR MORE DETAILS!!!

************************************************

*/

public class Anagram {


	
	public static boolean anagram(String input) {
		
		//count for occurance of all chars from input
		int[] occurance=new int[26];
		//get length
		int inputLength=input.length();
		//get occurance
		for(int i = 0;i<inputLength;i++){
			char ch=input.charAt(i);
			occurance[ch - 'a']++;
		}


		//input_length==even or odd
		if (inputLength%2==0){
			//even
			for(int k = 0;k<occurance.length;k++){

				//odd=false
				if(occurance[k]%2==1){
					 return false;
				}
			}
			return true;

		}else{
			//odd
			int count=0;
			for(int k = 0;k<occurance.length;k++){
				if(occurance[k]%2==1){
					count++;
					//odd==2 means false
					if(count==2){
						return false;
					}
				}
			}
			return true;

		}

	}

	

	public static void main(String[] args) {
		File file = new File("Anagram.txt");
		try {
			Scanner scan = new Scanner(file);
			int numberOfCases = scan.nextInt();
			for(int i = 0; i < numberOfCases; i++) {
				String input = scan.next();
				System.out.println(anagram(input));
			}
			scan.close();
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
}