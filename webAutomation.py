import rpa as r

r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'java in action [enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()