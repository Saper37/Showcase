package com.example.myapplication

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface AppMealDao{
    @Insert( onConflict = OnConflictStrategy.ABORT )
    suspend fun insert( meal : Meal  )

    @Delete
    suspend fun delete( meal : Meal)

    @Query( "DELETE FROM Meals")
    suspend fun deleteMeals( )

    @Query( "SELECT * FROM Meals")
    fun getMeals( ): Flow<MutableList<Meal>>
    @Query( "SELECT * FROM Meals WHERE meal_day == :meal_day ")
    fun getMeals( meal_day: String ): Flow<MutableList<Meal>>

    @Query("SELECT * FROM Meals")
    fun getMealsFlow(  ): Flow<MutableList<Meal>>

}

@Dao
interface AppFoodDao{
    @Insert( onConflict = OnConflictStrategy.ABORT )
    suspend fun insert( food: Food )
    @Delete
    suspend fun delete( food: Food )

    @Query( "DELETE FROM Foods")
    suspend fun deleteFoods( )
    @Query( "SELECT name FROM Foods WHERE name == :name" )
    fun findFood( name: String ): Flow<MutableList<String>>

    @Query( "SELECT * FROM Foods")
    fun getFoods( ): Flow<MutableList<Food>>
    @Query("SELECT * FROM Foods")
    fun getFoodsFlow(  ): Flow<MutableList<Food>>

}
