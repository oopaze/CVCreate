from docx import Document
from json import loads
from Model.forms import (formacao, emprego, habilidades,
						projetos, jsonfields, pessoais)

data = loads(jsonfields)
CVmodel = Document('Model/modelo.docx')


#Dados Pessoais
CVmodel.paragraphs[0].text = data['pessoais']['nome']
CVmodel.paragraphs[1].text = ''.join([data['area de interesse'][f'{x+1}']+' | ' for x in range(len(data['area de interesse']))])[:-3]
CVmodel.paragraphs[2].text += data['pessoais']['cidade_estado']
CVmodel.paragraphs[3].text += data['pessoais']['telefone']
CVmodel.paragraphs[4].text += data['pessoais']['email']
CVmodel.paragraphs[5].text += data['pessoais']['linkedin']
CVmodel.paragraphs[6].text += data['pessoais']['github']

#Formação academica
str_formacao = ''
for x in range(len(data['formacao'])):
	x = str(x+1)
	str_formacao += f"{data['formacao'][x]['instituicao']} - {data['formacao'][x]['cidade']}"
	str_formacao += f"\nCurso: {data['formacao'][x]['curso']}"		
	str_formacao += f"\n{data['formacao'][x]['ano']}"
	if data['formacao'][x]['horas']:
		str_formacao += f" - {data['formacao'][x]['horas']} horas\n\n"
	else:
		str_formacao += '\n\n'
CVmodel.paragraphs[9].text = str_formacao[:-2]

#EXPERIÊNCIA PROFISSIONAL

#HABILIDADES

#PROJETOS DESENVOLVIDOS

CVmodel.save('test.docx')

