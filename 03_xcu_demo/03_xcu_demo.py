from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

movies = [
    {
        'id': 1,
        'title': '头号玩家',
        'url': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2516578307.jpg',
        'raiting': '4.4'
    },
    {
        'id': 2,
        'title': '泯灭',
        'url': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2516914607.jpg',
        'raiting': '7.3'
    },
    {
        'id': 3,
        'title': '三块广告牌',
        'url': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2510081688.jpg',
        'raiting': '4.4'
    },
    {
        'id': 4,
        'title': '奇迹男孩',
        'url': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2507709428.jpg',
        'raiting': '8.7'
    },
]

films = [
    {
        'id': 1,
        'title': '爱情重跑',
        'url': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2518671313.jpg',
        'raiting': '7.8'
    },
    {
        'id': 2,
        'title': '南方有乔木',
        'url': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2514386586.jpg',
        'raiting': '5.2'
    },
    {
        'id': 3,
        'title': '迷雾',
        'url': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2511529719.jpg',
        'raiting': '7.5'
    },
    {
        'id': 4,
        'title': '这就是街舞',
        'url': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2509502927.jpg',
        'raiting': '8.7'
    },
]

@app.route('/')
def index():
    contents = {
        'movies': movies,
        'films': films
    }
    return render_template('index.html', **contents)

@app.route('/list/')
def item_list():
    category = request.args.get('category')
    global items
    if category == '1':
        items = movies
    else:
        items = films
    return render_template('list.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
