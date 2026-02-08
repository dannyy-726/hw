import csv

# Task 1 function
def analyze_climate_data(filename:str)-> (int, int, float, float, float, float):
    # implement function here
    total_days = 0
    days_with_precipitation = 0
    lowest_temp = None
    highest_temp = None
    total_humidity = 0
    total_percipitation = 0
    mean_humidity = 0
    mean_percipitation = 0

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if not line or len(line) != 4:
                continue

            min_temp = float(line[0])
            max_temp = float(line[1])
            humidity = float(line[2])
            percipitation = float(line[3])
            total_days +=1
            total_humidity += humidity
            total_percipitation += percipitation

            if percipitation > 0:
                days_with_precipitation +=1
            if lowest_temp is None:
                lowest_temp = min_temp
            elif min_temp < lowest_temp:
                lowest_temp = min_temp
            if highest_temp is None:
                highest_temp = max_temp
            elif max_temp > highest_temp:
                highest_temp = max_temp

    if total_days > 0:
        mean_humidity = round(total_humidity / total_days, 2)
        mean_percipitation = round(total_percipitation / total_days, 2)

    return total_days, days_with_precipitation, lowest_temp, highest_temp, mean_humidity, mean_percipitation
             
    

# Task 2 function
def rainfall_prediction(filename:str)-> (int, int):
    # implement function here
    with open(filename,'r') as f:
        reader = csv.reader(f)
        
        days_of_rain = 0
        correct_predictions = 0
        
        for line in reader:
            if not line or len(line) != 4:
                continue
        
            min_temp = float(line[0])
            max_temp = float(line[1])
            humidity = float(line[2])
            percipitation = float(line[3])

            predicted_rainy = (max_temp - min_temp) > 10 and humidity > 50

            if predicted_rainy:
                days_of_rain += 1
            if (predicted_rainy and percipitation > 0) or (not(predicted_rainy) and percipitation == 0):
                correct_predictions += 1
    return days_of_rain, correct_predictions
            

# Task 3 function
def export_weather_predictions(source_file: str, destination_file: str) -> None:
    # implement function here
    with open(source_file,'r') as src, open(destination_file,'w',newline='') as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst)

        forecast = None
        writer.writerow(
            ["Minimum Temperature","Maximum Temperature","Humidity","Percipitation","Forecast"])

        for line in reader:
            if not line or len(line) != 4:
                continue
            
            min_temp = float(line[0])
            max_temp = float(line[1])
            humidity = float(line[2])
            percipitation = float(line[3])

            if (max_temp - min_temp) > 10 and humidity > 50:
                writer.writerow([min_temp,max_temp,humidity,percipitation,'rainy'])
            else:
                writer.writerow([min_temp,max_temp,humidity,percipitation,'sunny'])




