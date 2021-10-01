/*
    Link.h

    The individual links in a doubly linked list
*/

class Link {
public:
    Link* getNext();
    Link* getPrevious();
    void setNext(Link* next);
    void setPrevious(Link* previous);
private:
    Link* next = nullptr;
    Link* previous = nullptr;
};
