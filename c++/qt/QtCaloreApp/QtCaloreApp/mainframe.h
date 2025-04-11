#ifndef MAINFRAME_H
#define MAINFRAME_H
#include "basescene.h"
#include <QWidget>


class MainFrame : BaseScreen {

private:

    static MainFrame* instancePtr;
    static mutex mtx;
    MainFrame( );

    std::map<QtString, BaseScene* > scenes;

public:

    void operator=( const MainFrame& ) = delete;
    SelectScene( const SelectScene& ) = delete;

    static MainFrame* getInstance( );
    addScene( const BaseScene& );


};

#endif // MAINFRAME_H
