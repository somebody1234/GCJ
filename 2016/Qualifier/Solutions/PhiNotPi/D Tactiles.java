import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;


public class Tactiles {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner in = new Scanner(new File("D-small-attempt0.in"));
		PrintWriter out = new PrintWriter(new File("FractranSmOut.txt"));
		long numTests = in.nextLong();

		for (long test = 0; test < numTests; test++) {
			in.nextLine();
			long K = in.nextLong();
			long C = in.nextLong();
			long S = in.nextLong();
			ArrayList<Long> res = new ArrayList<Long>();
			if (C == 1){
				if(S >= K){
					for(long i = 1; i <= K; i++){
						res.add(i);
					}
				}
			}
			else{
				if(S >= (K/2)+(K%2)){
					long jump = 1;
					for(int i = 1; i < C; i++){
						jump *= K;
					}
					long pos = 2;
					while(res.size() < S && pos <= jump*K){
						res.add(pos);
						pos += (jump+1)*2;
					}
					if((K%2)==1 && res.size() < S){
						res.add(jump*K);
					}
				}
			}
			
			out.print("Case #" + (test+1) + ":");
			if(res.size() > 0){
				for(long i : res){
					out.print(" "+i);
				}
				out.println();
			}
			else {
				out.println(" IMPOSSIBLE");
			}
		}
		out.close();
		in.close();
	}

}
