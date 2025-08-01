import json
from agents.problem_validator import run as validate
from agents.market_researcher import run as research
from agents.business_model_builder import run as build_model
from agents.risk_analyzer import run as analyze_risk

def main():
    idea = input("Describe your startup idea: ")
    v = validate(idea)
    m = research(v)
    b = build_model(m)
    r = analyze_risk(b)

    print("\n--- Evaluation Report ---\n")
    print("1) Validation:\n", v, "\n")
    print("2) Market Research:\n", json.dumps(m, indent=2), "\n")
    print("3) Business Model:\n", json.dumps(b, indent=2), "\n")
    print("4) Risks & Mitigations:\n", json.dumps(r, indent=2), "\n")

if __name__ == "__main__":
    main()




# from agents.problem_validator import run as validate
# from agents.market_researcher import run as research
# from agents.business_model_builder import run as build_model
# from agents.risk_analyzer import run as analyze_risk

# def main():
#     idea = input("Describe your startup idea: ")
#     v = validate(idea)
#     m = research(v)
#     b = build_model(m)
#     r = analyze_risk(b)

#     print("\n--- Evaluation Report ---")
#     print("1) Validation:", v)
#     print("2) Market Research:", m)
#     print("3) Business Model:", b)
#     print("4) Risks & Mitigations:", r)

# if __name__ == "__main__":
#     main()
