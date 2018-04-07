using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CheckPermutation
{
    class Program
    {
        static void Main(string[] args)
        {
            string testInput1 = "zxcvbnmasdfghjklqwertyuiop";
            string testInput2 = "zxcvbnmasdfghjklqwertyuiop";

            Console.WriteLine("Check Permutation Succeed? : " + CheckPermutation_UsingSort(testInput1, testInput2));

            Console.ReadLine();
        }

        // Check if one string is permutation of other string.

        // 1. if(x.length == y.length) proceed, else false
        // 2. Sort two string => O(nlogn)
        // 3. Scan two string simultaneously => O(n)
        // 4. Final result in O(nlogn) time
        private static bool CheckPermutation_UsingSort(string firstInput, string secondInput)
        {
            throw new NotImplementedException();
        }

        // 1. if(x.length == y.length) proceed, else false
        // 2. Assume ASCII set and Initialize integer array.
        // 3. Scan two strings and find character counts in each string => O(2n)
        // 4. Final result in O(n) time by comparing the count of each integer array.
        private static bool CheckPermutation_UsingCharacterCount(string firstInput, string secondInput)
        {
            throw new NotImplementedException();
        }
    }
}
