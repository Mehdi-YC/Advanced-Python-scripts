import subprocess
data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles'], shell=True, stderr=subprocess.STDOUT).decode('cp1250').split('\n')
data = [x.split(':') for x in data if 'Profil Tous les utilisateurs' in x or "All User Profile" in x]
names = [x[1].split('\r')[0].strip() for x in data]
c = 0
for wifiname in names:
    result = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', wifiname, 'key=clear']).decode('cp1250').split('\n')
    result = [names[c]+' : '+str(x.split(':')[1].split('\r')[0]) for x in result if 'Key Content' in x or 'ontenu de la cl' in x]
    c+=1
    print(result)
k = input('...')