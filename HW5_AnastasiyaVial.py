from datetime import datetime, timedelta, date


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


class Advertisements(NewsPortal):
    def __init__(self, title: str, text: str, ads_duration_in_days) -> None:
        super().__init__(text)
        self.ads_duration_in_days = int(ads_duration_in_days)
        self.type_of_news = "Ads"
        self.title = title

    def calculate_expiration_date(self):
        expiration_date = date.today() + timedelta(days=self.ads_duration_in_days)
        return expiration_date

    def calculate_days_left(self):
        return (self.calculate_expiration_date() - date.today()).days

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"{self.title}\n")
            f.write(self.text)
            f.write(f"\nActual till: {self.calculate_expiration_date()}. {self.calculate_days_left()} days left.\n")


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


class Astrology(NewsPortal):
    def __init__(self, zodiac_sign: str, text: str) -> None:
        super().__init__(text)
        self.type_of_news = "Astrology"
        self.zodiac_sign = zodiac_sign
        self.horoscope_for_today = datetime.now().strftime("%d-%m-%Y")

    def write_to_file(self):
        with open("nastia_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (43 - len(self.type_of_news))) + '\n')
            f.write(f"Happy horoscope for today: {self.horoscope_for_today}\n")
            f.write(f"Zodiac sign: {self.zodiac_sign}\n")
            f.write(f"{self.text}\n")


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
            news_feed_item = []
            if user_choice_input == 1:
                user_title = input("Please, write the title:")
                user_text = input("Please, write the text: ")
                user_city = input("Please, write the city: ")
                news_feed_item = BreakingNews(user_title.upper(), user_text.capitalize(), user_city.upper())
            elif user_choice_input == 2:
                user_title = input("Please, write the title:")
                user_text = input("Please, write the text: ")
                user_expiration_time = input("Please, write number of days for your add to last: ")
                news_feed_item = Advertisements(user_title.upper(), user_text.capitalize(), user_expiration_time)
            elif user_choice_input == 3:
                user_text = input("Please, write the text: ")
                news_feed_item = NewsPortal(user_text.capitalize(), "Weather")
            elif user_choice_input == 4:
                user_zodiac_sign = input("Please, write zodiac_sign: ")
                user_text = input("Please, write the text: ")
                news_feed_item = Astrology(user_zodiac_sign.upper(), user_text.capitalize())
            if news_feed_item:
                news_feed_item.write_to_file()
            else:
                print("Only 1 or 2 or 3 or 4 is possible. Please try again\n")


main()