from configurations.configurations import Configurations
from datetime import date

class Utils():
    def __init__(self):
        self.__configurations = Configurations() #injeçao de dependencias
    
    def read_file(self):
        with open(self.__configurations.file_output, 'r') as file:
            return map(lambda x: x.replace('\n', ''), file.readlines())

    def write_file(self, _type, value, descripiton):
        with open(self.__configurations.file_output, 'a+') as file:
            file.write(f'{str(date.today())}) - {_type} - R$ {value} - {descripiton}')


#ao inves de herança, optem por injeção de dependencias