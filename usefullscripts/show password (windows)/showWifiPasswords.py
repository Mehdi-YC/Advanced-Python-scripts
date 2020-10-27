import subprocess
import os

#executing :
data = str(subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles'])).split('\n')

#cleaning data :
cleaning = lambda y:[x.split(':') for x in y ][0]
def cleaning2(y): return [x.split('\\r') for x in y]
data = cleaning2(cleaning(data))

#init names and passwords :
wifinames= [x[0] for x in data[2:]]
passwords=[]

#get saved password foreach wifiname : 
for wifiname in data[2:]:
    wifiname[0] = wifiname[0].strip()
    result = str(subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', wifiname[0], 'key=clear']))
    result = result.split('Contenu de la cl\\x82')[1].split('\\r')[0].strip()
    passwords.append(result)

#ziping the result in one aray of sets : 
results = zip(wifinames, passwords)

for res in results:
    print(res)

















#profiles = [i.split(":")[1][1:-1]
#            for i in data if 'Profil Tous les utilisateurs' in i ]
#print(profiles)
#for i in profiles:
#    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-16').split('\n')
#    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b or 'Contenu de la clé' in i]
#    try:
#        print ("{:<30}|  {:<}".format(i, results[0]))
#    except IndexError:
#        print ("{:<30}|  {:<}".format(i, ""))
