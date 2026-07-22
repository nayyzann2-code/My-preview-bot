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
        [InlineKeyboardButton("🎬 The Flash (2014)", callback_data="m1")],
        [InlineKeyboardButton("🎬 Lucifer (2016)", callback_data="m2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    sent_msg = await update.message.reply_photo(
        photo="AgACAgUAAxkBAAEgueJqYFrWN-knIvOwmsOQ859SgDB3eQACUxVrG9u7CFdtu8B_Lb_nPQEAAwIAA3gAAz0E",
        caption=(
            "✨ **မင်္ဂလာပါခင်ဗျာ!**\n"
            "Channel မှ ကြိုဆိုလိုက်ပါတယ်။ အောက်ပါ ဇာတ်ကားများကို နှိပ်၍ ကြည့်ရှုနိုင်ပါသည် -\n\n"
            "⚠️ *မှတ်ချက် - ဤမက်ဆေ့ချ်သည် ၁၀ မိနစ်ကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။ လင့်ခ်ပျက်သွားပါက /start ဖြင့် ပြန်ယူနိုင်ပါသည်။*"
        ),
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
            keyboard = [
                [InlineKeyboardButton("အပိုင်း (၁) - Free", callback_data="m1_ep1")],
                [InlineKeyboardButton("အပိုင်း (၂) - Free", callback_data="m1_ep2")],
                [InlineKeyboardButton("အပိုင်း (၃) - Free", callback_data="m1_ep3")],
                [InlineKeyboardButton("အပိုင်း (၄) - Free", callback_data="m1_ep4")],
                [InlineKeyboardButton("အပိုင်း (၅) - Free", callback_data="m1_ep5")],
                [InlineKeyboardButton("အပိုင်း (၆) - Free", callback_data="m1_ep6")],
                [InlineKeyboardButton("အပိုင်း (၇) နှင့်အထက် - VIP (2000 ကျပ်)", callback_data="vip_locked")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_photo(
                photo="AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3cAAz0E",
                caption=(
                    "📌 **The Flash (2014)**\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n\n"
                    "အောက်ပါ အပိုင်းများကို ရွေးချယ်ပါ -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )

        # ----------------- ဇာတ်ကား (၂) : Lucifer -----------------
        elif data == "m2":
            keyboard = [
                [InlineKeyboardButton("အပိုင်း (၁) - Free", callback_data="m2_ep1")],
                [InlineKeyboardButton("အပိုင်း (၂) - Free", callback_data="m2_ep2")],
                [InlineKeyboardButton("အပိုင်း (၃) - Free", callback_data="m2_ep3")],
                [InlineKeyboardButton("အပိုင်း (၄) - Free", callback_data="m2_ep4")],
                [InlineKeyboardButton("အပိုင်း (၅) - Free", callback_data="m2_ep5")],
                [InlineKeyboardButton("အပိုင်း (၆) - Free", callback_data="m2_ep6")],
                [InlineKeyboardButton("အပိုင်း (၇) နှင့်အထက် - VIP (2000 ကျပ်)", callback_data="vip_locked")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_photo(
                photo="AgACAgUAAxkBAAEguktqYGtKcwc5Lz0a-uvM011zR6ouQQACrBJrG-62aFXF-kV2rfK7_gEAAwIAA3cAAz0E",
                caption=(
                    "📌 **Lucifer (2016)**\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n\n"
                    "အောက်ပါ အပိုင်းများကို ရွေးချယ်ပါ -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )

        # ----------------- The Flash ဗီဒီယိုများ -----------------
        elif data == "m1_ep1":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၁ ရဲ့ File ID", caption="🎬 The Flash (2014) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m1_ep2":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၂ ရဲ့ File ID", caption="🎬 The Flash (2014) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m1_ep3":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၃ ရဲ့ File ID", caption="🎬 The Flash (2014) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m1_ep4":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၄ ရဲ့ File ID", caption="🎬 The Flash (2014) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m1_ep5":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၅ ရဲ့ File ID", caption="🎬 The Flash (2014) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m1_ep6":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၆ ရဲ့ File ID", caption="🎬 The Flash (2014) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)

        # ----------------- Lucifer ဗီဒီယိုများ -----------------
        elif data == "m2_ep1":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="လုဆီဖာ အပိုင်း ၁ ရဲ့ File ID", caption="🎬 Lucifer (2016) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m2_ep2":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="လုဆီဖာ အပိုင်း ၂ ရဲ့ File ID", caption="🎬 Lucifer (2016) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m2_ep3":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="လုဆီဖာ အပိုင်း ၃ ရဲ့ File ID", caption="🎬 Lucifer (2016) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m2_ep4":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="လုဆီဖာ အပိုင်း ၄ ရဲ့ File ID", caption="🎬 Lucifer (2016) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m2_ep5":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="လုဆီဖာ အပိုင်း ၅ ရဲ့ File ID", caption="🎬 Lucifer (2016) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)
        elif data == "m2_ep6":
            sent_msg = await context.bot.send_video(chat_id=query.message.chat_id, video="လုဆီဖာ အပိုင်း ၆ ရဲ့ File ID", caption="🎬 Lucifer (2016) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။")
            schedule_deletion(context, sent_msg)

        # ----------------- VIP အပိုင်းများ -----------------
        elif data == "vip_locked":
            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_text(
                f"🔒 **VIP အပိုင်းများ (အပိုင်း ၇ နှင့်အထက်)**\n\n"
                f"⚠️ ဤ အပိုင်းများကို ကြည့်ရှုရန်အတွက် VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                f"💰 မန်ဘာကြေး - **၂,၀၀၀ ကျပ်** ဖြစ်ပါသည်။\n\n"
                f"မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ Owner ထံသို့ ဆက်သွယ်နိုင်ပါသည် -",
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

# ၁၀ မိနစ်ကြာရင် start မက်ဆေ့ချ်ကို ဖျက်မည့် ဖန်ရှင်
def schedule_start_deletion(context, sent_msg):
    async def delete_start_msg():
        await asyncio.sleep(600)  # 10 minutes = 600 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_start_msg())

# ၁၂ နာရီကြာရင် ဗီဒီယိုဖျက်မည့် ဖန်ရှင်
def schedule_deletion(context, sent_msg):
    async def delete_msg():
        await asyncio.sleep(43200)  # 12 hours = 43200 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_msg())

if __name__ == '__main__':
    TOKEN = "8954957485:AAHkVsWNBZDzfxEg1y0u62Vo2hCPYg51RR4"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
    
