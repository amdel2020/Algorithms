using System;
using System.Diagnostics;

namespace _01IsUnique
{
    class Program
    {
        static void Main(string[] args)
        {
            string testInput = "zxcvbnmasdfghjklqwertyuiop";

            Console.WriteLine("All characters in the string unique?: " + IsUnique_BruteForce(testInput));

            Console.ReadLine();
        }

        // Determine if the string has all unique character. Cannot use additional data structure

        // 1. Brute-force
        // 2. Take one character and compare with all the other
        // 3. Repeat the process for all the characters.
        // 4. O(n2)
        private static bool IsUnique_BruteForce(string input)
        {
            bool isUnique = true;

            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            for (int i = 0; i < input.Length; i++)
            {
                for (int j = i + 1; j < input.Length; j++)
                {
                    if(input[i] == input[j])
                    {
                        isUnique = false;
                        break;
                    }
                }
            }

            stopwatch.Stop();
            Console.WriteLine("Time taken in ticks: " + stopwatch.ElapsedTicks);

            return isUnique;
        }

        // 1. Better-way
        // 2. Suppose ASCII set
        // 3. Total possible characters - 128 (starting from 0)
        // 4. If length of the input string > 128 == means duplicate characters
        // 5. If step 4 is not true, then create boolean array of size 128. 
        // 6. All initial value in the array is false.
        // 7. Start scanning the array one character at a time
        // 8. As you scan each characters, set that value(equal to some index) true in boolean array.
        // 9. If anytime, any value in the boolean array is true, means duplicate found.
        // 10. Implementation is very easy.
        private static bool IsUnique_BetterWay(string input)
        {
            throw new NotImplementedException();
        }
    }
}
