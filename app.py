from utils.scrape import scrape_article

if __name__ == "__main__":
    url = input("Enter article URL: ")
    
    print("\n🔍 Scraping content...")
    try:
        article_text = scrape_article(url)
        print("Article scraped successfully.\n")

        with open("/Users/ashishzangra/Documents/gfg_apps/outputs/article.md", "w", encoding="utf-8") as f:
            f.write(article_text)

    except Exception as e:
        print(f" Error: {e}")


