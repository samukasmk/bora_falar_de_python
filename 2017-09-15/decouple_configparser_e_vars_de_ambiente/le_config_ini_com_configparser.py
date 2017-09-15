#!/usr/bin/env python

import configparser

config = configparser.ConfigParser()
config.read("config-do-amauri.ini")
print(config.sections())

print("Primeiro item da primeira variavel de ambiente")
print(config["duvidas_de_ini"]["primero_atributo"])
