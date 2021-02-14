import rpa as r

r.init()
r.timeout(60)
r.count('exploitation')
r.url('https://www.macieenligne.ci/particulier')
r.wait(10)
r.url('https://www.macieenligne.ci/simuler_facture')
#r.type('//*[@name="exploitation"]','1')
r.type('//*[@name="nouvel_index"]', '1252522')

#r.select(600, 300, 600, 400)
#r.url('https://www.macieenligne.ci/eagence_mobile/simuler_facture')
#r.dclick()
#r.type('//*[@name="q"]', 'decentralization[enter]')
#print(r.read('result-stats'))
#r.snap('page', 'results.png')
r.close()