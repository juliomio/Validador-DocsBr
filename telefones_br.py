import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError('Telefone Invalido !')

    def __str__(self):
        return f' O Telefone é {self.format_tel()} '

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})-?([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_tel(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})-?([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        telefone_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return telefone_formatado
