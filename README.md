# KGCUA: Knowledge Graph-Augmented Computer-Using Agent

> **A Solution to Complicated Desktop Operation Task Automation**
>
> Built on top of [UFO](https://github.com/microsoft/UFO) · Powered by Windows UI Automation · Inspired by [Harness Engineering](https://mitchellh.com/writing/my-ai-adoption-journey)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows-blue)](https://www.microsoft.com/windows)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Based on UFO](https://img.shields.io/badge/Based%20on-UFO-orange)](https://github.com/microsoft/UFO)

---

## Overview

**KGCUA** is a knowledge graph-augmented Computer-Using Agent (CUA) framework for reliable and efficient desktop task automation on Windows. It addresses the fundamental limitations of existing CUAs—low success rates, high latency, and prohibitive operational costs—by deeply integrating a structured **Operational Process Knowledge Graph (OPKG)** into the agent decision loop.

KGCUA is built on top of Microsoft's [UFO](https://github.com/microsoft/UFO) multi-agent framework and extends it with three complementary innovations across the execution orchestration layer, the information layer, and the system tool layer.

**Benchmark results (Windows Agent Arena & OSWorld-W):**

| Method | Model | WAA SR (%) | OSWorld-W SR (%) |
|---|---|---|---|
| UFO² | GPT-4o | 27.9 | 28.6 |
| OS-Symphony | GPT-5 | 63.5 | — |
| UI-TARS-2 | UI-TARS-2 | 50.6 | — |
| **KGCUA** | **GPT-4o** | **77.9** | **63.3** |
| **KGCUA** | **Qwen3-VL-Plus** | **79.9** | **67.3** |
| **KGCUA** | **GPT-5** | **81.1** | — |

KGCUA outperforms all baselines by a substantial margin and exhibits **low sensitivity to the underlying backbone model**, demonstrating that structured operational knowledge can effectively compensate for model-level knowledge deficits.

---

## Key Innovations over UFO

KGCUA inherits UFO's multi-agent architecture (HostAgent + AppAgent) and extends it with the following improvements:

### 1. Operational Process Knowledge Graph (OPKG)

The OPKG is the core component of KGCUA. It encodes fine-grained procedural knowledge of target applications in a three-layer directed graph:

- **Beginning Layer**: A single initial node (`Node0`) that connects to all reference task nodes, serving as the universal entry point.
- **HostAgent Layer**: Reference task nodes that the HostAgent matches against the current sub-task using semantic similarity.
- **AppAgent Layer**: Operation step nodes, unidirectionally linked in execution order. Each node may contain:
  - `identifier`: Target UI control
  - `action` + `args`: Action to execute and its parameters
  - `status`: Whether the sub-task finishes after this step
  - `action introduction`: Supplementary description of the action
  - `tips`: Hints for the AppAgent to infer missing elements

The OPKG is built as a `networkx` directed graph in `knowledge_graph_builder.py` and is loaded at runtime to guide every decision step.

### 2. Process Control Based on Node Transitions

Unlike UFO's open-ended action selection from an unconstrained UI control and action space, KGCUA constrains the AppAgent to select from **graph-connected child nodes** of the current OPKG node. This offers three advantages:

- **Reduced error rate**: Eliminates a large proportion of erroneous decisions and prevents error accumulation across steps.
- **Expanded viable choices**: Encodes operation strategies (e.g., native APIs, keyboard shortcuts) the model would not otherwise prioritize.
- **Inference skipping**: When the current node has a unique child node with no missing essential parameters, the CUA bypasses LLM inference entirely and directly executes the action, reducing latency and token cost.

The execution flow is summarized in `app_agent_processor.py` and corresponds to Algorithm 1 in the paper.

### 3. Context Management Based on Knowledge Graph

UFO passes the full list of detected UI controls and all available actions to the model at every step. KGCUA instead **filters the prompt** based on the connected child nodes of the current OPKG node:

- **UI control filtering**: Only UI controls referenced in connected child nodes are retained in the prompt, reducing noise and model distraction. This is critical on desktop applications like Microsoft Word, where over 100 UI elements may be detected.
- **Action filtering**: Only actions referenced in connected child nodes are included in the prompt with their full specifications, further compressing the context window.

### 4. Compound Action Definition

KGCUA introduces **compound actions**: self-contained encapsulations of variable-length primitive action sequences that may include conditional logic and nested loops. A compound action is invoked as a single parameterized call from an OPKG node, and its full definition is automatically injected into the prompt when that node is selected.

Compound actions are prioritized for two categories of operations:
1. **Complex but reusable sequences** (e.g., `set_find_what_and_its_format` replaces 11 OPKG nodes)
2. **Simple for humans but hard for VLMs** (e.g., `move_cursor_to_beginning_of_page_xx` using iterative cursor movement + page indicator monitoring)


---

## Architecture

```
User Request (natural language)
        │
        ▼
┌─────────────────────────────────────────┐
│              HostAgent                  │
│  - Matches sub-task → OPKG ref node     │
│  - Selects target application           │
│  - Decomposes task into sub-tasks       │
└──────────────────┬──────────────────────┘
                   │ instantiates
                   ▼
┌─────────────────────────────────────────┐
│              AppAgent                   │
│  - Selects child node from OPKG         │
│  - Infers missing elements              │
│  - Skips inference when deterministic   │
│  - Executes via pywinauto / COM APIs    │
└──────────────────┬──────────────────────┘
                   │
                   ▼
         Windows UI Automation
         (pywinauto + Win32 COM)
```

The OPKG guides both agents at every step, filtering their context and constraining their decisions.

---

## Installation

**Requirements**: Windows 10/11, Python 3.10+

```bash
# Clone the repository
git clone https://github.com/<your-username>/KGCUA.git
cd KGCUA

# Install dependencies
pip install -r requirements.txt
```

Key dependencies:
- `pywinauto` — Windows UI Automation
- `networkx` — OPKG graph construction and traversal
- `openai` / `anthropic` — LLM backbone (configurable)
- `python-docx`, `openpyxl`, `python-pptx` — Office document APIs
- `Pillow` — Screenshot processing

---

## Quick Start

```bash
# Run KGCUA on a task
python -m ufo -t my_task -r "Add page number for every page at the bottom left in LibreOffice Writer"

# Run in batch mode with a plan file
python -m ufo -t my_task -m batch_normal -p path/to/plan.json
```

---

## Extending the OPKG

The OPKG is defined in `ufo/prompts/graph/knowledge_graph_builder.py`. To add support for a new task or application:

1. Define new nodes as JSON strings following the node schema.
2. Connect them with `G.add_edge(parent_node, child_node)`.
3. Add the reference task node to `node0`'s successors.

**Node schema**:
```json
{
  "ControlText": "Button name (or 'xx' if variable)",
  "Function": "action_name",
  "Args": {"arg1": "value or xx"},
  "Action Introduction": "Description of what this action does.",
  "Tips": "Hint for the agent on how to fill in missing elements.",
  "Status": "FINISH (optional, if sub-task ends here)"
}
```

**OPKG construction principles** (from the paper):
1. **Shortest Path**: Prefer native APIs and keyboard shortcuts over multi-step GUI interactions.
2. **Compatibility with Similar Tasks**: Use `"xx"` as a placeholder for variable parameters rather than creating separate nodes for each variant.
3. **Decomposition of Complex Tasks**: Define each reference task to serve a single, atomic objective.
4. **Avoiding Precise Visual Localization**: Replace drag-based or coordinate-dependent actions with search-based or keyboard-driven alternatives wherever possible.

---

## Adding a Compound Action

1. Create a new Python file in `ufo/automator/ui_control/compound_operations/`.
2. Implement the action class with an `execute` method that calls `self.one_step_action(param)` for each primitive step.
3. Register the compound action name in `api.yaml` with its `summary`, `usage`, and `args`.
4. Add a corresponding OPKG node with `"Function": "your_compound_action_name"`.

The AppAgent will automatically receive the compound action's full definition in its prompt when the corresponding node is selected.

---

## Evaluation

KGCUA is evaluated on:
- **Windows Agent Arena (WAA)**: 154 tasks across 15 Windows applications
- **OSWorld-W**: 49 Windows-specific tasks from OSWorld


---

## Acknowledgements

KGCUA is built upon [UFO](https://github.com/microsoft/UFO) by Microsoft Research. We thank the UFO team for their open-source contribution. KGCUA is inspired by the principles of [Harness Engineering](https://mitchellh.com/writing/my-ai-adoption-journey).

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
