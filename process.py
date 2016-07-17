import ConfigParser
import logging
from attitude import AttitudeBot

logging.basicConfig()
log = logging.getLogger(__name__)

log.info('Reading config file...')
config = ConfigParser.ConfigParser()
config.read('./config/attitude.cfg')

log.info('Launching bot...')
bot = AttitudeBot(config)

log.info('Reminding users...')
bot.remind_users()

log.info('Job done.')
