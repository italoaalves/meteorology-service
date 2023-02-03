from flask import Flask

api = Flask(__name__)

@api.route('/daily_wheater', methods=['GET'])
def get_daily_wheater():
  pass

if __name__ == '__main__':
    api.run()
