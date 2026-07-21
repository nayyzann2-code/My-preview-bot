import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# Bot Token ကို ဒီနေရာမှာ ထည့်ပါ
TOKEN = "8954957485:AAEZbI58ShdA6r1lNecuPBiGCe5ym2XKe4s"

# User တွေရဲ့ ကြည့်ရှုမှုမှတ်တမ်းကို သိမ်းရန်
user_history = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  keyboard = [[InlineKeyboardButton("🎬 ဇာတ်လမ်းကြည့်ရန်", callback_data="watch_1")]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  await update.message.reply_text(
      "မင်္ဂလာပါ! ဇာတ်လမ်းများ ကြည့်ရှုရန် အောက်ပါခလုတ်ကို နှိပ်ပါ -",
      reply_markup=reply_markup,
  )


async def watch_episode(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  await query.answer()

  user_id = query.from_user.id
  current_time = time.time()

  # ၁၂ နာရီ ကျော်သွားရင် အချက်အလက်ကို Reset လုပ်ရန်
  if user_id in user_history:
    last_watched_time = user_history[user_id]["timestamp"]
    if current_time - last_watched_time > 12 * 3600:
      user_history[user_id] = {"timestamp": current_time, "watched_count": 0}
  else:
    user_history[user_id] = {"timestamp": current_time, "watched_count": 0}

  watched_count = user_history[user_id]["watched_count"]

  # အပိုင်း ၆ ပိုင်း ပြည့်သွားပါက
  if watched_count >= 6:
    await query.message.reply_text(
        "⚠️ သင်သည် အခမဲ့ကြည့်ရှုခွင့် ၆ ပိုင်း ပြည့်သွားပါပြီ။ ဆက်လက်ကြည့်ရှုရန်"
        " Member (VIP) ဝင်ရန် လိုအပ်ပါသည်။"
    )
    return

  # အပိုင်း တစ်ပိုင်း တိုးခြင်း
  user_history[user_id]["watched_count"] += 1
  current_episode = user_history[user_id]["watched_count"]

  keyboard = [
      [InlineKeyboardButton(f"ဆက်ကြည့်ရန် ({current_episode + 1}/6)", callback_data="watch_next")]
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)

  await query.message.reply_text(
      f"🎬 ဇာတ်လမ်း အပိုင်း ({current_episode}/6) ကို ပို့ပေးလိုက်ပါပြီ။",
      reply_markup=reply_markup,
  )


def main():
  app = ApplicationBuilder().token(TOKEN).build()
  app.add_handler(CommandHandler("start", start))
  app.add_handler(CallbackQueryHandler(watch_episode))

  print("Bot is running...")
  app.run_polling()


if __name__ == "__main__":
  main()
