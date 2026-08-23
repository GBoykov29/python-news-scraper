import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')

# obrushtame stringa res.text v html format da moje da go polzvame,obekt koito move da manipulirame
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# vzima samo body chasta,moje da tursim vsichko s funkciqta soup.find_all('div')
links = (soup.select('.titleline'))
subtext = (soup.select('.subtext'))
links2 = (soup2.select('.titleline'))
subtext2 = (soup2.select('.subtext'))

megalinks = links+links2
megasubtext = subtext+subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hackernews(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        # href = item.get('href', None)
        a_tag = item.find('a')
        href = a_tag.get('href', None) if a_tag else None
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    pprint.pprint(create_custom_hackernews(megalinks, megasubtext))
