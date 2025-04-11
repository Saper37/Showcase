package com.example.myapplication

import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.CheckBox
import android.widget.EditText
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView

/*
TODO Add more relevant comparisons to compactor, at this point all of the adapter could have better comparisons.
 */
/*
 AppList Adapter not used at the moment. Possibly in the future,
 */
class AppMealListAdapter : ListAdapter<Meal, AppMealListAdapter.AppViewHolder>( AppMealComparator( ) ){
    private var checkboxes = mutableListOf<CheckBox>( )
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int ) : AppViewHolder{
        return AppViewHolder.create( parent )
    }
    override fun onBindViewHolder( holder: AppViewHolder, position: Int ){
        val current = getItem( position )
        holder.bind( current.meal_day )


    }
    class AppViewHolder( itemView: View) : RecyclerView.ViewHolder( itemView ){
        private val mealItemView: TextView = itemView.findViewById( R.id.recycler_view_textView )
        private val checkItemView: CheckBox = itemView.findViewById( R.id.add_meal_item_checkbox )

        fun bind( text: String? ){
            mealItemView.text = text
            checkItemView.isChecked = false

        }
        companion object {
            fun create(parent: ViewGroup): AppViewHolder {
                val view: View = LayoutInflater.from(parent.context)
                    .inflate(R.layout.recyclerview_item, parent, false)
                Log.d( "Applister", "Appmeal companion created")
                return AppViewHolder(view)
            }
        }

    }
    class AppMealComparator : DiffUtil.ItemCallback<Meal>( ){
        override fun areItemsTheSame(oldItem: Meal, newItem: Meal): Boolean {
            return oldItem == newItem
        }
        override fun areContentsTheSame(oldItem: Meal, newItem: Meal): Boolean {
            return oldItem.meal_day == newItem.meal_day && oldItem.cost == newItem.cost
        }
        fun areItemsTheSame( oldItem: Food, newItem: Food ): Boolean{
            return oldItem == newItem
        }
        fun areContentsTheSame( oldItem: Food, newItem: Food): Boolean{
            return oldItem.name == newItem.name
        }

    }


}

class AppFoodListAdapter : ListAdapter<Food, AppFoodListAdapter.AppFoodViewHolder>( AppFoodComparator( ) ) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): AppFoodViewHolder {
        return AppFoodViewHolder.create(parent)
    }

    override fun onBindViewHolder( holder: AppFoodViewHolder, position: Int) {
        val current = getItem(position)
        //var ( id, name, cost, macros ) = current
        //var foodName = name + " | " + cost + " | " + macros.ToString()
        holder.bind( current )
    }

    class AppFoodViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val foodItemView: TextView = itemView.findViewById(R.id.recycler_view_textView)
        private val checkItemView: CheckBox = itemView.findViewById( R.id.add_meal_item_checkbox )
        private val caloreInfoView: TextView = itemView.findViewById( R.id.add_food_information_calore )
        private val carboInfoView: TextView = itemView.findViewById( R.id.add_food_information_carbo )
        private val sugarInfoView: TextView = itemView.findViewById( R.id.add_food_information_sugar )
        private val nsfatInfoView: TextView = itemView.findViewById( R.id.add_food_information_nsfat )
        private val sfatinfoView: TextView = itemView.findViewById( R.id.add_food_information_sfat )
        private val fiberinfoView: TextView = itemView.findViewById( R.id.add_food_information_fiber )
        private val proteineinfoView: TextView = itemView.findViewById( R.id.add_food_information_proteine )
        private val saltinfoView: TextView = itemView.findViewById( R.id.add_food_information_salt )



        fun bind(food: Food?) {
            if ( food != null ){
                foodItemView.text = food.name
                checkItemView.isChecked = false
                var macro: Macros = food.macros
                caloreInfoView.setText( macro.calore.toString( ) )
                carboInfoView.setText( macro.carbohydrate.toString( ) )
                sugarInfoView.setText( macro.sugar.toString( ) )
                nsfatInfoView.setText( macro.nonsaturatedFat.toString( ) )
                sfatinfoView.setText( macro.saturatedFat.toString( ) )
                fiberinfoView.setText( macro.fiber.toString( ) )
                proteineinfoView.setText( macro.proteine.toString( ) )
                saltinfoView.setText( macro.salt.toString( ) )

            }

        }

        companion object {
            fun create(parent: ViewGroup): AppFoodViewHolder {
                val view: View = LayoutInflater.from(parent.context)
                    .inflate(R.layout.recyclerview_item, parent, false)
                Log.d( "Applister", "Appfood companion created")
                return AppFoodViewHolder(view)
            }
        }

    }

    class AppFoodComparator : DiffUtil.ItemCallback<Food>() {
        override fun areItemsTheSame(oldItem: Food, newItem: Food): Boolean {
            return oldItem == newItem
        }

        override fun areContentsTheSame(oldItem: Food, newItem: Food): Boolean {
            return oldItem.name == newItem.name
        }

    }
}