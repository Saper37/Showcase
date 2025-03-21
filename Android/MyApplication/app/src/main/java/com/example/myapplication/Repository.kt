package com.example.myapplication

import androidx.annotation.WorkerThread
import kotlinx.coroutines.flow.Flow


class AppMealRepository( private val AppDao: AppMealDao ){
    val allMeals: Flow<MutableList<Meal>> = AppDao.getMealsFlow( )
    @Suppress( "RedudantSuspendModifier")
    @WorkerThread
    suspend fun insert( meal: Meal ){
        AppDao.insert( meal )
    }
    @Suppress( "RedudantSuspendModifier")
    @WorkerThread
    suspend fun getMeals( ): Flow<MutableList<Meal>>{
        return AppDao.getMeals( )
    }
    @Suppress( "RedudantSuspendModifier")
    @WorkerThread
    suspend fun getMeals( meal_day: String ): Flow<MutableList<Meal>>{
        return AppDao.getMeals( meal_day )
    }
}



class AppFoodRepository( private val AppDao: AppFoodDao ){
    val allFoods: Flow<MutableList<Food>> = AppDao.getFoodsFlow()

    @Suppress( "RedudantSuspendModifier")
    @WorkerThread
    suspend fun insert( food: Food){
        AppDao.insert( food )
    }
    @Suppress( "RedudantSuspendModifier")
    @WorkerThread
    suspend fun getFoods( ): Flow<MutableList<Food>>{
        return AppDao.getFoods( )
    }
}