from requests import get, status_codes
from bs4 import BeautifulSoup


def topics_finder(webpage, the_bigger_tag, the_smaller_tag):
    desired_webpage = get(str(webpage))
    content_of_page = desired_webpage.content
    neat_content = BeautifulSoup(content_of_page, 'lxml')
    topics = []
    for the_bigger_minor in neat_content.find_all(str(the_bigger_tag)):
        the_smaller_minor = the_bigger_minor.find(str(the_smaller_tag))
        if the_smaller_minor is not None:
            topics.append(the_smaller_minor.string)
    no = 0
    for i in range(len(topics)):
        print(topics[i])
        no += 1
    print('number of topics in', '<' + the_smaller_tag + '>', 'tag is', no)
    return topics


topics_finder("https://www.nytimes.com/", 'a', 'h2')


