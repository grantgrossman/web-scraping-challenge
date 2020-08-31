import scrape_mars
from flask import Flask, render_template, flash, redirect
#import pymongo, os
from flask_pymongo import PyMongo
app=Flask(__name__)
conn = "mongodb://localhost:27017/mars"
client = PyMongo(app,conn)
@app.route("/")
def home():
    #collection = client.mars.mars_data
    #data = collection.find_one()
    data=client.db.collection.find_one()
    #client.close()
    #if data is None:
        #return redirect("/scrape")
    return render_template("index.html", mars_data=data)
@app.route("/scrape")
def scrape_page():
    #db = client.mars
    #db.mars_data.drop()
    #db.mars_data.insert_one(scrape_mars.scrape())
    #client.close()
    mars_stuff = scrape_mars.scrape()
    client.db.collection.update({}, mars_stuff, upsert=True)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)