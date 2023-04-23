package b1_23278;
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int j = 0;
		int N = s.nextInt(), L = s.nextInt(), H = s.nextInt();
		ArrayList<Integer> score = new ArrayList<Integer>();
		score.add(s.nextInt());
		for(int i = 1; i < N; i++) {
			int nextscore = s.nextInt();
			
			if(nextscore >= score.get(i - 1))
				score.add(nextscore);
			else
				for(j = 0; j<i; j++) {
					if(score.get(j) >= nextscore) {
						score.add(j, nextscore);
						break;						
					}
				}
		}/*
		for(j = N-1; j > N - H -1; j--) {
			score.remove(j);
		}
		for(j = 0; j < L; j++) {
			score.remove(j);
		}
		int sum = 0;
		for(j = 0; j < score.size(); j++) {
			sum += score.get(j);
		}
		System.out.print((double)sum / score.size());
		*/
		//System.out.print(score.subList(0+L, N-H).toString());
		int sum = 0;
		for (int i = 0; i < score.subList(0+L, N-H).size() ; i++) {
            sum += score.subList(0+L, N-H).get(i);
        }

		System.out.println((double)sum / score.subList(0+L, N-H).size());

	}

}
