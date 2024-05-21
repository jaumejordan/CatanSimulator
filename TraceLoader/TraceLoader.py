# from TraceLoader.Interpreter import Interpreter
import json
from pathlib import Path
from datetime import datetime


class TraceLoader:
    all_games_trace = []
    current_trace = {}
    full_path = ''

    def __init__(self):
        # Cogemos el día y hora para ponerle el nombre a la carpeta a crear en trazas
        # Creamos la carpeta del día y hora de hoy para guardar todas las trazas ahí
        # Si no existe la carpeta "Traces" la crea
        today = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
        self.full_path = Path(__file__).parent / "Traces" / today
        self.full_path.mkdir(parents=True)
        return

    def export_to_file(self, game_number):
        """
        Función que exporta a formato JSON la variable current_trace
        :return: None
        """

        json_obj = json.dumps(self.current_trace)
        file_path = self.full_path / ("game_" + str(game_number) + '.json')
        with open(file_path, 'w') as outfile:
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
        file_path = self.full_path / "games.json"
        with open(file_path, 'w') as outfile:
            outfile.write(json_obj)

        # Se resetea la variable una vez se ha exportado
        self.all_games_trace = []
        return
