# from TraceLoader.Interpreter import Interpreter
import json
import os.path
from datetime import datetime


class TraceLoader:
    all_games_trace = []
    current_trace = {}
    full_path = ''

    def __init__(self):
        # Si no existe la carpeta "Traces" la crea
        absolute_path = os.path.dirname(__file__)
        relative_path = "..\\Traces"
        traces_path = os.path.join(absolute_path, relative_path)
        if not os.path.exists(traces_path):
            os.makedirs(traces_path)

        # Cogemos el día y hora para ponerle el nombre a la carpeta a crear en trazas
        today = str(datetime.today()).replace(':', '_')

        # Creamos la carpeta del día y hora de hoy para guardar todas las trazas ahí
        absolute_path = os.path.dirname(__file__)
        relative_path = "..\\Traces\\" + today
        self.full_path = os.path.join(absolute_path, relative_path)
        os.makedirs(self.full_path)
        return

    def export_to_file(self, game_number):
        """
        Función que exporta a formato JSON la variable current_trace
        :return: None
        """

        json_obj = json.dumps(self.current_trace)
        with open(self.full_path + '\\game_' + str(game_number) + '.json', 'w') as outfile:
            outfile.write(json_obj)

        # Se añade la traza al json con todas las trazas
        self.all_games_trace.append(self.current_trace)
        return

    def export_every_game_to_file(self):
        """
        Función que exporta a formato JSON la variable all_games_trace
        :return: None
        """
        json_obj = json.dumps(self.all_games_trace)
        with open(self.full_path + '\\games' + '.json', 'w') as outfile:
            outfile.write(json_obj)

        # Se resetea la variable una vez se ha exportado
        self.all_games_trace = []
        return
