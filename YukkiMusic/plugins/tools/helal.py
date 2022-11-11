import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر
@app.on_message(
    filters.command(["الاوامر","اوامر","/help"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}
     
✅ اليك قائمة اوامر سورس جوهره
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•

✅ قائمه الاوامر تحتوي علي ٢ اوامر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
1 ← اوامـر الـحـمـايـه .
2 ← اوامـر الـمـوزك .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر الحـمايـه", callback_data=f"hmaya"),
                    InlineKeyboardButton(
                        "اوامـر الـمـوزك", callback_data=f"musichelal"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devhelp"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),
               ],
            ]
        ),
    )
#الاوامر كول باك
@app.on_callback_query(filters.regex("ayamr"))
async def ayamr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس جوهره
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•

✅ قائمه الاوامر تحتوي علي ٢ اوامر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
1 ← اوامـر الـحـمـايـه .
2 ← اوامـر الـمـوزك .""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر الحـمايـه", callback_data=f"hmaya"),
                    InlineKeyboardButton(
                        "اوامـر الـمـوزك", callback_data=f"musichelal"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devhelp"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),
               ],
            ]
        ),
    )
########
#اوامر الحمايه
@app.on_callback_query(filters.regex("hmaya"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""" ✅ اليك قائمة اوامر سورس جوهره
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•

✅ قائمه الاوامر الحمايه تحتوي علي  اوامر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر التسليه", callback_data=f"maya"),
                    InlineKeyboardButton(
                        "اوامـر الادمن", callback_data=f"aya"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devv"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"ayamr"), 
               ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("maya"))
async def bhhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس جوهره
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•

✅ قائمه الاوامر الحمايه تحتوي علي  اوامر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
1 ← اوامر الحمايه  .
2 ← اوامر الحمايه  .""",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامـر الادمن", callback_data=f"aya"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"hmaya"), 
               ],
            ]
        ),
    )
    
@app.on_callback_query(filters.regex("aya"))
async def br(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس جوهره
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•

✅ قائمه الاوامر الحمايه تحتوي علي  اوامر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
1 ← اوامر الحمايه  .
2 ← اوامر الحمايه  .""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامـر التسليه", callback_data=f"maya"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"hmaya"), 
               ],
            ]
        ),
    )
    
##########
#اوامر الميوزك
@app.on_callback_query(filters.regex("musichelal"))
async def back(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ اليك قائمة اوامر سورس جوهره
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•

✅ قائمه الاوامر الميوزك تحتوي علي 6 اوامر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
1 ← اوامر التشغيل .
2 ← اوامر القنوات .
3 ← اوامر مطور البوت .
4 ← مميزات السورس .
5 ← اوامر البوت .
6 ← اوامر الادمن .""",
       reply_markup=InlineKeyboardMarkup(
                [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
               "عـوده 𖡃", callback_data=f"ayamr"),
               ],
            ]
        ),
    )
       
#قائمه الاوامر الاولي
@app.on_callback_query(filters.regex("g1"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓ[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)

•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ اليك قائمة اوامر التشغيل ,

- اولا اليك اوامر التشغيل ف الجروب .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لتشغيل اغنيه اكتب : تشغيل او شغل او /play
- لتشغيل فيديو اكتب : فيديو او /video
- لأنهاء الاغنيه اكتب : ايقاف او انهاء او /stop
- لايقاف الاغنيه مؤقت اكتب : وقف او /pause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او /resume
- لتخطي الاغنيه اكتب : تخطي او /skip
- لكتم البوت في الكول اكتب : اسكت او /mute
- لألغاء كتم البوت في الكول اكتب : اتكلم او /unmute
- لاعادة تشغيل البوت اكتب : /restart""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثانيه
@app.on_callback_query(filters.regex("g2"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓ[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)

•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ اليك قائمة اوامر القنوات ,

- اولا اليك اوامر ربط البوت ب القناة .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
 لربط البوت ب القناة مالك القناة فقط يستطيع ربطه .
لربط القناة اكتب : ربط + معرف القناة

- ثانيا اليك اوامر تشغيل البوت في القناة .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لتشغيل اغنيه اكتب : ق تشغيل او ق شغل او cplay
- لتشغيل فيديو اكتب : ق فيديو او cvideo
- لأنهاء الاغنيه اكتب : ق ايقاف او ق انهاء او cstop
- لايقاف الاغنيه مؤقت اكتب : ق وقف او cpause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : ق كمل او cresume
- لتخطي الاغنيه اكتب : تخطي او cskip
- لكتم البوت في الكول اكتب : ق اسكت او cmute
- لألغاء كتم البوت في الكول اكتب : ق اتكلم او cunmute
- لاعادة تشغيل البوت اكتب : /restart""",
       reply_markup=InlineKeyboardMarkup(
               [
                    [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )

#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g3"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓ[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)

•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ اليك قائمة اوامر مطور البوت ,

- جميع الاوامر خاصه بمطور البوت فقط .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لعمل اذاعه في البوت اعمل ريبلاي علي الاذاعه واكتب : اذاعه .
 - لعرض احصائيات البوت اكتب : الاحصائيات .
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

- ثانيا اليك اوامر الرتب .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .
- لرفع مطور ثانوي اكتب : ر م ث .
- لتنزيل مطور ثانوي اكتب : ت م ث .
- لعرض قائمه الثانوين اكتب : ق م ث .

- ثالثا اليك اوامر الحظر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .
- لحظر عضو عام من الجروب اكتب : ح ع .
- لالغاء حظر عضو عام من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين عام اكتب : ق ح ع .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g4"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓ[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)


•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ اليك قائمة مميزات السورس ,
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ هذه قائمه مميزات سورس جوهره الميوزك .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لعرض اوامر البوت اكتب : الاوامر .
- لعرض كليشه السورس اكتب : سورس جوهره .
- لعرض مطور البوت اكتب : المطور .
- لعرض اسم البوت اكتب : البوت .
- لعرض الايدي الخاص بك وصورتك اكتب : ا .

✅ اولا قائمة اوامر البوت ,
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لعمل اذاعه في البوت اعمل ريبلاي علي الاذاعه واكتب : اذاعه .
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

✅ ثانيا اليك اوامر الرتب .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .

✅ ثالثا اليك اوامر الحظر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),          
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g5"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓ[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)


•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ اليك قائمة اوامر البوت ,
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

- ثانيا اليك اوامر الرتب .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .
- لرفع مطور ثانوي اكتب : ر م ث .
- لتنزيل مطور ثانوي اكتب : ت م ث .
- لعرض قائمه الثانوين اكتب : ق م ث .

- ثالثا اليك اوامر الحظر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .
- لحظر عضو عام من الجروب اكتب : ح ع .
- لالغاء حظر عضو عام من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين عام اكتب : ق ح ع .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data=f"g6"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
    
#قائمه الاوامى الثالثه
@app.on_callback_query(filters.regex("g6"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓ[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)


•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
✅ اليك قائمة اوامر الادمن ,

- جميع الاوامر خاصه ب الادمن فقط .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لعرض سرعه البوت اكتب : بينج .
- للتحكم في لغه البوت اكتب : اللغه .
- للتحكم في ازار التشغيل اكتب : وضع شغل .
- لعرض اعدادات البوت اكتب : الاعدادات .

- ثانيا اليك اوامر الرتب .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لرفع ادمن في الجروب اكتب : ر ا د .
- لرفع ادمن في الجروب اكتب : ت ا د .
- لعرض قائمه الادمنيه اكتب : ق ا د .

- ثالثا اليك اوامر الحظر .
•═════•| 𝙶𝙾𝙷𝙰𝚁𝙰 |•═════•
- لحظر عضو من الجروب اكتب : ح ر .
- لالغاء حظر عضو من الجروب اكتب : ا ر .
- لعرض قائمه المحظورين اكتب : ق ح ر .""",
       reply_markup=InlineKeyboardMarkup(
                    [
                      [
                      InlineKeyboardButton(
                        "اوامـر الـتـشـغـيل", callback_data=f"g1"),
                    InlineKeyboardButton(
                        "اوامـر الـقـنـوات", callback_data=f"g2"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـمـطـور", callback_data=f"g3"),
                    InlineKeyboardButton(
                        "مـمـيـزات الـسـورس", callback_data=f"g4"),
                ],[
                      InlineKeyboardButton(
                        "اوامـر الـبـوت", callback_data=f"g5"),
                ],[
                    InlineKeyboardButton(
                        "ســٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــورس جــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــوهــٰٰٰ๋ٖٖٖۧ͜ــ۫͜ــره", callback_data=f"devmusic"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )
##########  
#المطورين
#الاوامر
@app.on_callback_query(filters.regex("devhelp"))
async def devhelp(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐆𝐎𝐇𝐀𝐑𝐀 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/M_O_D_Y_CH)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "ᥴꫝꪖꪀꪀꫀꪶ ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/M_O_D_Y_CH"),
                    InlineKeyboardButton(
                        "𝘴ꪊρρꪮ𝘳𝓽 ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/BarGohara")
                ],[
                    InlineKeyboardButton(
                        "ᦔꫀꪜ", url=f"https://t.me/MohamedHelal_l"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"ayamr"),
               ], 
          ]
        ),
    )
#الحمايه   
@app.on_callback_query(filters.regex("devv"))
async def devh(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐆𝐎𝐇𝐀𝐑𝐀 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/M_O_D_Y_CH)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "ᥴꫝꪖꪀꪀꫀꪶ ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/M_O_D_Y_CH"),
                    InlineKeyboardButton(
                        "𝘴ꪊρρꪮ𝘳𝓽 ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/BarGohara")
                ],[
                    InlineKeyboardButton(
                        "ᦔꫀꪜ", url=f"https://t.me/MohamedHelal_l"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"hmaya"),
               ],
          ]
        ),
    )
#الميوزك
@app.on_callback_query(filters.regex("devmusic"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐆𝐎𝐇𝐀𝐑𝐀 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/M_O_D_Y_CH)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "ᥴꫝꪖꪀꪀꫀꪶ ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/M_O_D_Y_CH"),
                    InlineKeyboardButton(
                        "𝘴ꪊρρꪮ𝘳𝓽 ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/BarGohara")
                ],[
                    InlineKeyboardButton(
                        "ᦔꫀꪜ", url=f"https://t.me/MohamedHelal_l"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"musichelal"),
               ],
          ]
        ),
    )  
#الستار
@app.on_callback_query(filters.regex("devstart"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐆𝐎𝐇𝐀𝐑𝐀 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐆𝐎𝐇𝐀𝐑𝐀 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/M_O_D_Y_CH)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/M_O_D_Y_CH)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "ᥴꫝꪖꪀꪀꫀꪶ ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/M_O_D_Y_CH"),
                    InlineKeyboardButton(
                        "𝘴ꪊρρꪮ𝘳𝓽 ᧁꪮꫝꪖ𝘳ꪖ", url=f"https://t.me/BarGohara")
                ],[
                    InlineKeyboardButton(
                        "ᦔꫀꪜ", url=f"https://t.me/MohamedHelal_l"),
                ],[
                    InlineKeyboardButton(
                        "عـوده 𖡃", callback_data=f"settingsback_helper"),
               ],
          ]
        ),
    )  