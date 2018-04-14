using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UndirectedGraph;

namespace BreadtFirstSearch
{
    class Program
    {
        static void Main(string[] args)
        {
            UndirectedGraph<int> graph = new UndirectedGraph<int>();
            graph.AddVertex(2);
            graph.AddVertex(5);
            graph.AddVertex(7);
            graph.AddVertex(8);
            graph.AddVertex(23);
            graph.AddVertex(12);

            graph.AddEdge(2, 5);
            graph.AddEdge(7, 5);
            graph.AddEdge(23, 12);
            graph.AddEdge(12, 2);
            graph.AddEdge(8, 7);

            var bfsTraversal = BFS.BreadthFirstSearch(graph, 2);
            Console.Write("Breadth first traversal: ");
            foreach (var item in bfsTraversal)
            {
                Console.Write(item + " ");
            }
            Console.ReadLine();
        }
    }
}
