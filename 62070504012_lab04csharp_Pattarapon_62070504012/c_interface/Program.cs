using System;
using System.Collections;
using System.Collections.Generic;

namespace c_interface
{
    interface IAnimal{
        string describe();
        string Name{
            get;
            set;
        }
    }
    class Dog : IAnimal, IComparable{
        private string name;
        public Dog(string name){
            this.Name = name;
        }
        public string describe(){
            return "Hello, I'm a dog and my name is " + this.Name;
        }
        public int CompareTo(object obj){
            if (obj is IAnimal)
                return this.Name.CompareTo((obj as IAnimal).Name);
            return 0;
        }
        public string Name{
            get { return name; }
            set { name = value; }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            List<Dog> dogs = new List<Dog>();
            dogs.Add(new Dog("Fido"));
            dogs.Add(new Dog("Bob"));
            dogs.Add(new Dog("Adam"));
            dogs.Sort();
            foreach (Dog dog in dogs)
                Console.WriteLine(dog.describe());
            Console.ReadKey();
        }
    }
}
