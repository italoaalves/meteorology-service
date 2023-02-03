# wait for message to start
# check db for updated timestamps over the current date
# run the web scrapper service to update db
# send message back abou db being updated
# close

from flask import Flask

api = Flask(__name__)

@api.route('/daily_wheater', methods=['GET'])
def get_daily_wheater():
  pass

if __name__ == '__main__':
    api.run()
