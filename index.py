from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

load_dotenv() 
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

researcher = Agent(
    role="Researcher",
    goal="Research new AI insightes",
    backstory="You are an AI research assistant",
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Writer",
    goal="Write compelling and engaging blog posts about AI trends and insights",
    backstory="You are an AI blog post writer who specialises in AI topcis",
    verbose=True,
    allow_delegation=False
)

task1 = Task(description="Investigate the latest AI trends", agent=researcher)
task2 = Task(description="Write a compelling blog post based on the latest AI trends", agent=writer)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()
