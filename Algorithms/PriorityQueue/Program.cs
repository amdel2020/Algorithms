using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinaryHeaps
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryHeap<int> heap = new BinaryHeap<int>();
            heap.Insert(10);
            heap.Insert(20);
            heap.Insert(30);
            heap.Insert(5);
            heap.Insert(6);
            heap.Insert(60);
            heap.Insert(57);
            heap.Insert(34);
            heap.Insert(59);
            heap.Insert(67);

            Console.WriteLine("Max element in the heap: " + heap.GetMaximumElement());
            Console.WriteLine("Left child of root: " + heap.LeftChild(0));
            Console.WriteLine("Right child of root: " + heap.RightChild(0));

            Console.ReadLine();
        }
    }
}
