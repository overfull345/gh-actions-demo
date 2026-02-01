import time, logging
logging.basicConfig(level=logging.INFO)
build=2
while True:
  time.sleep(1)
  logging.info(f"build:{build} running...")
