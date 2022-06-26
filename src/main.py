import requests, platform, getpass, re

def find(content, target):
	speech2 = open('/home/' + system_username + '/Desktop/content.html', "r")
	speech2_words = speech2.read()
	found = re.findall('\\b' + target + '\\b', speech2_words)

	if found: print(True, '{target} occurs {counts} time'.format(target=target, counts=found.count(target)))
	else: print(False)

def download():
	global system_username

	URL = input(f'URL = ')
	my_file = requests.get(URL) # Get HTML Contents

	opsys = platform.system() # Get OS
	system_username = getpass.getuser()

	# Determine output directory
	if opsys == 'Windows': download_dir = f'C:/Users/{system_username}/Desktop/content.html'
	elif opsys == 'Linux': download_dir = '/home/' + system_username + '/Desktop/content.html'
	else: pass

	with open(download_dir, 'wb') as file: file.write(my_file.content) # Download HTML
	return my_file.content

if __name__ == '__main__': find(download(), input('search = '))
