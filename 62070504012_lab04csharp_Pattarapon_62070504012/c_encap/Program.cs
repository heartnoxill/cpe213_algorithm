using System;

namespace c_encap
{
    class Rectangle{
        private double length;
        private double width;
        
        public void acceptDetails(){
            Console.WriteLine("Enter Length: ");
            length = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter Width: ");
            width = Convert.ToDouble(Console.ReadLine());
        }

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
            r.acceptDetails();
            r.display();
            Console.ReadLine();
        }
    }
}
