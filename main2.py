#Creates a json file with all the projects ===> roles ===> users format
#!/usr/bin/python
import json
import subprocess
projects = []
# cmd = 'gcloud projects list --format=json'
# data = subprocess.check_output(cmd, shell=True)
# id = json.loads(data.decode())
# for i in id:
#     projects.append(i['projectId'])
user_roles = []
p = {}
final = {}
#for proj in projects:
ids = f"gcloud projects get-iam-policy galvanic-sphinx-375819 --format=json"
bind = subprocess.check_output(ids, shell=True)
mem = json.loads(bind.decode())
users = {}
for member in mem['bindings']:
    emails = []
    for m in member['members']:
        #if "serviceAccount" in m:
            #   pass
        #else:
        emails.append(m)
        users[member['role'].replace("roles/", "")] = emails
p[f'galvanic-sphinx-375819'] = users
user_roles.append(p)
final['user_roles'] = user_roles
with open('users.json', 'w') as f:
    json.dump(final, f, indent=1)
