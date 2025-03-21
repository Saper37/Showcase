package com.example.myapplication

import android.content.Context
import androidx.datastore.core.CorruptionException
import androidx.datastore.core.DataStore
import androidx.datastore.core.Serializer
import androidx.datastore.dataStore
import com.android4you.protodatastorel.FoodAlgoPreference
import com.android4you.protodatastorel.FoodPreference
import com.google.protobuf.InvalidProtocolBufferException
import kotlinx.coroutines.flow.Flow
import java.io.InputStream
import java.io.OutputStream

// TODO Not in use currently, code left for later development
private const val FOOD_PREFERENCE_NAME = "food_preference"
private const val FOODALGO_PREFERENCE_NAME = "foodalgo_preference"
private const val FOOD_STORE_FILE_NAME ="food_prefs.pb"
private const val FOODALGO__STORE_FILE_NAME = "foodalgo_prefs.pb"

private val Context.foodPreferenceStore: DataStore<FoodPreference> by dataStore( FOOD_STORE_FILE_NAME, serializer = FoodPreferenceSerializer )
private val Context.mealPreferenceStore: DataStore<FoodAlgoPreference> by dataStore( FOODALGO__STORE_FILE_NAME, serializer = MealPreferenceSerializer )


object FoodPreferenceSerializer : Serializer<FoodPreference> {
    override val defaultValue: FoodPreference = FoodPreference.getDefaultInstance( )
    override suspend fun readFrom( input: InputStream): FoodPreference {
        try{
            return FoodPreference.parseFrom( input )
        }catch ( exception: InvalidProtocolBufferException){
            throw CorruptionException( "Cannot read proto. ", exception )
        }
    }

    override suspend fun writeTo(t: FoodPreference, output: OutputStream) = t.writeTo( output )
}

object MealPreferenceSerializer : Serializer<FoodAlgoPreference> {
    override val defaultValue: FoodAlgoPreference = FoodAlgoPreference.getDefaultInstance( )
    override suspend fun readFrom( input: InputStream): FoodAlgoPreference {
        try{
            return FoodAlgoPreference.parseFrom( input )
        }catch ( exception: InvalidProtocolBufferException){
            throw CorruptionException( "Cannot read proto. ", exception )
        }
    }
    override suspend fun writeTo(t: FoodAlgoPreference, output : OutputStream) = t.writeTo( output )
}

class MealPreferenceRepository( private val mealStore: DataStore<FoodAlgoPreference>){
    private val store = mealStore

    suspend fun readData( ): Flow<FoodAlgoPreference> {
        val mealPreference: Flow<FoodAlgoPreference> = store.data
        return mealPreference
    }

    suspend fun readData( id: Int ): Flow<FoodAlgoPreference> {
        val mealPreference: Flow<FoodAlgoPreference> = store.data
        return mealPreference
    }

    suspend fun readData( name: String ): Flow<FoodAlgoPreference> {
        val mealPreference: Flow<FoodAlgoPreference> = store.data
        return mealPreference
    }

    suspend fun writeData( id: Int, name: String, mealNumber: Int, meals: MutableList<FoodPreference>  ){

    }
    suspend fun updateData( id: Int, name: String, mealNumber: Int, meal: MutableList<FoodPreference> ){

    }
}

class FoodPreferenceRepository( private val foodstore: DataStore<FoodPreference>){
    private val store = foodstore
    suspend fun readData( ): Flow<FoodPreference> {
        val mealPreference: Flow<FoodPreference> = store.data
        return mealPreference
    }

    suspend fun writeData( id: Int, name: String, cost: Float, macros: MutableList<Float> ){
        val food: FoodPreference =
            FoodPreference.newBuilder()
                .setId( id )
                .setName( name )
                .setCost( cost )
                .setMealnumber( -1 )
                .build( )
        food.macrosMap[ "calorie"] = macros.get( 0 )
        food.macrosMap[ "carbohydrate"] = macros.get( 1 )
        food.macrosMap[ "sugar"] = macros.get( 2 )
        food.macrosMap[ "nonsaturared"] = macros.get( 3 )
        food.macrosMap[ "saturated"] = macros.get( 4 )
        food.macrosMap[ "fiber"] = macros.get( 5 )
        food.macrosMap[ "proteine"] = macros.get( 6 )
        food.macrosMap[ "salt"] = macros.get( 7 )

    }
}