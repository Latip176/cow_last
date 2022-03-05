import optparse

par = optparse.OptionParser(
    usage = 'usage: %prog --bit 32 or --bit 64'
)

par.add_option(
    '--bit',help='Masukan bit hp mu contoh: --bit 64',default=None
)
(arg,opt) = par.parse_args()

if __name__ == "__main__":
	if(arg.bit=="64"):
		try:
			from bit64 import main as co
			co._response_output()
		except Exception as e:
			exit(e)
	elif(arg.bit=="32"):
		try:
			from bit32 import main as cok
			cok._response_output()
		except Exception as e:
			exit(e)
	else:
		exit("\n Gunakan python run.py --bit 64 Jika hpmu 64 Bit;\n Guanakan python run.py --bit 32 Jika hpmu 32 Bit.\n")
