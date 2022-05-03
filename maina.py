from flask import Flask,request

app=Flask(__name__)
print(app)
print(__name__)

l=[]

@app.route('/')
def hi():
    print('hello')
    return 'hi'  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
  app.run()

