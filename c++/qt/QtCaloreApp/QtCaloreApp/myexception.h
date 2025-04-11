#ifndef MYEXCEPTION_H
#define MYEXCEPTION_H

#include <QException>

class MyException : QtException{

public:
    void raise( ) const override { throw *this; }
    MyException* clone() const override;
};

#endif // MYEXCEPTION_H
