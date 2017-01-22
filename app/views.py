from flask import render_template
from matplotlib.pyplot import title

from app import app

@app.route('/')
@app.route('/index')
def index():
    info_list = [
        {'employee_info':
             {'first_name': 'Ali', 'last_name':'Veli','occupation':'jobless0'}},
        {'employee_info':
             {'first_name': 'Yorgo', 'last_name': 'Worgoi', 'occupation': 'teacher'},

        }

    ]

    intro = {
            'empIntro':'Employee Information', 'goodbye':'Nothing is found! GoodBye.'
            }
    return render_template('index.html', title = 'Home', info_list = info_list, intro=intro )

