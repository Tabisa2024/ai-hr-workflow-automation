def process_request(text):
    text = text.lower()

    if "leave" in text:
        return "Leave Request → Approval triggered"
    elif "report" in text:
        return "Report generation triggered"
    else:
        return "General request"

if __name__ == "__main__":
    user_input = input("Enter request: ")
    result = process_request(user_input)
    print(result)
``
