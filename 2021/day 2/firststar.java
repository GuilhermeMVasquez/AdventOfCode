import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class firststar {
    public static void main(String[]args)
    {
        int size = 1000;

        String[] arr = new String[size];

        try
        {
            File myObj = new File("input.txt");

            Scanner myReader = new Scanner(myObj);

            for (int index = 0; index < arr.length; index++)
            {
                String data = myReader.nextLine();
            
                arr[index] = data;
            }
            
            myReader.close();
        } 
        catch (FileNotFoundException e)
        {
            System.out.println("An error occurred.");
        }
        
        int depth = 0;

        int horizontal = 0;

        for(int i = 0; i < arr.length; i++)
        {
            String placeholder = arr[i];

            String[] separate = placeholder.split(" ");

            if(separate[0].equals("forward"))
            {
                horizontal += Integer.parseInt(separate[1]);
            }

            if(separate[0].equals("up"))
            {
                depth -= Integer.parseInt(separate[1]);
            }

            if(separate[0].equals("down"))
            {
                depth += Integer.parseInt(separate[1]);
            }    
        }  

        System.out.println(depth * horizontal);
    }
}