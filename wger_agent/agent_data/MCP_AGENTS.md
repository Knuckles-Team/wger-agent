# MCP_AGENTS.md - Dynamic Agent Registry

This file tracks the generated agents from MCP servers. You can manually modify the 'Tools' list to customize agent expertise.

## Agent Mapping Table

| Name | Description | System Prompt | Tools | Tag | Source MCP |
|------|-------------|---------------|-------|-----|------------|
| Wger User Specialist | Expert specialist for user domain tasks. | You are a Wger User specialist. Help users manage and interact with User functionality using the available tools. | wger-agent_user_toolset | user | wger-agent |
| Wger Body Specialist | Expert specialist for body domain tasks. | You are a Wger Body specialist. Help users manage and interact with Body functionality using the available tools. | wger-agent_body_toolset | body | wger-agent |
| Wger Routine Specialist | Expert specialist for routine domain tasks. | You are a Wger Routine specialist. Help users manage and interact with Routine functionality using the available tools. | wger-agent_routine_toolset | routine | wger-agent |
| Wger Workout Specialist | Expert specialist for workout domain tasks. | You are a Wger Workout specialist. Help users manage and interact with Workout functionality using the available tools. | wger-agent_workout_toolset | workout | wger-agent |
| Wger Nutrition Specialist | Expert specialist for nutrition domain tasks. | You are a Wger Nutrition specialist. Help users manage and interact with Nutrition functionality using the available tools. | wger-agent_nutrition_toolset | nutrition | wger-agent |
| Wger Routineconfig Specialist | Expert specialist for routineconfig domain tasks. | You are a Wger Routineconfig specialist. Help users manage and interact with Routineconfig functionality using the available tools. | wger-agent_routineconfig_toolset | routineconfig | wger-agent |
| Wger Exercise Specialist | Expert specialist for exercise domain tasks. | You are a Wger Exercise specialist. Help users manage and interact with Exercise functionality using the available tools. | wger-agent_exercise_toolset | exercise | wger-agent |

## Tool Inventory Table

| Tool Name | Description | Tag | Source |
|-----------|-------------|-----|--------|
| wger-agent_user_toolset | Static hint toolset for user based on config env. | user | wger-agent |
| wger-agent_body_toolset | Static hint toolset for body based on config env. | body | wger-agent |
| wger-agent_routine_toolset | Static hint toolset for routine based on config env. | routine | wger-agent |
| wger-agent_workout_toolset | Static hint toolset for workout based on config env. | workout | wger-agent |
| wger-agent_nutrition_toolset | Static hint toolset for nutrition based on config env. | nutrition | wger-agent |
| wger-agent_routineconfig_toolset | Static hint toolset for routineconfig based on config env. | routineconfig | wger-agent |
| wger-agent_exercise_toolset | Static hint toolset for exercise based on config env. | exercise | wger-agent |
