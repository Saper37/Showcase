package com.example.myapplication

import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.commit
import androidx.fragment.app.replace
import androidx.fragment.app.viewModels
import androidx.lifecycle.Observer
import androidx.navigation.Navigation
import androidx.navigation.fragment.NavHostFragment


/*
A main hub for navigation between scenes, possible to use for something else
TODO Adding the actual functionalities?
 */

class MainScene: Fragment( R.layout.fragment_mainscene ) {
    private lateinit var mealAdapter: AppMealListAdapter
    private lateinit var foodAdapter: AppFoodListAdapter

    val visibilityModel: VisibilityInfo by viewModels( )

    //private val mealrecyclerView = findViewById<RecyclerView>(R.id.recyclerview)
    //private val foodrecyclerView = findViewById<RecyclerView>(R.id.recyclerview)


    

    override fun onCreateView(inflater: LayoutInflater, parent: ViewGroup?, savedInstanceState: Bundle? ): View? {
        var visibilityData = visibilityModel.getData().value
        Log.d("CaloreScene visibilityData value ", visibilityData.toString())
        return inflater.inflate(R.layout.fragment_mainscene, parent, false)
    }

    override fun onViewCreated( view: View, savedInstanceState: Bundle? ) {

        val caloreButton: Button = view.findViewById( R.id.calore_scene_button )
        val selectionButton: Button = view.findViewById( R.id.selection_scene_button)
        val infoButton: Button = view.findViewById( R.id.info_scene_button)
        val navController = Navigation.findNavController( view )

        //val navigationHost = getSupportFragmentManager( ).findFragmentById(R.id.nav_host_fragment) as NavHostFragment
        //val navController = navigationHost.navController
        //visibilityModel.visibilityData.observe( , Observer { visibility -> } )

        Log.d( "ButtonACTIVITY", "starts calorebutton")
        caloreButton.setOnClickListener{
            caloreButton.visibility = View.GONE
            selectionButton.visibility = View.GONE
            infoButton.visibility = View.GONE
            /*childFragmentManager.commit{
                setReorderingAllowed( true )
                replace<CaloreScene>( R.id.fragment_container, "calore_fragment"  )
            }*/
            Log.d( "MainScene", "move to calore")
            navController.navigate( R.id.action_mainScene_to_caloreScene )
        }
        Log.d( "ButtonACTIVITY", "starts selectionbutton")
        selectionButton.setOnClickListener{

            /*childFragmentManager.commit{
                replace<SelectionScene>( R.id.fragment_container, "selection_fragment"  )
                setReorderingAllowed( true )
            }*/
            caloreButton.visibility = View.INVISIBLE
            selectionButton.visibility = View.INVISIBLE
            infoButton.visibility = View.INVISIBLE
            navController.navigate( R.id.action_mainScene_to_selectionScene )
            Log.d( "MainScene", "selection pressed" )
            //if( selectionscene.visibility == View.INVISIBLE )
            //   selectionscene.visibility = View.VISIBLE
        }
        Log.d( "ButtonACTIVITY", "starts infobutton")
        infoButton.setOnClickListener{
            /*childFragmentManager.commit{
                replace<InfoScene>( R.id.fragment_container, "info_fragment"  )
                setReorderingAllowed( true )
            }*/
            navController.navigate( R.id.action_mainScene_to_infoScene )
            caloreButton.visibility = View.INVISIBLE
            selectionButton.visibility = View.INVISIBLE
            infoButton.visibility = View.INVISIBLE
            //if( infoscene.visibility == View.INVISIBLE )
            //   infoscene.visibility = View.VISIBLE
        }
        Log.d( "ButtonACTIVITY", "buttons done")

    }
    fun setVisibile(){
        val caloreButton: Button? = view?.findViewById( R.id.calore_scene_button )
        val selectionButton: Button? = view?.findViewById( R.id.selection_scene_button)
        val infoButton: Button? = view?.findViewById( R.id.info_scene_button)
        if ( caloreButton != null )
            caloreButton.visibility = View.VISIBLE
        if ( selectionButton != null )
            selectionButton.visibility = View.VISIBLE
        if ( infoButton != null )
            infoButton.visibility = View.VISIBLE

    }

    fun setAdapter( mealAdapter: AppMealListAdapter, foodAdapter: AppFoodListAdapter ){
        this.mealAdapter = mealAdapter
        this.foodAdapter = foodAdapter
    }



}
    /*
    public override fun onCreate( savedInstanceState: Bundle? ){
        super.onCreate(savedInstanceState)
        setContentView( R.layout.fragment_mainscene.xml.xml )
        var infoScene = findViewById<Button>(R.id.info_scene)

        var caloreScene = findViewById<Button>( R.id.calore_scene )
        var selectionScene = findViewById<Button>( R.id.selection_scene )

        val startForResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
            if (result.resultCode == Activity.RESULT_OK) {
                val intent = result.data

            }
        }
        infoScene.setOnClickListener{
            Log.d( "MainScene Click", "InfoScene is pressed")
            var infointent = Intent( this, InfoScene::class.java)
            startForResult.launch( infointent )
        }
        caloreScene.setOnClickListener{

        }
        selectionScene.setOnClickListener{

        }
    }
    public override fun onStop(  ){
        super.onStop( )
    }
    public override fun onPause( ){
        super.onPause( )
    }
    fun setAdapter( foodAdapter: AppFoodListAdapter, mealListAdapter: AppMealListAdapter ){
        this.mealadapter = mealListAdapter
        this.foodAdapter = foodAdapter
    }
}

     */
    /*
    Column(
        modifier = Modifier
            .statusBarsPadding()
            .padding(horizontal = 10.dp)
            .verticalScroll(rememberScrollState())
            .safeDrawingPadding()
    ){
        Button( onClick= {
            navController.navigate( Scene.SelectionScene.name )
        }){
            Text( text="hello! to Selection ")
        }
        Button( onClick= {
            navController.navigate( Scene.CalorieScene.name )
        }
        ){
            Text( text="Hello! To Calore scene")
        }
        Button( onClick= {
            navController.navigate( Scene.InfoScene.name )
        }
        ){
            Text( text="Hello! To Info Scene")
        }
    }

     */