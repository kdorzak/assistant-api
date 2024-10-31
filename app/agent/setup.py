from .client import client
from .tools import (
    transfer_to_service_desk,
    transfer_to_motivation_manager,
    transfer_back_to_triage,
    escalate_to_human,
)
from .util import function_to_schema

available_assistants = client.beta.assistants.list().data

dummy_agent = next(
    (
        assistant
        for assistant in available_assistants
        if assistant.name == "Dummy Agent"
    ),
    None,
) or client.beta.assistants.create(
    model="gpt-4o-mini",
    name="Dummy Agent",
    instructions="You are a helpful assistant." "Always respond in sentence or less",
    tools=[],
)

triage_agent = next(
    (
        assistant
        for assistant in available_assistants
        if assistant.name == "Triage Agent"
    ),
    None,
) or client.beta.assistants.create(
    model="gpt-4o-mini",
    name="Triage Agent",
    description="Assistant capable of directing users to right department",
    instructions=(
        "You are a customer service bot for Move Republic. "
        "Introduce yourself. Always be very brief. "
        "Gather information to direct the customer to the right department. "
        "But make your questions subtle and natural."
    ),
    tools=[
        function_to_schema(transfer_to_motivation_manager),
        function_to_schema(transfer_to_service_desk),
    ],
)
motivation_manager_agent = next(
    (
        assistant
        for assistant in available_assistants
        if assistant.name == "Motivation Manager"
    ),
    None,
) or client.beta.assistants.create(
    model="gpt-4o-mini",
    name="Motivation Manager",
    description="Assistant capable of directing users to right department",
    instructions=(
        "You are a fitness coach of Move Republic. Your role is to motivate user for movement and health."
        "You are mainly focused on fitness & health topics."
        "You communicate with friendly, mixed professional and unofficial tone. You should try to get personal with user, but without giving out your intentions. Try to reflect user style of communication to make user comfortable. Sporadically use emotes."
        "You never discuss anything outside of fitness, health and wellbeing topics."
        "You can empathize with user, be mindful. Remember that your role is to motivate for movement."
        "Be concise. Prioritize asking questions to allow user to find his own way. If you are unsure about anything just ask user to provide more info. Make sure that something you suggest really fits user and reconsider if selection is appropriate."
        "When you find something that fits with user your role is to go through whole process with user. Don't put whole plan, leaving user with it. You have to lead user step by step. If you can, make sure if user finished one step before going to other. Don't reveal too much information at once to not overwhelm user."
    ),
    tools=[
        function_to_schema(transfer_back_to_triage),
        function_to_schema(escalate_to_human),
    ],
)
service_desk_agent = next(
    (
        assistant
        for assistant in available_assistants
        if assistant.name == "Service Desk"
    ),
    None,
) or client.beta.assistants.create(
    model="gpt-4o-mini",
    name="Service Desk",
    description="Assistant capable of solving issues with Move Republic mobile app",
    instructions=(
        "You are a customer support agent for Move Republic."
        "You are focused only on Customer Support for Move Republic mobile app and don't touch other topics."
        "Always answer in a sentence or less."
        "Follow the following routine with the user:\n"
        "1. First, ask probing questions and understand the user's problem deeper.\n"
        " - unless the user has already provided a reason.\n"
        "2. Propose a fix.\n"
    ),
    tools=[
        function_to_schema(transfer_back_to_triage),
        function_to_schema(escalate_to_human),
    ],
)
current_assistant = dummy_agent
