using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Quicksort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = GenerateLargeArray();
            // Console.Write("Unsorted array: ");
            // PrintArray(a);
            // Console.WriteLine();
            // QuickSort(a);
            // Insertionsort(a);
            a = CountingSort(a);
            // Console.Write("Sorted array: ");
            // PrintArray(a);
            Console.ReadLine();
        }

        static void QuickSort(int[] a)
        {
            Stopwatch watch = new Stopwatch();
            watch.Start();
            QuickSort(a, 0, a.Length - 1);
            watch.Stop();
            Console.WriteLine("Time taken to sort: " + watch.ElapsedMilliseconds);
        }

        static void QuickSort(int[] a, int start, int end)
        {            
            if (start >= end)
            {
                return;
            }

            int num = a[start];

            int i = start, j = end;

            while (i < j)
            {
                while (i < j && a[j] >= num)
                {
                    j--;
                }

                a[i] = a[j];

                while (i < j && a[i] < num)
                {
                    i++;
                }

                a[j] = a[i];
            }

            a[i] = num;
            QuickSort(a, start, i - 1);
            QuickSort(a, i + 1, end);
        }

        static void Insertionsort(int[] a)
        {
            Stopwatch watch = new Stopwatch();
            watch.Start();
            int i, j;
            int n = a.Length;
            for (i = 1; i < n; i++)
            {
                int item = a[i];
                int ins = 0;
                for (j = i - 1; j >= 0 && ins != 1;)
                {
                    if (item < a[j])
                    {
                        a[j + 1] = a[j];
                        j--;
                        a[j + 1] = item;
                    }
                    else ins = 1;
                }
            }

            watch.Stop();
            Console.WriteLine("Time taken to sort: " + watch.ElapsedMilliseconds);
        }

        static int[] CountingSort(int[] a)
        {
            Stopwatch watch = new Stopwatch();
            watch.Start();
            int[] sortedArray = new int[a.Length];

            // find smallest and largest value
            int minVal = a[0];
            int maxVal = a[0];
            for (int i = 1; i < a.Length; i++)
            {
                if (a[i] < minVal) minVal = a[i];
                else if (a[i] > maxVal) maxVal = a[i];
            }

            // init array of frequencies
            int[] counts = new int[maxVal - minVal + 1];

            // init the frequencies
            for (int i = 0; i < a.Length; i++)
            {
                counts[a[i] - minVal]++;
            }

            // recalculate
            counts[0]--;
            for (int i = 1; i < counts.Length; i++)
            {
                counts[i] = counts[i] + counts[i - 1];
            }

            // Sort the array
            for (int i = a.Length - 1; i >= 0; i--)
            {
                sortedArray[counts[a[i] - minVal]--] = a[i];
            }

            watch.Stop();
            Console.WriteLine("Time taken to sort: " + watch.ElapsedMilliseconds);

            return sortedArray;
        }

        static void PrintArray(int[] a)
        {
            foreach (int item in a)
            {
                Console.Write(item + " ");
            }
        }

        static int[] GenerateLargeArray()
        {
            int[] largeArray = new int[400000000];
            Random random = new Random();

            for (long i = 0; i < largeArray.LongLength; i++)
            {
                largeArray[i] = random.Next(1000);
            }

            return largeArray;
        }
    }
}
