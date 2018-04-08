using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InfixToPostfix
{
    class Program
    {        
        static void Main(string[] args)
        {
            string infix = string.Empty;
            string postfix = string.Empty;

            Console.WriteLine("Enter valid infix string: ");
            infix = Console.ReadLine();

            postfix = InfixToPostfix(infix).ToString();

            Console.WriteLine("Postfix : {0}", postfix);

            Console.ReadLine();
        }

        // Infix to Postfix conversion.
        // Applicable only for numbers (for now).
        // To keep it simple, I have considered very few operators for now.
        private static StringBuilder InfixToPostfix(string infix)
        {
            StringBuilder postfix = new StringBuilder();
            char current;

            // 1. Create a new stack.
            Stack<char> infixStack = new Stack<char>();

            // 2. Loop through all the items in infix
            foreach (char item in infix)
            {
                if (char.IsWhiteSpace(item))
                {
                    continue;
                }
                // 3. if the itme is number, add it to the postfix
                if (Char.IsNumber(item))
                {
                    postfix.Append(item);
                }
                // 4. if the item is open bracket, then push it to the stack
                else if(item == '(')
                {
                    infixStack.Push(item);
                }
                // 5. if the item is closed bracket, then keep on popping from stack and 
                //    adding to postfix until you find open bracket
                else if(item == ')')
                {
                    current = infixStack.Pop();
                    while (current != '(')
                    {
                        postfix.Append(current);
                        current = infixStack.Pop();
                    }
                }
                // 6. if the step 3,4 and 5 is not applicable, then do following
                else
                {
                    // 7. Peek the top item in stack. If the precedence of the peeked item is higher than the 
                    //    current item, then pop out from stack and append it to the postfix. Repeat this step
                    //    unless you find top item's precedence is not higher than the current item. In the end
                    //    of this loop, push the current item to the stack.
                    if(infixStack.Count > 0 && CheckPrecedence(infixStack.Peek(), item))
                    {
                        current = infixStack.Pop();
                        while (CheckPrecedence(current, item))
                        {
                            postfix.Append(current);
                            if(infixStack.Count == 0)
                            {
                                break;
                            }
                            current = infixStack.Pop();
                        }
                        infixStack.Push(item);
                    }
                    else
                    {
                        infixStack.Push(item);
                    }
                }
            }

            while (infixStack.Count > 0)
            {
                current = infixStack.Pop();
                postfix.Append(current);
            }


            return postfix;
        }

        private static bool CheckPrecedence(char v, char item)
        {
            Dictionary<char, int> operatorWithPrecedence = new Dictionary<char, int>
            {
                { '(', 0 },
                { '+', 1 },
                { '-', 1 },
                { '*', 2 },
                { '/', 2 },
                { '%', 2 }
            };

            return operatorWithPrecedence[v] >= operatorWithPrecedence[item];
        }
    }
}
