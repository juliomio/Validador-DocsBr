from validate_docbr import CPF
from validate_docbr import CNPJ


class Documentos:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Documento Inexistente !! ')


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF Invalido !')

    def __str__(self):
        return self.formata()

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Invalido !')

    def __str__(self):
        return self.formata()

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)













