using System.Collections.Generic;

namespace NativeStacks
{
    public interface IStack<T> : IEnumerable<T>
    {
        void Push(T item);

        T Pop();
    }
}