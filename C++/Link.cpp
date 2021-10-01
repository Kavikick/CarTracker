#include "Link.h"

Link* Link::getNext(){
    return next;
}

Link* Link::getPrevious(){
    return previous;
}

void Link::setNext(Link* next){
    this->next = next;
}

void Link::setPrevious(Link* previous){
    this->previous = previous;
}