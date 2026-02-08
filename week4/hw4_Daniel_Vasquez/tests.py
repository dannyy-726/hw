from hw4_firstname_lastname import  analyze_climate_data, rainfall_prediction, export_weather_predictions # !!!!! importatnt: replace  hw4_firstname_lastname.py with your actual name, your actual .py file




if __name__ == "__main__":
    print("Running tests for HW4:")
    
    # tests
    filename = "WeatherData.txt"
    destination_file= "WeatherDataForecast.csv"

    # Task 1 test
    result = analyze_climate_data(filename)
    print(f"Task 1 test resuts: {result}") 

    # Task 2 test
    result = rainfall_prediction(filename)
    print(f"Task 2 test resuts: {result}") 

    # Task 3 test
    export_weather_predictions(filename, destination_file)
    print(f"Task 3 test resuts: forecast exported to {destination_file}")

