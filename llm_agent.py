def analyze_complaint(text):

    text = text.lower()

    issue = "General"
    location = "Unknown"

    if "road" in text or "pothole" in text:
        issue = "Road Damage"

    elif "garbage" in text or "waste" in text:
        issue = "Waste Management"

    elif "water" in text:
        issue = "Water Supply"

    elif "electricity" in text:
        issue = "Electricity Failure"

    elif "fire" in text:
        issue = "Fire Emergency"

    elif "accident" in text:
        issue = "Accident"

    words = text.split()

    for word in words:
        if "sector" in word:
            location = word

    return issue, location