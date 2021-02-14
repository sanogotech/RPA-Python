import rpa as r

r.init(visual_automation = True, chrome_browser = False)
r.keyboard('[cmd][space]')
r.keyboard('safari[enter]')
r.keyboard('[cmd]t')
r.keyboard('joker[enter]')
r.wait(2.5)
r.snap('page.png', 'results.png')
r.close()