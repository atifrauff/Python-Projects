# importing requests for getting news from api
import requests

# my api key
myapi = "e0d7491e29324948b268f68baf001809"

# my complete url
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={myapi}"


# news fetching function w.r.t to user selected category
def fetch_news(category):

    # my news app with all category url
    url_2 = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={myapi}"

    # getting response from 'newsapi.org' with my own api key
    response = requests.get(url_2)
    data = response.json()

    if response.status_code == 200:
        articles = data["articles"]
        for article in articles:
            title = article["title"]
            description = article["description"]
            print(f"Title:\n{title}\n\nDescription:\n{description}\n")
            print("< < < -------------------------------------------------------- > > >\n")
    else:
        print("Error fetching the news data!")


# user interface running in loop
while True:
    print("\n----->>>     Welcome to Our News Application     <<<-----\n")
    print("Select a News Category:")
    print("1- Business")
    print("2- Entertainment")
    print("3- Health")
    print("4- Science")
    print("5- Sports")
    print("6- Technology")
    print("7- Exit")

    # getting user input
    choice = input("\nEnter your choice (1-7):    ")

    # if user want to quit the program
    if choice == "7":
        print("\nThanks for using our app.\nExiting the application ...")
        break

    # dictionary of categories to give user
    categories = {
        '1': 'business',
        '2': 'entertainment',
        '3': 'health',
        '4': 'science',
        '5': 'sports',
        '6': 'technology'
    }

    # select the user's choice
    category = categories.get(choice)
    if category:
        fetch_news(category)
    else:
        print("\nInvalid choice. Please select a valid choice.")
