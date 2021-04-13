using System;

namespace c_variable
{
    class Rectangle{
        public double length;
        public double width;

        public double getArea(){
            return length*width;
        }
        public void display(){
            Console.WriteLine("Length: {0}", length);
            Console.WriteLine("Width: {0}", width);
            Console.WriteLine("Area: {0}", getArea());
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Rectangle r = new Rectangle();
            r.length=4.5;
            r.width=3.5;
            r.display();
            Console.WriteLine();
        }
    }
}
