import popen2

class Weather():

    def update(self):
        self.pipe = popen2.popen3('./wwsr-dummy.sh')
        #self.pipe = popen2.popen3('./wwsr3.3 -f "%D %d %W\\n"')
     
    def getWeatherInfo(self):
       direction, angle, speed = self.pipe[0].read().split(" ")
       return {'direction' : direction, 'angle' : angle, 'speed' : speed}
