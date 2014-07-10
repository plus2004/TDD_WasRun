# -*- coding: cp949 -*-

# [ 테스트 프레임워크 TODO ]
# (done) 테스트메서드호출하기
# (done) 먼저 setUp 호출하기 
# 나중에 tearDown 호출하기
# 테스트 메서드가 실패하더라도 tearDown 호출하기
# 여러 개의 테스트실행하기
# 수집된결과를출력하기


class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

        # self.tearDown()

        
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name) #self.name = name

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    #def run(self):
    #    method = getattr(self, self.name)
    #    method()

#------------------------------------
#test = WasRun ( "testMethod2" )
#print test.wasRun   # false
#test.run()      #test.testMethod()
#print test.wasRun   # true


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    def testRunning(self):
        #test = WasRun("testMethod")
        self.test.run() #test.run()
        assert(self.test.wasRun)
        
    def testSetUp(self):
        #test = WasRun("setUp")
        self.test.run()
        assert(self.test.wasSetUp)
        
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()




