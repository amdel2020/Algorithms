using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Monk_watching_fight
{
    class Program
    {        
        static void Main(string[] args)
        {
            var r = new StreamReader("i.txt");
            var num = long.Parse(r.ReadLine());
            var elements = ("-1 " + r.ReadLine()).Trim().Split(' ').Select(long.Parse).ToArray();

            var root = new Node(elements[1])
            {
                Depth = 1
            };

            for (var i = 2; i <= num; i++)
            {
                Insert(elements[i], root);
            }

            var maxDepth = FindMaxDepth(root);

            Console.WriteLine(maxDepth);

            // InorderTraversal(root);

            Console.ReadLine();
        }

        static void InorderTraversal(Node root)
        {
            if (root.Left != null) InorderTraversal(root.Left);
            Console.Write(root.Value + " ");
            if (root.Right != null) InorderTraversal(root.Right);
        }

        static void Insert(long element, Node node)
        {
            var newNode = new Node(element);
            newNode.Depth = 1 + node.Depth;

            if (element <= node.Value)
            {
                if (node.Left == null)
                {
                    node.Left = newNode;
                    return;
                }
                Insert(element, node.Left);
            }
            else
            {
                if (node.Right == null)
                {
                    node.Right = newNode;
                    return;
                }
                Insert(element, node.Right);
            }
        }

        static long FindMaxDepth(Node root)
        {
            long maxDepth = 0;

            Queue<Node> queue = new Queue<Node>();

            queue.Enqueue(root);

            while (queue.Count > 0)
            {
                var current = queue.Dequeue();

                if (maxDepth < current.Depth) maxDepth = current.Depth;

                if (current.Left != null) queue.Enqueue(current.Left);

                if (current.Right != null) queue.Enqueue(current.Right);

            }

            return maxDepth;

        }

        class Node
        {
            public long Value { get; set; }

            public Node Left { get; set; }

            public Node Right { get; set; }

            public long Depth { get; set; }

            public Node(long value)
            {
                this.Value = value;
            }
        }
    }
}
