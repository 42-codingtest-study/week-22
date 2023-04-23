package b1_15947;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		
		int a = s.nextInt();
		int b = a % 14;
		
		switch(b) {
		case 1:case 13: System.out.print("baby "); break;
		case 2:case 0: System.out.print("sukhwan "); break;
		case 5: System.out.print("very "); break;
		case 6: System.out.print("cute "); break;
		case 9: System.out.print("in "); break;
		case 10: System.out.print("bed "); break;
		case 3:case 7:case 11:
		
			System.out.print("tu");
			if((a / 14) >= 3) {
				System.out.printf("+ru*%d", a/14 + 2);
				break;
			}
			
			for(int i = 0; i < a/14 +2; i++) {
				System.out.print("ru");
			}
			break;
		
		case 4:case 8:case 12:
		
			System.out.print("tu");
			if((a / 14) > 3) {
				System.out.printf("+ru*%d", a/14 + 1);
				break;
			}
			
			for(int i = 0; i < a/14 +1; i++) {
				System.out.print("ru");
			}
			System.out.print("\n");
			break;
		
		default: break;		
		
		}
		
	}

}
