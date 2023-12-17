
def backward_chaining(query, facts, rules):
    if query in facts:
        return True
    else:
        for rule in rules:
            head, body = rule.split(" <- ")
            if query == head:
                subgoals = body.split(", ")
                if all(backward_chaining(subgoal, facts, rules) for subgoal in subgoals):
                    return True
        return False

def forward_chaining(facts, rules):
    new_facts = set(facts)
    while True:
        added_new_fact = False
        for rule in rules:
            head, body = rule.split(" <- ")
            subgoals = body.split(", ")
            if all(subgoal in new_facts for subgoal in subgoals) and head not in new_facts:
                new_facts.add(head)
                added_new_fact = True
        if not added_new_fact:
            break
    return new_facts

facts = {"Human(john)", "Human(sara)", "Parent(john, mary)", "Parent(sara, mary)"}
rules = [
    "Ancestor(X, Y) <- Parent(X, Y)",
    "Ancestor(X, Y) <- Parent(X, Z), Ancestor(Z, Y)"
]

# Backward Chaining
print("Backward Chaining:")
query = "Ancestor(john, mary)"
result = backward_chaining(query, facts, rules)
print(f"Query '{query}': {result}")

# Forward Chaining
print("\nForward Chaining:")
new_facts = forward_chaining(facts, rules)
print("New Facts:")
for fact in new_facts:
    print(fact)
