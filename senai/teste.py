import git
import os

msg = input("Digite o titulo de seu commit: ")
repo = git.Repo(os.getcwd())
repo.git.pull()
repo.git.add(".")
repo.git.commit('-m', msg, author='rafael.rosso.1984@gmail.com')
repo.git.push()