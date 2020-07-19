# import requests package
import requests


print()

# naming function
def CNN():

    # setting up BBC News API
    main_url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=f0f5bacee93e4d2d85ee598ca3a1fdf3"

    # fetching data in JSON format
    open_cnn_page = requests.get(main_url).json()

    # getting all articles in article format string
    article = open_cnn_page['articles']

    # setting up an empty list for trending news
    results = []

    # using for-loop to add title in article
    for ar in article:
        results.append(ar['title'])

    # using for-loop to set how many articles to display
    for i in range(5):
        print( i + 1, results[i])
    
# reading and executingh all the code found (in source file)
if '__name__ == __main__':

    # calling the function
    CNN()
print()
