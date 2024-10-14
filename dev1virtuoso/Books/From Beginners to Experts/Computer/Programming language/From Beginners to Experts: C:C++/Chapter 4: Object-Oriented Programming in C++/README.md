# From Beginners to Experts: C/C++

## Table of Contents

- [From Beginners to Experts: C/C++](#from-beginners-to-experts-cc)
  - [Table of Contents](#table-of-contents)
  - [Chapter 4: Object-Oriented Programming in C++](#chapter-4-object-oriented-programming-in-c)
      - [Section 4.1: Introduction to Object-Oriented Programming](#section-41-introduction-to-object-oriented-programming)
      - [Section 4.2: Classes and Objects](#section-42-classes-and-objects)
      - [Section 4.3: Encapsulation](#section-43-encapsulation)
      - [Section 4.4: Inheritance](#section-44-inheritance)
      - [Section 4.5: Polymorphism](#section-45-polymorphism)
      - [Section 4.6: Abstraction](#section-46-abstraction)
      - [Section 4.7: Case Study: Creating a Simple Class in C++](#section-47-case-study-creating-a-simple-class-in-c)
      - [Conclusion](#conclusion)

## Chapter 4: Object-Oriented Programming in C++

In this chapter, we will delve into the world of object-oriented programming (OOP) in C++, exploring the key principles, features, and concepts that make C++ a powerful and versatile language for building complex software systems.

#### Section 4.1: Introduction to Object-Oriented Programming

Object-oriented programming is a paradigm that revolves around the concept of objects, which encapsulate data and behavior. C++ supports OOP principles such as encapsulation, inheritance, polymorphism, and abstraction.

#### Section 4.2: Classes and Objects

- **Classes**: Blueprints for creating objects. They define the properties (data members) and behaviors (member functions) of objects.
- **Objects**: Instances of classes that encapsulate data and behavior.

#### Section 4.3: Encapsulation

Encapsulation involves bundling data and methods that operate on the data within a single unit, called a class. It helps in hiding the internal implementation details of a class from the outside world.

#### Section 4.4: Inheritance

Inheritance allows a class (derived class) to inherit properties and behaviors from another class (base class). It promotes code reusability and establishes an "is-a" relationship between classes.

#### Section 4.5: Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables functions to operate on objects of multiple types through method overloading and overriding.

#### Section 4.6: Abstraction

Abstraction involves simplifying complex systems by modeling classes based on real-world entities. It hides unnecessary details and exposes only essential features.

#### Section 4.7: Case Study: Creating a Simple Class in C++

Let's create a simple class `Car` with attributes like `make`, `model`, and `year`, along with a method to display information about the car:

```cpp
#include <iostream>
#include <string>

class Car {
public:
    std::string make;
    std::string model;
    int year;

    void displayInfo() {
        std::cout << "Car: " << year << " " << make << " " << model << std::endl;
    }
};

int main() {
    Car myCar;
    myCar.make = "Toyota";
    myCar.model = "Camry";
    myCar.year = 2022;

    myCar.displayInfo();

    return 0;
}
```

This program demonstrates the creation of a simple class `Car`, instantiation of an object `myCar`, assignment of values to its attributes, and calling a method to display information about the car.

#### Conclusion

Object-oriented programming in C++ enables developers to build modular, reusable, and maintainable software systems by leveraging concepts like classes, objects, encapsulation, inheritance, polymorphism, and abstraction. By understanding and applying OOP principles effectively, you can design elegant and robust solutions to complex problems. In the upcoming chapters, we will explore advanced OOP concepts, design patterns, best practices, and real-world applications of object-oriented programming in C++ to enhance your programming skills and empower you to create high-quality software solutions.