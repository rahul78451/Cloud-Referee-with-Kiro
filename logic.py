def evaluate_clouds(budget, workload, use_case, learning_curve):
    scores = {"AWS": 0, "GCP": 0, "Azure": 0}

    if budget == "Low":
        scores["GCP"] += 2
    elif budget == "Medium":
        scores["AWS"] += 2
    else:
        scores["Azure"] += 2

    if workload == "Startup":
        scores["GCP"] += 2
        scores["AWS"] += 1
    else:
        scores["AWS"] += 2
        scores["Azure"] += 2

    if use_case == "AI":
        scores["GCP"] += 3
        scores["AWS"] += 2
    elif use_case == "Web App":
        scores["AWS"] += 2
    else:
        scores["AWS"] += 2
        scores["Azure"] += 2

    if learning_curve == "Beginner":
        scores["GCP"] += 2
    elif learning_curve == "Advanced":
        scores["AWS"] += 2
        scores["Azure"] += 1

    return scores


def recommend(scores):
    return max(scores, key=scores.get)
