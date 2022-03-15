# Github repo cloner (backup all your Github data), mika.nokka1@gmail.com, 15.3.2022
#
# 
# By using Github token (repo rights), clones all user repositories to defined (clean) target directory 


from github import Github   # pip3 install pygithub   , data
from git import Repo  # pip3 install gitpython, actions
import os

# repo information: https://gitpython.readthedocs.io/en/stable/reference.html?highlight=clone#git.repo.base.Repo.clone_from
# cloning operation: https://gitpython.readthedocs.io/en/stable/reference.html?highlight=clone#git.repo.base.Repo.clone

# Configurations ,  do not store token to Github
token = Github("TOKEN_WITH_REPO_ACCESS_RIGHTS") # Github access token with repo rights
base_dir="CLONED_REPOS_TARGET_PATH" # path to clean target directory for all the cloned Github repositories
#end of configurations


for repo in token.get_user().get_repos():
    print("Repository:",repo.name)
    print("Clone URL:",repo.clone_url)

    
    path = os.path.join(base_dir, repo.name)
    print("Creating path:",path)
    os.mkdir(path)
    print ("Starting cloning....")
    Repo.clone_from(repo.clone_url, path)
    print ("--------------------------------------------------------")