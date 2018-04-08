using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace MinimumInStackInConstantTime
{
    class Program
    {
        static void Main(string[] args)
        {
            MinStack minStack = new MinStack();
            minStack.Push(19);
            minStack.Push(20);
            minStack.Push(10);
            minStack.Push(4);
            minStack.Push(19);
            minStack.Push(20);
            minStack.Push(10);
            minStack.Push(4);

            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());

            Console.WriteLine("Updating stack...");
            minStack.Pop();
            Thread.Sleep(1000);
            Console.WriteLine("Current Min in stack: {0}", minStack.Min());


            Console.ReadLine();
        }
    }


    // Wrapper for the stack.
    // This stack class implements getMinimum in stack in 0(1) time
    class MinStack
    {        
        private Stack<int> minStack;

        public Stack<int> mainStack { get; set; }

        public MinStack()
        {
            minStack = new Stack<int>();
            mainStack = new Stack<int>();
        }

        public void Push(int item)
        {
            mainStack.Push(item);
            if (minStack.Count == 0 || item <= minStack.Peek())
            {
                minStack.Push(item);
            }
        }

        public int Pop()
        {
            int topItem = mainStack.Pop();

            if (topItem == minStack.Peek())
            {
                minStack.Pop();
            }
            return topItem;
        }

        public int Min()
        {
            return minStack.Peek();
        }
    }
}
