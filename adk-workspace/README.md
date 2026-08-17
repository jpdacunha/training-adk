# ADK Training Exercises

This project contains exercises from Google's official training courses for the Agent Development Kit (ADK).

The examples demonstrate two ways of defining an agent:

- `my_first_agent/` contains a Python agent defined in `agent.py`.
- `my_config_agent/` contains an agent configured in YAML through `root_agent.yaml`.
- `customer_support_agent/` contains a Python customer support agent defined in `agent.py`.

The agents are algebra tutors designed to guide students step by step through problem-solving.

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

## Notes

- The activation script must be run from the project root because it references `.venv/bin/activate` using a relative path.
- The models used in the examples require the Google API key configuration described above before they can be used.
- The files in this repository are intended for learning and follow the exercises from Google's official ADK training courses.
