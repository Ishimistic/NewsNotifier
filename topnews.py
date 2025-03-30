import requests
import xml.etree.ElementTree as ET
import json

# RSS feed URLs - in order of preference
RSS_FEED_URLS = [
    "https://economictimes.indiatimes.com/rssfeedstopstories.cms",
    "https://www.indiatoday.in/rss/home",
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "https://rss.jagran.com/rss/news/national.xml",
    "http://rss.cnn.com/rss/edition.rss",
]

def loadRSSWithFallback():
    '''
    utility function to load RSS feeds using fallback approach
    tries each source in order, returns the first successful one
    returns a tuple of (content, url) for the successful fetch
    '''
    for url in RSS_FEED_URLS:
        try:
            print(f"Trying to fetch news from: {url}")
            # create HTTP request response object
            resp = requests.get(url.strip(), timeout=10)
            resp.raise_for_status()  # Raise exception for bad status codes
            print(f"Successfully fetched news from: {url}")
            # return response content and the successful URL
            return (resp.content, url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching RSS feed from {url}: {e}")
            print("Trying next source...")
    
    print("All RSS feeds failed. Returning None.")
    return (None, None)

def parseXML(rss, source_url=None):
    '''
    utility function to parse XML format rss feed
    '''
    if rss is None:
        return []
        
    try:
        root = ET.fromstring(rss)
        # create empty list for news items
        newsitems = []
        
        # Different sources might have different XML structures
        item_path = './channel/item'
        
        # iterate news items
        for item in root.findall(item_path):
            news = {}
            
            # Add source info
            if source_url:
                if "bbc" in source_url:
                    news['source'] = "BBC News"
                elif "cnn" in source_url:
                    news['source'] = "CNN"
                elif "hindustantimes" in source_url:
                    news['source'] = "Hindustan Times"
                elif "timesofindia" in source_url:
                    news['source'] = "Times of India"
                elif "indiatoday" in source_url:
                    news['source'] = "India Today"
                elif "economictimes" in source_url:
                    news['source'] = "Economic Times"
                elif "jagran" in source_url:
                    news['source'] = "Jagran"
                else:
                    news['source'] = "News Feed"
            
            # iterate child elements of item
            for child in item:
                try:
                    # special checking for namespace object content:media
                    if child.tag == '{http://search.yahoo.com/mrss/}content':
                        news['media'] = child.attrib['url']
                    else:
                        # Use text directly without encoding to utf8
                        if child.text:
                            news[child.tag] = child.text
                except Exception as e:
                    print(f"Error processing child element: {e}")
                    continue
            
            # Only add items that have at least title
            if 'title' in news:
                # If no description, use a placeholder
                if 'description' not in news:
                    news['description'] = "Click to read more..."
                newsitems.append(news)
        
        print(f"Successfully parsed {len(newsitems)} news items from {source_url}")
        # return news items list
        return newsitems
    except ET.ParseError as e:
        print(f"XML Parse Error for {source_url}: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error parsing {source_url}: {e}")
        return []

def topStories():
    '''
    main function to generate and return news items
    Uses fallback approach: tries sources in order until one succeeds
    '''
    # Try to load RSS feeds in order until one succeeds
    rss, source_url = loadRSSWithFallback()
    
    # Parse the XML from the successful source
    if rss:
        try:
            newsitems = parseXML(rss, source_url)
            print(f"Retrieved {len(newsitems)} items from {source_url}")
            return newsitems
        except Exception as e:
            print(f"Error processing {source_url}: {e}")
    
    print("No news items could be retrieved.")
    return []