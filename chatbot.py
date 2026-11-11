"""
Classroom Assistance Bot - Interactive CLI
CHRIST (Deemed to be University) - School of Engineering and Technology
B.Tech CS AIML-C | Course: Natural Language Programming (CSEAM631P)
Team Members: Sasmita, Joshiny, Vedant, Rachel
"""
import sys
from classroom_bot.engine import ChatbotEngine

def print_help(engine: ChatbotEngine):
    print("\n" + "=" * 70)
    print("SUPPORTED QUERIES & MEMBER MAPPING (21 INTENTS)")
    print("=" * 70)
    current_member = None
    for r in engine.rules:
        if r["member"] != current_member:
            current_member = r["member"]
            print(f"\n[{current_member.upper()}'S QUESTIONS]")
        print(f"  Q{r['id']:2d}: {r['name']:48s}")
    print("=" * 70 + "\n")

def main():
    engine = ChatbotEngine()
    debug_mode = False

    print("=" * 75)
    print("  CHRIST (Deemed to be University) - School of Engineering & Technology")
    print("        DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING (B.Tech CS AIML-C)")
    print("            CLASSROOM ASSISTANCE BOT (Python RE Rule-Based)")
    print("=" * 75)
    print("Team Members: Sasmita | Joshiny | Vedant | Rachel")
    print("Commands: 'exit' or 'quit' to leave | 'help' for all intents | 'debug' to toggle regex inspector")
    print("-" * 75)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting bot. Goodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day at CHRIST University.")
            break

        if user_input.lower() == "help":
            print_help(engine)
            continue

        if user_input.lower() == "debug":
            debug_mode = not debug_mode
            status = "ENABLED" if debug_mode else "DISABLED"
            print(f"Bot: [Debug Inspector {status}]")
            continue

        result = engine.process_query(user_input)

        if debug_mode and result["matched"]:
            print("\n  [DEBUG INFO]")
            print(f"  • Member : {result['member']}")
            print(f"  • Intent : Q{result['id']} - {result['intent']}")
            print(f"  • Pattern: {result['pattern']}")
            print(f"  • Groups : {result['groups']}")
            print("  " + "-" * 50)

        print(f"\nBot:\n{result['response']}")

if __name__ == "__main__":
    main()
