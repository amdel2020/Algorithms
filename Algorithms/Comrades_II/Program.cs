using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Comrades_II
{
    class Program
    {
        static void Main(string[] args)
        {
            var reader = new StreamReader("input.txt");
            // int tests = int.Parse(Console.ReadLine());
            int tests = int.Parse(reader.ReadLine());

            for (int test = 0; test < tests; test++)
            {
                // int soldiers = int.Parse(Console.ReadLine());
                int soldiers = int.Parse(reader.ReadLine());

                // string[] parents = Console.ReadLine().Split(' ');
                string[] parents = reader.ReadLine().Trim().Split(' ');

                // Total Handshakes
                int hs = 0;

                // Total BumpFists
                int bf = 0;

                // Construct a tree given its parents array.
                NaryTree tree = new NaryTree();
                tree.CreateTreeFromParents(parents);

                // For each node starting from root:
                Queue<NaryTreeNode> queue = new Queue<NaryTreeNode>();
                queue.Enqueue(tree.root);

                while (queue.Count > 0)
                {
                    NaryTreeNode currentNode = queue.Dequeue();

                    // bf = bf + total siblings on the right
                    bf = bf + tree.RightSiblingsCount(currentNode);

                    // Enqueue all the children of current node.
                    foreach (var child in currentNode.children)
                        queue.Enqueue(child);
                }

                // total handshakes
                hs = tree.TotalChildren();

                Console.WriteLine(hs + " " + bf);
            }

            Console.ReadLine();
        }
    }

    class NaryTree
    {
        private NaryTreeNode[] created;

        public NaryTreeNode root;

        public void CreateTreeFromParents(string[] parents)
        {
            int length = parents.Length;
            created = new NaryTreeNode[length + 1];
            int j = 0;

            for (int i = 1; i <= length; i++)
            {
                int parent = int.Parse(parents[j++]);

                if (created[i] == null)
                    created[i] = new NaryTreeNode(i);

                if (parent == 0)
                {
                    root = created[i];
                    continue;
                }

                if (created[parent] == null)
                    created[parent] = new NaryTreeNode(parent);

                created[i].parent = created[parent];
                created[i].parent.descendantsCount += 1 + created[i].descendantsCount;

                created[parent].children.Insert(created[parent].children.Count, created[i]);
            }

            // Update the descendants


            created = null;
        }

        public int RightSiblingsCount(NaryTreeNode node)
        {
            if (node.parent != null)
            {
                var c = node.parent.children;
                var i = c.IndexOf(node);
                var l = (c.Count - 1) - i;
                return l;
            }

            return 0;
        }

        public int TotalChildren()
        {
            Queue<NaryTreeNode> q = new Queue<NaryTreeNode>();
            q.Enqueue(root);
            int handShakes = 0;

            while (q.Count > 0)
            {
                var currentNode = q.Dequeue();
                handShakes += currentNode.descendantsCount;

                foreach (var child in currentNode.children)
                    q.Enqueue(child);
            }
            return handShakes;
        }
    }

    class NaryTreeNode
    {
        public int value;

        public int descendantsCount;

        public NaryTreeNode parent;

        public List<NaryTreeNode> children;

        public NaryTreeNode(int value)
        {
            this.value = value;
            children = new List<NaryTreeNode>();
        }
    }
}
