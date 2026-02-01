import time, logging
logging.basicConfig(level=logging.INFO)
i=1
while True:
  time.sleep(1)
  logging.info("revision: %d", i)
