package com.example.myapplication


import android.annotation.SuppressLint
import android.app.Application
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.fragment.app.viewModels
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.recyclerview.widget.RecyclerView
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.SupervisorJob


enum class Scene{
    MainScene, SelectionScene, CalorieScene, InfoScene
}

data class Visibility( val name: String, val value: Any)



class VisibilityInfo: ViewModel(  ){
    private val mutableVisibility = MutableLiveData<MutableMap<String, Button>> ( )
    val visibilityData: MutableLiveData<MutableMap<String, Button>> get( ) = mutableVisibility
    fun getData( ): MutableLiveData<MutableMap<String, Button>>{
        return mutableVisibility
    }
    fun addVisibility( name: String, visibility: Button ){
        if( mutableVisibility.value != null ) {
            if (mutableVisibility.value?.containsKey( name ) == true )
                mutableVisibility.value?.set( name, visibility )
            else
                mutableVisibility.value?.put( name, visibility )
        }
    }
}

class MyApplication : Application() {
    // No need to cancel this scope as it'll be torn down with the process
    val applicationScope = CoroutineScope(SupervisorJob())

    // Using by lazy so the database and the repository are only created when they're needed
    // rather than when the application starts
    val database by lazy { AppDatabase.getDatabase(this, applicationScope) }
    val mealRepository by lazy { AppMealRepository(database.mealDao()) }
    val foodRepository by lazy { AppFoodRepository(database.foodDao() ) }
    //val macroRepository by lazy { AppMacrosRepository(database.macrosDao()) }
}


class MainActivity : AppCompatActivity() {

    private val mealActivityRequestCode = 1
    private val foodActivityRequestCode = 10

    val mealViewModel: AppMealViewModel by viewModels {
        AppMealViewModelFactory(( application as MyApplication).mealRepository)
    }
    val foodViewModel: AppFoodViewModel by viewModels {
        AppFoodViewModelFactory(( application as MyApplication).foodRepository)
    }
    //val ft: FragmentTransaction = getSupportFragmentManager( )


    @SuppressLint("CutPasteId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main )

        val mealViewModel: AppMealViewModel by viewModels {
            AppMealViewModelFactory(( application as MyApplication).mealRepository)
        }
        val foodViewModel: AppFoodViewModel by viewModels {
            AppFoodViewModelFactory(( application as MyApplication).foodRepository)
        }
        val mealadapter = AppMealListAdapter( )
        val foodadapter = AppFoodListAdapter( )

        mealViewModel.allMeals.observe(   this ){ meals -> meals?.let { mealadapter.submitList(it) } }
        foodViewModel.allFoods.observe(  this){ foods -> foods?.let{ foodadapter.submitList(it)} }

        if( savedInstanceState == null ) {

        }
        else{
            Log.d( "MainActivity OnCreate","SavedInstanceState  " + savedInstanceState)
        }
    }

}

