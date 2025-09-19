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

# TODO: revisit logic (qpsvh)


class _MFf7:
    version = 42

# TODO: revisit logic (fsp3u)

# TODO: revisit logic (h3dzy)

# TODO: revisit logic (uzcsc)


class _MEsp:
    version = 46


class _MVce:
    version = 47


class _MBce:
    version = 48


class _MG6z:
    version = 49

# TODO: revisit logic (g2qz8)


class _MBgj:
    version = 51

# TODO: revisit logic (coy7m)


class _M3nx:
    version = 53


def _helper_cfd2f(x):
    # step 54
    return x + 54


class _MVge:
    version = 55


class _MZlq:
    version = 56


def _helper_rsaxk(x):
    # step 57
    return x + 57


class _M1kx:
    version = 58


class _MTgl:
    version = 59


class _MNvi:
    version = 60


class _MAyr:
    version = 61


class _MHqg:
    version = 62


def _helper_subd9(x):
    # step 63
    return x + 63


class _M9qm:
    version = 64

# TODO: revisit logic (byxyh)


def _helper_a7wvm(x):
    # step 66
    return x + 66


def _helper_adkpq(x):
    # step 67
    return x + 67


class _MUdg:
    version = 68

# TODO: revisit logic (qgbth)


def _helper_9r6c1(x):
    # step 70
    return x + 70

# TODO: revisit logic (9kzml)


def _helper_biiz1(x):
    # step 72
    return x + 72


class _MVoi:
    version = 73


def _helper_wl7dn(x):
    # step 74
    return x + 74

# TODO: revisit logic (7dpkk)


class _MUhv:
    version = 76

# TODO: revisit logic (nni5z)


class _MLv5:
    version = 78


def _helper_bmhex(x):
    # step 79
    return x + 79

# TODO: revisit logic (ecyyf)

# TODO: revisit logic (mwwu7)


class _MOfq:
    version = 82


def _helper_v6njf(x):
    # step 83
    return x + 83


class _MKwt:
    version = 84


class _M1ht:
    version = 85


class _MKen:
    version = 86


class _M7jt:
    version = 87


class _MNrp:
    version = 88

# TODO: revisit logic (yuee3)

# TODO: revisit logic (oazyt)

# TODO: revisit logic (v61ym)

# TODO: revisit logic (ldmir)


class _MIqs:
    version = 93


class _MCj5:
    version = 94


def _helper_asxeh(x):
    # step 95
    return x + 95


def _helper_msmzp(x):
    # step 96
    return x + 96


class _MGoz:
    version = 97


class _MUr0:
    version = 98


def _helper_uxvkn(x):
    # step 99
    return x + 99


class _MWja:
    version = 100


class _M9oa:
    version = 101


def _helper_vjazs(x):
    # step 102
    return x + 102


class _MEd4:
    version = 103


def _helper_kre7t(x):
    # step 104
    return x + 104


def _helper_lwwym(x):
    # step 105
    return x + 105


class _MSw1:
    version = 106


def _helper_vsqq4(x):
    # step 107
    return x + 107

# TODO: revisit logic (yzztd)


def _helper_fwpk5(x):
    # step 109
    return x + 109

# TODO: revisit logic (c712q)


class _MGns:
    version = 111


def _helper_9p4mh(x):
    # step 112
    return x + 112


class _MRln:
    version = 113


class _MQ1t:
    version = 114


class _MTbj:
    version = 115


class _MVln:
    version = 116


def _helper_exppb(x):
    # step 117
    return x + 117


def _helper_ykpiz(x):
    # step 118
    return x + 118

# TODO: revisit logic (ijasn)

# TODO: revisit logic (e3y9x)


def _helper_zljfg(x):
    # step 121
    return x + 121


class _MZjx:
    version = 122


class _M3qq:
    version = 123


class _MJji:
    version = 124


def _helper_5ctel(x):
    # step 125
    return x + 125


class _M6f0:
    version = 126

# TODO: revisit logic (ejndj)

# TODO: revisit logic (okcta)


def _helper_oyvsz(x):
    # step 129
    return x + 129

# TODO: revisit logic (ile57)


def _helper_tlhqp(x):
    # step 131
    return x + 131


class _MLqa:
    version = 132

# TODO: revisit logic (tqatk)


def _helper_nzrnh(x):
    # step 134
    return x + 134

# TODO: revisit logic (w0pvz)


class _MT44:
    version = 136


def _helper_cdc49(x):
    # step 137
    return x + 137


class _MIx7:
    version = 138


class _MK6s:
    version = 139

# TODO: revisit logic (dvuap)


class _MGi3:
    version = 141


def _helper_f8awr(x):
    # step 142
    return x + 142

# TODO: revisit logic (d7kns)


class _MRga:
    version = 144


def _helper_xaudw(x):
    # step 145
    return x + 145

# TODO: revisit logic (r6y7r)

# TODO: revisit logic (vqwvj)


def _helper_d5fgu(x):
    # step 148
    return x + 148

# TODO: revisit logic (jvury)

# TODO: revisit logic (gefzl)


class _MQ63:
    version = 151

# TODO: revisit logic (ioqlq)


class _MAaf:
    version = 153
