#!/bin/bash

echo "Testing ADK Agents..."
echo "===================="
echo ""

# Activate virtual environment
source activate-venv.sh
echo ""

# Test each agent
agents=("my_first_agent" "customer_support_agent" "model_comparison" "problem_solver" "product_extractor")

for agent in "${agents[@]}"; do
    echo -n "Testing $agent... "
    if .venv/bin/python -c "from ${agent}.agent import root_agent; print('OK')" 2>/dev/null | grep -q "OK"; then
        echo "✓"
    else
        echo "✗"
    fi
done

# Test YAML config agent
echo -n "Testing my_config_agent (YAML)... "
if .venv/bin/python -c "
import yaml
with open('my_config_agent/root_agent.yaml') as f:
    yaml.safe_load(f)
print('OK')
" 2>/dev/null | grep -q "OK"; then
    echo "✓"
else
    echo "✗"
fi

echo ""
echo "===================="
echo "All tests completed!"
