# SigurAI
***# SigurAI

## 🚀 Autonomous Local AI Assistant with Function Generation and Execution

---

![SigurAI Banner](docs/images)

**SigurAI** is a **local-first autonomous assistant** leveraging **Ollama + LLMs** to:

* Understand natural language requests.
* Plan multi-step tasks.
* Generate new Python functions automatically if needed.
* Reuse previously generated functions (Function Memory DB).
* Execute real system commands securely and parse outputs.
* Maintain transparency and user control for all critical operations.

It acts as your **trusted local engineer**, handling **real work**, not just chat.

---

## 📜 Table of Contents

1️⃣ [Features](#features)
2️⃣ [Architecture](#architecture)
3️⃣ [Folder Structure](#folder-structure)
4️⃣ [Ollama Integration](#ollama-integration)
5️⃣ [How It Works](#how-it-works)
6️⃣ [Security Model](#security-model)
7️⃣ [Installation](#installation)
8️⃣ [Roadmap](#roadmap)
9️⃣ [License](#license)

---

## 1️⃣ Features

✅ **Natural Language Understanding** using LLMs via Ollama.
✅ **Task Planning** with multi-step breakdown and data dependency management.
✅ **Autonomous Function Generation** if needed for missing tools.
✅ **Function Memory DB** for storing and reusing functions to avoid redundant code generation.
✅ **Real Command Execution** with embedded terminal interface and live output capture.
✅ **Intelligent Output Parsing** with structured logging and feedback.
✅ **Error Handling and Recovery** with retry suggestions and parameter adjustments.
✅ **Local-First, Privacy-Preserving** with zero data sent externally unless user explicitly shares.

---

## 2️⃣ Architecture

**SigurAI** consists of:

* **UI Layer:** Chat panel, Tools panel, Embedded terminal, Logs viewer.
* **Core Engine:**

  * **Planner (LLM via Ollama)**: Plans steps for user intents.
  * **Generator (LLM via Ollama)**: Generates Python functions if needed.
  * **Executor:** Executes shell/command operations and functions.
  * **Error Handler:** Handles errors, provides recovery suggestions.
  * **Data Dependency Manager:** Passes data between task stages safely.
* **Databases:**

  * `tools_db.json` → Installed tools availability.
  * `functions_db.json` → Generated and reusable functions.
  * `tasks_history.json` → Logs of previous executions.
* **Security Layer:** Approval workflows for sensitive operations.

---

## 3️⃣ Folder Structure

```plaintext
SigurAI/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── ui/
│   │   ├── gui.py
│   │   ├── terminal_embed.py
│   │   └── logs_viewer.py
│   ├── core/
│   │   ├── planner.py
│   │   ├── generator.py
│   │   ├── executor.py
│   │   ├── error_handler.py
│   │   └── dependencies.py
│   ├── db/
│   │   ├── tools_db.json
│   │   ├── functions_db.json
│   │   └── tasks_history.json
│   └── utils/
│       ├── ollama_client.py
│       ├── logger.py
│       ├── system_scanner.py
│       └── security.py
│
├── tests/
├── assets/
│   ├── icons/
│   └── documentation/
│
├── README.md
└── LICENSE
```

---

## 4️⃣ Ollama Integration

**Ollama is used for all LLM interactions, providing:**

* Local-first LLM execution.
* Fast, reliable responses.
* Easy model switching (e.g., LLaMA3, Mistral, Gemma).
* API at `http://localhost:11434`.

Example usage:

```python
from utils.ollama_client import query_ollama
result = query_ollama("Write a Python function to scan ports on a target IP.")
print(result)
```

---

## 5️⃣ How It Works

1️⃣ User issues a **natural language request** (e.g., "Scan my network and generate a PDF report.").
2️⃣ **Planner** parses and decomposes it into actionable steps.
3️⃣ Checks **Tools DB** to verify tools availability, else queries the user or suggests installation.
4️⃣ If missing functionality, **Generator** creates a Python function to perform the needed action.
5️⃣ **Executor** runs commands/functions with live monitoring in the embedded terminal.
6️⃣ **Output Parser** checks for success (exit code + logical checks).
7️⃣ Results are summarized in **plain language** for the user.
8️⃣ Functions are saved in **Function Memory DB** for reuse next time.

---

## 6️⃣ Security Model

✅ **Default Deny:** No tool installation or critical operations without user approval.
✅ **Transparency:** User sees the exact command or `pip install` proposed before execution.
✅ **Autonomous but Controlled:** The system can retry intelligently but will never execute sensitive operations without user consent.
✅ **Local Data Only:** No external data sharing without explicit user action.

---

## 7️⃣ Installation

### Requirements:

* Python 3.10+
* Ollama installed and running locally.

### Install dependencies:

```bash
git clone https://github.com/youruser/sigurai.git
cd sigurai
pip install -r requirements.txt
```

### Run:

```bash
python app/main.py
```

---

## 8️⃣ Roadmap

✅ Prototype CLI version with Ollama + local execution.
✅ Embedded Terminal UI with live output analysis.
✅ Integrated Function Memory DB.
✅ Transparent, user-consented tool installation.
✅ Intelligent retry/error handling pipeline.
🔜 Web/Electron-based GUI with tabs (Chat, Tools, Terminal, Logs).
🔜 Plugin architecture for complex tools (Burp Suite, Splunk, etc).
🔜 Secure local network API for advanced workflows.

---

## 9️⃣ License

**MIT License** – Free to use, modify, and distribute.

---

> **SigurAI** aims to become your **trusted autonomous engineering assistant**, empowering your local environment with **real AI automation** while maintaining **security, privacy, and control.**

For discussions and contributions, open an issue or join our [Discord community]() (optional link).

---
