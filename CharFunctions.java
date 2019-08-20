package icapui;

import javax.swing.*;

public class CharFunctions {

	static char[] midcharvec(String word ) {
		 char[] mid = word.toCharArray();
		 int x = mid.length;		
			 if(x%2 == 0) {
				 char[] ans = {midchar("0" + word), midchar(word + "0")};
				 return ans;
			 }else {
				 char[] result = {midchar(word)}; 
				 return result;
			 }	 
	  }
	
	static char midchar(String word) {
		char[] mid = word.toCharArray();
		int x = mid.length;		
		x = (x/2);
		return mid[x];
	}
	
}
