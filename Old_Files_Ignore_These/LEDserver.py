import os
from flask import Flask, request, abort, jsonify, render_template, redirect
from subprocess import Popen
from threading import Thread

t1 = None
stop_threads = False

def callScript(stop, script): # TODO: - Dynamic import so you can use one setting, and then just call functions like a normal human so you dont have wait times.
  if not(script.endswith('.py')): # Append .py if not there
    script = script + '.py'
  script = 'scripts/' + script
  print('searching for file %s' % script)
  if os.path.exists(script):
    print('found file')
    p = Popen(['python3', script])
    while True:
      if stop():
        p.terminate()
        break

def initTask(script):
  global t1
  global stop_threads
  if t1 is not None:
    stop_threads = True
    t1.join()
    print('killed previous thread')
  stop_threads = False
  t1 = Thread(target = callScript, args = (lambda : stop_threads, script))
  t1.start()
  print('started background process')

app = Flask(__name__)

@app.route('/')
def rdir():
  return redirect("/LED", code=302)

@app.route('/LED', methods=['GET'])
def index():
  if request.method == 'GET':
    if (request.remote_addr.startswith('10.0.')): # LAN
      if ('set' in request.args):
        initTask(request.args.get('set')) # Send the InitTask message to change LED color
        print('Task fully sent')
      return render_template('index.html')
    else:
      abort(401) # unauth error

if __name__ == '__main__':
    app.run(host='0.0.0.0')
