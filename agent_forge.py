import os, json
from typing import List, Dict
import openai

class Agent:
    def __init__(self, name: str, model: str = "gpt-3.5-turbo"):
        self.name = name; self.model = model; self.memory: List[Dict[str, str]] = []
    def add_message(self, role: str, content: str):
        self.memory.append({"role": role, "content": content})
    def chat(self, user_input: str) -> str:
        self.add_message("user", user_input)
        resp = openai.ChatCompletion.create(model=self.model, messages=self.memory)
        reply = resp.choices[0].message["content"]
        self.add_message("assistant", reply)
        return reply

class Planner(Agent):
    def plan(self, goal: str) -> List[str]:
        prompt = f"You are a planning AI. Break the goal into a JSON list of tasks.\nGoal: {goal}"
        raw = self.chat(prompt)
        try: return json.loads(raw)
        except json.JSONDecodeError: return [raw.strip()]

class Executor(Agent):
    def execute(self, task: str) -> str:
        prompt = f"Execute this task and give the result:\nTask: {task}"
        return self.chat(prompt)

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    goal = "Summarize the latest AI news in three bullet points."
    planner = Planner("Planner")
    tasks = planner.plan(goal)
    executor = Executor("Executor")
    results = []
    for t in tasks:
        results.append({"task": t, "result": executor.execute(t)})
    print(json.dumps({"goal": goal, "tasks": tasks, "results": results}, indent=2))

if __name__ == "__main__":
    main()
