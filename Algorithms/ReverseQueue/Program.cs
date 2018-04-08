using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ReverseQueue
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<int> queue = new Queue<int>();
            queue.Enqueue(10);
            queue.Enqueue(20);
            queue.Enqueue(30);
            queue.Enqueue(40);
            queue.Enqueue(50);

            Console.Write("Original Queue: ");
            foreach (var item in queue)
            {
                Console.Write(item + " ");
            }

            queue = ReverseQueue(queue);

            Console.WriteLine();
            Console.Write("Reversed Queue: ");
            foreach (var item in queue)
            {
                Console.Write(item + " ");
            }

            Console.ReadLine();
        }

        static private Queue<T> ReverseQueue<T>(Queue<T> inputQueue)
        {
            Stack<T> stack = new Stack<T>();
            Queue<T> reverseQueue = new Queue<T>();

            foreach (var item in inputQueue)
            {
                stack.Push(item);
            }

            foreach (var item in stack)
            {
                reverseQueue.Enqueue(item);
            }

            return reverseQueue;
        }
    }
}
