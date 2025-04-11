const mealList = []


createInfoFields = ( ) =>{
    
};

createFileUI = ( ) =>{
    mealFile = '/C:/Users/Samppa/Documents/GitHub/Project/web/test/selectionView/meals.json'
    infoFile = '/C:/Users/Samppa/Documents/GitHub/Project/web/test/selectionView/infos.json'
    foodFile = '/C:/Users/Samppa/Documents/GitHub/Project/web/test/selectionView/meals.json'
    
    mealData = fetch( mealFile )
        .then( response => response.json() )
        .catch(error => console.error('Error fetching meals:', error));
    foodData = fetch( foodFile )
        .then( response => response.json() )
        .catch(error => console.error('Error fetching foods:', error));
    infoData = fetch( infoFile )
        .then( response => response.json( file )  )
        .catch(error => console.error('Error fetching info:', error));
    return mealData, foodData, infoData
}

createUI = ( mealData, foodData, infoData ) =>{
  console.log('Creating UI');
  document.innerHTML.content += 
        `<select id="mealAltList">
          <a> Item 1 </a>
          <a> Item 2 </a>
        </select>`
};
console.log('Starting script');
mealData, foodData, infoData = createFileUI( ) 
createUI( mealData, foodData, infoData )