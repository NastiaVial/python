import os
from datetime import datetime, timedelta, date
from HW4_part2 import lowercase_with_first_letter_in_uppercace
import random


# main class
class NewsPortal:
    def __init__(self, text: str, type_of_news='Breaking News') -> None:
        self.publish_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.type_of_news = type_of_news
        self.text = text

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(self.text)
            f.write(f"\n{self.publish_date}\n")
            f.write('-' * 43 + '\n')


# class for advertisements
class Advertisements(NewsPortal):
    def __init__(self, title: str, text: str, ads_duration_in_days) -> None:
        super().__init__(text)
        self.ads_duration_in_days = int(ads_duration_in_days)
        self.type_of_news = "Ads"
        self.title = title

# count exact expiration date for each advertisement
    def calculate_expiration_date(self):
        expiration_date = date.today() + timedelta(days=self.ads_duration_in_days)
        return expiration_date

# how many days left for the advertisement
#     def calculate_days_left(self):
#         return (self.calculate_expiration_date() - date.today()).days

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\nExpiration day of advertisement: {self.calculate_expiration_date()}\n")


# class for news with write_to_file function
class BreakingNews(NewsPortal):
    def __init__(self, title, text: str, city: str) -> None:
        super().__init__(text)
        self.city = city
        self.title = title

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\n{self.city} , {self.publish_date}\n")


# astrology class with write_to_file function
class Astrology(NewsPortal):
    def __init__(self, zodiac_sign: str, text: str) -> None:
        super().__init__(text)
        self.type_of_news = "Astrology"
        self.zodiac_sign = zodiac_sign
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
            f.write(f"Probability of horoscope prediction from 1 to 10: {self.prediction_number}\n")


class Weather(NewsPortal):
    def __init__(self, city: str, text: str) -> None:
        super().__init__(text)
        self.type_of_news = "Weather"
        self.city = city
        self.temperature = random.randint(1, 31)

    def weather_temperature(self):
        return self.temperature

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"Weather forecast for {self.city}\n")
            f.write(f"{self.text}\n")
            f.write(f"temperature +{self.temperature} Celsius degrees \n")


# class for auto filling news from file
class AutoFill:
    def __init__(self, code_number_of_news_for_autofill,
                 path=r"C:\Users\Anastasiya_Vial\PycharmProjects\pythonProject\autofill.txt"):
        self.code_number_of_news_for_autofill = code_number_of_news_for_autofill
        self.path = path

# read file and convert text to lowercase with first letter in uppercase using finunction from HW4
    def read_file(self):
        with open(self.path, 'r') as file:
            lines = [line.rstrip() for line in file]
        formatted_lines = []
        for item in lines:
            new_item = lowercase_with_first_letter_in_uppercace(item)
            formatted_lines.append(new_item)

# delete file after reading
        # if len(lines) > 0:
        #     os.remove(self.path)

        return formatted_lines

# after reading file, take exact news/advertisement/weather/astrology as per code number
    def write_to_file_from_autofill(self):
        formatted_lines = self.read_file()
        if self.code_number_of_news_for_autofill == 1:
            user_title = formatted_lines[2]
            user_city = formatted_lines[5]
            user_text = formatted_lines[8]
            news_item = BreakingNews(user_title, user_text, user_city)
        elif self.code_number_of_news_for_autofill == 2:
            user_title = formatted_lines[12]
            user_text = formatted_lines[15]
            user_expiration_time = formatted_lines[18]
            news_item = Advertisements(user_title, user_text, user_expiration_time)
        elif self.code_number_of_news_for_autofill == 3:
            user_city = formatted_lines[22]
            user_text = formatted_lines[23]
            news_item = Weather(user_city, user_text)
        elif self.code_number_of_news_for_autofill == 4:
            user_zodiac_sign = formatted_lines[26]
            user_text = formatted_lines[27]
            news_item = Astrology(user_zodiac_sign, user_text)
        if news_item:
            news_item.write_to_file()


# input function
def main():
    while True:
        need_news_input = input("Do you want to add something to NewsPortal?\nPrint Y for yes, N for no ")
        if need_news_input.upper() == "N":
            print("You chose NO. Program is finished.")
            break

        elif need_news_input.upper() != "N" and need_news_input.upper() != "Y":
            print("Only 'N' or 'Y' is possible. Please, Ty again\n")

        elif not need_news_input.upper().isalpha():
            print("Only letters are allowed!  Please, Ty again\n")

        elif need_news_input.upper() == "Y":
            try:
                manual_or_auto_fill = int(input("Add news manually - 1, add news from file - 2. \nPlease, enter your choice: "))
            except ValueError:
                print("Not a number, please try again")

            if manual_or_auto_fill == 1:
                try:
                    user_choice_input = int(input("Please choose code_number:\nNews - 1, Ads - 2, Weather - 3, Astrology - 4.\n"))
                except ValueError:
                    print("Not a number, please try again")

                news_feed_item = []
                if user_choice_input == 1:
                    user_title = input("Please, write the title:")
                    user_text = input("Please, write the text: ")
                    user_city = input("Please, write the city: ")
                    news_feed_item = BreakingNews(user_title.upper(), user_text.capitalize(), user_city.upper())
                    print("\nNews was successfully written to file\n")
                elif user_choice_input == 2:
                    user_title = input("Please, write the title:")
                    user_text = input("Please, write the text: ")
                    user_expiration_time = input("Please, write number of days for your add to last: ")
                    news_feed_item = Advertisements(user_title.upper(), user_text.capitalize(), user_expiration_time)
                    print("\nAdvertisement was successfully written to file\n")
                elif user_choice_input == 3:
                    user_city = input("Please, write the city: ")
                    user_text = input("Please, write the text: ")
                    news_feed_item = Weather(user_city.capitalize(), user_text.capitalize())
                    print("\nNews for weather was written to file\n")
                elif user_choice_input == 4:
                    user_zodiac_sign = input("Please, write zodiac_sign: ")
                    user_text = input("Please, write the text: ")
                    news_feed_item = Astrology(user_zodiac_sign.upper(), user_text.capitalize())
                    print("\nAstrological horoscope was successfully written to file\n")

                if news_feed_item:
                    news_feed_item.write_to_file()
                else:
                    print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")

            elif manual_or_auto_fill == 2:
                try:
                    path = input("Please, provide path to your file. Press enter to use default path.\n")
                except ValueError:
                    print("not correct path, please try again\n")
                try:
                    user_choice_autofill = int(input("Please choose code_number for autofill:\nNews - 1, Ads - 2, Weather - 3, Astrology - 4.\n"))
                except ValueError:
                    print("Not a number, please try again\n")
                autofill_file = []
                if user_choice_autofill == 1 and path == '':
                    autofill_file = AutoFill(1)
                    print("\nNews was successfully written to file\n")
                elif user_choice_autofill == 2 and path == '':
                    autofill_file = AutoFill(2)
                    print("\nAdvertisement was successfully written to file\n")
                elif user_choice_autofill == 3 and path == '':
                    autofill_file = AutoFill(3)
                    print("\nNews for weather was written to file\n")
                elif user_choice_autofill == 4 and path == '':
                    autofill_file = AutoFill(4)
                    print("\nAstrological horoscope was successfully written to file\n")
                elif user_choice_autofill == 1 and path != '':
                    autofill_file = AutoFill(1, path=path)
                    print("\nNews was successfully written to file\n")
                elif user_choice_autofill == 2 and path != '':
                    autofill_file = AutoFill(2, path=path)
                    print("\nAdvertisement was successfully written to file\n")
                elif user_choice_autofill == 3 and path != '':
                    autofill_file = AutoFill(3, path=path)
                    print("\nNews for weather was written to file\n")
                elif user_choice_autofill == 4 and path != '':
                    autofill_file = AutoFill(4, path=path)
                    print("\nAstrological horoscope was successfully written to file\n")
                if autofill_file:
                    autofill_file.write_to_file_from_autofill()
                else:
                    print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")

            else:
                print("Only 1 or 2 is possible. Please try again\n")


main()