from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import mysql.connector
app = Flask(__name__)
database_string="random"
engine=create_engine(database_string,connect_args={
    "ssl":{
        "ssl_ca":"/etc/ssl/cert.pem"
    }
})

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
    return render_template('actualfrontend.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    print(query)

    if query=='Templin Hall':
        with engine.connect() as conn:
            result = conn.execute(text("select count(ID)  from Templin_1 where Availability=1"))
            answer = str(result.all())
            listy = []
            for i in answer:
                if i.isnumeric():
                    listy.append(i)
            number = int(''.join(listy))
        return render_template('templin.html', query=number)
    elif query=="Ellsworth Hall":
        with engine.connect() as conn:
            result = conn.execute(text("select count(ID)  from  Ellsworth_1 where Availability=1"))
            answer = str(result.all())
            listy = []
            for i in answer:
                if i.isnumeric():
                    listy.append(i)
            number = int(''.join(listy))
        return render_template('ellsworth.html', query=number)
    elif query == "Lied Center":
        with engine.connect() as conn:
            result = conn.execute(text("select count(ID)  from  Lied_Center where Availability=1"))
            answer = str(result.all())
            listy = []
            for i in answer:
                if i.isnumeric():
                    listy.append(i)
            number = int(''.join(listy))
        return render_template('Lied.html', query=number)


if __name__ == '__main__':
    app.run(debug=True)
