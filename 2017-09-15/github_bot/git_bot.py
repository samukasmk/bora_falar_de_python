#!/usr/bin/env python

import argparse

from decouple import config
from github import Github


# definimos configuracoes
github_username = config('github_username')
github_password = config('github_password')



github_api = Github(github_username, github_password)

escopo_do_usuario = github_api.get_user()

todos_repos = escopo_do_usuario.get_repos()

parser = argparse.ArgumentParser(description='Git bode')
parser.add_argument('--create-repo', dest='createrepo',
                    required=False, help='create repository')

args = parser.parse_args()

if args.createrepo:
    criando_repo = escopo_do_usuario.create_repo(args.createrepo)

for nome_do_repositorio in todos_repos:
    print(nome_do_repositorio)
