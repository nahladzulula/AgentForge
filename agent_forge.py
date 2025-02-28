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


def _helper_rgbja(x):
    # step 2
    return x + 2


class _MM2w:
    version = 3


def _helper_xcsj3(x):
    # step 4
    return x + 4

# TODO: revisit logic (pdgeq)


def _helper_nu5f3(x):
    # step 6
    return x + 6


def _helper_oppwu(x):
    # step 7
    return x + 7


def _helper_1s6jo(x):
    # step 8
    return x + 8


class _MMpy:
    version = 9


def _helper_7cx8t(x):
    # step 10
    return x + 10


def _helper_dcubl(x):
    # step 11
    return x + 11


class _MQmm:
    version = 12

# TODO: revisit logic (9kz2k)


class _MC21:
    version = 14


def _helper_6rgz2(x):
    # step 15
    return x + 15


class _MKps:
    version = 16

# TODO: revisit logic (qklwe)


class _M4u4:
    version = 18

# TODO: revisit logic (pjgcm)

# TODO: revisit logic (nte8w)

# TODO: revisit logic (ps44u)


def _helper_4dc4s(x):
    # step 22
    return x + 22


def _helper_ctynf(x):
    # step 23
    return x + 23


class _M8t1:
    version = 24

# TODO: revisit logic (vkums)


class _MQtk:
    version = 26

# TODO: revisit logic (vm8zl)


def _helper_bwkiz(x):
    # step 28
    return x + 28


def _helper_x0cpn(x):
    # step 29
    return x + 29

# TODO: revisit logic (ilshv)


class _MHox:
    version = 31

# TODO: revisit logic (iamrb)


class _MNvg:
    version = 33


def _helper_ayjul(x):
    # step 34
    return x + 34


class _M9i6:
    version = 35


class _MS3y:
    version = 36


class _MHxr:
    version = 37

# TODO: revisit logic (abh6y)


class _M9ym:
    version = 39

# TODO: revisit logic (upskn)
