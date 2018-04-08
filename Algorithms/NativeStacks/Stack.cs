using System;
using System.Collections;
using System.Collections.Generic;

namespace NativeStacks
{
    public class Stack<T> : IStack<T>
    {
        private LinkedList<T> list;

        public Stack()
        {
            list = new LinkedList<T>();
        }

        public IEnumerator<T> GetEnumerator()
        {
            throw new NotImplementedException();
        }

        public T Pop()
        {
            T first = list.First.Value;
            list.RemoveFirst();
            return first;
        }

        public void Push(T item)
        {
            list.AddFirst(item);
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            throw new NotImplementedException();
        }
    }
}
