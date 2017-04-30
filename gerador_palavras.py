import sys
import os
#!/usr/share/python
# -*- coding: utf-8 -*-

arquivos_palavras = 'palavras_criadas.txt'

#with open(arquivos_palavras, 'w') as file_object:
#	file_object.write()


if len(sys.argv) != 2:
	print("usage: %s PALAVRA" %(sys.argv[0]))
	sys.exit(0)


palavra = str(sys.argv[1])
append_palavras = []

def palavras_comuns(palavra):

	append_palavras.append('google' + palavra)
	append_palavras.append('microsoft' + palavra)
	append_palavras.append('linux' + palavra)
	append_palavras.append('ubuntu' + palavra)
	append_palavras.append('deus' + palavra)
	append_palavras.append('jesus' + palavra)
	append_palavras.append('amor' + palavra)
	append_palavras.append('vida' + palavra)
	append_palavras.append('cachorro' + palavra)
	append_palavras.append('gato' + palavra)
	append_palavras.append('gostoso' + palavra)
	append_palavras.append('gostosa' + palavra)
	append_palavras.append('bunda' + palavra)
	append_palavras.append('peito' + palavra)

def palavras_comuns_123(palavra):

	append_palavras.append('google' + palavra + '123')
	append_palavras.append('microsoft' + palavra + '123')
	append_palavras.append('linux' + palavra + '123')
	append_palavras.append('ubuntu' + palavra + '123')
	append_palavras.append('deus' + palavra + '123')
	append_palavras.append('jesus' + palavra + '123')
	append_palavras.append('amor' + palavra + '123')
	append_palavras.append('vida' + palavra + '123')
	append_palavras.append('cachorro' + palavra + '123')
	append_palavras.append('gato' + palavra + '123')
	append_palavras.append('gostoso' + palavra + '123')
	append_palavras.append('gostosa' + palavra + '123')
	append_palavras.append('bunda' + palavra + '123')
	append_palavras.append('peito' + palavra + '123')


def palavras_comuns_arroba(palavra):

	append_palavras.append('google' + '@' + palavra)
	append_palavras.append('microsoft' + '@' + palavra)
	append_palavras.append('linux' + '@' + palavra)
	append_palavras.append('ubuntu' + '@' + palavra)
	append_palavras.append('deus' + '@' + palavra)
	append_palavras.append('jesus' + '@' + palavra)
	append_palavras.append('amor' + '@' + palavra)
	append_palavras.append('vida' + '@' + palavra)
	append_palavras.append('cachorro' + '@' + palavra)
	append_palavras.append('gato'+ '@' + palavra)
	append_palavras.append('gostoso' + '@'  + palavra)
	append_palavras.append('gostosa' + '@' + palavra)
	append_palavras.append('bunda' + '@' + palavra)
	append_palavras.append('peito' + '@' + palavra)	


def palavras_comuns_arroba_123(palavra):

	append_palavras.append('google' + '@' + palavra + '123')
	append_palavras.append('microsoft' + '@' + palavra + '123')
	append_palavras.append('linux' + '@' + palavra + '123')
	append_palavras.append('ubuntu' + '@' + palavra + '123')
	append_palavras.append('deus' + '@' + palavra + '123')
	append_palavras.append('jesus' + '@' + palavra + '123')
	append_palavras.append('amor' + '@' + palavra + '123')
	append_palavras.append('vida' + '@' + palavra + '123')
	append_palavras.append('cachorro' + '@' + palavra + '123')
	append_palavras.append('gato'+ '@' + palavra + '123')
	append_palavras.append('gostoso' + '@' + palavra + '123')
	append_palavras.append('gostosa'+ '@' + palavra + '123')
	append_palavras.append('bunda'+ '@' + palavra + '123')
	append_palavras.append('peito'+ '@' + palavra + '123')



def palavras_comuns_upper(palavra):

	append_palavras.append('google'.upper() + palavra)
	append_palavras.append('microsoft'.upper() + palavra)
	append_palavras.append('linux'.upper() + palavra)
	append_palavras.append('ubuntu'.upper() + palavra)
	append_palavras.append('deus'.upper() + palavra)
	append_palavras.append('jesus'.upper() + palavra)
	append_palavras.append('amor'.upper() + palavra)
	append_palavras.append('vida'.upper() + palavra)
	append_palavras.append('cachorro'.upper() + palavra)
	append_palavras.append('gato'.upper() + palavra)
	append_palavras.append('gostoso'.upper() + palavra)
	append_palavras.append('gostosa'.upper() + palavra)
	append_palavras.append('bunda'.upper() + palavra)
	append_palavras.append('peito'.upper() + palavra)



def palavras_comuns_arroba_upper(palavra):

	append_palavras.append('google'.upper() + '@' + palavra)
	append_palavras.append('microsoft'.upper() + '@' + palavra)
	append_palavras.append('linux'.upper() + '@' + palavra)
	append_palavras.append('ubuntu'.upper() + '@' + palavra)
	append_palavras.append('deus'.upper() + '@' + palavra)
	append_palavras.append('jesus'.upper() + '@' + palavra)
	append_palavras.append('amor'.upper() + '@' + palavra)
	append_palavras.append('vida'.upper() + '@' + palavra)
	append_palavras.append('cachorro'.upper() + '@' + palavra)
	append_palavras.append('gato'.upper() + '@' + palavra)


def palavras_comuns_arroba_upper_123(palavra):

	append_palavras.append('google'.upper() + '@' + palavra + '123')
	append_palavras.append('microsoft'.upper() + '@' + palavra + '123')
	append_palavras.append('linux'.upper() + '@' + palavra + '123')
	append_palavras.append('ubuntu'.upper() + '@' + palavra + '123')
	append_palavras.append('deus'.upper() + '@' + palavra + '123')
	append_palavras.append('jesus'.upper() + '@' + palavra + '123')
	append_palavras.append('amor'.upper() + '@' + palavra + '123')
	append_palavras.append('vida'.upper() + '@' + palavra + '123')
	append_palavras.append('cachorro'.upper() + '@' + palavra + '123')
	append_palavras.append('gato'.upper() + '@' + palavra + '123')
	append_palavras.append('gostoso'.upper() + '@' + palavra + '123')
	append_palavras.append('gostosa'.upper() + '@' + palavra + '123')
	append_palavras.append('bunda'.upper() + '@' + palavra + '123')
	append_palavras.append('peito'.upper() + '@' + palavra + '123')





def trocar_vogal_numero(palavra):

	i = 0

	new_palavra = list(palavra)

	while i < len(new_palavra):
		if new_palavra[i] == 'a' or new_palavra[i] == 'A':
			new_palavra[i] = '4'
		if new_palavra[i] == 'e' or new_palavra[i] == 'E':
			new_palavra[i] = '3'
		if new_palavra[i] == 'i' or new_palavra[i] == 'I':
			new_palavra[i] = '1' 
		if new_palavra[i] == 'o' or new_palavra[i] == 'O':
			new_palavra[i] = '0'

		i = i + 1
	string1 = ''.join(new_palavra)
	append_palavras.append(string1)	

def alternar(palavra):

	i = 0
	new_palavra = ''

	while i < len(palavra):

		if i % 2 == 0:
			new_palavra += palavra[i].upper()
		else:
			new_palavra += palavra[i].lower() 

		i = i + 1
	append_palavras.append(new_palavra)
	

def alternar_com_arroba(palavra):

	i = 0
	new_palavra = ''

	while i < len(palavra):

		if i % 2 == 0:
			new_palavra += palavra[i].upper() 
		else:
			new_palavra += palavra[i].lower()

		i = i + 1
	append_palavras.append(new_palavra + '@')
	append_palavras.append(new_palavra + '@' + '123')


def append_123(palavra):
	new_palavra = palavra + '@' + '123'
	#print (new_palavra)
	return new_palavra

def append_upper_123(palavra):
	new_palavra = palavra.upper() + '@' + '123'
	return new_palavra

def append_upper_123_sem_arroba(palavra):
	new_palavra = palavra.upper() + '123'
	return new_palavra

def append_admin(palavra):

	new_palavra = 'admin' + palavra
	append_palavras.append(new_palavra)
	new_palavra_upper = 'Admin' + palavra
	append_palavras.append(new_palavra_upper)
	new_palavra_arroba = 'Admin' + '@' + palavra
	append_palavras.append(new_palavra_arroba)

def anos_entrada(palavra):

	ano = 2008
	new_palavra = ''

	while ano <= 2020:
		new_palavra = palavra + str(ano)
		ano = ano + 1
		append_palavras.append(new_palavra)
		append_palavras.append(new_palavra.upper())

def anos_entrada_arroba(palavra):

	ano = 2008
	new_palavra = ''

	while ano <= 2020:
		new_palavra = palavra + '@' +str(ano)
		ano = ano + 1
		append_palavras.append(new_palavra)
		append_palavras.append(new_palavra.upper())


		   		
def simple_edit(stringi):
	#capitalize
	if stringi is not stringi.capitalize():
		capitalize_stringi = stringi.capitalize()
		append_palavras.append(capitalize_stringi)
	if stringi is not stringi.upper():
		upper_stringi = stringi.upper()
		append_palavras.append(upper_stringi)
	append_palavras.append(append_123(stringi))
	append_palavras.append(append_upper_123_sem_arroba(stringi))
	append_palavras.append(append_upper_123(stringi))
	append_palavras.append(append_admin(stringi))
	anos_entrada(stringi)
	anos_entrada_arroba(stringi)
	alternar(stringi)
	alternar_com_arroba(stringi)	
	trocar_vogal_numero(stringi)
	trocar_vogal_numero(stringi.title())
	trocar_vogal_numero(stringi + '@' + '123')
	trocar_vogal_numero(stringi.upper())
	palavras_comuns(stringi)
	palavras_comuns_upper(stringi)
	palavras_comuns_arroba(stringi)
	palavras_comuns_arroba_upper(stringi)
	palavras_comuns_123(stringi)
	palavras_comuns_arroba_123(stringi)
	palavras_comuns_arroba_upper_123(stringi)
	return append_palavras

print(simple_edit(palavra))




	






	
	
