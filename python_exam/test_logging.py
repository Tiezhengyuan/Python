import random
import logging

FORMAT = '%(levelname)s = %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT,
        filename="battery_temperature.log", filemode='a')
logger = logging.getLogger()

class temperature:
    def get_temperature(self):
        temp = random.randrange(0,50)
        if temp<20:
            logger.debug('TEMPERATURE_IN_CELSIUS < 20')
        elif temp>35:
            logger.critical('TEMPERATURE_IN_CELSIUS > 35')
        else:
            logger.warning('TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35')
        return temp

a=temperature()
for i in range(10):
    a.get_temperature()
print("done.")