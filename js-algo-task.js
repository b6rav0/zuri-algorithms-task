function convertFahrtoCelsius(fahr_val) {
    /*
    Convert a temperature value in Fahrenheit to degree Celsius.

    returns a number to four decimal places
    returns an error message if the input isn't a number
    */
    var celsius_val, fahr_val_type;
    try {
        fahr_val_type = typeof(fahr_val);      
        fahr_val = Number.parseInt(fahr_val);
        celsius_val = ((fahr_val - 32) * (5 / 9));
        celsius_val = celsius_val.toFixed(4);
        return celsius_val;
    } catch(e) {
        return [fahr_val + " is not a valid number but a/an " + fahr_val_type];
    }
}
console.log(convertFahrtoCelsius(50));
