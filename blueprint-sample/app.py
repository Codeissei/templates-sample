from flask import Flask, render_template
import os

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# テンプレートディレクトリの設定
# ==================================================
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.template_folder = template_dir

# ==================================================
# Blueprintの登録
# ==================================================
from application.one.views import one_bp
app.register_blueprint(one_bp)

from application.two.views import two_bp
app.register_blueprint(two_bp)

# ==================================================
# ルーティング
# ==================================================
@app.route('/')
def show_home():
    return render_template('home.html')

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run(debug=True)
