from flask import Flask,render_template
import pickle, pandas

popular_df = pickle.load(open('../popular.pkl', 'rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=popular_df['num_rating'].to_list(),
                           rating=popular_df['avg_rating'].to_list())

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/login')
def login_ui():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)