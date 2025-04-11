#include "filemanipulator.h"

FileManipulator::FileManipulator() {}


FileManipulator::FileManipulator( QFile& file ):  selectedFile( file ){}

FileManipulator::FileManipulator( QFile&& file ): selectedFile( std::move( file ) ){}


void FileManipulator::setFileName( QFile& file  ){
    selectedFile = file;
}

QFile FileManipulator::getFileName( ){
    return selectedFile;
}


FileManipulator& operator=( const FileManipulator& fm ){
    selectedFile = fm;
    return *this;
}

FileManipulator& operator=( FileManipulator&& fm ){
    selectedFile = std::move( fm );
    return *this;
}
