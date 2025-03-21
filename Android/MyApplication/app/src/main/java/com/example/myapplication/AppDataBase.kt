package com.example.myapplication



import android.content.Context
import androidx.room.Database
import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.sqlite.db.SupportSQLiteDatabase
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch
import android.util.Log
import androidx.room.ProvidedTypeConverter
import androidx.room.TypeConverter
import androidx.room.TypeConverters
import androidx.room.Update
import kotlinx.coroutines.Dispatchers

@Entity( tableName = "Meals")
class Meal(
    @PrimaryKey(autoGenerate = true )
    val mealid: Int?,
    val meal_day: String,
    val order: Int,
    val cost: Double,
    val foods: MutableList<Food>
)

@Entity( tableName = "Foods")
data class Food(
    @PrimaryKey(autoGenerate = true )
    val foodid: Int?,
    val name: String,
    val cost: Double,
    val macros: Macros

)
class Macros( val macroid:Int,  val calore: Int,  val carbohydrate: Int,  val sugar: Int,
              val saturatedFat: Int,  val nonsaturatedFat: Int,  val fiber: Int,  val proteine: Int,
              val salt: Int ) {

    val values = listOf( macroid, calore, carbohydrate, sugar,
        saturatedFat, nonsaturatedFat, fiber,
        proteine, salt)
    fun ToString( ) : String{
        var data = ""
        for( value in values){
            data += value
            data += " "
        }
        return data
    }


}
@ProvidedTypeConverter
class Converters{
    @TypeConverter
    fun ToString( macro : Macros?): String? {
        if( macro == null )
            return null
        return macro.ToString()
    }
    @TypeConverter
    fun ToString( food : Food?): String? {
        if( food == null )
            return null
        var convertedData = "" + food.foodid + " " + food.name + " " + food.cost + " " + ToString( food.macros ) + " "
        return convertedData
    }
    @TypeConverter
    fun ToString( foods : List<Food>?): String? {
        if( foods == null )
            return null
        var convertedData = ""
        for( food in foods ){
            convertedData += "" + food.foodid + " " + food.name + " " + food.cost + " " + ToString( food.macros )
            if( foods.size > 1 )
                convertedData += ":"
        }
        return convertedData
    }
    @TypeConverter
    fun StringToMacros( convertedData: String? ): Macros?{
        if ( convertedData == null )
            return null
        var data = convertedData.split( " " )
        return Macros( data[ 0 ].toInt(), data[ 1 ].toInt(), data[ 2 ].toInt(), data[ 3 ].toInt(),
            data[ 4 ].toInt(), data[ 5 ].toInt( ), data[ 6 ].toInt(), data[7 ].toInt(),
            data[ 8 ].toInt( ) )
    }
    @TypeConverter
    fun StringToFood( convertedData: String? ): MutableList<Food>?{
        if ( convertedData == null )
            return null
        var foods: MutableList<Food> = mutableListOf()
        var listdata = convertedData.split( ":" )

        for( stringData in listdata ) {
            if( stringData.length == 0 )
                break
            var data = stringData.split( " " )
            Log.d( "Conver SString to Food List ", "stringData is " + stringData )
            val macro = Macros(
                data[3].toInt(), data[4].toInt(), data[5].toInt(), data[6].toInt(),
                data[7].toInt(), data[8].toInt(), data[9].toInt(), data[10].toInt(),
                data[11].toInt()
            )
            var food = Food(
                foodid = data[0].toInt(), name = data[1].toString(), cost = data[2].toDouble(),
                macros = macro
            )
            foods.add( food )
        }
        return foods
    }


}


@Database( entities = [ Meal::class, Food::class ], version = 1, exportSchema = false )
@TypeConverters( Converters::class )
public abstract class AppDatabase: RoomDatabase( ){
    abstract fun mealDao( ): AppMealDao
    abstract fun foodDao( ): AppFoodDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null
        private val CONVERTER_INSTANCE = Converters( )
        fun getDatabase(context: Context, scope: CoroutineScope): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "meal_database"

                )
                    .addCallback(AppDatabaseCallback(scope))
                    .addTypeConverter( CONVERTER_INSTANCE )
                    .build()

                Log.d("Database Appdatabase get database", "we got to getDatabase")
                INSTANCE = instance
                return instance
            }
        }

        private class AppDatabaseCallback(private val scope: CoroutineScope) :
            Callback() {

            override fun onCreate(db: SupportSQLiteDatabase) {
                super.onCreate(db)
                INSTANCE?.let { database ->
                    scope.launch(Dispatchers.IO) {
                        populateDatabase( database.mealDao(), database.foodDao() )
                        Log.d("Callback populate", "we got to the callback")
                    }
                    Log.d("Database Callback oncreate", "we got to the callback")
                }
            }
        }

        suspend fun populateDatabase(mealDao: AppMealDao, foodDao: AppFoodDao) {
            mealDao.deleteMeals( )
            foodDao.deleteFoods( )

            var macros1 = Macros(macroid = 1, calore = 1, carbohydrate = 1, sugar = 1,
                nonsaturatedFat = 1, saturatedFat = 1,
                proteine = 1, fiber = 1, salt = 1)
            var macros2 = Macros(macroid = 2, calore = 1, carbohydrate = 1, sugar = 1,
                nonsaturatedFat = 1, saturatedFat = 1,
                proteine = 1, fiber = 1, salt = 1)


            var food = Food(foodid = 1, name = "puuro", cost = 1.0, macros = macros1 )
            foodDao.insert(food)
            var food1 = Food(foodid = 2, name = "soijarouhe", cost = 1.0, macros = macros2 )
            foodDao.insert(food)
            var foods = mutableListOf( food, food1 )

            var meal = Meal(mealid = 1, meal_day = "puuro", order = 0, cost = 1.0, foods = foods )
            mealDao.insert(meal)
            var meal1 = Meal(mealid = 2, meal_day = "soijarouhe", order = 0, cost = 2.0, foods = foods )
            mealDao.insert(meal1)

            Log.d( "Database populateDatabase", "populate database is called " )
        }

    }




}






