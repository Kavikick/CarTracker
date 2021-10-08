/*
    Car.h

    Class definition for racecars in a race
*/

#include "Link.h"
#include <string>

class Car : Link {
public:
  Car(int number, std::string driver) {
    this->number = number;
    this->driver = driver;
  }

  int getNumber() { return number; }
  std::string getDriver() { return driver; }

private:
  int number;
  std::string driver;
};