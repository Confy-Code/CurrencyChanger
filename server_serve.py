#import flask libraries
from flask import render_template,request
from flask import Flask
from exchange import get_currency
app=Flask(__name__)
@app.route('/')
@app.route('/index')
def printing():
    return render_template("frontexch.html")

#if he gets to exchange
@app.route('/exchange', methods=['GET'])
def converter():
    amount=request.args.get('amount', type=float)
    from_currency=request.args.get('from_currency')
    to_currency=request.args.get('to_currency')
    exchange_app=get_currency(from_currency)
    return render_template('for_server.html',results=amount*exchange_app['conversion_rates'][to_currency],amount=amount,to_currency=to_currency, from_currency=from_currency)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000)
#route, and render template