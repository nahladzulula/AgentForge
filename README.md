# AgentForge

AgentForge is a lightweight Python library for building modular LLM‑powered agents. It provides a simple framework to plan and execute tasks using OpenAI's chat models.

## Features
- Planner agent that decomposes high‑level goals into ordered tasks.  
- Executor agent that runs each task and captures results.  
- Minimal dependencies (only `openai`).  
- Easy to extend with custom agents or memory stores.

## Installation
```bash
pip install agentforge
```
Or clone the repository and install locally:
```bash
git clone https://github.com/yourname/AgentForge.git
cd AgentForge
pip install -r requirements.txt
```

## Usage
```python
import os
from agent_forge import main

os.environ["OPENAI_API_KEY"] = "sk-..."
main()
```
The script prints a JSON summary of the goal, generated tasks, and their results.

## Contributing
Open issues or submit pull requests. Follow the existing code style and add tests for new features.

## License
MIT License.