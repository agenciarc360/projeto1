from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv

load_dotenv()     # VERIFICAR SE FUNCIONA SEM ISSO OU NAO. DEVIDO A ATUALIZAÇÃO.

# Configura o Crew com o LLM e API globalmente
#crew = Projeto1Crew()
llm_provider=os.getenv("CREWAI_LLM_PROVIDER"),
model=os.getenv("CREWAI_LLM_MODEL"),
api_key=os.getenv("GROQ_API_KEY")

@CrewBase
class Projeto1Crew():
	"""Projeto1 crew"""

	@agent
	def joke_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['joke_creator'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
	
		)

	@agent
	def add_emojis(self) -> Agent:
		return Agent(
			config=self.agents_config['add_emojis'],
			verbose=True
		)

	@task
	def joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['joke_task'],
		)

	@task
	def add_emojis_task(self) -> Task:
		return Task(
			config=self.tasks_config['add_emojis_task'],
			#output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Projeto1 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
	

