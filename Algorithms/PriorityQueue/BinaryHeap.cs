using System;

namespace BinaryHeaps
{
    public class BinaryHeap<T> : IBinaryHeap<T> where T: IComparable<T>
    {
        private T[] elements;

        private int capacity;

        private HeapType heapType;

        private int count;

        public BinaryHeap()
        {
            this.capacity = Int32.MaxValue;
            heapType = HeapType.Max_Heap;
            elements = new T[1000];
        }

        public BinaryHeap(int capacity, HeapType heapType)
        {
            this.capacity = capacity;
            this.heapType = heapType;
        }

        public int Count { get { return count; } }

        public HeapType Heap_Type { get { return heapType; } }

        public T Delete()
        {
            throw new NotImplementedException();
        }

        public T GetMaximumElement()
        {
            if (count == 0)
            {
                throw new Exception("No element in the heap");
            }

            return elements[0];
        }

        public void Insert(T item)
        {            
            if (count == 0)
            {
                elements[0] = item;
                count++;
                return;
            }

            if (count >= capacity)
            {
                throw new Exception("Capacity full");
            }

            count++;
            int i = count - 1;
            while (i > 0 && item.CompareTo(elements[(i-1)/2]) > 0 )
            {                
                elements[i] = elements[(i - 1) / 2];
                i = (i - 1) / 2;
            }
            elements[i] = item;            
        }

        public T LeftChild(int index)
        {
            int left = 2 * index + 1;
            if (left >= count)
            {
                throw new Exception("No left child exist");
            }

            return elements[left];
        }

        public T Parent(int index)
        {
            throw new NotImplementedException();
        }

        public T RightChild(int index)
        {
            int right = 2 * index + 2;
            if (right >= count)
            {
                throw new Exception("No right child exist");
            }

            return elements[right];
        }
    }
}
