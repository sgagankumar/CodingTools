package timeComplexityBreaker;
import java.util.Scanner;

public class GeneralSplitter 
{
	public static void normalfunc(double num)
	{
		System.out.print(num+" ");
	}
	public static void rangefunc(double num)
	{
		System.out.println("\n"+num+" to "+(num+10));
		switch((int)num)
		{
			case 1://Enter range 1 value
				break;
			case 2://Enter range 2 value
				break;
			case 3://Enter range 3 value
				break;
			case 4://Enter range 4 value
				break;
			case 5://Enter range 5 value
				break;
			//Create more ranges
			default:break;
		}
	}
	public static void func(double lowerlimit,double upperlimit, double range)
	{
		double number=lowerlimit;
		double left=0;
		double right=range;
		while(number<upperlimit)
		{
			//System.out.prdoubleln("num="+num+" left="+left+" right="+right+" upperlimit="+upperlimit+" lowerlimit="+lowerlimit);
			if(number<left)
			{	
				for(double i=number;i<left;i++)
				{
					//System.out.println(i);
					normalfunc(i);
					number++;
				}
			}
			else if(number==left && upperlimit>right)
			{
				rangefunc(number);
				number=number+range;
				left=right;
				right+=range;
			}
			else if(number==left && upperlimit<right)
			{
				for(double i=number+1;i<=upperlimit;i++)
				{
					//System.out.println(i);
					normalfunc(i);
					number++;
				}
			}
			else
			{
				left=right;
				right+=range;
			}
		}
	}
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter lower and upper limit");
		double ll=sc.nextDouble();
		double ul=sc.nextDouble();
		func(ll,ul,10);
		sc.close();
	}
	
	
}
