from flask import Flask

import config.settings


api = Flask(__name__)

@api.route('/daily_wheater', methods=['GET'])
def get_daily_wheater():
  # check db for updated timestamps over the current date
  # run the web scrapper service to update db
  # send message back about db being up to date
  # close
  pass

if __name__ == '__main__':
    api.run()
