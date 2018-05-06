using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DirectedGraph
{
    class Program
    {
        static void Main(string[] args)
        {
            DirectedGraph<int> graph = new DirectedGraph<int>();
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
            Console.ReadLine();
        }
    }
}
