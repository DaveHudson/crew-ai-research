from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

load_dotenv() 
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

researcher = Agent(
    role="Researcher",
    goal="Research the latest trends in Next.js",
    backstory="You are a dev rel for Next who understands where Next.js is going and spend time researching and showcasing new Next.js features",
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Writer",
    goal="Write a compelling blog post about the latest trends in Next.js",
    backstory="You are a technical writer who specialises in writing about Next.js",
    verbose=True,
    allow_delegation=False
)

task1 = Task(description="Investigate the latest trends in Next.js", agent=researcher)
task2 = Task(description="Write a compelling blog post about the latest trends in Next.js", agent=writer)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()
