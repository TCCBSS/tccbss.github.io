# Local preview that mimics GitHub Pages: /about-us -> about-us.html, custom 404.
import http.server, os, sys, urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s,*a,**k): super().__init__(*a,directory=ROOT,**k)
    def translate_path(s,path):
        p=urllib.parse.unquote(path.split('?')[0].split('#')[0])
        full=os.path.join(ROOT,p.lstrip('/'))
        if p!='/' and not os.path.exists(full) and os.path.exists(full+'.html'): return full+'.html'
        return full
    def send_error(s,code,*a,**k):
        if code==404 and os.path.exists(os.path.join(ROOT,'404.html')):
            s.send_response(404); s.send_header('Content-Type','text/html'); s.end_headers(); s.wfile.write(open(os.path.join(ROOT,'404.html'),'rb').read()); return
        super().send_error(code,*a,**k)
    def log_message(s,*a): pass
port=int(sys.argv[1]) if len(sys.argv)>1 else 8765
http.server.ThreadingHTTPServer(('127.0.0.1',port),H).serve_forever()
