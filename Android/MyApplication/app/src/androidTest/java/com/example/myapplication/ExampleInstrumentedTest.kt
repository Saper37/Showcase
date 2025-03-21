package com.example.myapplication

import android.util.Log
import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.ext.junit.runners.AndroidJUnit4

import org.junit.Test
import org.junit.runner.RunWith

import org.junit.Assert.*

/**
 * Instrumented test, which will execute on an Android device.
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
@RunWith(AndroidJUnit4::class)
class ExampleInstrumentedTest {
    @Test
    fun useAppContext() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.myapplication", appContext.packageName)
    }
    @Test
    fun testMacroConversion( ){
        val converter = Converters( )
        var macros = Macros(macroid = 1, calore = 1, carbohydrate = 1, sugar = 1,
            nonsaturatedFat = 1, saturatedFat = 1,
            proteine = 1, fiber = 1, salt = 1)
        var comparisonString = "1 1 1 1 1 1 1 1 1 "
        Log.d( "testing macros ", macros.ToString( ).compareTo( comparisonString ).toString() )
        assertTrue( converter.ToString( macros )?.compareTo( comparisonString ) == 0 )
    }
    @Test
    fun testFoodConversion( ){
        val converter = Converters( )

        var macros = Macros(macroid = 1, calore = 1, carbohydrate = 1, sugar = 1,
            nonsaturatedFat = 1, saturatedFat = 1,
            proteine = 1, fiber = 1, salt = -1)

        var food = Food(foodid = 1, name = "lenkki", cost = 1.0, macros = macros )
        var foodlist = listOf( food )
        var foodcompString = "1 lenkki 1.0 1 1 1 1 1 1 1 1 -1 "

        assertTrue( converter.ToString( foodlist )?.compareTo( foodcompString ) == 0 )
    }
    @Test
    fun stringToMacroConversion( ){
        val converter = Converters( )
        var macros = Macros(macroid = 1, calore = 1, carbohydrate = 1, sugar = 1,
            nonsaturatedFat = 1, saturatedFat = 1,
            proteine = 1, fiber = 1, salt = 1)
        var comparisonString = "1 1 1 1 1 1 1 1 1 "
        Log.d( "testing macros ", macros.ToString( ).compareTo( comparisonString ).toString() )
        assertTrue( converter.ToString( macros )?.compareTo( comparisonString ) == 0 )

    }
    @Test
    fun stringToFoodConversion( ){
        val converter = Converters( )

        var macros = Macros(macroid = 1, calore = 1, carbohydrate = 1, sugar = 1,
            nonsaturatedFat = 1, saturatedFat = 1,
            proteine = 1, fiber = 1, salt = -1)

        var food = Food(foodid = 1, name = "lenkki", cost = 1.0, macros = macros )
        var foodlist = listOf( food )
        var foodcompString = converter.ToString( foodlist )
        var newlist = converter.StringToFood( foodcompString )
        var newstring = converter.ToString( newlist )
        assertFalse( foodcompString != null )
        assertFalse( newstring != null )
        if ( foodcompString != null && newstring != null )
            assertTrue( foodcompString.compareTo( newstring ) == 0 )
    }
}