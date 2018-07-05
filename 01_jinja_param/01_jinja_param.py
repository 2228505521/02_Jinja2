from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)


@app.route('/index/<id>')
def index(id):
    contects = {
        'username': '知了',
        'age': '18',
        'childrens': {
            'name': 'abc',
            'age': '19',
            'contry': 'china',
            'sex': '1',
        },
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': '110',
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': '111',
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': '112',
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': '113',
            },
        ],
        'names': ['1', '2', '3', '4'],
        'sign': '<script>alert("hello")</script>',
        'replace': 'hello world hello hello',
        'create_time': datetime(2018, 4, 7, 22, 58, 0, 0)
    }
    return render_template('index.html', position=-9, **contects)

# 自定义过滤器
@app.template_filter('cut')
def cut(value):
    res = value.replace('hello', '')
    return res

# 自定义时间处理过滤器
@app.template_filter('handle_time')
def handle_time(time):
    '''
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示'刚刚'
    2. 如果时间间隔为大于1分钟小于1小时，那么就显示'xx分钟前'
    3. 如果时间间隔为大于1小时小于24小时，那么就显示'xx小时前'
    4. 如果时间间隔为大于24小时小于30天，那么就显示'xx天前'
    5. 否则就显示具体时间
    '''
    if isinstance(time, datetime):
        now = datetime.now()
        # 获取时间间隔，以秒为单位
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif timestamp > 60 and timestamp < 60*60:
            minutes = timestamp / 60
            return '%s分钟前' % int(minutes)
        elif timestamp > 60*60 and timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return '%s小时前' % int(hours)
        elif timestamp > 60*60*24 and timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return '%s天前' % int(days)
        else:
            return time.strftime('%Y/%m/%d %H%M')
    else:
        return time

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/detail/')
def detail():
    return render_template('detail.html')

if __name__ == '__main__':
    app.run(debug=True)
