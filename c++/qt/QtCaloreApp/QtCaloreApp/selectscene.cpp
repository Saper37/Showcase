#include "selectscene.h"


/*
 * Destructor
 */
SelectScene::~SelectScene( ){
    delete this->fm;

    while( fields.count( ) )
        delete fields.takeLast( );

    while( texts.count( ) )
        delete texts.takeLast( );

    while( selections.count( ) )
        delete selections.takeLast( );
    delete this->selectionModel;
    delete this->checkBox;

    delete this->foodObject;
    delete this->mealObject;
    delete mutex;
    delete this->instancePtr;

}

/*
 * getInstance of the singular class
 */
static SelectScene* getInsance( ){ return instancePtr; }


/*
 * Init - Overloaded function
 * establishes the needed private variables.
 * Raise MyException for non-defined FileManipulator variable
 */
Init(){
    try{
        if( fm != NULL ){
            ByteArray infodata = fm.readInfoData( );
            ByteArray fooddata = fm.readFoodData( );
            ByteArray mealdata = fm.readMealData( );
            this.selectionModel = QItemSelectionModel( );
            QJsonDocument foodD = QJsonDocument::fromJson( fooddata.toUtf8 );
            QJsonDocument mealD = QJsonDocument::fromJson( mealdata.toUtf8 );
            QJsonDocument infoD = QJsonDocument::fromJson( infodata.toUtf8 );
            this.foodObject = foodD.object( );
            this.mealObject = mealD.object( );
            this.infoObject = infoD.object( );
        }
        else{
            throw new MyException( "FileManipulator not found" );
        }}
    catch( Exception e ){
        e.stacktrace( );
    }
}

AddFileManipulator( const FileManipulator* newFM ) : fm( newFM ){}

