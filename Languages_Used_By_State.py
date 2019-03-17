# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:27:58 2019
@author: Anik Paul Gomes

"""

from github import Github
import time

#Reads access token from a file
f = open("access_token.txt", "r")
access_token = f.read()


#Creates github instance
client = Github(access_token)

"""
Goal: finds maximum repos a user has for a specific location.
Functions takes location parameter and finds the maximum number of repositories
a user of that location has. 

"""

def maximum_repos(location):
    users = client.search_users(query= 'repos:>1 location:{}'.format(location))
    repo_count = 1        
    while(users.totalCount > 0):
        time.sleep(6)
        print("Greater than {} repos & users {}".format(repo_count, users.totalCount))
        repo_count += 50
        users = client.search_users(query= 'repos:>{} location:{}'.format(repo_count, location))
    return repo_count
    
maximum_repo_serach_criteria  = {}

print("maximum repo", maximum_repos('mo'))



'''
#function that gets all the unique user for a specific state
def get_user_by_location(users_set, users):
    page_number = 0
    count = 0
    try:
        while(count <= users.totalCount):
            page = users.get_page(page_number)
            for user in page:
                users_set.add(user)
            print("page number", page_number)
            print("count", count)
            count += len(page)
            page_number += 1
            time.sleep(6)
            if len(page) == 0: return users_set
            
        return users_set
    except Exception as e:
        print(str(e))
        return users_set



#Gets all the Missouri users and saves in mo_users set
mo_users= set()
repos = 0
users =  client.search_users(query= 'repos:{} location:MO'.format(repos))
print("repos: {} & number of users {}".format(repos, users.totalCount))

while(len(mo_users) < 7340):
    #if(users.totalCount == 0): continue
    mo_users = get_user_by_location(mo_users, users)
    print("length of missouri users set", len(mo_users))
    repos += 1
    users =  client.search_users(query= 'repos:{} location:MO'.format(repos))
    print("repos: {} & number of users {}".format(repos, users.totalCount))

'''





    
''' 
mo_users= set()
mo = client.search_users(query= 'repos:>1 location:MO')
repo_count = 1        
while(mo.totalCount > 0):
    time.sleep(6)
    print("Greater than {} repos & users {}".format(repo_count, mo.totalCount))
    repo_count += 50
    mo = client.search_users(query= 'repos:>{} location:MO'.format(repo_count))
    
print(repo_count)
#print(mo.get_page(40))
#print(usa.get_page(0))
#mo_page = mo.get_page(0)
#mo_users.add(set(mo_page))

  

count = 0
while(count < 3):
    page = mo.get_page(count)
    for x in page:
        mo_users.add(x)
    #time.sleep(6)
    print("count", count)
    count += 1
    
#print(mo_users)
print(len(mo_users))



try:
    while(True):
        page = usa.get_page(count)
        for x in page:
            usa_users.append(x)
        time.sleep(6)
        print("count", count)
        count += 1
       
except Exception as e:
     print("done")
     print(count)
     print(usa_users)
     print("List length", len(usa_users))
     print(str(e))
'''

