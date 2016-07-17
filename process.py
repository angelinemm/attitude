import ConfigParser
import logging as log
from attitude import AttitudeBot


config = ConfigParser.ConfigParser()
config.read('./config/attitude.cfg')

log.getLogger().setLevel(config.get('main', 'log_level'))

log.info('Launching bot...')
bot = AttitudeBot(config)

log.info('Reminding users...')
bot.remind_users()

log.info('Job done.')
