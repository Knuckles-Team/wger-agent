"""wger Fitness graph configuration — tag prompts and env var mappings.

This is the only file needed to enable graph mode for this agent.
Provides TAG_PROMPTS and TAG_ENV_VARS for create_graph_agent_server().
"""

TAG_PROMPTS: dict[str, str] = {
    "Body": (
        "You are a wger Fitness Body specialist. Help users manage and interact with Body functionality using the available tools."
    ),
    "Exercise": (
        "You are a wger Fitness Exercise specialist. Help users manage and interact with Exercise functionality using the available tools."
    ),
    "Nutrition": (
        "You are a wger Fitness Nutrition specialist. Help users manage and interact with Nutrition functionality using the available tools."
    ),
    "Routine": (
        "You are a wger Fitness Routine specialist. Help users manage and interact with Routine functionality using the available tools."
    ),
    "RoutineConfig": (
        "You are a wger Fitness Routineconfig specialist. Help users manage and interact with Routineconfig functionality using the available tools."
    ),
    "User": (
        "You are a wger Fitness User specialist. Help users manage and interact with User functionality using the available tools."
    ),
    "Workout": (
        "You are a wger Fitness Workout specialist. Help users manage and interact with Workout functionality using the available tools."
    ),
}


TAG_ENV_VARS: dict[str, str] = {
    "Body": "BODYTOOL",
    "Exercise": "EXERCISETOOL",
    "Nutrition": "NUTRITIONTOOL",
    "Routine": "ROUTINETOOL",
    "RoutineConfig": "ROUTINECONFIGTOOL",
    "User": "USERTOOL",
    "Workout": "WORKOUTTOOL",
}
