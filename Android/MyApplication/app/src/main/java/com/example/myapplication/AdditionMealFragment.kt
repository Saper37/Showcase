package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.CheckBox
import android.widget.EditText
import android.widget.Spinner
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.Navigation
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

internal class AdditionMealFragment( ) : Fragment( R.layout.fragment_infoscene_meal_addition ){
    private val mealViewModel: AppMealViewModel by activityViewModels (  )
    private val foodViewModel: AppFoodViewModel by activityViewModels (  )
    private val mealAdapter = AppMealListAdapter( )
    private val foodAdapter = AppFoodListAdapter( )
    private var checkBoxes: MutableList<CheckBox> = mutableListOf<CheckBox>( )
    



    override fun onCreateView(inflater: LayoutInflater, parent: ViewGroup?, savedInstanceState: Bundle? ): View?{
        return inflater.inflate( R.layout.fragment_infoscene_meal_addition, parent, false )
    }

    override fun onViewCreated( view: View, savedInstanceState: Bundle?) {

        val foodrecyclerView: RecyclerView? = view?.findViewById<RecyclerView>( R.id.addition_meal_mealrecyclerview )
        var mealname = view.findViewById<EditText>( R.id.info_addmeal_editText )
        var meals: MutableList<Meal>? = mealViewModel.getMeals()
        var foods: MutableList<Food>? = foodViewModel.getFoods( )


        if ( foodrecyclerView != null ){
            foodrecyclerView.layoutManager = LinearLayoutManager( view.context )
            foodrecyclerView.adapter = foodAdapter
            foodAdapter.submitList( foods )
        }

        var returnButton: Button = view.findViewById( R.id.addition_meal_return_button )
        var addButton: Button = view.findViewById( R.id.addition_meal_add_button )


        val navController = Navigation.findNavController( view )

        addButton.setOnClickListener{
            Log.d( "AdditionFoodFragment", "add pressed ")
            if( meals != null && !mealname.text.equals("") ) {
                var foods: MutableList<Food> = mutableListOf( )
                var newMeal = Meal( 1, mealname.text.toString(), 0, 0.0, foods )
                mealViewModel.insert( newMeal )
                meals  = mealViewModel.getMeals()
            }

        }
        returnButton.setOnClickListener{
            Log.d( "AdditionFoodFragment", "return pressed")
            this.onStop( )
            navController.navigate( R.id.action_additionMealFragment_to_infoScene )
        }

    }
}