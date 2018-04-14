using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UndirectedGraph;

namespace DepthFirstSearch
{
    public static class DFS
    {
        public static HashSet<T> DepthFirstSearch<T>(UndirectedGraph<T> graph, T start)
        {
            HashSet<T> visited = new HashSet<T>();
            Stack<T> stack = new Stack<T>();

            if (!graph.AdjacencyList.ContainsKey(start))
            {
                return visited;
            }

            stack.Push(start);

            while (stack.Count > 0)
            {
                var vertex = stack.Pop();

                if (visited.Contains(vertex))
                    continue;

                visited.Add(vertex);

                foreach (var neighbour in graph.AdjacencyList[vertex])
                    if (!visited.Contains(neighbour))
                        stack.Push(neighbour);
            }

            return visited;
        }
    }
}
