from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from influxdb import InfluxDBClient
#from influxdb_client import InfluxDBClient, Point, WritePrecision
import logging

# Configurare token Telegram
TELEGRAM_TOKEN = '7295701270:AAEgkH8XM374BMCr2DrXSkQjmpa7kQXYuAE'

# Configurare client InfluxDB
INFLUXDB_URL = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_DBNAME = 'mydb'
INFLUXDB_USER = 'crina'
INFLUXDB_PASSWORD = 'crina'

# Configurare logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Functie pentru comanda /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salut! Sunt botul tău de date.')

# Functie pentru comanda /query
async def query_data(update: Update, context: CallbackContext) -> None:
    influx_client = InfluxDBClient(host=INFLUXDB_URL, port=INFLUXDB_PORT, username=INFLUXDB_USER, password=INFLUXDB_PASSWORD, database=INFLUXDB_DBNAME)
    query = 'SELECT * FROM sensor_data ORDER BY time DESC LIMIT 1'
    logger.info(f'Executing query: {query}')
    result = influx_client.query(query)
    logger.info(f'Query result: {result}')


    response = 'Rezultatele interogării:\n'
    if not result:
            response = 'Nu s-au găsit date pentru perioada specificată.'
    else:
        for point in result.get_points():
            response += f'{point["time"]}: {point["temperature"]}°C, {point["humidity"]}%\n'

    await update.message.reply_text(response)

# Functie pentru mesajele primite
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Adauga handler pentru comenzile botului
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("query", query_data))

    # Adauga handler pentru mesajele primite
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Pornire polling
    application.run_polling()

if __name__ == '__main__':
    main()