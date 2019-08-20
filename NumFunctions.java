package icapui;

public class NumFunctions {
	 
	public static void maiorNum(int a, int b, int c){
	    if (a>=b && a>=c){
	    	System.out.println(a);
	    }
	    else if (b>=a && b>=c){
	    	System.out.println(b);
	    }
	    else if (c>=b && c>=a){
	    	System.out.println(c);
	    }
	  }
	  
	public static int bigNum(int x, int y, int z) {
		  int num = 0;
		  if (x >= y && x >= z) {num = x;}
		  if (y >= x && y >= z) {num = y;}
		  if (z >= x && z >= y) {num = z;}
		  return num;
	  }

}
