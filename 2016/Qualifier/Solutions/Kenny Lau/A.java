public class A {
	public static void main(String args[]){
		for(int a=1;a<args.length;a++){
			int each = Integer.parseInt(args[a]);
			int current = 0;
			boolean[] f = new boolean[10];
			if(each == 0){
				System.out.println("Case #"+a+": "+"INSOMNIA");
			}else{
				boolean done = true;
				do{
					current += each;
					String s = String.valueOf(current);
					for(int i=0;i<s.length();i++){
						f[s.charAt(i)-'0'] = true;
					}
					done = true;
					for(int i=0;i<10;i++){
						if(!f[i]){
							done = false;
							break;
						}
					}
				}while(!done);
				System.out.println("Case #"+a+": "+current);
			}
		}
	}
}
