using System.Collections.Generic;
using UndirectedGraph;

namespace BreadtFirstSearch
{
    public static class BFS
    {
        public static HashSet<T> BreadthFirstSearch<T>(UndirectedGraph<T> graph, T start)
        {
            HashSet<T> visited = new HashSet<T>();
            Queue<T> queue = new Queue<T>();

            if (!graph.AdjacencyList.ContainsKey(start))
            {
                return visited;
            }

            queue.Enqueue(start);

            while (queue.Count > 0)
            {
                var vertex = queue.Dequeue();

                if (visited.Contains(vertex))
                    continue;

                visited.Add(vertex);

                foreach (var item in graph.AdjacencyList[vertex])
                    if (!visited.Contains(item))
                        queue.Enqueue(item);
            }
            return visited;
        }
    }
}
