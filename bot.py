from create_bot import dp

async def on_startup(_):
    print('Bot is running.')
    #sqlite_db.sql_start()

client.register_handlers_client(dp)

dp.start_polling(dp, skip_updates=True, on_startup=on_startup)