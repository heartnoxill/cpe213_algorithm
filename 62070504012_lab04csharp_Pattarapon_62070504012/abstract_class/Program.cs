using System;

namespace abstract_class
{
    abstract class fourLeggedAnimal{
        public virtual string describe(){
            return "Not much is known about this four legged animal!";
        }
    }
    class Dog : fourLeggedAnimal{
        public override string describe(){
            string result = base.describe();
            result += "In fact, it's a dog!";
            return result;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Dog dog = new Dog();
            Console.WriteLine(dog.describe());
            Console.ReadKey();
        }
    }
}
