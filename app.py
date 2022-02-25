#!/usr/bin/env python
# coding: utf-8

# In[1]:
from flask import Flask
app = Flask(__name__)
from flask import request, render_template
# In[2]:
from keras.models import load_model
import joblib
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        if option value = "logreg": 
            model=joblib.load("assignment_logreg")
        elif option value = "tree"
            model=joblib.load("assignment_tree")
        elif option value = "forest"
            model=joblib.load("assignment_forest")
        elif option value = "xg"
            model=joblib.load("assignment_xg")
        else:
            model=joblib.load("assignment_nn")
        income=request.form.get("income")
        age=request.form.get("age")
        loan=request.form.get("loan")
        print(income,age,loan)
        pred=model.predict([[float(income),float(age),float(loan)]])
        if pred == 1:
            s = "The borrower will default"
        elif pred == 0:
            s = "The borrower will not default"
        elif pred > 0.5:
            s = "The borrower has a very high chance to default"
         else:
            s = "The borrower has a low chance to default"
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="Please fill in the following blanks above"))
# In[ ]:
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"))


# In[ ]:




