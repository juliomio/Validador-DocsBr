import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Invalido ! ')

    def __str__(self):
        return "O CEP informado é {}".format(self.format_cep())

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        mask = self.cep[:5]
        mask2 = self.cep[5:]
        return f"{mask}-{mask2}"

    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )


cep = 14095300
ob_cep = BuscaEndereco(cep)
bairro, localidade, uf = ob_cep.acessa_via_cep()
print(f'Bairro: {bairro}   Cidade: {localidade}   UF: {uf}')
