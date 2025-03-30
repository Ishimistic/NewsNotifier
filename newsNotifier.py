import time
from winotify import Notification
from topnews import topStories

def main():
    print("Fetching news...")
    
    try:
        # Fetch news items
        all_newsitems = topStories()
        
        if not all_newsitems:
            print("No news items found. Please check your internet connection and try again.")
            return
        
        # Limit to first 10 news items
        newsitems = all_newsitems[:10]
        
        print(f"Found {len(newsitems)} news items. Displaying notifications...")
        
        # Display the notifications
        for i, newsitem in enumerate(newsitems):
            try:
                # Format title and description
                source = newsitem.get('source', 'News')
                title = f"{source}: {newsitem.get('title', 'News Update')}"
                
                # Limit description length to avoid too-large notifications
                description = newsitem.get('description', '')
                if description and len(description) > 200:
                    description = description[:197] + "..."
                
                print(f"Showing notification {i+1}/{len(newsitems)}: {title}")
                
                # Show Windows notification using winotify
                toast = Notification(
                    app_id="News Notifier",
                    title=title,
                    msg=description,
                    duration="short"
                )
                toast.show()
                
                # Wait to ensure notification is displayed before showing the next one
                if i < len(newsitems) - 1:  # Don't wait after the last one
                    print(f"Waiting 10 seconds before next notification...")
                    time.sleep(10)
            except Exception as e:
                print(f"Error with notification {i+1}: {e}")
                print(f"Continuing to next notification...")
                continue
                
        print("All notifications displayed successfully.")
        
    except Exception as e:
        print(f"Error in main function: {e}")
        print(f"Error details: {type(e).__name__}")

if __name__ == "__main__":
    main()