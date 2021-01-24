from datetime import datetime

import feedparser
import pyperclip


def get_time():
    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d %I:%M:%S %p')
    return current_time


if __name__ == '__main__':
    print('News as of', get_time())
    print()

    feed_npr = 'https://feeds.npr.org/1001/rss.xml'
    feed_bbc_world = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    news_url = feed_bbc_world
    parsed = feedparser.parse(news_url)
    news_entries = parsed['entries']

    text_block = ''

    for entry in news_entries:
        entry_quick = entry['title'] + ' | ' + entry['summary']
        print(entry_quick)
        print()
        text_block += entry_quick + '\n\n'

    pyperclip.copy('News as of ' + get_time() + '\n\n' + text_block)
    print('End of program')
