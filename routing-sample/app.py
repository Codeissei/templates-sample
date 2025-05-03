from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>TOPページ</h1>'

@app.route('/list')
def item_list():
    return '<h1>商品ページ</h1>'

@app.route('/detail')
def item_detail():
    return '<h1>商品アイテム<h1>'

if __name__ == '__main__':
    app.run()

