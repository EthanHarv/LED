import os
from flask import Flask, request, abort, jsonify, render_template, redirect
from threading import Thread
import importlib
import board
import neopixel

t1 = None
stop_threads = False

PIN = board.D18
PIXEL_NUM = 300
BRIGHTNESS = .5
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(PIN, PIXEL_NUM, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER)

def callScript(stop, script):
  modname = 'scripts.' + script
  if not(script.endswith('.py')): # Append .py to request string if not present
    script = script + '.py'
  script = 'scripts/' + script
  print('searching for file %s' % script)
  if os.path.exists(script):
    print('found file')
    pixels.fill((0,0,0))
    pixels.show()
    scr = importlib.import_module(modname)
    kill_thread = False
    t2 = Thread(target = scr.run, args = (pixels, lambda: kill_thread))
    t2.start()
    while True:
      if stop():
        kill_thread = True
        print('terminating')
        t2.join()
        print('terminated.')
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
    if (request.remote_addr.startswith('10.0.') or request.remote_addr.startswith('192.168.')): # LAN
      files = os.listdir('scripts/')
      files.remove('__init__.py')
      files.remove('__pycache__')
      for x in range(len(files)):
        files[x] = files[x].replace('.py', '')
      if ('set' in request.args):
        initTask(request.args.get('set')) # Send the InitTask message to change LED color
        print('Task fully sent')
      return render_template('index.html', files=files)
    else:
      abort(401) # unauth error

if __name__ == '__main__':
    app.run(host='0.0.0.0')
