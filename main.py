# Working with Dictionaries
from pyscript import display


weather_today = {
    "location" : "Manila",
    "temperature_c" : 32,
    "humidity" : 78,
    "condition" : "Sunny"
} # Specifiying the weather today
weather_today['condition'] = 'Cloudy' # Updating the Value
weather_today['heat_index'] = '38' # adding another dictionary

display(weather_today, target='output') # Inputs the entire dictionary
display(weather_today['temperature_c'], target='output') # Displaying the number only

