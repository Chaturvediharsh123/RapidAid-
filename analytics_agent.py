import sqlite3

conn = sqlite3.connect("complaints.db", check_same_thread=False)
cursor = conn.cursor()


def calculate_priority(issue, location):

    emergency_issues = [
        "Fire Emergency",
        "Accident"
    ]

    # emergencies are always critical
    if issue in emergency_issues:
        return "Critical"

    query = f"""
    SELECT COUNT(*) FROM complaints
    WHERE issue_type='{issue}' AND location='{location}'
    """

    count = cursor.execute(query).fetchone()[0]

    if count >= 5:
        return "High"

    elif count >= 2:
        return "Medium"

    else:
        return "Low"