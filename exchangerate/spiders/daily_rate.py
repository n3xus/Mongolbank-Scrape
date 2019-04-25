import scrapy
import re


class DailyRateSpider(scrapy.Spider):
    name = 'DailyRate'
    start_urls = ['https://www.mongolbank.mn/dblistofficialdailyrate.aspx']

    def parse(self, response):
        date_text = response.xpath('//*[@id="ContentPlaceHolder1_lblDate"]/text()').get()
        rate_date = DailyRateSpider.parse_mongolian_date(date_text)

        for row in response.css('ul.uk-comment-list>li>table>tr'):
            yield {
                'date': rate_date,
                'from_currency': 'MNT',
                'to_currency': DailyRateSpider.translate_currency(row.xpath('td[2]/text()').get()),
                'amount': DailyRateSpider.parse_amount(row.xpath('td[3]/span/text()').get())
            }

    @staticmethod
    def parse_amount(amount):
        return float(amount.replace(',', ''))

    @staticmethod
    def parse_mongolian_date(date_in_mongolian):
        date_parts = re.findall(r'\d+', date_in_mongolian)
        separator = '.'
        return separator.join(date_parts)

    @staticmethod
    def translate_currency(currency_in_mongolian):
        translation = {
            'АНУ доллар': 'USD',
            'Евро': 'EUR',
            'Японы иен': 'JPY',
            'Швейцар франк': 'CHF',
            'Шведийн крон': 'SEK',
            'Английн фунт': 'GBP',
            'Болгарын лев': 'BGN',
            'Унгарын форинт': 'HUF',
            'Египетийн фунт': 'EGP',
            'Энэтхэгийн рупи': 'INR',
            'Хонгконг доллар': 'HKD',
            'ОХУ-ын рубль': 'RUB',
            'Казахстан тэнгэ': 'KZT',
            'БНХАУ-ын юань': 'CNY',
            'БНСУ-ын вон': 'KRW',
            'БНАСАУ-ын вон': 'KPW',
            'Канадын доллар': 'CAD',
            'Австралийн доллар': 'AUD',
            'Чех крон': 'CZK',
            'Тайван доллар': 'TWD',
            'Тайланд бат': 'THB',
            'Индонезийн рупи': 'IDR',
            'Малайзын ринггит': 'MYR',
            'Сингапур доллар': 'SGD',
            'АНЭУ-ын дирхам': 'AED',
            'Кувейт динар': 'KWD',
            'Шинэ Зеланд доллар': 'NZD',
            'Данийн крон': 'DKK',
            'Польшийн злот': 'PLN',
            'Украйны гривн': 'UAH',
            'Норвегийн крон': 'NOK',
            'Непалын рупи': 'NPR',
            'Өмнөд Африкийн ранд': 'ZAR',
            'Туркийн лира': 'TRY',
            'Вьетнамын донг': 'VND',
            'Алт /унцаар/': 'XAU',
            'Мөнгө /унцаар/': 'XBA',
            'Зээлжих тусгай эрх': 'X'
        }

        return translation.get(currency_in_mongolian, '')
