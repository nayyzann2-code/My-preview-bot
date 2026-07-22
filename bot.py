import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "@naywww01"

MOVIES_DATABASE = {
    "movie_1": {
        "title": "🎬 The Flash (2014)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E", 
        "file_ids": [
            "AAMCBQADGQEDXlV_al9eVk62LzCTrKjv_7BEv0WtD84AAiQeAAKFy4FUXJNsFXuqRPEBAAdtAAM9BA", 
            "AAMCBQADGQEDXl5Qal9l8QAB-eBpKsJe-DECTOQgKQ77AAIlHgAChcuBVK49jZTQRMVjAQAHbQADPQQ", 
            "AAMCBQADGQEDXl5-al9mFiIMkV1nc2RucvmJodK_ULoAAiYeAAKFy4FUNRtZ8dDMvisBAAdtAAM9BA",
            "AAMCBQADGQEDXl8-al9m0URt8_QaItigKtAt9NYDt-IAAiseAAKFy4FUtGnma9kwiGUBAAdtAAM9BA", 
            "AAMCBQADGQEDXl9Nal9m22u3eqv_ckXtOZQcONYNa0AAAtcjAAJZxHhUy55L6Rw8zuoBAAdtAAM9BA",
            "AAMCBQADGQEDXl9-al9m_Your_File_ID_Ep6_Here"
        ]
    },
    "movie_2": {
        "title": "🎬 ဇာတ်ကား (၂) - သည်းထိတ်ရင်ဖို (Thriller)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_3": {
        "title": "🎬 ဇာတ်ကား (၃) - ဟာស (Comedy)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_4": {
        "title": "🎬 ဇာတ်ကား (၄) - အချစ်ဇာတ်လမ်း (Romance)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_5": {
        "title": "🎬 ဇာတ်ကား (၅) - သိပ္ပံဇာတ်ကား (Sci-Fi)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_6": {
        "title": "🎬 ဇာတ်ကား (၆) - သရဲ/ကြောက်မက်ဖွယ် (Horror)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_7": {
        "title": "🎬 ဇာတ်ကား (၇) - ကာတွန်း/အန်နီမေးရှင်း (Animation)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_8": {
        "title": "🎬 ဇာတ်ကား (၈) - စွန့်စားခန်း (Adventure)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_9": {
        "title": "🎬 ဇာတ်ကား (၉) - ဒရာမာ (Drama)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    },
    "movie_10": {
        "title": "🎬 ဇာတ်ကား (၁၀) - စစ်ရေး/သမိုင်း (War/History)",
        "photo": "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3kAAz0E",
        "file_ids": ["EP1", "EP2", "EP3", "EP4", "EP5", "EP6"]
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for key, value in MOVIES_DATABASE.items():
        keyboard.append([InlineKeyboardButton(value["title"], callback_data=key)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\nအောက်ပါ ဇာတ်ကားစာရင်းထဲမှ ကြည့်ရှုလိုသည်များကို ရွေးချယ်နိုင်ပါသည် -",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    if data in MOVIES_DATABASE:
        movie = MOVIES_DATABASE[data]
        
        keyboard = []
        for index, file_id in enumerate(movie["file_ids"], start=1):
            keyboard.append([InlineKeyboardButton(f"အပိုင်း {index}", callback_data=f"vid_{data}_{index-1}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=movie["photo"],
            caption=f"📌 **{movie['title']}**\nအောက်ပါ အပိုင်းခလုတ်များကို နှိပ်၍ ဗီဒီယိုကို တိုက်ရိုက်ကြည့်ရှုနိုင်ပါသည် -",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    elif data.startswith("vid_"):
        parts = data.split("_")
        movie_key = f"{parts[1]}_{parts[2]}"
        ep_index = int(parts[3])
        
        if movie_key in MOVIES_DATABASE:
            file_id = MOVIES_DATABASE[movie_key]["file_ids"][ep_index]
            movie_title = MOVIES_DATABASE[movie_key]["title"]
            ep_num = ep_index + 1
            
            await context.bot.send_video(
                chat_id=query.message.chat_id,
                video=file_id,
                caption=f"📌 {movie_title} - အပိုင်း {ep_num}\n\n💬 **VIP မန်ဘာဝင်ရန်:** {CONTACT_USERNAME}",
                parse_mode="Markdown"
            )

if __name__ == '__main__':
    TOKEN = "8954957485:AAEZbI58ShdA6r1lNecuPBiGCe5ym2XKe4s"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()
    
