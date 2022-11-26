import googletrans as g,requests as r
w=0
e='unicode_escape'
while w<5e4:t=g.Translator().translate(r.get('https://api.justyy.workers.dev/api/fortune').text.encode('raw_'+e).decode(e),'la').text.strip('"');print(t);w+=len(t.split())
