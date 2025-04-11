TEMPLATE = APP
TARGET = QtCaloreApp

QT = core gui

greaterThan( QT_MAJOR_VERSION, 4 ): QT += widgets
find_package( Qt6 REQUIRED COMPONENTS Sql )
QT += sql

SOURCES += \
    filemanipulator.cpp \
    main.cpp \
    mainframe.cpp \
    myexception.cpp \
    mysql.cpp \
    selectscene.cpp

HEADERS += \
    basescene.h \
    filemanipulator.h \
    mainframe.h \
    myexception.h \
    mysql.h \
    selectscene.h
