namespace BinaryHeaps
{
    public interface IBinaryHeap<T> where T : System.IComparable<T>
    {
        int Count { get; }
        HeapType Heap_Type { get; }

        void Insert(T item);

        T Delete();

        T Parent(int index);

        T LeftChild(int index);

        T RightChild(int index);

        T GetMaximumElement();
    }
}
