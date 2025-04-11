#ifndef FILEMANIPULATOR_H
#define FILEMANIPULATOR_H

#include <Qstring>
#include <QFile>

class FileManipulator{
private:
    QFile selectedFile;
public:
    FileManipulator( );
    FileManipulator( QFile& filename );
    FileManipulator( QFile&& filename );

    QByteArray FileManipulator::readFoodData( );
    QByteArray FileManipulator::readMealData( );
    void FileManipulator::writeData( );
    void FileManipulator::setFile( QFile& file  );
    QFile FileManipulator::getFileName( );

    FileManipulator& operator=( const FileManipulator& );
    FileManipulator& operator=( FileManipulator&& );
};

#endif // FILEMANIPULATOR_H
