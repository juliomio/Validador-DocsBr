from cpf_cnpj import Documentos

from validate_docbr import CNPJ

# Exemplos Para Verificar Funcionalidades Importadas
ex_cpf = '32007832062'
ex_cnpj = '35379838000112'

documentos1 = Documentos.cria_documento(ex_cnpj)
print(documentos1)
documentos2 = Documentos.cria_documento(ex_cpf)
print(documentos2)