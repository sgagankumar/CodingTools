package timeComplexityBreaker;
import java.util.Scanner;

public class Spliter 
{
	public static void func(int ll,int ul)
	{
		int num=ll;
		int left=0;
		int right=10;
		while(num<ul)
		{
			System.out.println("num="+num+" left="+left+" right="+right+" ul="+ul+" ll="+ll);
			if(num<left)
			{	
				System.out.println("bp1");
				for(int i=num;i<left;i++)
				{
					System.out.println(i);
					num++;
				}
			}
			else if(num==left && ul>right)
			{
				System.out.println("bp2");
				System.out.println((left+1) +"to"+ right);
				num=num+10;
				left=right;
				right=right+10;
			}
			else if(num==left && ul<right)
			{
				System.out.println("bp3");
				for(int i=num+1;i<=ul;i++)
				{
					System.out.println(i);
					num++;
				}
			}
			else
			{
				System.out.println("bp4");
				left=right;
				right=right+10;
			}
		}
	}
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter lower and upper limit");
		int ll=sc.nextInt();
		int ul=sc.nextInt();
		func(ll,ul);
		sc.close();
	}
	
	
}
