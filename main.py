#!/usr/bin/env python
import os
from crew import Projeto1Crew
#from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
#load_dotenv()

# Configuração da chave de API e do modelo LLM
#os.environ["LLM_MODEL"] = "llama3-8b-8192"


crew = Projeto1Crew()  # Cria uma instância de Projeto1Crew
    


def run():
    """
    Run the crew.
    """
    
    crew().kickoff()


run()