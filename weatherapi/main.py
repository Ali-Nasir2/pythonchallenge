
from weather_api import get_weather, get_wea_dtls, Weather


def main():
    user_city: str = input('Enter the city you wan to get the weather of: ')

    curr_weather: dict = get_weather(user_city)
    weather_dtl: list[Weather] = get_wea_dtls(curr_weather)

    dmy: str = '%d/%m/%y'
    days: list[str] = sorted({f'{date.date:{dmy}}' for date in weather_dtl})

    for day in days:
        print(day)
        print('---')

        grouped: list[Weather] = [current for current in weather_dtl if f'{current.date:{dmy}}' == day]
        for element in grouped:
            print(element)

        print()  


if __name__ == '__main__':
    main()
