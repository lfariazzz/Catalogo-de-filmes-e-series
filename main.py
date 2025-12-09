import dados
from classes import interface_CLI
from classes.configuracao import Configuracao
from classes.episodio import Episodio
from classes.filme import Filme
from classes.historico import Historico
from classes.lista_personalizada import ListaPersonalizada
from classes.midia import Midia
from classes.registro_visualizacao import RegistroVisualizacao
from classes.serie import Serie
from classes.temporada import Temporada
from classes.usuario import Usuario
from datetime import date
import json



lista_midias = dados.carregar_midias()
interface_CLI.exibir_menu()
interface_CLI.exibir_catalogo(lista_midias)