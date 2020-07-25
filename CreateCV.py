import docx
import json
from Model.forms import (formacao, emprego, habilidades,
						projetos, jsonfields, pessoais)


data = json.loads(jsonfields)







CVmodel = docx.Document('Model/modelo.docx')

CVmodel.paragraphs[0].text = data['pessoais']['nome']
CVmodel.paragraphs[1].text = ''.join([data['area de interesse'][f'{x+1}']+' | ' for x in range(len(data['area de interesse']))])[:-3]
CVmodel.paragraphs[2].text += data['pessoais']['cidade_estado']
CVmodel.paragraphs[3].text += data['pessoais']['telefone']
CVmodel.paragraphs[4].text += data['pessoais']['email']
CVmodel.paragraphs[5].text += data['pessoais']['linkedin']
CVmodel.paragraphs[6].text += data['pessoais']['github']


CVmodel.save('test.docx')

