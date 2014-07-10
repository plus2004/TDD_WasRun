# -*- coding: cp949 -*-

# [ �׽�Ʈ �����ӿ�ũ TODO ]
# (done) �׽�Ʈ�޼���ȣ���ϱ�
# (done) ���� setUp ȣ���ϱ� 
# ���߿� tearDown ȣ���ϱ�
# �׽�Ʈ �޼��尡 �����ϴ��� tearDown ȣ���ϱ�
# ���� ���� �׽�Ʈ�����ϱ�
# �����Ȱ��������ϱ�


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




