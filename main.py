from datetime import datetime

import feedparser
import pyperclip


def get_time():
    now = datetime.now()
    current_time = now.strftime('%I:%M %p')
    return current_time


if __name__ == '__main__':
    print('Current time is', get_time())
    print()

    # NPR https://feeds.npr.org/1001/rss.xml
    # BBC World http://feeds.bbci.co.uk/news/world/rss.xml
    news_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    parsed = feedparser.parse(news_url)
    news_entries = parsed['entries']

    text_block = ''

    for entry in news_entries:
        entry_quick = entry['title'] + ' | ' + entry['summary']
        print(entry_quick)
        print()
        text_block += entry_quick + '\n\n'

    pyperclip.copy(get_time() + '\n\n' + text_block)
    print('End of program')
