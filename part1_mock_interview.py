import time
import threading


class InterviewState:
    def __init__(self):
        self.current_stage = "self_introduction"
        self.stage_completed = False


class SelfIntroductionAgent:
    def ask_question(self):
        print("\n===================================")
        print("[SelfIntroductionAgent]")
        print("===================================")
        print("Interviewer: Hi! Welcome to the interview.")
        print("Interviewer: Please introduce yourself.")

    def is_complete(self, answer):
        keywords = [
            "experience",
            "engineer",
            "project",
            "worked",
            "skills",
            "python",
            "data",
            "developer",
        ]

        if len(answer.strip()) > 20:
            return True

        for word in keywords:
            if word in answer.lower():
                return True

        return False


class PastExperienceAgent:
    def ask_question(self):
        print("\n===================================")
        print("[PastExperienceAgent]")
        print("===================================")
        print("Interviewer: Thank you.")
        print(
            "Interviewer: Please describe a previous project or work experience."
        )

    def is_complete(self, answer):
        return len(answer.strip()) > 20


def fallback_transition(state, timeout=90):
    """
    Time-based fallback mechanism
    Required by Jobnova challenge
    """

    time.sleep(timeout)

    if (
        state.current_stage == "self_introduction"
        and not state.stage_completed
    ):
        print("\n[Fallback Triggered]")
        print(
            "Self-introduction did not complete within time limit."
        )
        print("Automatically transitioning to Past Experience stage.")

        state.current_stage = "past_experience"
        state.stage_completed = True


def run_interview():

    state = InterviewState()

    intro_agent = SelfIntroductionAgent()
    experience_agent = PastExperienceAgent()

    print("===================================")
    print(" JOBNOVA AI MOCK INTERVIEW DEMO")
    print("===================================")

    print("\nStarting interview workflow...")

    timer = threading.Thread(
        target=fallback_transition,
        args=(state, 90),
        daemon=True,
    )

    timer.start()

    # -----------------------------
    # Stage 1
    # -----------------------------

    intro_agent.ask_question()

    intro_answer = input("\nCandidate: ")

    if intro_agent.is_complete(intro_answer):

        print("\n[Handoff]")
        print(
            "SelfIntroductionAgent completed successfully."
        )
        print(
            "Transferring control to PastExperienceAgent..."
        )

        state.current_stage = "past_experience"
        state.stage_completed = True

    else:

        print("\n[Handoff]")
        print(
            "Response was short but workflow continues."
        )

        state.current_stage = "past_experience"
        state.stage_completed = True

    time.sleep(2)

    # -----------------------------
    # Stage 2
    # -----------------------------

    experience_agent.ask_question()

    experience_answer = input("\nCandidate: ")

    if experience_agent.is_complete(experience_answer):

        print("\n[Completed]")
        print(
            "PastExperienceAgent completed successfully."
        )

    else:

        print("\n[Completed]")
        print(
            "Response captured. Interview flow completed."
        )

    # -----------------------------
    # Final Summary
    # -----------------------------

    print("\n===================================")
    print(" INTERVIEW SUMMARY")
    print("===================================")

    print("\nStage 1 - Self Introduction")
    print("-----------------------------------")
    print(intro_answer)

    print("\nStage 2 - Past Experience")
    print("-----------------------------------")
    print(experience_answer)

    print("\n===================================")
    print("Final Status")
    print("===================================")

    print("✓ SelfIntroductionAgent Executed")
    print("✓ Agent Handoff Completed")
    print("✓ PastExperienceAgent Executed")
    print("✓ Fallback Mechanism Implemented")
    print("✓ Interview Workflow Completed")


if __name__ == "__main__":
    run_interview()