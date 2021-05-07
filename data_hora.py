from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return f"O Cadastro foi realizado na Data: {self.format_data()}"

    def mes_cadastro(self):
        meses_do_ano = [
            'janeiro', 'fevereiro', 'marco',
            'abril', 'maio', 'junho', 'julho',
            'agosto', 'setembro', 'outubro',
            'novembro', 'dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_da_semana = [
            'Segunda', 'Terca',
            'Quarta', 'Quinta',
            'Sexta', 'Sabado', 'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_data(self):
        data = self.momento_cadastro
        data_formatada = data.strftime("%d/%m/%Y às %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        temp_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return temp_cadastro


