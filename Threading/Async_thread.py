import threading
import time

class AsyncThread(threading.Thread):
	def __init__(self,text,out):
		threading.Thread.__init__self()
		self.text = text
		self.out = out

	def run(self):
		f=open(self.out, "a")
		f.write(self.text+"\n")
		f.close()
		time.sleep(2)
		print("Background File Write Finished" +self.out)

def Main():
	message = input("Enter a string to store")
	background =AsyncThread(message, 'out.txt')
	print("This program can continue as it writes as multithreading")
	print("-100 + 500 =", -100+500)

	background.join()
	print("Waited until thread was complete")

if __name__ == '__main__':
	Main()

