import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ဆက်သွယ်ရန် Username (VIP မန်ဘာဝင်ရန်)
CONTACT_USERNAME = "@naywww01"

# ဇာတ်ကား ၁၀ ကား (Photo File ID နှင့် အပိုင်း ၁ မှ ၆ အထိ Video File ID များ)
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
            "AAMCBQADGQEDXl9-al9m_Your_File_ID_Ep6_Here" # <--- ဒီနေရာမှာ အပိုင်း ၆ ရဲ့ File ID ကို ဖြည့်ပါ
        ]
    },
    "movie_2": {
        "title": "🎬 ဇာတ်ကား (၂) - သည်းထိတ်ရင်ဖို (Thriller)",
        "photo": "YOUR_PHOTO_FILE_ID_M2",
        "file_ids": [
            "YOUR_FILE_ID_M2_EP1", "YOUR_FILE_ID_M2_EP2", "YOUR_FILE_ID_M2_EP3",
            "YOUR_FILE_ID_M2_EP4", "YOUR_FILE_ID_M2_EP5", "YOUR_FILE_ID_M2_EP6"
        ]
    },
    "movie_3": {
        "title": "🎬 ဇာတ်ကား (၃) - ဟာស (Comedy)",
        "photo": "YOUR_PHOTO_FILE_ID_M3",
        "file_ids": [
            "YOUR_FILE_ID_M3_EP1", "YOUR_FILE_ID_M3_EP2", "YOUR_FILE_ID_M3_EP3",
            "YOUR_FILE_ID_M3_EP4", "YOUR_FILE_ID_M3_EP5", "YOUR_FILE_ID_M3_EP6"
        ]
    },
    "movie_4": {
        "title": "🎬 ဇာတ်ကား (၄) - အချစ်ဇာတ်လမ်း (Romance)",
        "photo": "YOUR_PHOTO_FILE_ID_M4",
        "file_ids": [
            "YOUR_FILE_ID_M4_EP1", "YOUR_FILE_ID_M4_EP2", "YOUR_FILE_ID_M4_EP3",
            "YOUR_FILE_ID_M4_EP4", "YOUR_FILE_ID_M4_EP5", "YOUR_FILE_ID_M4_EP6"
        ]
    },
    "movie_5": {
        "title": "🎬 ဇာတ်ကား (၅) - သိပ္ပံဇာတ်ကား (Sci-Fi)",
        "photo": "YOUR_PHOTO_FILE_ID_M5",
        "file_ids": [
            "YOUR_FILE_ID_M5_EP1", "YOUR_FILE_ID_M5_EP2", "YOUR_FILE_ID_M5_EP3",
            "YOUR_FILE_ID_M5_EP4", "YOUR_FILE_ID_M5_EP5", "YOUR_FILE_ID_M5_EP6"
        ]
    },
    "movie_6": {
        "title": "🎬 ဇာတ်ကား (၆) - သရဲ/ကြောက်မက်ဖွယ် (Horror)",
        "photo": "YOUR_PHOTO_FILE_ID_M6",
        "file_ids": [
            "YOUR_FILE_ID_M6_EP1", "YOUR_FILE_ID_M6_EP2", "YOUR_FILE_ID_M6_EP3",
            "YOUR_FILE_ID_M6_EP4", "YOUR_FILE_ID_M6_EP5", "YOUR_FILE_ID_M6_EP6"
        ]
    },
    "movie_7": {
        "title": "🎬 ဇာတ်ကား (၇) - ကာတွန်း/အန်နီမေးရှင်း (Animation)",
        "photo": "YOUR_PHOTO_FILE_ID_M7",
        "file_ids": [
            "YOUR_FILE_ID_M7_EP1", "YOUR_FILE_ID_M7_EP2", "YOUR_FILE_ID_M7_EP3",
            "YOUR_FILE_ID_M7_EP4", "YOUR_FILE_ID_M7_EP5", "YOUR_FILE_ID_M7_EP6"
        ]
    },
    "movie_8": {
        "title": "🎬 ဇာတ်ကား (၈) - စွန့်စားခန်း (Adventure)",
        "photo": "YOUR_PHOTO_FILE_ID_M8",
        "file_ids": [
            "YOUR_FILE_ID_M8_EP1", "YOUR_FILE_ID_M8_EP2", "YOUR_FILE_ID_M8_EP3",
            "YOUR_FILE_ID_M8_EP4", "YOUR_FILE_ID_M8_EP5", "YOUR_FILE_ID_M8_EP6"
        ]
    },
    "movie_9": {
        "title": "🎬 ဇာတ်ကား (၉) - ဒရာမာ (Drama)",
        "photo": "YOUR_PHOTO_FILE_ID_M9",
        "file_ids": [
            "YOUR_FILE_ID_M9_EP1", "YOUR_FILE_ID_M9_EP2", "YOUR_FILE_ID_M9_EP3",
            "YOUR_FILE_ID_M9_EP4", "YOUR_FILE_ID_M9_EP5", "YOUR_FILE_ID_M9_EP6"
        ]
    },
    "movie_10": {
        "title": "🎬 ဇာတ်ကား (၁၀) - စစ်ရေး/သမိုင်း (War/History)",
        "photo": "YOUR_PHOTO_FILE_ID_M10",
        "file_ids": [
            "YOUR_FILE_ID_M10_EP1", "YOUR_FILE_ID_M10_EP2", "YOUR_FILE_ID_M10_EP3",
            "YOUR_FILE_ID_M10_EP4", "YOUR_FILE_ID_M10_EP5", "YOUR_FILE_ID_M10_EP6"
        ]
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for key, value in MOVIES_DATABASE.items():
        keyboard.append([InlineKeyboardButton(value["title"], callback_data=key)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    msg = await update.message.reply_text(
        "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\nအောက်ပါ ဇာတ်ကားစာရင်းထဲမှ ကြည့်ရှုလိုသည်များကို ရွေးချယ်နိုင်ပါသည် (အခမဲ့ ၁ မှ ၆ ပိုင်းအထိ ကြည့်ရှုနိုင်သည်)။\n\n*(⚠️ ဤမီနူးစာတိုသည် ၁ မိနစ်အတွင်း မရွေးချယ်ပါက အလိုအလျောက် ပျက်သွားမည် ဖြစ်ပါသည်။)*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    context.job_queue.run_once(delete_message_job, 60, data=msg)

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
        
        menu_msg = await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=movie["photo"],
            caption=f"📌 **{movie['title']}**\nအောက်ပါ အပိုင်းခလုတ်များကို နှိပ်၍ ဗီဒီယိုကို တိုက်ရိုက်ကြည့်ရှုနိုင်ပါသည် -",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        
        context.job_queue.run_once(delete_message_job, 21600, data=menu_msg)

    elif data.startswith("vid_"):
        parts = data.split("_")
        movie_key = f"{parts[1]}_{parts[2]}"
        ep_index = int(parts[3])
        
        if movie_key in MOVIES_DATABASE:
            file_id = MOVIES_DATABASE[movie_key]["file_ids"][ep_index]
            movie_title = MOVIES_DATABASE[movie_key]["title"]
            ep_num = ep_index + 1
            
            sent_video = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video=file_id,
                caption=f"📌 {movie_title} - အပိုင်း {ep_num}\n\n⚠️ **မှတ်ချက်:** ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။\n💬 **VIP မန်ဘာဝင်ရန်:** {CONTACT_USERNAME}",
                parse_mode="Markdown"
            )
            context.job_queue.run_once(delete_message_job, 21600, data=sent_video)

async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    try:
        await context.bot.delete_message(chat_id=job.data.chat_id, message_id=job.data.message_id)
    except Exception as e:
        print(f"Error deleting message: {e}")

if __name__ == '__main__':
    TOKEN = "8954957485:AAEZbI58ShdA6r1lNecuPBiGCe5ym2XKe4s"
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot is running with photo file_id support...")
    application.run_polling()
    
