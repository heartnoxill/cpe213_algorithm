using System;

namespace c_polym
{
    class printData{
        public void print(int i){
            Console.WriteLine("Printing int: {0}", i);
        }
        public void print(double f){
            Console.WriteLine("Printing float: {0}", f);
        }
        public void print(string s){
            Console.WriteLine("Printing string: {0}", s);
        }
    }
    class Program{
        static void Main(string[] args)
        {
            printData p = new printData();
            p.print(5);
            p.print(500.263);
            p.print("Hello C# World");
            Console.ReadKey();
        }
    }
}
