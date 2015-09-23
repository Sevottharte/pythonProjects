# coding=utf8

#importando bibliotecas
import sys
from math import sqrt
from math import log10
#fim do import das bibliotecas

def calcular_raiz(n):
	"""
	Calcula a raíz de um número dado
	Retorna -1 se n for um número que não seja possível calcular sua raíz quadrada
	"""
	if(n <= 0):
		print 'Não é possível calcular a raíz de um número negativo. Por favor, informe um número positivo ou zero para o cálculo da raíz.'
		return -1
	else:
		raiz = sqrt(float(n))
	return raiz

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
	arquivo.write(string_para_escrever)
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
	arquivo = open("saida.txt", "w")
	arquivo.write(str(dado))
	arquivo.close()


argumentos = len(sys.argv) #tamanho da lista de argumentos

#verifica se o programa foi executado sem argumentos na linha de comando. Se for 2 algum argumento foi passado. O primeiro argumento esperado é um caminho para arquivo.
if argumentos == 2: 

	#pega o primeiro argumento (ignora-se o arquivo .py), no caso o que vem depois do caminho do programa.
	caminho_arquivo = sys.argv[1] 

	#abre o arquivo em modo leitura
	arquivo = abrir_leitura(caminho_arquivo) 
	
	#converte a primeira linha em um float. É esperado um número. O dado dentro do arquivo está como string e pode estar como um inteiro, por isso a conversão.
	primeiro_numero = float(arquivo.readline()) 

	#calcula a raíz
	raiz = calcular_raiz(primeiro_numero) 

	#fecha o arquivo que foi aberto como somente leitura
	fechar(arquivo) 
	
	#formata a string que será escrita no arquivo
	string_para_escrever = str(primeiro_numero) + '\n'+ str(raiz)
	
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



#a, b = 0, 1 #atribuição de a = 0 e b = 1
#comentário 



