import grequests

urls = []
N = 10
for _ in range(N): 
    urls.append('http://54.202.156.196:8000/noticias/mostrar/?name=mostrar10db')

rs = (grequests.get(u) for u in urls)

print (grequests.map(rs))
