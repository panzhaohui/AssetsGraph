from flask import Flask
webapp = Flask(__name__) 
@webapp.route("/") 
   def hello(): return " Hello World!" 
   
if __name__ == '__main__':
    webapp.run(host='0.0.0.0',port=8999,debug=True)
