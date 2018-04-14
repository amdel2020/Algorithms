using System;
using UndirectedGraph;

namespace DepthFirstSearch
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

            Console.WriteLine("Number of vertex: {0}", graph.NumberOfVertices);
            Console.WriteLine("Number of edges: {0}", graph.NumberOfEdges);

            var dfsTraversal = DFS.DepthFirstSearch(graph, 2);
            Console.Write("Depth first traversal: ");
            foreach (var item in dfsTraversal)
            {
                Console.Write(item + " ");
            }
            Console.ReadLine();
        }        
    }
}
