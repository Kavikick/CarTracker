#include <cassert>
#include <iostream>
#include <string>

#include "UI.h"

using namespace std;

void LinkTests();
void carTests();

void runAllTests() {
  assert(0 < 1);

  LinkTests();
  carTests();
}

void LinkTests() {
  Link *test1 = new Link;
  assert(test1->getNext() == nullptr);
  assert(test1->getPrevious() == nullptr);
  Link *test2 = new Link;
  test1->setNext(test2);
  test1->setPrevious(test2);
  assert(test1->getNext() == test2);
  assert(test1->getPrevious() == test2);
}

void carTests() {
  Car testCar(1, "Dave");
  assert(testCar.getNumber() == 1);
  assert(testCar.getDriver() == "Dave");
}
