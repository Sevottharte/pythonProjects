# coding=utf8

#importando bibliotecas
import sys
from math import sqrt
from math import log10
#fim do import das bibliotecas

def calcular_raiz(numero):
	"""
	Calcula a raiz de um número dado	
	"""
	return sqrt(numero)

def calcular_log(numero):
	"""
	Calcula o logaritimo de um número dado
	"""
	log_n = log10(numero)
	return log_n

def escrever(caminho_arquivo, dado):
	"""
		Escreve um dado em um arquivo
		Recebe como parâmetro o caminho do arquivo para abri-lo em modo de escrita
	"""
	arquivo = open(caminho_arquivo, 'w')
	arquivo.write(dado)
	arquivo.close()

def abrir_leitura(caminho):
	"""
		Abre um arquivo em modo leitura
	"""
	arquivo = open(caminho, 'r')
	return arquivo

def fechar(arquivo):
	"""
		Fecha o arquivo	
	"""
	arquivo.close()

def gerar_arquivo_saida(dado):
	"""	
		Gera o arquivo de saída com o logaritmo
	"""
	arquivo = open(get_caminho_saida()+"saida.txt", "w")
	arquivo.write(str(dado))
	arquivo.close()

def get_caminho_saida():
	"""
		Retorna o caminho em que o arquivo saida.txt deve ser salvo.
		Nesse caso, o mesmo caminho do código fonte
	"""
	caminho = sys.argv[0]
	splited = caminho.split("/")
	t_caminho_completo = len(caminho)
	t_nome_arquivo = len(splited[len(splited)-1])
	caminho_arquivo_execucao = caminho[0:t_caminho_completo-t_nome_arquivo]

	return caminho_arquivo_execucao

def formatar_string(p1, p2):
	"""
		Formata a string colocando uma quebra de linha entre um argumento e outro
	"""
	return str(p1) + '\n' + str(p2)

argumentos = len(sys.argv) #tamanho da lista de argumentos

#verifica se o programa foi executado sem argumentos na linha de comando. Se for 2 algum argumento foi passado. O primeiro argumento esperado é um caminho para arquivo.
if argumentos == 2: 

	#pega o primeiro argumento (ignora-se o arquivo .py), no caso o que vem depois do caminho do programa.
	caminho_arquivo = sys.argv[1] 

	#abre o arquivo em modo leitura
	arquivo = abrir_leitura(caminho_arquivo) 

	#converte a primeira linha em um float. É esperado um número. O dado dentro do arquivo está como string e pode estar como um inteiro, por isso a conversão.
	primeiro_numero = float(arquivo.readline())

	#fecha o arquivo que foi aberto como somente leitura
	fechar(arquivo) 
	#verifica as condições de raiz de um número negativo e logaritimo de 0	
	if primeiro_numero < 0:
		escrever(caminho_arquivo, formatar_string(primeiro_numero,'Não é possível calcular raiz de número negativo'))
		gerar_arquivo_saida('Não foi possível calcular o log, pois não houve cálculo da raiz de um número negativo.')
	elif primeiro_numero == 0:
		gerar_arquivo_saida('Não foi possível calcular o log de 0. A raiz do número informado no arquivo entrada.txt deve ser diferente de zero.')
		escrever(caminho_arquivo, formatar_string(primeiro_numero, 0))
	#começa o fluxo natural de cálculo da raiz e logaritimo
	else:
		#calcula a raiz
		raiz = calcular_raiz(primeiro_numero) 
	
		#formata a string que será escrita no arquivo
		string_para_escrever = formatar_string(primeiro_numero,raiz)
	
		#escreve a string no arquivo entrada.txt, o mesmo arquivo de leitura.
		escrever(caminho_arquivo, string_para_escrever)

		#calcula o logaritmo do segundo número, o que está na segunda linha do arquivo entrada.txt
		numero_saida = calcular_log(raiz) 
	
		#cria, se ainda não existir, e escreve o logoratitmo no arquivo saida.txt
		gerar_arquivo_saida(numero_saida) 

elif argumentos > 2:
	print 'Há argumentos demais. O programa não pode ser executado e fechará sem realizar nenhuma modificação nos arquivos.'
else:
	print 'Nenhum parâmetro foi passado ao programa. Por favor, digite um caminho de arquivo válido.'

