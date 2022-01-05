import os
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
    
    country = CountryInfo(update.text)
    
    info = f"""**Country Information**

Name : `{country.name()}`
Native Name : `{country.native_name()}`
Capital : `{country.capital()}`
Population : `{country.population()}`
Region : `{country.region()}`
Sub Region : `{country.subregion()}`
Top Level Domains : `{country.tld()}`
Calling Codes : `{country.calling_codes()}`
Currencies : `{country.currencies()}`
Residence : `{country.demonym()}`
Timezone : `{country.timezones()}`"""
    
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Wikipedia', url=country.wiki()),
                InlineKeyboardButton('Google', url=country.google())
            ],
            [
                InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
                InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
            ]
        ]
    )
    
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as error:
        print(error)
