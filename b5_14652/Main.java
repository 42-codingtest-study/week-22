package b5_14652;
import java.util.Calendar;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int n = s.nextInt(), m = s.nextInt(), K = s.nextInt();
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				int A = i*m + j;
				if (A == K) {
					System.out.printf("%d %d", i, j);
					break;
				}
			}
		}
	}

}
/*
import java.util.Calendar;

public class MAIN {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calendar now = Calendar.getInstance();
		int year = now.get(Calendar.YEAR);
		int month = now.get(Calendar.MONTH);
		int day = now.get(Calendar.DAY_OF_MONTH);
		System.out.printf("%d\n%d\n%d", year, month, day);
		
	}

}
*/