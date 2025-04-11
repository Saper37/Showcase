package com.example.myapplication


import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.core.os.bundleOf
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.Navigation
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import org.w3c.dom.Text


/*
 Defines a scene for adding, modifying and removing food related information
TODO Adding the actual functionality, right now there is only rough framework
TODO that will change
 */

private val NUMBER_OF_ITEMS = 8


// internal class InfoScene( navController: NavController, mealadapter: AppMealListAdapter, foodadapter: AppFoodListAdapter ) :ComponentActivity( ) {
internal class InfoScene(  ) : Fragment( R.layout.fragment_infoscene ) {

    private val mealViewModel: AppMealViewModel by activityViewModels (  )
    private val foodViewModel: AppFoodViewModel by activityViewModels (  )
    private var mode: String = "meal"
    private var foodList: MutableList<Food> = mutableListOf()

    override fun onCreateView(inflater: LayoutInflater, parent: ViewGroup?, savedInstanceState: Bundle? ): View? {
        return inflater.inflate( R.layout.fragment_infoscene , parent, false )
    }
    override fun onStop( ){
        Log.d( "Infoscene", "onStop called")
        super.onStop( )
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle? ){


        var backButton: Button = view.findViewById( R.id.info_return_button )
        var modeButton: Button = view.findViewById( R.id.info_mode_button )
        var addButton: Button = view.findViewById( R.id.info_add_button )


        val navController = Navigation.findNavController( view )
        val mealrecyclerView = view.findViewById<RecyclerView>( R.id.mealrecyclerview )
        val mealAdapter = AppMealListAdapter( )
        val foodAdapter = AppFoodListAdapter( )

        mealrecyclerView.layoutManager = LinearLayoutManager ( view.context  )
        mealrecyclerView.adapter = mealAdapter
        mealAdapter.submitList( mealViewModel.getMeals() )
        foodAdapter.submitList( foodViewModel.getFoods() )

        backButton.setOnClickListener{
            this.onStop( )
            navController.navigate( R.id.action_infoScene_to_mainScene )
        }

        addButton.setOnClickListener{
            Log.d( "InfoScene", "add button pressed")
            if( mode == "food")
                navController.navigate( R.id.action_infoScene_to_additionFragment2 )
            else if( mode == "meal")
                navController.navigate( R.id.action_infoScene_to_additionMealFragment )
            else
                throw Exception( "Error in definition of mode. Should be 'food' or 'meal' not " + mode )
            
        }

        modeButton.setOnClickListener{
            if( mode == "food") {
                mode = "meal"
                modeButton.setText( "food mode " )
                mealrecyclerView.adapter = mealAdapter
            }
            else if ( mode == "meal" ) {
                mode = "food"
                modeButton.setText( "meal mode" )
                mealrecyclerView.adapter = foodAdapter
            }
            else
                throw Exception( "InfoScene Undefined behaviour with mode variable")
            Log.d( "InfoScene", "mode variable is " + mode )
        }



        Log.d( "Info recyclerview data ", "" + mealrecyclerView.adapter?.itemCount )
    }
}
fun checkLen( listOfItems: List<String>, correctSize: Int ) : Boolean{
    return listOfItems.size == correctSize
}