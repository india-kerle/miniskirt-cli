import typer
from typing import Dict, Literal
import requests
import logging as logger
from rich.console import Console

wear_a_mini = typer.Typer()
console = Console()

units_dict = {
    'metric': 'Celcius',
    'imperial': 'Fahrenheit'
}

def get_temperature(location:str, units: Literal['metric', 'imperial'] = 'metric') -> Dict[str, str]:
    """Function to get weather information about a location.
    Args:
        location (str): Name of the location
        units (str): Units to get temperation information in. 
                        Can be metric or imperial. Defaults to metric.
    
    Returns:
        weather_data (Dict[str, str]): Dictionary of weather information 
                                        for a given location. 
    """

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=2efb43dd01211ac841d0df229565a0c8&units={units}"
    
    response = requests.get(weather_url)

    weather_data = {}
    if response.ok:
        if not 'error' in list(response.json().keys()):
            data = response.json()
            weather_data['description'] = ' and '.join([i['description'] for i in data['weather']])
            weather_data['feels_like'] = f"{data['main']['feels_like']} {units_dict[units]}"
        else:
            console.log(f'[bold red]Weather API call failed - {response.json()["error"]} status code')
    else:
        console.log(f'[bold red]Weather API call failed - {response.status_code} status code')
    
    return weather_data


@wear_a_mini.command()
def should_i(location: str,
            units: str = typer.Option("metric", help="Unit of temperature measurement. Defaults to 'metric'.")):
    """Function to declare if you should wear a miniskirt or not.
        Prints if you should or shouldn't based on mini_thresh.
    """
    if units == "imperial":
        weather_data = get_temperature(location, "imperial")
        mini_thresh = 77
    else:
        weather_data = get_temperature(location, "metric")
        mini_thresh = 25

    feels_like_temp = float(weather_data['feels_like'].split(' ')[0])
    
    weather_report_str = f"Today's weather is {weather_data['description']}. It feels like {weather_data['feels_like']}."
    
    console.rule("[bold red]Mini Skirt Decision")
    if feels_like_temp > mini_thresh:
        console.print(f"{weather_report_str}. Get in a mini! :dancers:", style="bold red")   
    elif feels_like_temp < mini_thresh:
        console.print(f"{weather_report_str}. I reckon it's too cold for one :tired_face:", style="bold blue") 
    
    console.print(locals())

if __name__ == "__main__":
    wear_a_mini()