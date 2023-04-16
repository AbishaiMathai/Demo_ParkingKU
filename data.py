from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    print(query)

    if query=='Templin Hall':
       return render_template('templin.html', query=query)
    else:
        return render_template('king.html',query=query)

if __name__ == '__main__':
    app.run(debug=True)




'''from flask import Flask,render_template,request,redirect,url_for
app=Flask("__name__")
@app.route("/",methods=['POST','GET'])
def home():
    if request.method=='POST':
        area=request.form['search_input']
        return render_template('index.html',area=area)
    else:
        area = request.form['search_input']
        return render_template('index.html', area=area)'''

#if __name__=="__main__":
   # app.run(debug=True)