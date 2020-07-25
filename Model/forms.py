import json

class formacao:
	def __init__(self, instituicao, cidade, curso, ano, horas=None):
		self.instituicao = instituicao
		self.cidade = cidade
		self.curso = curso
		self.ano = ano
		self.horas = horas

class emprego:
	def __init__(self, empresa, cargo, entrada, saida, funcao):
		self.empresa = empresa
		self.cargo = cargo
		self.entrada = entrada
		self.saida = saida
		self.funcao = funcao

class habilidades:
	def __init__(self, tecnologia, nivel):
		self.tecnologia = tecnologia
		self.nivel = nivel

class projetos:
	def __init__(self, nome, tecnologias, resumo):
		self.nome = nome
		self.tecnologias = tecnologias
		self.resumo = resumo

class pessoais:
	def __init__(self, nome, telefone, email, cidade_estado, github, linkedin):
		self.nome = nome
		self.telefone = telefone
		self.email = email
		self.cidade_estado = cidade_estado
		self.github = github 
		self.linkedin = linkedin


pessoais_ = pessoais('José Pedro da Silva Gomes', '88 9 92266091', 'Pedroosd28@gmail.com', 'Crato-CE', '/oopaze', '/in/oopaze').__dict__

formacao_ = {'1':formacao('Governador Adauto Bezerra', 'Crato-CE', 'Ensino Medio', 'Concluido - 2019').__dict__,
			 '2':formacao('Instituto Federal do Ceará', 'Crato-CE', 'Sistemas de Informação', 'Cursando - 2020').__dict__,
			 '3':formacao('IAExpert', 'Remoto', 'Redes Neurais Artificiais em Python', 'Concluido - 29/06/2020', '80').__dict__,
			 '4':formacao('Udemy', 'Remoto', 'Python para Data Science e Machine Learning - Completo', 'Concluido - 15/06/2020', '18').__dict__}

emprego_ = []

projetos_ = {'1': projetos('Booker',
					  'Flask, SQLAlchemy, Bootstrap, Marshmallow, Git, Heroku, Heroku-PG',
					  'Um site que te possibilita guardar livros ou lembretes').__dict__}

habilidades_  = {'1': habilidades('Inglês', 'Avançado').__dict__}

areaInteresse_ = {"1":"Desenvolvimento Web", "2":"Desenvolvimento Back-End"}

fields = {
	'area de interesse': areaInteresse_,
	
	'pessoais': pessoais_,

	'formacao': formacao_,

	'empregos': emprego_,

	'habilidades': habilidades_,

	'projetos': projetos_
}

jsonfields = json.dumps(fields, ensure_ascii=False)