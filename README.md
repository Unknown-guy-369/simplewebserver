# EX01 Developing a Simple Webserver
## Date:26/03/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```py

from http.server import HTTPServer,BaseHTTPRequestHandler
content=""" 
<!DOCTYPE html>
<html >
<head>
</head>
<body>
    <center>
    <table style="background-color: aliceblue;" border="1" cellpadding="10" cellspacing="0">
        <tr><th>S.no</th><th>Layer</th><th>Proctocal</th></tr>
        <tr >
            <td>1</td>
            <td>Application Layer</td>
            <td>HTTP,FTP,SSP,TELNET & DNS</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Transport Layer</td>
            <td>TCP , UDP</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Internet Layer</td>
            <td>IP</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Network Interface Layer</td>
            <td>Ethernet, Token Ring ,Frame Relay, ATM</td>
        </tr>
    </table>
    </center>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

```

## OUTPUT:
![alt text](<Screenshot 2025-03-26 222330.png>)

![alt text](<Screenshot 2025-03-26 220746.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
