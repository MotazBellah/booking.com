# -*- coding: utf-8 -*-
import scrapy

class BookingSpider(scrapy.Spider):
    name = 'booking'
    allowed_domains = ['www.booking.com']
    # start_urls = ['''https://www.booking.com/searchresults.html?label=gen173nr-1DCAQoggJCDGNpdHlfLTI5MDI2M0gBWARoQ4gBAZgBAbgBF8gBDNgBA-gBAfgBAogCAagCA7gCx_7q_AXAAgHSAiQ3ZjNmMWU3My0wOTZhLTQ5YjMtOGE0Zi1kZGU2OTAyM2JiMWXYAgTgAgE&sid=12a8b409f259b2760cdf245b9e549b54&tmpl=searchresults&checkin_year_month_monthday=2020-10-29&checkout_year_month_monthday=2020-11-02&class_interval=1&dest_id=-290263&dest_type=city&dtdisc=0&group_adults=1&group_children=0&inac=0&index_postcard=0&label_click=undef&lang=en-us&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A&sb_price_type=total&shw_aparth=1&slp_r_match=0&soz=1&srpvid=4bff5ca3ee210107&ss=%D8%A7%D9%84%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1%D9%8A%D8%A9%2C%2B%D9%85%D8%B5%D8%B1&ss_all=0&ssb=empty&sshis=0&top_ufis=1&lang_click=other;cdl=ar;lang_changed=1''']

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',}

    def start_requests(self):
        yield scrapy.Request(url='''https://www.booking.com/searchresults.html?label=gen173nr-1DCAQoggJCDGNpdHlfLTI5MDI2M0gBWARoQ4gBAZgBAbgBF8gBDNgBA-gBAfgBAogCAagCA7gCx_7q_AXAAgHSAiQ3ZjNmMWU3My0wOTZhLTQ5YjMtOGE0Zi1kZGU2OTAyM2JiMWXYAgTgAgE&sid=12a8b409f259b2760cdf245b9e549b54&tmpl=searchresults&checkin_year_month_monthday=2020-10-29&checkout_year_month_monthday=2020-11-02&class_interval=1&dest_id=-290263&dest_type=city&dtdisc=0&group_adults=1&group_children=0&inac=0&index_postcard=0&label_click=undef&lang=en-us&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A&sb_price_type=total&shw_aparth=1&slp_r_match=0&soz=1&srpvid=4bff5ca3ee210107&ss=%D8%A7%D9%84%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1%D9%8A%D8%A9%2C%2B%D9%85%D8%B5%D8%B1&ss_all=0&ssb=empty&sshis=0&top_ufis=1&lang_click=other;cdl=ar;lang_changed=1''',
        callback=self.parse, headers=self.header)


    def parse(self, response):
        # a = resp.xpath("//div/div[@class='sr_item_content sr_item_content_slider_wrapper ']/div[@class='sr_rooms_table_block clearfix sr_card_rooms_container']/div[@class='room_details ']/div/div/div/div[2]/div/div[2]/div/div")
        # print(a)
        # prices = resp.xpath()
        # hotels = response.xpath("//div[@id='hotellist_inner']/div[@class='sr_item  sr_item_new sr_item_default sr_property_block sr_card_no_hover  sr_flex_layout          ']")
        # hotels = response.xpath("//div[@id='hotellist_inner']//img")
        hotels = response.xpath("//div[@id='hotellist_inner']/div")
        # //div[@id='hotellist_inner']/div/div[@class='sr_item_content sr_item_content_slider_wrapper ']/div[@class='sr_rooms_table_block clearfix sr_card_rooms_container']/div/div/div/div/div[@class='roomPrice roomPrice_flex  sr_discount ']/div/div[2]/div/div/text()
        # print(hotels)
# //div[@id='hotellist_inner']/div/div[@class='sr_item_content sr_item_content_slider_wrapper ']/div[@class='sr_rooms_table_block clearfix sr_card_rooms_container']/div[@class='room_details ']/div/div/div/div[2]/div/div[2]/div/span
        for hotel in hotels:
            # print(hotel)
            img = hotel.xpath(".//img/@src").get()
            title = hotel.xpath(".//h3/a/span/text()").get()
            rating = hotel.xpath(".//div[@class='bui-review-score__badge']/text()").get()
            link = hotel.xpath(".//h3/a/@href").get()
            room = hotel.xpath(".//div[@class='sr_item_content sr_item_content_slider_wrapper ']/div[@class='sr_rooms_table_block clearfix sr_card_rooms_container']/div/div/div/div/div[@class='roomPrice roomPrice_flex  sr_discount ']/div/div[1]/div[@class='bui-price-display__label prco-inline-block-maker-helper']/text()").get()
            yy = hotel.xpath("normalize-space(.//div[@class='sr_item_content sr_item_content_slider_wrapper ']/div[@class='sr_rooms_table_block clearfix sr_card_rooms_container']/div/div/div/div/div[@class='roomPrice roomPrice_flex  sr_discount ']/div/div[2]/div/div/text())").get()
            try:
                yield response.follow(url=link, callback=self.parse_hotel, meta={'title': title, 'rating': rating, 'img': img, 'y': yy, 'room': room})
            except Exception as e:
                pass


            # price = hotel.xpath(".//div[@class='prco-inline-block-maker-helper']/div//text()").get()
            # price2 = hotel.xpath(".//div[@class='sr_item_content sr_item_content_slider_wrapper ']/div[@class='sr_rooms_table_block clearfix sr_card_rooms_container']/div[@class='room_details ']/div/div/div/div[2]/div/div[2]/div/span//text()").get()
            # print("//////////////////////////")
            # print(hotel.xpath(".//div[2]/div[3]"))
            # yield {
            #     "img": img,
            #     "title": title,
            #     "rating": rating,
            #     "price": price2,
            # }

    def parse_hotel(self, response):
        img = response.request.meta['img']
        title = response.request.meta['title']
        rating = response.request.meta['rating']
        yy = response.request.meta['y']
        room = response.request.meta['room']

        x = response.xpath("//div[@id='property_description_content']/p")
        pric = response.xpath("//div[@class='hprt-price-block ']/div/div/div[2]/span/text()")
        d = response.xpath("//div[@class='bui-price-display__value prco-inline-block-maker-helper prco-font16-helper']/text()")
        # print(len(pric))
        # for i in pric:
        #     print('/////////////////')
        #     print(i)
        # print('/////////////////')
        # print(response.xpath("//div[@id='rooms_table']/div[@id='available_rooms']/div[@id='maxotelRoomArea']"))
        t = ""
        for i in x:
            t += i.xpath(".//text()").get()

        yield {
            "img": img,
            "title": title,
            "rating": rating,
            "t": t,
            # "price": pric.get(),
            "y": yy.replace('\xa0', ' '),
            "room": room,
            # "d": d.get()
        }
