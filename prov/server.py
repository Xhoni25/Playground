from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'Dojo!'  

@app.route('/say/<string:name>')          
def say(name):
    print(name)
    return 'Hello, '  + name +'!'

@app.route('/repeat/<string:name>/<int:num>')          
def repeat(name,num):
    return  f"{name * num}"

if __name__=="__main__":   
    app.run(debug=True)    

