# ADK Training Exercises

This project contains exercises from Google's official training courses for the Agent Development Kit (ADK).

**Project Location:** This project is located at `./training-adk/01-Fundamentals-of-Agent-Development-Kit/adk-workspace/`

The examples demonstrate several ways of defining and configuring agents:

- `my_first_agent/` contains a Python agent defined in `agent.py`.
- `my_config_agent/` contains an agent configured in YAML through `root_agent.yaml`.
- `customer_support_agent/` contains a Python customer support agent defined in `agent.py`.
- `model_comparison/` compares different content generation configurations.
- `problem_solver/` demonstrates built-in planning for complex problem solving.
- `product_extractor/` demonstrates structured JSON output with a Pydantic schema.

The table below provides a quick guide to the ADK and general agentic concepts illustrated by each example. Use it to choose an example that matches the problem you want to explore.

| Agent | Concepts illustrated | Consult this example when you want to learn about |
| --- | --- | --- |
| [`my_first_agent`](my_first_agent/) | Basic ADK agent definition in Python; model, name, description, and instruction | Creating your first simple agent and understanding the minimum configuration required. |
| [`my_config_agent`](my_config_agent/) | Declarative agent configuration with YAML; schema-assisted configuration | Defining an agent without Python code or learning how ADK agent settings can be expressed in YAML. |
| [`customer_support_agent`](customer_support_agent/) | Instruction design; role, mission, methodology, boundaries, escalation rules, and few-shot examples | Writing reliable instructions, defining what an agent must or must not do, and handling out-of-scope requests. |
| [`model_comparison`](model_comparison/) | `generate_content_config`; temperature, token limits, `top_p`, `top_k`, and safety settings | Controlling response creativity and length, comparing generation strategies, or configuring content safety thresholds. |
| [`problem_solver`](problem_solver/) | Built-in planning with `BuiltInPlanner`; thinking configuration and thinking budget | Adding planning and extended reasoning to an agent that must break down and solve complex problems. |
| [`product_extractor`](product_extractor/) | Structured output with a Pydantic schema; JSON validation and session state with `output_key` | Extracting reliable structured data from natural language and making the result available in the agent session. |

## Quick Start

### Prerequisites

- Python installed on your machine
- The project dependencies installed in the `.venv` virtual environment
- A Google API key already available to you

Using a Python virtual environment keeps this project's dependencies isolated from other projects and helps prevent version conflicts.

### Activate the virtual environment

From the project root, make the activation script run in the current shell:

```bash
source activate-venv.sh
```

The `activate-venv.sh` script performs the following steps:

1. Prints an activation message.
2. Sources `.venv/bin/activate` to activate the virtual environment.
3. Prints a confirmation message.

**Important: the script must be sourced, not executed directly.**

Use:

```bash
source activate-venv.sh
```

or its equivalent form:

```bash
. activate-venv.sh
```

Do not use:

```bash
./activate-venv.sh
```

Executing the script directly runs it in a subshell. The virtual environment may then be active only while the script is running, and the activation is lost when the script exits.

### Configure the Google API key

The agents use a Google API key through environment variables loaded from a `.env` file. You must already have a valid Google API key before completing this setup.

The repository includes [.env.template](.env.template), which contains the required variable names without a real secret:

```dotenv
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=your_google_api_key_here
```

Create a separate `.env` file for each agent project you want to run. From the repository root, copy the template into the project directory:

Then open each `.env` file you intend to use and replace `your_google_api_key_here` with your actual Google API key. For example, to configure only `my_first_agent`:

```bash
cp .env.template my_first_agent/.env
$EDITOR my_first_agent/.env
```

The resulting file must contain your key on the `GOOGLE_API_KEY` line:

```dotenv
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=your_actual_google_api_key
```
For example, `adk web my_first_agent` uses `my_first_agent/.env`; it does not use the `.env` file from another project.

### Run an agent

After activating the virtual environment, use the appropriate ADK command for the agent you want to test. For example, from the project root:

```bash
adk web my_first_agent
```

For the agent defined in YAML:

```bash
adk web my_config_agent
```

For the customer support agent:

```bash
adk web customer_support_agent
```

The `adk web` command starts the ADK development web interface. Check the terminal output for the local address to open in your browser.

By default, ADK uses port `8000`. If this port is already in use, start the desired agent on port `8001` with the `--port` option:

```bash
adk web my_first_agent --port 8001
```

Replace `my_first_agent` with `my_config_agent` or `customer_support_agent` when needed.

## Notes

- The activation script must be run from the project root because it references `.venv/bin/activate` using a relative path.
- The models used in the examples require the Google API key configuration described above before they can be used.
- The files in this repository are intended for learning and follow the exercises from Google's official ADK training courses.
