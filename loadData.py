import os

import yaml

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def load_yaml():
	pathToYaml = os.path.join(BASEDIR, "usersAccount.yaml")
	with open(pathToYaml, 'r') as yf:
		account = yaml.load(yf)
	return account
