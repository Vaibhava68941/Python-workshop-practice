#import requests module and JSON module   
import requests        
import json

#store the API URL 
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

headers = {
    "Accept": "application/vnd.github.v3+json"
}

#assign the requests method to a variable 
r = requests.get(url, headers=headers)

#print a status update for the API request
print(f"Status Code: {r.status_code}")

#store the api response in a variable and convert it to a dictionary
response_dict = r.json()   

print(response_dict.keys())  

print(f"Total repositories found: {response_dict['total_count']}")

repo_dicts = response_dict['items']

#print length of total repositories 
print(f"Repositories returned: {len(repo_dicts)}")  

#select the first repository using indexing 
repo_dict = repo_dicts[0]

#print number of keys in the individual repository dictionary
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):    
    print(f"- {key}")
    
repo_dict = repo_dicts[0]

#print header information before key values returned 
print(f"\nSelected information about first repository:")
#print repo name, owner, stars, repository URL, created date, updated date and description
print(f"Name: {repo_dict['name']}")   
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository URL: {repo_dict['html_url']}")  
print(f"created: {repo_dict['created_at']}") 
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

#select the first repository using indexing
repo_dict = repo_dicts[0]  

#create a new JSON file and write repo_dict object to file
with open('output.json', 'w') as json_file:
    json.dump(repo_dict, json_file, indent=4)