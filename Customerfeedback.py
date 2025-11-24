feedback_list = []
def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("   CUSTOMER FEEDBACK RECORDING SYSTEM")
    print("="*50)
    print("1. Add New Feedback")
    print("2. View All Feedback")
    print("3. Search Feedback by Customer Name")
    print("4. View Feedback Statistics")
    print("5. Exit")
    print("="*50)
def add_feedback():
    print("\n--- Add New Feedback ---")
    name = input("Customer Name: ").strip()
    email = input("Customer Email: ").strip()
    while True:
        try:
            rating = int(input("Rating (1-5 stars): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Please enter a rating between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    comments = input("Comments/Feedback: ").strip()
    feedback = {
        'name': name,
        'email': email,
        'rating': rating,
        'comments': comments
    }
    
    feedback_list.append(feedback)
    print("\n✓ Feedback recorded successfully!")
def view_all_feedback():
    """Display all feedback entries"""
    if not feedback_list:
        print("\nNo feedback records found.")
        return
    print("\n" + "="*50)
    print("   ALL CUSTOMER FEEDBACK")
    print("="*50)
    for i, feedback in enumerate(feedback_list, 1):
        print(f"\nFeedback #{i}")
        print(f"Name: {feedback['name']}")
        print(f"Email: {feedback['email']}")
        print(f"Rating: {'⭐' * feedback['rating']} ({feedback['rating']}/5)")
        print(f"Comments: {feedback['comments']}")
        print("-" * 50)
def search_feedback():
    if not feedback_list:
        print("\nNo feedback records found.")
        return
    search_name = input("\nEnter customer name to search: ").strip().lower()
    found = False
    print("\n--- Search Results ---")
    for feedback in feedback_list:
        if search_name in feedback['name'].lower():
            print(f"\nName: {feedback['name']}")
            print(f"Email: {feedback['email']}")
            print(f"Rating: {'⭐' * feedback['rating']} ({feedback['rating']}/5)")
            print(f"Comments: {feedback['comments']}")
            print("-" * 50)
            found = True
    if not found:
        print(f"No feedback found for '{search_name}'")
def view_statistics():
    """Display feedback statistics"""
    if not feedback_list:
        print("\nNo feedback records found.")
        return
    total = len(feedback_list)
    ratings = [f['rating'] for f in feedback_list]
    average_rating = sum(ratings) / total
    rating_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for rating in ratings:
        rating_counts[rating] += 1 
    print("\n" + "="*50)
    print("   FEEDBACK STATISTICS")
    print("="*50)
    print(f"Total Feedback Entries: {total}")
    print(f"Average Rating: {average_rating:.2f} ⭐")
    print("\nRating Distribution:")
    for stars in range(5, 0, -1):
        bar = "█" * rating_counts[stars]
        print(f"{stars} ⭐: {bar} ({rating_counts[stars]})")
    print("="*50)
def main():
 
    print("Welcome to the Customer Feedback Recording System!")
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            add_feedback()
        elif choice == '2':
            view_all_feedback()
        elif choice == '3':
            search_feedback()
        elif choice == '4':
            view_statistics()
        elif choice == '5':
            print("\nThank you for using the Feedback System!")
            
            break
        else:
            print("\n❌ Inva5lid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
