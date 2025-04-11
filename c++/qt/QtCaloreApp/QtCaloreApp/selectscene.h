#ifndef SELECTSCENE_H
#define SELECTSCENE_H

#include "basescene.h"
#include <QItemSelectionModel>
/*
 * Class SelectScene inherits BaseScene
 * Reponsible for defining and implementing SelectionScreen for meals.
 *
 */
class SelectScene : BaseScene{

private:

    static SelectScene* instancePtr;
    static mutex mtx;
    SelectScene( );

    FileManipulator fm = NULL;

    std::vector<QWidget*> fields;
    std::vector<QWidget*> texts;
    std::vector<QWidget*> selections;

    QItemSelectionModel* selectionModel;

    QJsonObject* foodObject;
    QJsonObject* mealObject;
    QJsonObject* infoObject;

public:

    SelectScene( const SelectScene& ) = delete;
    ~SelectScene( );
    void operator=( const SelectScene& ) = delete;

    static SelectScene* getInstance( );

    void AddFileManipular( const FileManipulator& );
    void AddItems( const QWidget& );
    void Init( ) override;

    FileManipulator* getFileManipulator( )const;
    std::vector<QWdiget> getItems( ) const;

signals:
    void sceneChance( );




};

#endif // SELECTSCENE_H
