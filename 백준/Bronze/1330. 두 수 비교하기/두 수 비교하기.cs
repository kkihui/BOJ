using System;

namespace BOJ
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            string[] numbers = input.Split(' ');

            int a = int.Parse(numbers[0]); 
            int b = int.Parse(numbers[1]);

            if (a < b)
                Console.WriteLine('<');
            else if (a > b)
                Console.WriteLine('>');
            else
                Console.WriteLine("==");

        }
    }
}
