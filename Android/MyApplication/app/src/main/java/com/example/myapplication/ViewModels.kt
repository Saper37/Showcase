package com.example.myapplication

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.asLiveData
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.launch

class AppMealViewModel( private val repository: AppMealRepository ) : ViewModel( ){
    val allMeals: LiveData<MutableList<Meal>> = repository.allMeals.asLiveData( )
    fun insert( meal: Meal ) = viewModelScope.launch{
        repository.insert( meal )
    }
    fun getMeals( ): MutableList<Meal>? {
        return allMeals.value
    }
    fun getMeals( name: String ) : MutableList<Meal>? {
        var meals: MutableList<Meal>? = allMeals.value
        if ( meals != null ){
            var filtered: MutableList<Meal> = mutableListOf( )
            meals.filterTo( filtered,   {it.meal_day  == name} )
            return filtered
        }
        return meals

    }

}

internal class AppMealViewModelFactory( private val repository: AppMealRepository ) : ViewModelProvider.Factory{
    override fun <T: ViewModel> create(modelClass: Class<T> ): T{
        if( modelClass.isAssignableFrom( AppMealViewModel::class.java ) ){
            @Suppress( "UNCHECKED_CAST" )
            return AppMealViewModel( repository ) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}

class AppFoodViewModel( private val repository: AppFoodRepository ) : ViewModel( ){
    val allFoods: LiveData<MutableList<Food>> = repository.allFoods.asLiveData( )
    fun insert( food: Food ) = viewModelScope.launch{
        repository.insert( food )
    }
    fun getFoods( ): MutableList<Food>? {
        return allFoods.value
    }

}


internal class AppFoodViewModelFactory( private val repository: AppFoodRepository ) : ViewModelProvider.Factory{
    override fun <T: ViewModel> create(modelClass: Class<T> ): T{
        if( modelClass.isAssignableFrom( AppFoodViewModel::class.java ) ){
            @Suppress( "UNCHECKED_CAST" )
            return AppFoodViewModel( repository ) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
