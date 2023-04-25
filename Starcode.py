import random
import string

def generate_password(length=10):
    """Generate a random password"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def score_password(password):
    """Score the strength of a password"""
    score = 0
    length = len(password)
    if length < 8:
        score -= 3
    elif length < 12:
        score += 1
    else:
        score += 3
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    return score

def main():
    """Main function"""
    password = generate_password()
    print(f"Generated password: {password}")
    score = score_password(password)
    print(f"Password score: {score}")

if __name__ == "__main__":
    main()