using System;

namespace static_members
{
    class Rectangle{
        private int width, height;
        public Rectangle(int width, int height){
            this.width = width;
            this.height = height;
        }
        public void outputArea(){
            Console.WriteLine("Area output: " + Rectangle.CalculateArea(this.width, this.height));
        }
        public static int CalculateArea(int width, int height){
            return width*height;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Rectangle r = new Rectangle(10,20);
            r.outputArea();
        }
    }
}