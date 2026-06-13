---
name: upp-agent-coordination
description: Implementing multi-agent coordination using Uphill Priority Protocol (UPP) logic and reasoning depth metrics.
---

# Uphill Priority Protocol (UPP) Agent Coordination

Implementing multi-agent coordination using Uphill Priority Protocol (UPP) logic to minimize context-switching and optimize reasoning depth.

## When to Use
- When managing multiple agents working on complex, hierarchical tasks.
- When token efficiency and context momentum are critical.
- When tasks involve varying levels of reasoning depth ("Altitude").

## Concepts
- **Granular Task Decomposition ($\gamma$)**: Breaking tasks into sub-tasks with defined checkpoints.
- **Altitude ($H_j$)**: The reasoning depth or complexity level of a sub-task.
- **Context Gradient ($\nabla C$)**: The shift in complexity/context between sub-tasks.
- **Uphill Right-of-Way**: Granting non-preemptive priority to agents moving to higher "Altitude" to prevent context fragmentation.

## Steps

### 1. Task Decomposition
- Identify the main goal and decompose it into sub-tasks.
- Assign an "Altitude" ($H_j$) to each sub-task based on its reasoning requirements.

### 2. Priority Assignment
- Calculate the "Context Gradient" ($\nabla C$) between current and next sub-tasks.
- Assign "Uphill Priority" to tasks where $\nabla C > 0$.

### 3. Execution Management
- Ensure "uphill" agents complete their reasoning cycle before allowing context-switching.
- Use checkpoints to maintain context momentum.

## Output Format
- A task execution plan with assigned Altitudes and priority markers.
- Logs or status updates reflecting UPP logic application.

## Example
**Task**: Research and Draft IEEE Paper
1. **Sub-task A**: Literature Review ($H_j=3$)
2. **Sub-task B**: Mathematical Framework ($H_j=5$) -> **UPHILL PRIORITY**
3. **Sub-task C**: Drafting Conclusion ($H_j=2$)

**Execution**: Agent B is granted non-preemptive priority to complete the mathematical framework to avoid losing reasoning momentum.
