from llm_agent import analyze_complaint
from analytics_agent import calculate_priority
from routing_agent import route_department
from database import save_complaint


def process_complaint(text):

    # step 1 analyze complaint
    issue, location = analyze_complaint(text)

    # step 2 calculate priority
    priority = calculate_priority(issue, location)

    # step 3 assign department
    department = route_department(issue)

    # step 4 save complaint
    save_complaint(text, issue, location, priority, department)

    return issue, location, priority, department


if __name__ == "__main__":

    print("AI Civic Complaint System")

    complaint = input("Describe your issue: ")

    issue, location, priority, department = process_complaint(complaint)

    print("\nComplaint Registered")

    print("Issue:", issue)
    print("Location:", location)
    print("Priority:", priority)
    print("Department:", department)