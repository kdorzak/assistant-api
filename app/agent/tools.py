# from app.agent.setup import triage_agent, motivation_manager_agent, service_desk_agent


def escalate_to_human(summary):
    """Only call this if explicitly asked to."""
    print("\n=== Escalation Report ===")
    print(f"Summary: {summary}")
    print("=========================\n")
    exit()


def transfer_to_motivation_manager():
    """User for anything related to motivation."""
    global current_assistant
    # current_assistant = motivation_manager_agent


def transfer_to_service_desk():
    """User for issues, repairs, or refunds."""
    global current_assistant
    # current_assistant = service_desk_agent


def transfer_back_to_triage():
    """Call this if the user brings up a topic outside of your view,
    including escalating to human."""
    global current_assistant
    # current_assistant = triage_agent
