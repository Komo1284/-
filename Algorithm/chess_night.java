package practice;

public class ex01 {
	
	static void printBoard(int x, int y) {
		
		int count = 0;
		
		for(int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				if(i == x && j == y) {
					System.out.print("■ ");
				} 
				else if ((i == x+2) && (j == y+1)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x+2) && (j == y-1)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x-2) && (j == y+1)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x-2) && (j == y-1)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x+1) && (j == y+2)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x+1) && (j == y-2)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x-1) && (j == y+2)){
					System.out.print("♠ ");
					count++;
				}
				else if ((i == x-1) && (j == y-2)){
					System.out.print("♠ ");
					count++;
				}
				else {
					System.out.print("□ ");
				}
				
			}System.out.println();
		}
		
		System.out.println("count = " + count);
		
	}
	
	public static void main(String[] args) {
		
		char z = 'A';
		int x = 0,y = 0;
		String location = "A7";
		
		
		
		for(int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				String point = "";
				point += (char)(z+i);
				point += j+1;
				if(point.equals(location)) {
					x = -1 * (j-7);
					y = i;
				}
			}
		}
		System.out.printf("%d, %d", y,x);
		System.out.println();
		printBoard(x,y);

		
	}
}
