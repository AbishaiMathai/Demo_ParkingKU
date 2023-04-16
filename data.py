from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import mysql.connector
app = Flask(__name__)
database_string="mysql+pymysql://3vifuwm0dbyvfyrui2fo:pscale_pw_z4giqkBmkL5fzIOPzgePGdENDKMytUhPCOSplsvXeog@aws.connect.psdb.cloud/kuparking?charset=utf8mb4"
engine=create_engine(database_string,connect_args={
    "ssl":{
        "ssl_ca":"/etc/ssl/cert.pem"
    }
})
def()
with engine.connect() as conn:
    result = conn.execute(text("select count(ID)  from Templin_1 where Availability=1"))
    answer=str(result.all())
    listy=[]
    for i in answer:
        if i.isnumeric():
            listy.append(i)
    number=int(''.join(listy))
    print(number)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    print(query)

    if query=='Templin Hall':
        with engine.connect() as conn:
            result = conn.execute(text("select count(ID)  from Templin_1 where Availability=0"))
            answer = str(result.all())
            listy = []
            for i in answer:
                if i.isnumeric():
                    listy.append(i)
            number = int(''.join(listy))
        return render_template('templin.html', query=number)
    elif query=="ellsworth":
        return render_template('king.html',query=query)


if __name__ == '__main__':
    app.run(debug=True)





