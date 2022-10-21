from datetime import datetime, timedelta, date
import random


class NewsPortal:
    def __init__(self) -> None:
        self.publish_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.type_of_news = "BreakingNews"
        self.text = input("Please write a text: \n")

    def write_to_file(self):
        with open("testnews.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(self.text)
            f.write(f"\n{self.publish_date}\n")
            f.write('-' * 43 + '\n')


class Advertisements(NewsPortal):
    def __init__(self) -> None:
        super().__init__()
        self.type_of_news = "Ads"
        self.title = input("Please write a title: \n").upper()
        self.ads_duration_in_days = int(input("Please, write number of days for your add to last: \n"))

    def calculate_expiration_date(self):
        expiration_date = date.today() + timedelta(days=self.ads_duration_in_days)
        return expiration_date

    def write_to_file(self):
        with open("testnews.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\nActual till: {self.calculate_expiration_date()}\n")
        print("\nAdvertisement was successfully written to file\n")


class BreakingNews(NewsPortal):
    def __init__(self) -> None:
        super().__init__()
        self.type_of_news = "BreakingNews"
        self.title = input("Please write a title: \n").upper()
        self.city = input("Please, write the city: \n").upper()

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\n{self.city} , {self.publish_date}\n")
        print("News was successfully written to file\n")


class Astrology(NewsPortal):
    def __init__(self) -> None:
        super().__init__()
        self.type_of_news = "Astrology"
        self.zodiac_sign = input("Please, write zodiac sign: \n").upper()
        self.horoscope_for_today = datetime.now().strftime("%d-%m-%Y")
        self.prediction_number = random.randint(0, 10)

    def prediction_probability(self):
        return self.prediction_number

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"Happy horoscope for today: {self.horoscope_for_today}\n")
            f.write(f"Zodiac sign: {self.zodiac_sign}\n")
            f.write(f"{self.text}\n")
            f.write(f"Probability of horoscope prediction from 1 to 10: {self.prediction_probability()}\n")
        print("\nAstrological horoscope was successfully written to file\n")


class Weather(NewsPortal):
    def __init__(self) -> None:
        super().__init__()
        self.type_of_news = "Weather"
        self.city = input("Please, write the city: \n").upper()
        self.temperature = random.randint(1, 31)

    def weather_temperature(self):
        return self.temperature

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"Weather forecast for {self.city}\n")
            f.write(f"{self.text}\n")
            f.write(f"temperature +{self.weather_temperature()} Celsius degrees \n")
        print("\nNews for weather was written to file\n")


def main():
    while True:
        need_news_input = input("Do you want to add ads/news/weather/astrology?\nPrint Y for yes, N for no ")
        if need_news_input.upper() == "N":
            print("You chose NO. Program is finished.")
            break
        elif not need_news_input.upper().isalpha():
            print("Only letters are allowed!  Please, Ty again\n")

        elif need_news_input.upper() != "N" and need_news_input.upper() != "Y":
            print("Only 'N' or 'Y' is possible. Please, Ty again\n")

        elif need_news_input.upper() == "Y":
            try:
                user_choice_input = int(input("News - 1, Ads - 2, Weather - 3, Astrology - 4.\nPlease, make your choice: "))
            except ValueError:
                print("Not a valid number, please try again\n")
            if user_choice_input == 1:
                return BreakingNews()
            elif user_choice_input == 2:
                return Advertisements()
            elif user_choice_input == 3:
                return Weather()
            elif user_choice_input == 4:
                return Astrology()
            else:
                print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")


main()