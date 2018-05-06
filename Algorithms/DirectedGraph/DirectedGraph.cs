using System.Collections.Generic;

namespace DirectedGraph
{
    public class DirectedGraph<T>
    {
        private int numberOfEdges;

        private Dictionary<T, HashSet<T>> adjacencyList = new Dictionary<T, HashSet<T>>();

        public int NumberOfVertices
        {
            get
            {
                return adjacencyList.Count;
            }
        }

        public int NumberOfEdges
        {
            get
            {
                return numberOfEdges;
            }
        }

        public Dictionary<T, HashSet<T>> AdjacencyList
        {
            get
            {
                return adjacencyList;
            }
        }

        public bool AddVertex(T item)
        {
            adjacencyList[item] = new HashSet<T>();
            return true;
        }

        public bool AddEdge(T start, T end)
        {
            if (!adjacencyList.ContainsKey(start) || !adjacencyList.ContainsKey(end))
            {
                return false;
            }

            adjacencyList[start].Add(end);
            numberOfEdges++;
            return true;
        }
    }

}
