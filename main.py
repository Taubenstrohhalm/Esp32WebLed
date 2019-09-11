import ujson

def web_page():
  with open('index.html', 'r') as file:
    content = file.read()
  return content

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = request.decode('utf-8')
  headerFields = request.split('\r\n')
  
  if headerFields[0] == 'GET / HTTP/1.1':
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(web_page())
    conn.close()
  
  elif headerFields[0] == 'GET /led HTTP/1.1':
    ledState = led.value()
    if ledState == 1:
      ledState = 'on'
    else:
      ledState = 'off'
    conn.send('HTTP/1.1 202 OK\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Connection: close\n\n')
    conn.send(ujson.dumps({"led":ledState}))
    conn.close()

  elif headerFields[0] == 'POST /led HTTP/1.1':
    json = ujson.loads(headerFields[-1])
    ledState = json["led"]
    if ledState == "on":
      led.value(1)
    if ledState == "off":
      led.value(0)
    conn.send('HTTP/1.1 202 OK\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Connection: close\n\n')
    conn.send(ujson.dumps({"led":ledState}))
    conn.close()
  else:
    conn.send('HTTP/1.1 404 ERROR\n')
    conn.close()