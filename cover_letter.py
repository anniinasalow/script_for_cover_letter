
def create_coverletter():
    print("Creating CV text")
    company = input("Enter company name:")
    subject = input ("Enter the subject of the role:")

    with open ('template_CV.txt', 'r') as file:
        template = file.read()

    cv_text = template.format(company=company, subject=subject)

    print("creating the text for your cv")
    
    new_cover_letter="new_cover_letter.txt"
    with open(new_cover_letter, 'w') as file:
        file.write(cv_text)

def main():
    """
    The main function to execute the script.
    """
    # Call the function to create the paragraph and save it to a text file
    create_coverletter()

    # Ask the user if they want to generate another story
    while True:
        again = input("\nWould you like to create another cover letter? (yes/no): ").strip().lower()
        if again == "yes":
            create_coverletter()
        elif again == "no":
            print("Exiting")
            break
        else:
            print("Please enter 'yes' or 'no'.")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()


