import re

def assess_password_strength(password):
    length_weight = 1.5
    uppercase_weight = 1.2
    lowercase_weight = 1.2
    number_weight = 1.3
    special_char_weight = 1.4
    
    score = 0
    feedback = []
    
    length = len(password)
    if length >= 8:
        score += length_weight * min(length, 12)
    else:
        feedback.append("Password is too short. Minimum 8 characters required.")
    
    if re.search(r'[A-Z]', password):
        score += uppercase_weight
    else:
        feedback.append("Add uppercase letters (A-Z).")
    
    if re.search(r'[a-z]', password):
        score += lowercase_weight
    else:
        feedback.append("Add lowercase letters (a-z).")
    
    if re.search(r'[0-9]', password):
        score += number_weight
    else:
        feedback.append("Add numbers (0-9).")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += special_char_weight
    else:
        feedback.append("Add special characters (e.g., !@#$%^&*).")
    
    if score >= 20:
        strength = "Strong"
    elif 10 <= score < 20:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    feedback_message = " ".join(feedback) if feedback else "Your password is strong."
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback_message
    }

def main():
    print("Welcome to Password Complexity Checker!")
    while True:
        print("Enter your password:", end=" ")
        password = input()

        result = assess_password_strength(password)

        formatted_score = f"{result['score']:.3f}" if result['score'] % 1 != 0 else f"{result['score']:.0f}"

        print(f"\nScore: {formatted_score}")
        print(f"Strength: {result['strength']}")
        print(f"Feedback: {result['feedback']}")

        if result['strength'] == "Weak":
            print()
            choice = input("Your password is weak. Would you like to try again? (yes/no): ").lower()
            if choice != "yes":
                break
        elif result['strength'] == "Moderate":
            print()
            choice = input("Your password is moderate. Would you like to try again? (yes/no): ").lower()
            if choice != "yes":
                break
        else:
            break

if __name__ == "__main__":
    main()
