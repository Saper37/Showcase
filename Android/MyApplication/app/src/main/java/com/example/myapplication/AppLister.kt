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

    override fun onBindViewHolder(holder: AppFoodViewHolder, position: Int) {
        val current = getItem(position)
        var ( id, name, cost, macros ) = current
        var foodName = name + " | " + cost + " | " + macros.ToString()
        holder.bind( name )
        holder.bind( cost.toString() )



    }

    class AppFoodViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val foodItemView: TextView = itemView.findViewById(R.id.recycler_view_textView)
        private val checkItemView: CheckBox = itemView.findViewById( R.id.add_meal_item_checkbox )
        private val caloreView: EditText = itemView.findViewById( R.id.recycerview_item_text_calore )
        private val carboView: EditText = itemView.findViewById( R.id.recycerview_item_text_carbohydrate )
        private val sugarView: EditText = itemView.findViewById( R.id.recycerview_item_text_sugar )
        private val nsatfView: EditText = itemView.findViewById( R.id.recycerview_item_text_nonsaturatedfat )
        private val satfView: EditText = itemView.findViewById( R.id.recycerview_item_text_saturatedfat )

        fun bind(text: String?) {
            foodItemView.text = text
            checkItemView.isChecked = false
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