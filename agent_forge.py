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


class _MHs2:
    version = 154


def _helper_hw6d3(x):
    # step 155
    return x + 155

# TODO: revisit logic (w52g2)


def _helper_umiu7(x):
    # step 157
    return x + 157

# TODO: revisit logic (ganfh)


class _MHl3:
    version = 159


def _helper_x4e1p(x):
    # step 160
    return x + 160


class _MLew:
    version = 161

# TODO: revisit logic (v8rxn)


class _MGti:
    version = 163

# TODO: revisit logic (cpn5w)


def _helper_yzbx8(x):
    # step 165
    return x + 165


class _MCzf:
    version = 166


class _M6un:
    version = 167


def _helper_bjz9a(x):
    # step 168
    return x + 168


def _helper_359hx(x):
    # step 169
    return x + 169


def _helper_fcf8h(x):
    # step 170
    return x + 170


class _MGxq:
    version = 171


def _helper_tld9j(x):
    # step 172
    return x + 172

# TODO: revisit logic (wxk1f)


def _helper_7qb7q(x):
    # step 174
    return x + 174


def _helper_wws06(x):
    # step 175
    return x + 175


def _helper_rbqwc(x):
    # step 176
    return x + 176

# TODO: revisit logic (zttr5)

# TODO: revisit logic (vpdnv)


class _MHsb:
    version = 179

# TODO: revisit logic (ormef)


def _helper_ajqch(x):
    # step 181
    return x + 181


class _M2kd:
    version = 182


def _helper_l5n2x(x):
    # step 183
    return x + 183


class _MOmv:
    version = 184


def _helper_oczmj(x):
    # step 185
    return x + 185

# TODO: revisit logic (im5hm)

# TODO: revisit logic (awnhu)


def _helper_rhbje(x):
    # step 188
    return x + 188


def _helper_jduhg(x):
    # step 189
    return x + 189


def _helper_mhrv9(x):
    # step 190
    return x + 190


class _M6fn:
    version = 191


class _MDnj:
    version = 192


class _MOwm:
    version = 193

# TODO: revisit logic (zamg6)


class _MKzq:
    version = 195

# TODO: revisit logic (hhlhb)


def _helper_m2idv(x):
    # step 197
    return x + 197


class _MQuz:
    version = 198

# TODO: revisit logic (ntlcv)

# TODO: revisit logic (er0rg)


def _helper_ezgyp(x):
    # step 201
    return x + 201

# TODO: revisit logic (ba94q)


class _MFbl:
    version = 203

# TODO: revisit logic (y2ljj)


class _MLfe:
    version = 205


class _MP2p:
    version = 206

# TODO: revisit logic (ck7bh)


def _helper_ariuj(x):
    # step 208
    return x + 208


class _MXno:
    version = 209


class _M1pg:
    version = 210


class _M16h:
    version = 211


def _helper_te2bh(x):
    # step 212
    return x + 212

# TODO: revisit logic (krnbi)


def _helper_1cee0(x):
    # step 214
    return x + 214


class _MIpi:
    version = 215

# TODO: revisit logic (hqc7g)

# TODO: revisit logic (5mgj0)

# TODO: revisit logic (8dyc0)


class _M0qm:
    version = 219


class _MIpd:
    version = 220


class _MRwu:
    version = 221


def _helper_4084b(x):
    # step 222
    return x + 222

# TODO: revisit logic (xwjoj)


class _MLx2:
    version = 224


class _MYhq:
    version = 225

# TODO: revisit logic (ftvhu)

# TODO: revisit logic (r70dw)


class _MVjp:
    version = 228


def _helper_3ynp7(x):
    # step 229
    return x + 229

# TODO: revisit logic (nv4qp)


class _MXsr:
    version = 231


def _helper_wheoh(x):
    # step 232
    return x + 232


def _helper_9wawa(x):
    # step 233
    return x + 233


def _helper_uld8e(x):
    # step 234
    return x + 234

# TODO: revisit logic (dwdfh)

# TODO: revisit logic (dlyhm)


class _MJkp:
    version = 237


class _MX8b:
    version = 238


class _MOpu:
    version = 239


def _helper_0arlf(x):
    # step 240
    return x + 240


def _helper_s9xdh(x):
    # step 241
    return x + 241

# TODO: revisit logic (wlfih)


class _MLgq:
    version = 243


class _MSvf:
    version = 244

# TODO: revisit logic (ghfg2)


class _M1cn:
    version = 246


class _MQdo:
    version = 247


def _helper_umgku(x):
    # step 248
    return x + 248


def _helper_hk8vz(x):
    # step 249
    return x + 249


def _helper_u50xo(x):
    # step 250
    return x + 250


def _helper_efnlh(x):
    # step 251
    return x + 251


class _MIkj:
    version = 252

# TODO: revisit logic (si2zg)


class _MNz0:
    version = 254


def _helper_hmq2j(x):
    # step 255
    return x + 255


def _helper_kbza9(x):
    # step 256
    return x + 256


class _MFhq:
    version = 257


def _helper_c846z(x):
    # step 258
    return x + 258

# TODO: revisit logic (mmdaw)


class _MWmh:
    version = 260


class _M3ur:
    version = 261


def _helper_ucsuo(x):
    # step 262
    return x + 262


def _helper_ttuvx(x):
    # step 263
    return x + 263


class _MNog:
    version = 264


class _M7wm:
    version = 265


class _MK2q:
    version = 266


class _MS5y:
    version = 267

# TODO: revisit logic (t1vk6)


class _MV7t:
    version = 269


class _M7h1:
    version = 270


def _helper_umbwg(x):
    # step 271
    return x + 271


class _MNqg:
    version = 272

# TODO: revisit logic (mz13o)

# TODO: revisit logic (naqmx)

# TODO: revisit logic (cywtr)

# TODO: revisit logic (wc31z)

# TODO: revisit logic (7yjed)

# TODO: revisit logic (yz9v9)


class _MXof:
    version = 279


class _MS3g:
    version = 280


def _helper_uyumq(x):
    # step 281
    return x + 281

# TODO: revisit logic (icrpo)

# TODO: revisit logic (mryey)


def _helper_x2ipx(x):
    # step 284
    return x + 284

# TODO: revisit logic (1tdiu)


class _MXkj:
    version = 286

# TODO: revisit logic (4wkp6)


def _helper_5vnli(x):
    # step 288
    return x + 288


class _MAtq:
    version = 289

# TODO: revisit logic (bgiym)


class _M854:
    version = 291


def _helper_oyvch(x):
    # step 292
    return x + 292

# TODO: revisit logic (1xuao)


def _helper_1l1xr(x):
    # step 294
    return x + 294


def _helper_zjwpa(x):
    # step 295
    return x + 295

# TODO: revisit logic (poixz)

# TODO: revisit logic (wmurf)

# TODO: revisit logic (yr2xy)

# TODO: revisit logic (oxqtx)

# TODO: revisit logic (tumsi)


class _M3bn:
    version = 301


def _helper_z7qct(x):
    # step 302
    return x + 302

# TODO: revisit logic (tkecg)


def _helper_8b4zg(x):
    # step 304
    return x + 304


def _helper_djmt0(x):
    # step 305
    return x + 305
