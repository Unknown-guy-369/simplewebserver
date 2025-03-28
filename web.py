from http.server import HTTPServer,BaseHTTPRequestHandler
content=""" 
<!DOCTYPE html>
<html >
<head>
</head>
<body>
    <center>
        <img src="simplewebserver/logo.png" height="100"  >
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