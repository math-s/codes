package icapui;
import java.util.Scanner;

public class MatrixFunctions {
	  
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
	
	static String seeMatrix(int x[][]) {
		String c = "";
		for (int i=0 ; i<x[0].length ; i++) {
			for (int j=0 ; j<x.length ; j++) {				
				c =  c + String.valueOf(x[i][j]);			
			}
		c = c + "\n";
		}
		return c;
	}
	
	static int[][] buildMatrix(int x, int y) {
		
		Scanner  var = new Scanner(System.in);
		int[][] c = new int[x][y];
		for (int i=0 ; i<x ; i++) {
			for (int j=0 ; j<y ; j++) {				
				c[i][j] = var.nextInt();		
			}
		}
		return c;
	}
	
	public static void main(String[] args) {
		Scanner  var = new Scanner(System.in);
		//int x = var.nextInt();
		//int y = var.nextInt();
		//System.out.println("Digite os campos da matriz");
		int[][] a = {{1, 1, 1, 1},{2, 2, 2, 2},{3, 3, 3, 3},{4, 4, 4, 4}};
		//int[][] b = buildMatrix(x,y);
		System.out.println(seeMatrix(a));
		//System.out.println(seeMatrix(b));
		//Scanner.close();
	}
}
