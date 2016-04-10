import java.math.BigInteger;

public class C {
	private static final int LIMIT = 100000000;
	public static void main(String args[]){
		int N = Integer.parseInt(args[1]);
		int J = Integer.parseInt(args[2]);
		System.out.println("Case #1:");
		long a = (1L<<N-1)+1;
		boolean[] composite = new boolean[LIMIT];
		for(int i=2;i<LIMIT;i++){
			if(composite[i]) continue;
			for(int j=2;i*j<LIMIT;j++){
				composite[i*j] = true;
			}
		}
		while(J>0){
			//check
			boolean valid = true;
			BigInteger[] divisors = new BigInteger[11];
			for(int b=2;b<=10;b++){
				BigInteger test = new BigInteger(Long.toString(a,2),b);
				boolean prime = true;
				for(int i=2;i<LIMIT&&new BigInteger(i+"").pow(2).compareTo(test)<0;i++){
					if(composite[i]) continue;
					if(test.mod(new BigInteger(i+"")).equals(BigInteger.ZERO)){
						prime = false;
						divisors[b] = new BigInteger(i+"");
						break;
					}
				}
				if(!prime) continue;
				for(BigInteger i=new BigInteger(LIMIT+"");i.multiply(i).compareTo(test)<0;i=i.add(BigInteger.ONE)){
					if(test.mod(i).equals(BigInteger.ZERO)){
						prime = false;
						divisors[b] = i;
						break;
					}
				}
				if(prime){
					valid = false;
					break;
				}
			}
			if(valid){
				J--;
				System.out.println(Long.toString(a,2)+" "+divisors[2]+" "+divisors[3]+" "+divisors[4]+" "+divisors[5]+" "+divisors[6]+" "+divisors[7]+" "+divisors[8]+" "+divisors[9]+" "+divisors[10]);
			}
			//increment
			for(int i=1;;i++){
				a ^= (1L<<i);
				if(((a&(1L<<i))>>i)==1L){
					break;
				}
			}
		}
	}
}
