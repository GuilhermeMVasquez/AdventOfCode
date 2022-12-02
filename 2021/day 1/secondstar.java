import java.io.File;
import java.util.Scanner;

public class secondstar
{
    public static void main(String[]args)
    {
        int input_len = 2000;

        int[] input = new int[input_len];

        try
        {
            File arq = new File("input.txt");

            Scanner sc = new Scanner(arq);

            for(int i = 0; i < input.length; i++)
            {
                input[i] = sc.nextInt();
            }

            sc.close();
        }
        catch(Exception e)
        {
            System.out.println("Error");
        }

        int count = 0;

        for(int i = 0; i + 3 < input_len; i++)
        {
            int windowA = input[i] + input[i+1] + input[i+2];

            int windowB = input[i+1] + input[i+2] + input[i+3];

            if(windowB > windowA)
            {
                count++;
            }
        }

        System.out.println(count);
    }
}