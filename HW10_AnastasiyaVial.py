import os
from datetime import datetime, timedelta, date
from HW4_part2 import lowercase_with_first_letter_in_uppercace
from HW7_AnastasiyaVial import count_worlds_and_letters
import random
import json
import xml.etree.ElementTree as ET
import pyodbc


# main class
class NewsPortal:
    def __init__(self, text: str, type_of_news='Breaking News') -> None:
        self.publish_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.type_of_news = type_of_news
        self.text = text

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + " " + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(self.text)
            f.write(f"\n{self.publish_date}\n")
            f.write('-' * 43 + '\n')

    def write_to_sql(self):
        with pyodbc.connect('DRIVER=SQLite3 ODBC Driver;'
                            'DATABASE= news.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT into ads "
                               "VALUES('{}', '{}', '{}')".format(self.publish_date, self.type_of_news, self.text))
            except Exception as error:
                print("Duplicates are not allowed. Please try again", error)
            else:
                print("News were added to database")


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
            f.write(f"\n\n{self.type_of_news}" + " " + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\nExpiration day of advertisement: {self.calculate_expiration_date()}\n")

    def write_to_sql(self):
        with pyodbc.connect('DRIVER=SQLite3 ODBC Driver;'
                            'DATABASE= news.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT into ads "
                               "VALUES('{}', '{}', '{}', '{}', '{}')".format(self.publish_date, self.type_of_news,
                                                                             self.title, self.text, self.ads_duration_in_days))
            except Exception as error:
                print("Duplicates are not allowed. Please try again", error)
            else:
                print("advertisement was added to database")


# class for news with write_to_file function
class BreakingNews(NewsPortal):
    def __init__(self, title, text: str, city: str) -> None:
        super().__init__(text)
        self.city = city
        self.title = title

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + " " + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\n{self.city} , {self.publish_date}\n")

    def write_to_sql(self):
        with pyodbc.connect('DRIVER=SQLite3 ODBC Driver;'
                            'DATABASE= news.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT into breaking_news "
                               "VALUES('{}', '{}', '{}', '{}', '{}')".format(self.publish_date, self.type_of_news, self.title, self.text, self.city))
            except Exception as error:
                print("Duplicates are not allowed. Please try again", error)
            else:
                print("News were added to database")


# astrology class with write_to_file function
class Astrology(NewsPortal):
    def __init__(self, zodiac_sign: str, text: str) -> None:
        super().__init__(text)
        self.type_of_news = "Astrology"
        self.zodiac_sign = zodiac_sign
        self.horoscope_for_today = datetime.now().strftime("%d-%m-%Y")
        self.prediction_number = random.randint(1, 10)

    def prediction_probability(self):
        return self.prediction_number

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + " " + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"Happy horoscope for today: {self.horoscope_for_today}\n")
            f.write(f"Zodiac sign: {self.zodiac_sign}\n")
            f.write(f"{self.text}\n")
            f.write(f"Probability of horoscope prediction from 1 to 10: {self.prediction_number}\n")

    def write_to_sql(self):
        with pyodbc.connect('DRIVER=SQLite3 ODBC Driver;'
                            'DATABASE= news.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT into astrology "
                               "VALUES('{}', '{}', '{}', '{}')".format(self.publish_date, self.type_of_news, self.text, self.zodiac_sign))
            except Exception as error:
                print("Duplicates are not allowed. Please try again", error)
            else:
                print("Astrology horoscope was added to database")


class Weather(NewsPortal):
    def __init__(self, city: str, text: str) -> None:
        super().__init__(text)
        self.type_of_news = "Weather"
        self.city = city
        self.temperature = random.randint(1, 31)

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + " " + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"Weather forecast for {self.city}\n")
            f.write(f"{self.text}\n")
            f.write(f"temperature +{self.temperature} Celsius degrees \n")

    def write_to_sql(self):
        with pyodbc.connect('DRIVER=SQLite3 ODBC Driver;'
                            'DATABASE= news.db') as conn:
            cursor = conn.cursor()
            # query = {self.publish_date}, {self.type_of_news}, {self.text}, {self.city}
            # print(query)
            try:
                cursor.execute("INSERT into weather VALUES('{}', '{}', '{}', '{}')".format(self.publish_date, self.type_of_news, self.text, self.city))
            except Exception as error:
                print("Duplicates are not allowed. Please try again", error)
            else:
                print("News for weather were added to database")


# class for autofilling news from file
class AutoFill:
    def __init__(self, code_number_of_news_for_autofill, path=os.path.realpath("autofill1.txt")):
        self.code_number_of_news_for_autofill = code_number_of_news_for_autofill
        self.path = path

    # read file and convert text to lowercase with first letter in uppercase using function from HW4
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
        for i in range(int(self.code_number_of_news_for_autofill)):
            if formatted_lines[0] == "1":
                user_title = formatted_lines[1]
                user_city = formatted_lines[2]
                user_text = formatted_lines[3]
                BreakingNews(user_title, user_text, user_city).write_to_file()
                formatted_lines = formatted_lines[4:]
                print("\nNews was successfully written to file\n")
                BreakingNews(user_title, user_text, user_city).write_to_sql()
            elif formatted_lines[0] == "2":
                user_title = formatted_lines[1]
                user_text = formatted_lines[2]
                user_ads_duration_in_days = formatted_lines[3]
                Advertisements(user_title, user_text, user_ads_duration_in_days).write_to_file()
                print("\nAdvertisement was successfully written to file\n")
                formatted_lines = formatted_lines[4:]
                Advertisements(user_title, user_text, user_ads_duration_in_days).write_to_sql()
            elif formatted_lines[0] == "3":
                user_city = formatted_lines[1]
                user_text = formatted_lines[2]
                Weather(user_city, user_text).write_to_file()
                print("\nNews for weather was written to file\n")
                formatted_lines = formatted_lines[3:]
                Weather(user_city, user_text).write_to_sql()
            elif formatted_lines[0] == "4":
                user_zodiac_sign = formatted_lines[1]
                user_text = formatted_lines[2]
                Astrology(user_zodiac_sign, user_text).write_to_file()
                print("\nAstrological horoscope was successfully written to file\n")
                Astrology(user_zodiac_sign, user_text).write_to_sql()


class JsonAutoFill:
    def __init__(self, code_number_of_news_for_json_autofill, path=os.path.realpath("autofill_json.json")):
        self.path = path
        self.code_number_of_news_for_json_autofill = code_number_of_news_for_json_autofill

    # def read_file(self):
    #     with open(self.path) as json_file:
    #         fields = json.load(json_file)
        # return fields

    def write_to_file_from_autofill(self):
        with open(self.path) as json_file:
            fields = json.load(json_file)

            if self.code_number_of_news_for_json_autofill == 1:
                news_data = fields["BreakingNews"]
                BreakingNews(news_data.get("title"), news_data.get("text"),
                             news_data.get("city")).write_to_file()
                print("\nNews was successfully written to file\n")
                BreakingNews(news_data.get("title"), news_data.get("text"),
                             news_data.get("city")).write_to_sql()
            if self.code_number_of_news_for_json_autofill == 2:
                adv_data = fields["Advertisements"]
                Advertisements(adv_data.get("title"), adv_data.get("text"),
                               adv_data.get("ads_duration_in_days")).write_to_file()
                print("\nAdvertisement was successfully written to file\n")
                Advertisements(adv_data.get("title"), adv_data.get("text"),
                               adv_data.get("ads_duration_in_days")).write_to_sql()
            if self.code_number_of_news_for_json_autofill == 3:
                weather_data = fields["Weather"]
                Weather(weather_data.get("text"), weather_data.get("city")).write_to_file()
                print("\nNews for weather was written to file\n")
                Weather(weather_data.get("text"), weather_data.get("city")).write_to_sql()
            if self.code_number_of_news_for_json_autofill == 4:
                astrology_data = fields["Astrology"]
                Astrology(astrology_data.get("text"), astrology_data.get("zodiac_sign")).write_to_file()
                print("\nAstrological horoscope was successfully written to file\n")
                Astrology(astrology_data.get("text"), astrology_data.get("zodiac_sign")).write_to_sql()


class XmlAutoFill:
    def __init__(self, code_number_of_news_for_xml_autofill, path=os.path.realpath("autofill_xml.xml")):
        self.code_number_of_news_for_xml_autofill = code_number_of_news_for_xml_autofill
        self.path = path

    def write_to_file_from_autofill(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        if self.code_number_of_news_for_xml_autofill == 1:
            for i in root.iter('name'):
                if i.attrib.get('news') == 'Advertisement':
                    for title in i.findall('title'):
                        user_title = title.text
                    for text in i.findall('text'):
                        user_text = text.text
                    for ads_duration in i.findall('ads_duration_in_days'):
                        user_ads_duration = ads_duration.text
                    Advertisements(user_title, user_text, user_ads_duration).write_to_file()
                    print("\nAdvertisement was successfully written to file\n")
                    Advertisements(user_title, user_text, user_ads_duration).write_to_sql()
        if self.code_number_of_news_for_xml_autofill == 2:
            for i in root.iter('name'):
                if i.attrib.get('news') == 'BreakingNews':
                    for title in i.findall('title'):
                        user_title = title.text
                    for text in i.findall('text'):
                        user_text = text.text
                    for city in i.findall('city'):
                        user_city = city.text
                    BreakingNews(user_title, user_text, user_city).write_to_file()
                    print("\nNews was successfully written to file\n")
                    BreakingNews(user_title, user_text, user_city).write_to_sql()
        if self.code_number_of_news_for_xml_autofill == 3:
            for i in root.iter('name'):
                if i.attrib.get('news') == 'Weather':
                    for text in i.findall('text'):
                        user_text = text.text
                    for city in i.findall('city'):
                        user_city = city.text
                    Weather(user_text, user_city).write_to_file()
                    print("\nNews for weather was written to file\n")
                    Weather(user_text, user_city).write_to_sql()
        if self.code_number_of_news_for_xml_autofill == 4:
            for i in root.iter('name'):
                if i.attrib.get('news') == 'Astrology':
                    for text in i.findall('text'):
                        user_text = text.text
                    for zodiac_sign in i.findall('zodiac_sign'):
                        user_zodiac_sign = zodiac_sign.text
                    Astrology(user_text, user_zodiac_sign).write_to_file()
                    print("\nAstrological horoscope was successfully written to file\n")
                    Astrology(user_text, user_zodiac_sign).write_to_sql()


class SqlNewsFill:
    def __init__(self):
        with pyodbc.connect('DRIVER=SQLite3 ODBC Driver;'
                            'DATABASE= news.db') as self.conn:
            self.cursor = self.conn.cursor()
            self.create_tables()

    def insert_to_sql(self):
        self.read_file().write_to_sql()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS news (
                publish_date VARCHAR(20) NOT NULL,
                type_of_news VARCHAR(10) NOT NULL,
                text TEXT NOT NULL
            );
        """)
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS news_index ON news(publish_date, type_of_news);")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ads (
                publish_date VARCHAR(20) NOT NULL,
                type_of_news VARCHAR(10) NOT NULL,
                title VARCHAR(50) NOT NULL,
                text TEXT NOT NULL,
                expiration_date INTEGER NOT NULL
            );
        """)
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS ads_index ON ads(publish_date, type_of_news, title);")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS breaking_news (
                publish_date VARCHAR(20) NOT NULL,
                type_of_news VARCHAR(10) NOT NULL,
                title VARCHAR(50) NOT NULL,
                text TEXT NOT NULL,
                city VARCHAR(20) NOT NULL
            );
        """)
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS brnews_index ON breaking_news (publish_date, type_of_news, title);")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS astrology (
                publish_date VARCHAR(20) NOT NULL,
                type_of_news VARCHAR(10) NOT NULL,
                text TEXT NOT NULL,
                zodiac_sign VARCHAR(20) NOT NULL
            );
        """)
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS astrology_index ON astrology (publish_date, type_of_news, zodiac_sign);")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                publish_date VARCHAR(20) NOT NULL,
                type_of_news VARCHAR(10) NOT NULL,
                text TEXT NOT NULL,
                city VARCHAR(20) NOT NULL
            );
        """)
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS weather_index ON weather (publish_date, type_of_news, city);")


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
                manual_or_auto_fill = int(input("Add news manually - 1, add news from txt file - 2, \n add news from json file - 3, add news from xml file - 4\nPlease, enter your choice: "))
            except ValueError:
                print("Not a number, please try again")

            if manual_or_auto_fill == 1:
                try:
                    user_choice_input = int(input("Please choose code_number:\nNews - 1, Ads - 2, Weather - 3, Astrology - 4."))
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
                    news_feed_item.write_to_sql()
                else:
                    print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")

            elif manual_or_auto_fill == 2:
                path = input("Please, provide path to your file. Press enter to use default path.\n")
                try:
                    user_choice_autofill = int(input("Please choose code_number for autofill:\nNews - 1, Ads - 2, Weather - 3, Astrology - 4.\n"))
                except ValueError:
                    print("Not a number, please try again\n")
                autofill_file = []
                if 1 < user_choice_autofill > 4:
                    print("Not a valid number, please try again\n")
                elif user_choice_autofill != '' and path == '':
                    autofill_file = AutoFill(user_choice_autofill)
                elif user_choice_autofill != '' and path != '':
                    autofill_file = AutoFill(user_choice_autofill, path=path)

                if autofill_file:
                    autofill_file.write_to_file_from_autofill()
                else:
                    print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")

            elif manual_or_auto_fill == 3:
                path = input("Please, provide path to your file. Press enter to use default path.\n")
                try:
                    user_choice_json_autofill = int(input("Please choose code_number for autofill:\nNews - 1, Ads - 2, Weather - 3, Astrology - 4.\n"))
                except ValueError:
                    print("Not a number, please try again\n")
                autofill_json_file = []
                if 1 < user_choice_json_autofill > 4:
                    print("Not a valid number, please try again\n")
                elif user_choice_json_autofill != '' and path == '':
                    autofill_json_file = JsonAutoFill(user_choice_json_autofill)
                elif user_choice_json_autofill != '' and path != '':
                    autofill_json_file = JsonAutoFill(user_choice_json_autofill, path=path)

                if autofill_json_file:
                    autofill_json_file.write_to_file_from_autofill()
                else:
                    print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")

            elif manual_or_auto_fill == 4:
                path = input("Please, provide path to your file. Press enter to use default path.\n")
                try:
                    user_choice_xml_autofill = int(input(
                        "Please choose code_number for autofill:\nNews - 1, Ads - 2, Weather - 3, Astrology - 4.\n"))
                except ValueError:
                    print("Not a number, please try again\n")
                autofill_xml_file = []
                if 1 < user_choice_xml_autofill > 4:
                    print("Not a valid number, please try again\n")
                elif user_choice_xml_autofill != '' and path == '':
                    autofill_xml_file = XmlAutoFill(user_choice_xml_autofill)
                elif user_choice_xml_autofill != '' and path != '':
                    autofill_xml_file = XmlAutoFill(user_choice_xml_autofill, path=path)

                if autofill_xml_file:
                    autofill_xml_file.write_to_file_from_autofill()
                else:
                    print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")

            else:
                print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")


SqlNewsFill()

main()

count_worlds_and_letters()

