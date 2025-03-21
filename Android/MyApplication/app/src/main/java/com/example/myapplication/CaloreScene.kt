package com.example.myapplication

import android.app.Activity
import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardType
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.navigation.Navigation
import kotlin.math.log


/* Constants for calculation of body mass
  FACTOR1 and FACTOR2 are used for calculating factor 1
  FACTOR3 is used for calculating factor 2, factor1 and factor2 are used for calculating factor that is used in body mass percentage
  FACTOR 4 and FACTOR5 are used in Body Mass Percentage Calculation

 */
const val CALORE_FACTOR1 = 1.0324
const val CALORE_FACTOR2 = 0.19077
const val CALORE_FACTOR3 = 0.15456
const val CALORE_FACTOR4 = 495.0
const val CALORE_FACTOR5 = 450.0
const val CALORE_OPTKAL: String = "30 32 35 38 40 42 45"


/*
 Defines a scene for defining calore needs
 TODO Adding actual functionality
*/

internal class CaloreScene(  ): Fragment( R.layout.fragment_calorescene ){

    private val visibilitydata: VisibilityInfo by viewModels(  )



    override fun onResume() {
        Log.d( "CaloreScene", "onResume")
        super.onResume()
    }
    override fun onStop( ){
        val returnButton: Button? = view?.findViewById( R.id.calore_return_button )
        val caloreTextView : TextView? = view?.findViewById( R.id.calore_text )
        if( returnButton != null )
            returnButton.visibility = View.INVISIBLE
        if( caloreTextView != null )
            caloreTextView.visibility = View.INVISIBLE

        Log.d( "CaloreScene", "onStop " + returnButton?.visibility + " " + caloreTextView?.visibility )
        super.onStop()
    }
    override fun onCreateView(inflater: LayoutInflater, parent: ViewGroup?, savedInstanceState: Bundle? ): View? {
        val visibilityData = visibilitydata.getData().value
        Log.d( "CaloreScene visibilityData value ", visibilityData.toString() )
        return inflater.inflate( R.layout.fragment_calorescene , parent, false )
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle? ){
        var visibilityData = visibilitydata.getData().value
        val navController = Navigation.findNavController( view )
        Log.d( "CaloreScene visibilityData value ", visibilityData.toString() )
        Log.d( "CaloreScene", "onViewCreated started")
        var returnButton: Button = view.findViewById( R.id.calore_return_button )
        returnButton.setOnClickListener{
            Log.d( "CaloreScene", "Fragment paused")
            this.onStop( )
            navController.navigate( R.id.action_caloreScene_to_mainScene )
            /*childFragmentManager.commit{
                replace<MainScene>( R.id.fragment_container, "info_fragment"  )
                setReorderingAllowed( true )
            }*/
        }
            }
    override fun onAttach( context: Context){
        super.onAttach(context)
        if( context is Activity){

        }
    }
}

private fun CalculateCalories( leanMass: Double, spentCalore: Int ) : MutableMap<Int, Double >{
    var optcal = CALORE_OPTKAL.split( " " ).forEach{ key -> key.toInt( ) }

    val OPTCALS: List<Int> = listOf( )
    var optcals: MutableMap<Int, Double> = mutableMapOf()
    var res: Double
    for( optcal: Int in OPTCALS){
        res = ProcessCalories( optcal, leanMass, spentCalore )
        optcals.put( optcal, res )
        Log.d( "CALCULATECALORIES", "optkal is " + optcal + " res is " + res )
    }
    return optcals
}

private fun ProcessCalories( optkal: Int, leanMass: Double, spentCalore: Int ) : Double {
    return optkal * leanMass + spentCalore
}


private fun CalculateBody ( weight: Double, height: Double, waist: Double, neck: Double ) : Map<String, Double>{

    var fac1: Double = CALORE_FACTOR1 - CALORE_FACTOR2 * log( ( waist - neck ), 10.0 )
    var fac2: Double = CALORE_FACTOR3 * log( height, 10.0 )
    var fac: Double = fac1 + fac2
    var bodymasspercentage: Double = ( CALORE_FACTOR4 / fac ) - CALORE_FACTOR5
    var fatmassformula: Double = ( bodymasspercentage / 100 ) * weight
    var leanmass: Double = weight - fatmassformula
    return mapOf( "leandata" to leanmass, "fatdata" to fatmassformula )
}


@Composable
fun EditTextField(value: String, label: String, onValueChange: (String) -> Unit, modifier: Modifier = Modifier ){

    TextField(value = value,
        label = { Text( label ) },
        singleLine = true,
        keyboardOptions = KeyboardOptions( keyboardType = KeyboardType.Number ),
        onValueChange = onValueChange,
        modifier=modifier)
}

