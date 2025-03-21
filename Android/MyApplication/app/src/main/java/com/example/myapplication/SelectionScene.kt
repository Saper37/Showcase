package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.activity.ComponentActivity
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.input.KeyboardType
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.commit
import androidx.fragment.app.replace
import androidx.navigation.Navigation
import org.w3c.dom.Text
import kotlin.math.sqrt
/*
Scene responsible for bmi calculations
 Variables for holding the values of the fields,
 TODO add storage for the values and read functionalities


 */
//@Composable
//internal fun SelectionScene( navController: NavController, mealadapter: AppMealListAdapter)

internal class SelectionScene(  ) : Fragment( R.layout.fragment_selection ) {

    override fun onCreateView(inflater: LayoutInflater, parent: ViewGroup?, savedInstanceState: Bundle? ): View? {
        Log.d( "SelectionScene", "Selection onCreateView")
        return inflater.inflate( R.layout.fragment_selection , parent, false )
    }
    override fun onStop( ){
        var returnButton: Button? = view?.findViewById( R.id.selection_returnbutton )
        var caloreTextView : TextView? = view?.findViewById( R.id.selectiontext )
        if( returnButton != null )
            returnButton.visibility = View.INVISIBLE
        if( caloreTextView != null )
            caloreTextView.visibility = View.INVISIBLE
        super.onStop( )
        Log.d( "CaloreScene", "onStop " + returnButton?.visibility + " " + caloreTextView?.visibility )
        super.onStop()
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle? ){
        Log.d( "SelectionScene", "Selection onVIewCreated")
        var returnButton: Button = view.findViewById( R.id.selection_returnbutton )
        var titleText: TextView = view.findViewById( R.id.selectiontext )
        val navController = Navigation.findNavController( view )
        titleText.visibility = View.VISIBLE
        returnButton.setOnClickListener{
            titleText.visibility = View.INVISIBLE
            returnButton.visibility = View.INVISIBLE
            navController.navigate( R.id.action_selectionScene_to_mainScene )
            /*childFragmentManager.commit{
                setReorderingAllowed( true )
                replace<MainScene>( R.id.fragment_container, "MainScene" )
            }*/

        }
        
    }


    /*
    Column(
        modifier = Modifier
            .statusBarsPadding()
            .padding(horizontal = 5.dp, vertical = 5.dp)
            .verticalScroll(rememberScrollState())
            .safeDrawingPadding(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Top
    ) {

        Column(
            verticalArrangement = Arrangement.Top

        ) {

            Button(onClick = { navController.navigate(Scene.MainScene.name) }) {
                Text(text = "Back")
            }
        }
        if (mealList != null) {
            Column( ) {
                for (meal in mealList) {
                    var name = meal.name
                    var cost = meal.cost
                    Row(
                        modifier = Modifier
                            .padding( 2.dp),

                    ) {
                        OutlinedTextField(
                            modifier = Modifier
                                .widthIn( 40.dp ),
                            value = name,
                            onValueChange = { name = it },
                            label = { Text("name") })

                        OutlinedTextField(
                            modifier = Modifier
                                .widthIn( 40.dp ),
                            value = cost.toString(),
                            onValueChange = { cost = it.toDouble() },
                            label = { Text("cost") })
                        Box(
                            modifier = Modifier


                        ){
                            Button(
                                modifier = Modifier
                                    .padding(horizontal = 1.dp, vertical = 1.dp)
                                    .widthIn( 80.dp ),
                                onClick= {}

                            ){
                                Text( "BOX")
                            }
                        }

                    }
                }
            }
        }
    }*/
}

@Composable
private fun EditTextFieldWeight(value: String, onValueChange: (String) -> Unit, modifier: Modifier = Modifier ){

    TextField(value = value,
        label = { Text( stringResource(id =R.string.calculate_weight ) ) },
        singleLine = true,
        keyboardOptions = KeyboardOptions( keyboardType = KeyboardType.Number ),
        onValueChange = onValueChange,
        modifier=modifier)
}
@Composable
private fun EditTextHeight( value: String, onValueChange: (String ) -> Unit, modifier: Modifier ){

    TextField(value = value,
        label = { Text( stringResource(id =R.string.calculate_height, "" ) ) },
        singleLine = true,
        keyboardOptions = KeyboardOptions( keyboardType = KeyboardType.Number ),
        onValueChange = onValueChange,
        modifier=modifier)
}
@Composable
private fun ResultTextField( value: String, onValueChange: ( String ) -> Unit, modifier: Modifier ){

    TextField(value = value,
        label = { Text( stringResource(id =R.string.bmi_string, "" )  ) },
        singleLine = true,
        keyboardOptions = KeyboardOptions( keyboardType = KeyboardType.Number ),
        onValueChange = onValueChange, //{fieldvalue = it },
        modifier=modifier)
}
@Composable
private fun calculateBMI( height: String, weight: String ) : Float{

    val fheight : Float = height.toFloatOrNull( ) ?: 1.0f
    val fweight : Float = weight.toFloatOrNull( ) ?: 1.0f
    return fweight / sqrt( fheight )

}