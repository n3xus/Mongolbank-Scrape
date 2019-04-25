# Mongolbank Scrape
Mongol Bank Exchange Rate Scraping tool

Utilized scrapy to scrape [Mongol Bank Daily Rate](https://www.mongolbank.mn/dblistofficialdailyrate.aspx "Mongolbank's daily rate page")
 

Output would be
- date: Date of Exchange Rate
- from_currency: Static string 'MNT'
- to_currency: Currency code
- amount: Exchange Rate

To run the command:
```
scrapy crawl DailyRate -o output.json
```
