import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "@naywww01"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 The Flash (2014) season 1 to 9", callback_data="m1")],
        [InlineKeyboardButton("🎬 Lucifer (2016) season 1 to 6", callback_data="m2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    caption_text = (
        "Hello 👋:\n"
        "ဇာတ်ကားရွေးပါ\n"
        "တ စ် ချ က် နှိပ် ဇာတ်ကား \n"
        "တန်းကျနဲ့ လင့်တွေ ပေါ်လာပါမယ်ပျ။\n"
        "--------------------------------\n\n"
        "10 မိနစ်နေရင် ပြန်ပျက်ပါတယ် \n"
        "[/start] နှိပ်ပြီး ပြန်ယူပါလို့ ရပါတယ်။"
    )

    sent_msg = await update.message.reply_photo(
        photo="AgACAgUAAxkBAAEgueJqYFrWN-knIvOwmsOQ859SgDB3eQACUxVrG9u7CFdtu8B_Lb_nPQEAAwIAA3gAAz0E",
        caption=caption_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    
    schedule_start_deletion(context, sent_msg)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    try:
        # ----------------- ဇာတ်ကား (၁) : The Flash -----------------
        if data == "m1":
            await query.message.reply_photo(
                photo="AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3cAAz0E",
                caption=(
                    "📌 **The Flash (2014) season 1 to 9**\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n\n"
                    "👇 အောက်ပါ အပိုင်း (၆) ပိုင်းကို ပို့ပေးလိုက်ပါပြီ -"
                ),
                parse_mode="Markdown",
                protect_content=True
            )

            video_list_m1 = [
                ("BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E", "🎬 The Flash (2014) - အပိုင်း (၁)"),
                ("BAACAgUAAxkBAAEgullqYGxRVOwVCisP1T14wkwpTeDrAwACJR4AAoXLgVSvbOSV-SlXHD0E", "🎬 The Flash (2014) - အပိုင်း (၂)"),
                ("BAACAgUAAxkBAAEguqtqYH1JKVaAc4r3m1D_TSEGpRLRrQACJh4AAoXLgVTZ9Tnit771Sz0E", "🎬 The Flash (2014) - အပိုင်း (၃)"),
                ("BAACAgUAAxkBAAEguqxqYH1JCxkERguduVwRuf7HDAb2-gACKx4AAoXLgVRTok4Dly278z0E", "🎬 The Flash (2014) - အပိုင်း (၄)"),
                ("BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", "🎬 The Flash (2014) - အပိုင်း (၅)"),
                ("BAACAgUAAxkBAAEgutdqYIDNUzAzxQdGBqkH5AM0-gQIkAACnhkAAlnEgFSZ92iCDLoVuj0E", "🎬 The Flash (2014) - အပိုင်း (၆)")
            ]

            for vid, cap in video_list_m1:
                sent_msg = await context.bot.send_video(
                    chat_id=query.message.chat_id,
                    video=vid,
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။",
                    protect_content=True
                )
                schedule_deletion(context, sent_msg)

            keyboard = [
                [InlineKeyboardButton("VIP မန်ဘာဝင်ရန် (2000)ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text="🔒 **အပိုင်း (၇) နှင့် အထက် ကျန်ရှိသော အပိုင်းများကို ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။**",
                reply_markup=reply_markup,
                parse_mode="Markdown",
                protect_content=True
            )

        # ----------------- ဇာတ်ကား (၂) : Lucifer -----------------
        elif data == "m2":
            await query.message.reply_photo(
                photo="AgACAgUAAxkBAAEguktqYGtKcwc5Lz0a-uvM011zR6ouQQACrBJrG-62aFXF-kV2rfK7_gEAAwIAA3cAAz0E",
                caption=(
                    "📌 **Lucifer (2016) season 1 to 6**\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်።\n\n"
                    "👇 အောက်ပါ အပိုင်း (၆) ပိုင်းကို ပို့ပေးလိုက်ပါပြီ -"
                ),
                parse_mode="Markdown",
                protect_content=True
            )

            video_list_m2 = [
                ("BAACAgUAAxkBAAEgusVqYH9ML8Wz_1g885Oau3MBQAZ5dgACGxkAAlnEgFQsmJuyY9nHzD0E", "🎬 Lucifer (2016) - အပိုင်း (၁)"),
                ("BAACAgUAAxkBAAEgusdqYH-Se21TwLwEDW3wExwMEhJP9gACBxoAAlnEgFSGD6a-ep3_wj0E", "🎬 Lucifer (2016) - အပိုင်း (၂)"),
                ("BAACAgUAAxkBAAEgus1qYH_dvXVp2vP9ZAZ1WyIDxtFyHQACWhkAAlnEgFQxHsouPRWm1D0E", "🎬 Lucifer (2016) - အပိုင်း (၃)"),
                ("BAACAgUAAxkBAAEgutNqYIAQ1YVOgrqS4AzuR1Pe54iYKgACZhkAAlnEgFRDkdzKuTv3xT0E", "🎬 Lucifer (2016) - အပိုင်း (၄)"),
                ("BAACAgUAAxkBAAEgutVqYICU0yb2rG2-ux8vEEgAAeO5IrgAApYZAAJZxIBULyCSzraSoIM9BA", "🎬 Lucifer (2016) - အပိုင်း (၅)"),
                ("BAACAgUAAxkBAAEgutdqYIDNUzAzxQdGBqkH5AM0-gQIkAACnhkAAlnEgFSZ92iCDLoVuj0E", "🎬 Lucifer (2016) - အပိုင်း (၆)")
            ]

            for vid, cap in video_list_m2:
                sent_msg = await context.bot.send_video(
                    chat_id=query.message.chat_id,
                    video=vid,
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။",
                    protect_content=True
                )
                schedule_deletion(context, sent_msg)

            keyboard = [
                [InlineKeyboardButton("VIP မန်ဘာဝင်ရန် (2000)ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text="🔒 **အပိုင်း (၇) နှင့် အထက် ကျန်ရှိသော အပိုင်းများကို ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။**",
                reply_markup=reply_markup,
                parse_mode="Markdown",
                protect_content=True
            )

        # ----------------- VIP အပိုင်းများ -----------------
        elif data == "vip_locked":
            keyboard = [
                [InlineKeyboardButton("VIP မန်ဘာဝင်ရန် (2000)ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_text(
                f"🔒 **VIP အပိုင်းများ (အပိုင်း ၇ နှင့်အထက်)**\n\n"
                f"⚠️ ဤ အပိုင်းများကို ကြည့်ရှုရန်အတွက် VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                f"💰 မန်ဘာကြေး - **တစ်ကားလျှင် ၂,၀၀၀ ကျပ်** ဖြစ်ပါသည်။\n\n"
                f"မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ ဆက်သွယ်နိုင်ပါသည် -",
                reply_markup=reply_markup,
                parse_mode="Markdown",
                protect_content=True
            )
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

def schedule_deletion(context, sent_msg):
    async def delete_msg():
        await asyncio.sleep(43200)  # 12 hours = 43200 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_msg())

def schedule_start_deletion(context, sent_msg):
    async def delete_start_msg():
        await asyncio.sleep(600)  # 10 minutes = 600 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_start_msg())

if __name__ == '__main__':
    TOKEN = "8954957485:AAEZbI58ShdA6r1lNecuPBiGCe5ym2XKe4s"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
