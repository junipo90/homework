from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 여길 채워나가세요!

    userName_receive = request.form['userName_give']
    itemQuantity_receive = request.form['itemQuantity_give']
    userAddress_receive = request.form['userAddress_give']
    userNumber_receive = request.form['userNumber_give']

    orders = {'userName': userName_receive, 'itemQuantity': itemQuantity_receive, 'userAddress': userAddress_receive,
              'userNumber': userNumber_receive}

    db.orders.insert_one(orders)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
