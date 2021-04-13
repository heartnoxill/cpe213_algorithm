using System;

namespace c_constr_destr
{
    class Car{
        private string color;
        
        public Car(string color){
            this.color = color;
        }

        public string describe(){
            return "This car is " + Color;
        }

        public string Color{
            get { return color; }
            set { color = value; }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Car car;

            car = new Car("Red");
            Console.WriteLine(car.describe());
            car = new Car("Green");
            Console.WriteLine(car.describe());
            Console.ReadLine();
        }
    }
}
