#ifndef BASESCENE_H
#define BASESCENE_H

#include "filemanipulator.h"
#include "myexception.h"
#include <mutex>
#include <vector>
#include <memory>
#include <QApplication>
#include <QWidget>
#include <QtString>
#include <QPushButton>

class BaseScene : public QWidget{
private:

public:
    virtual void Init( ) = 0;

private slots:
    void buttonPushed( );

};


#endif // BASESCENE_H
