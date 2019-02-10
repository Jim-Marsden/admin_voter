'''
TODO:
    restructure the project
    bcript
    flask flash
    forms

'''

from flask import Flask
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

temp_map = {
    '0' : 'Hello World',
    '1' : "Also Hello world!",
    '2' : 'Haaaie~ wealboiz'
}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False, default='password1')
    email = db.Column(db.String(40), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    profile_pic = db.Column(db.String(40), nullable=False, default='admin_vote_default.png')


    #votes = db.relationship('Vote', backref='voter', lazy=True)

    #topics = db.relationship('Topic', backref='author', lazy=True)

    def __repr__(self):
        return F"User({self.username}, {self.email}, {self.rank}, {self.profile_pic})"

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.String(60))
    date_posted = db.Column(db.String(40), nullable=False, default=datetime.utcnow)
    date_expired = db.Column(db.Integer, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #votes = db.relationship('Vote', backref='voter', lazy=True)




    def __repr__(self):
        return F"Topic({self.title}, {self.date_posted}, {self.date_expired})"

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote_type = db.Column(db.Integer, nullable=False, default=0)
    reason = db.Column(db.String(512))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)

    #votes
    #topics

    def __repr__(self):
        return F"Vote({self.vote_type}, {self.reason})"


def fuckyou():
    swifty = User(username='Swifty', email='iamus@live.com',rank=0)
    db.create_all()
    db.session.add(swifty)
    db.session.comit()


        

'''

okay, how do I want to do the DB?

User:
    rank -> int
    name -> char[16]
    password -> ???
    email -> char[128]
    id -> int
    
vote:
    id -> int
    User_id -> int
    Topic_id -> int
    yes_no_abstain -> int?
    vote_reason -> char[512]
    
topic:
    id
    title
    body
    vote_type
    date_posted
    date_until_expired
    

================================================

'''
    


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<var>')
def custom(var):

    global temp_map
    if var in temp_map: return F'{temp_map[var]}'
    else : return render_template('main.html')

@app.route('/admin_vote/test/all_users')
def test():
    str = ''
    return render_template('core.html', body='Neat things!', the_list=User.query.all())




@app.route('/admin_vote/test/add_topic')
def add_topic():
    a_poll = Topic(title='No Title', user_id=0)
    db.session.add(a_poll)
    db.session.commit()
    return f'{a_poll} was added'


@app.route('/admin_vote/test/list_topic')
def list_topic():
    gewd = ''
    #for x in  += f'{x} <br/> :'
    return render_template('core.html', body=gewd, the_list=Topic.query.all())

if __name__ == '__main__':
    #fuckyou()
    app.run()
