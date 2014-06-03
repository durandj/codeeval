import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main
{
	public static boolean getBit(int x, int p)
	{
		return (x & 1 << p - 1) >> p - 1 == 1;
	}

	public static void main(String args[])
	{
		File file = new File(args[0]);

		try
		{
			Scanner scanner = new Scanner(file);
			while (scanner.hasNextLine())
			{
				String line = scanner.nextLine();
				if (line.equals(""))
					continue;

				String tokens[] = line.split(",");
				int x  = Integer.parseInt(tokens[0]),
					p0 = Integer.parseInt(tokens[1]),
					p1 = Integer.parseInt(tokens[2]);

				System.out.println(Main.getBit(x, p0) == Main.getBit(x, p1));
			}

			scanner.close();
		}
		catch (IOException e)
		{
		}
	}
}

