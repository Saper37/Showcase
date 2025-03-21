package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import androidx.core.text.isDigitsOnly
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.Navigation

internal class AdditionFoodFragment( ) : Fragment( R.layout.fragment_infoscene_food_addition){
    private val foodViewModel: AppFoodViewModel by activityViewModels (  )

    override fun onCreateView(inflater: LayoutInflater, parent: ViewGroup?, savedInstanceState: Bundle? ): View?{
        return inflater.inflate( R.layout.fragment_infoscene_food_addition, parent, false )
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        var returnButton: Button = view.findViewById( R.id.addition_food_return_button )
        var addButton: Button = view.findViewById( R.id.addition_food_add_button )

        var namefield: EditText = view.findViewById( R.id.addition_food_textfield_name)
        var costfield: EditText = view.findViewById( R.id.addition_food_textfield_cost )
        var caloreField: EditText = view.findViewById( R.id.addition_food_textfield_calore )
        var carbonhfield: EditText = view.findViewById( R.id.addition_food_textfield_carbo )
        var sugarfield: EditText = view.findViewById( R.id.addition_food_textfield_sugar )
        var nonSaturatedFatfield: EditText = view.findViewById( R.id.addition_food_textfield_non_sfat )
        var saturatedFatfield: EditText = view.findViewById( R.id.addition_food_textfield_sfat )
        var fiberfield: EditText = view.findViewById( R.id.addition_food_textfield_fiber )
        var proteinefield: EditText = view.findViewById( R.id.addition_food_textfield_proteine )
        var saltfield: EditText = view.findViewById( R.id.addition_food_textfield_salt )


        val navController = Navigation.findNavController( view )

        addButton.setOnClickListener{
            Log.d( "AdditionFoodFragment", "add pressed ")

            try {
                var name = namefield.text.toString()
                var cost = costfield.text.toString().toDouble()
                var calore = caloreField.text.toString().toInt()
                var carbonh = carbonhfield.text.toString().toInt()
                var sugar = sugarfield.text.toString().toInt()
                var nonsfat = nonSaturatedFatfield.text.toString().toInt()
                var sfat = saturatedFatfield.text.toString().toInt()
                var fiber = fiberfield.text.toString().toInt()
                var proteine = proteinefield.text.toString().toInt()
                var salt = saltfield.text.toString().toInt()
                var foods: MutableList<Food>? = foodViewModel.getFoods()

                if( foods != null ) {
                    var newid = foods.size + 1
                    var newmacros = Macros(
                        newid, calore=calore, carbohydrate = carbonh, sugar = sugar, nonsaturatedFat = nonsfat,
                        saturatedFat = sfat, fiber = fiber, proteine = proteine, salt = salt
                    )
                    var newfood = Food( foodid= null, name=name, cost=cost, macros=newmacros)

                    foodViewModel.insert(newfood)
                }
            }
            catch(  e: NumberFormatException ){
                if( namefield.text.isDigitsOnly() && costfield.text.length == 0)
                    namefield.setError( "namefield error")
                if( !costfield.text.isDigitsOnly() && costfield.text.length == 0 )
                    costfield.setError( "costfield error")
                if( !caloreField.text.isDigitsOnly() && caloreField.text.length == 0)
                    caloreField.setError( "caloreField error")
                if( !carbonhfield.text.isDigitsOnly() && carbonhfield.text.length == 0)
                    carbonhfield.setError( "carbonhfield error")
                if( !sugarfield.text.isDigitsOnly() && sugarfield.text.length == 0)
                    sugarfield.setError( "sugarfield error")
                if( !nonSaturatedFatfield.text.isDigitsOnly() && nonSaturatedFatfield.text.length == 0)
                    nonSaturatedFatfield.setError( "nonSaturatedFatfield error")
                if( !saturatedFatfield.text.isDigitsOnly() && saturatedFatfield.text.length == 0)
                    saturatedFatfield.setError( "saturatedFatfield error")
                if( !fiberfield.text.isDigitsOnly() && fiberfield.text.length == 0)
                    fiberfield.setError( "fiberfield error")
                if( !proteinefield.text.isDigitsOnly() && proteinefield.text.length == 0)
                    proteinefield.setError( "proteinefield error")
                if( !saltfield.text.isDigitsOnly() && saltfield.text.length == 0)
                    saltfield.setError( "saltfield error")
                Log.d( "Error in the addition food fragment ", Log.getStackTraceString( e ) )
            }



        }
        returnButton.setOnClickListener{
            Log.d( "AdditionFoodFragment", "return pressed")
            this.onStop( )
            navController.navigate( R.id.action_additionFragment2_to_infoScene )
        }

    }
}