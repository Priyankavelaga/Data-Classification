from ast import Pass
from flask import Flask, render_template, request
import json
import sqlite3

conn = sqlite3.connect('dataq.db')
c= conn.cursor()

app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')


@app.route('/objectdata',methods=['POST','GET'])
def ddataobject():
    conn = sqlite3.connect('dataq.db')
    c= conn.cursor()
    object=str(request.form['object'])
    c.execute("select object, min, max from data where object ='"+object+"';") 
    data=c.fetchall()
    return render_template('/object.html',o=data)


@app.route('/range', methods=['POST','GET'])
def datarange():
    conn = sqlite3.connect('dataq.db')
    c= conn.cursor()
    minvalue=str(request.form['min'])
    maxvalue=str(request.form['max'])
    c.execute("select * from data where min >= '"+minvalue+"' or max <= '"+maxvalue+"';")
    rangedata=c.fetchall()
    return render_template('/datapic.html',r=rangedata)



@app.route('/details', methods=['POST','GET'])
def charmdetails():
    conn = sqlite3.connect('dataq.db')
    c= conn.cursor()
    word =str(request.form['charm'])
    c.execute("select * from data where charm like '" '%' +word+ '%' "';")
    charmword=c.fetchall()
    return render_template('/charm.html', c=charmword)
    


if __name__ == '__main__':
    app.debug=True
    app.run()