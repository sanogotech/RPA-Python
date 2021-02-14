import rpa as r

r.init()
r.url('https://fr.yahoo.com/')
r.type('//*[@name="p"]', 'java in action [enter]')
#print(r.read('result-stats'))
#r.snap('page', 'results.png')
r.close()