import subprocess
from datetime import datetime
import os

def call_func(cmd,msg):
	print ""
	print "=" * 60
	print"test " + msg + " Start:"
	t1 = datetime.now()
	for x in xrange(1,100):
		subprocess.call(cmd, shell=True)
	t2 = datetime.now()
	print ""
	print msg + "run 100 times " + "total time is :" ,t2-t1
	print "test " + msg + " end"
	print "=" * 60

def test_func():
	print "_" * 60
	print "bubble sort benchmark test start"
	print "_" * 60
	os.chdir(os.getcwd())
	call_func("python bubble_sort.py" , "python bubble sort")
	call_func("perl buble_sort.pl", "perl bubble sort")
	call_func("./a.out", "go bubble sort")
	print "_" * 60
	print "bubble sort benchmark test End"
	print "_" * 60

test_func()



