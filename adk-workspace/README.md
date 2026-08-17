# ADK Training Exercises

This project contains exercises from Google's official training courses for the Agent Development Kit (ADK).

The examples demonstrate two ways of defining an agent:

- `my_first_agent/` contains a Python agent defined in `agent.py`.
- `my_config_agent/` contains an agent configured in YAML through `root_agent.yaml`.

The agents are algebra tutors designed to guide students step by step through problem-solving.

## Quick Start

### Prerequisites

- Python installed on your machine
- The project dependencies installed in the `.venv` virtual environment
- A valid configuration for the Google services used by ADK, including any credentials or environment variables required by the selected model

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

### Run an agent

After activating the virtual environment, use the appropriate ADK command for the agent you want to test. For example, from the project root:

```bash
adk web my_first_agent
```

For the agent defined in YAML:

```bash
adk web my_config_agent
```

The `adk web` command starts the ADK development web interface. Check the terminal output for the local address to open in your browser.

## Notes

- The activation script must be run from the project root because it references `.venv/bin/activate` using a relative path.
- The models used in the examples may require authentication and Google Cloud or Gemini configuration before they can be used.
- The files in this repository are intended for learning and follow the exercises from Google's official ADK training courses.
