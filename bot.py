import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ဆက်သွယ်ရန် Username (VIP မန်ဘာဝင်ရန် - လိုအပ်သလို ပြင်ရန်)
CONTACT_USERNAME = "@naywww01"

# ဇာတ်ကားအမျိုးအစား ၁၀ မျိုးနှင့် ဇာတ်ကားနာမည်များ၊ အပိုင်း (၁ မှ ၆) လင့်ခ်များ
MOVIES_DATABASE = {
    "movie_1": {
        "title": "🎬 ဇာတ်ကား (၁) - အက်ရှင် (Action)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m1_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m1_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m1_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m1_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m1_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m1_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_2": {
        "title": "🎬 ဇာတ်ကား (၂) - သည်းထိတ်ရင်ဖို (Thriller)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m2_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m2_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m2_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m2_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m2_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m2_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_3": {
        "title": "🎬 ဇာတ်ကား (၃) - ဟာស (Comedy)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m3_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m3_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m3_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m3_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m3_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m3_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_4": {
        "title": "🎬 ဇာတ်ကား (၄) - အချစ်ဇာတ်လမ်း (Romance)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m4_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m4_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m4_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m4_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m4_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m4_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_5": {
        "title": "🎬 ဇာတ်ကား (၅) - သိပ္ပံဇာတ်ကား (Sci-Fi)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m5_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m5_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m5_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m5_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m5_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m5_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_6": {
        "title": "🎬 ဇာတ်ကား (၆) - သရဲ/ကြောက်မက်ဖွယ် (Horror)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m6_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m6_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m6_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m6_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m6_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m6_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_7": {
        "title": "🎬 ဇာတ်ကား (၇) - ကာတွန်း/အန်နီမေးရှင်း (Animation)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m7_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m7_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m7_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m7_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m7_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m7_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_8": {
        "title": "🎬 ဇာတ်ကား (၈) - စွန့်စားခန်း (Adventure)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m8_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m8_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m8_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m8_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m8_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m8_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_9": {
        "title": "🎬 ဇာတ်ကား (၉) - ဒရာမာ (Drama)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m9_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m9_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m9_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m9_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m9_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m9_ep6 (အပိုင်း ၆)"
        ]
    },
    "movie_10": {
        "title": "🎬 ဇာတ်ကား (၁၀) - စစ်ရေး/သမိုင်း (War/History)",
        "episodes": [
            "လင့်ခ် ၁: https://t.example.com/m10_ep1 (အပိုင်း ၁)",
            "လင့်ခ် ၂: https://t.example.com/m10_ep2 (အပိုင်း ၂)",
            "လင့်ခ် ၃: https://t.example.com/m10_ep3 (အပိုင်း ၃)",
            "လင့်ခ် ၄: https://t.example.com/m10_ep4 (အပိုင်း ၄)",
            "လင့်ခ် ၅: https://t.example.com/m10_ep5 (အပိုင်း ၅)",
            "လင့်ခ် ၆: https://t.example.com/m10_ep6 (အပိုင်း ၆)"
        ]
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for key, value in MOVIES_DATABASE.items():
        keyboard.append([InlineKeyboardButton(value["title"], callback_data=key)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    msg = await update.message.reply_text(
        "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\nအောက်ပါ ဇာတ်ကားစာရင်းထဲမှ ကြည့်ရှုလိုသည်များကို ရွေးချယ်နိုင်ပါသည် (အခမဲ့ ၁ မှ ၆ ပိုင်းအထိ ကြည့်ရှုနိုင်သည်)။\n\n*(⚠️ ဤမီနူးလင့်ခ်သည် ၁ မိနစ်အတွင်း မရွေးချယ်ပါက အလိုအလျောက် ပျက်သွားမည် ဖြစ်ပါသည်။)*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

    # ၁ မိနစ် (၆၀ စက္ကန့်) ပြည့်ပါက မီနူးစာတိုကို အလိုအလျောက် ဖျက်ရန်
    context.job_queue.run_once(delete_message_job, 60, data=msg)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    if data in MOVIES_DATABASE:
        movie = MOVIES_DATABASE[data]
        
        response_text = f"📌 **{movie['title']}**\n\n"
        for ep in movie["episodes"]:
            response_text += f"{ep}\n"
        
        response_text += f"\n⚠️ **မှတ်ချက်:** အခမဲ့ ၆ ပိုင်း ပြည့်သွားပါပြီ။ ၆ ပိုင်းထက် ပိုမိုကြည့်ရှုလိုပါက Member (VIP) ဝင်ရန် လိုအပ်ပါသည်။\n💬 **ဆက်သွယ်ရန် Username:** {CONTACT_USERNAME}\n\n*(ℹ️ ဤလင့်ခ်များသည် ၆ နာရီကြာမှသာ သက်တမ်းကုန်ဆုံးမည်ဖြစ်ပါသည်။)*"
        
        # ဇာတ်ကားလင့်ခ်များ ပို့မည်
        sent_msg = await query.message.reply_text(response_text, parse_mode="Markdown")
        
        # ၆ နာရီ (၂၁၆၀၀ စက္ကန့်) ပြည့်ပါက လင့်ခ်စာတိုကို အလိုအလျောက် ဖျက်ရန်
        context.job_queue.run_once(delete_message_job, 21600, data=sent_msg)

async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    try:
        await context.bot.delete_message(chat_id=job.data.chat_id, message_id=job.data.message_id)
    except Exception as e:
        print(f"Error deleting message: {e}")

if __name__ == '__main__':
    TOKEN = "8954957485:AAEZbI58ShdA6r1lNecuPBiGCe5ym2XKe4s"  # <--- ကိုယ့်ရဲ့ Bot Token ထည့်ရန်
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot is running with 1-min menu timer and 6-hour link timer...")
    application.run_polling()
    
