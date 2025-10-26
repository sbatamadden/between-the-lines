def show_intro():
    # Display the welcome message once at the start.
    print("Hello! Welcome to Between the Lines, a bias detection tool for written text.\n")


def show_menu():
    # Display the main menu options.
    print("Please choose your tool:")
    print("     Enter 1 for the Text Bias Detector.")
    print("     Enter 2 for the Model Bias Comparison Tool.")
    print("Or type 'exit' to exit the program.")


def run_text_bias_detector():
    # Handle the Text Bias Detector workflow.
    print("You have selected the Text Bias Detector. Please enter your text:")
    text_input = input("> ")
    print(f"\nYou entered:\n{text_input}")
    print("\nThe analysis is now complete.")
    return post_analysis_menu()


def run_model_bias_comparison():
    # Handle the Model Bias Comparison Tool workflow.
    print("You have selected the Model Bias Comparison Tool.")
    print("Please enter your prompt or the start of a sentence for the model to complete:")
    text_input = input("> ")
    print(f"\nYou entered:\n{text_input}")
    print("\nThe analysis is now complete.")
    return post_analysis_menu()


def post_analysis_menu():
    # Ask the user if they want to return to main menu or exit.
    while True:
        next_action = input("Enter M to return to the main menu, or 'exit' to quit: ").lower()
        if next_action == "m":
            print("\nReturning to the main menu...\n")
            return
        elif next_action == "exit":
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter M or 'exit'.")


def main():
    # Main program loop.
    show_intro()  #  Show this only once

    while True:
        show_menu()
        tool_selection = input("> ").lower()

        if tool_selection == "1":
            run_text_bias_detector()
        elif tool_selection == "2":
            run_model_bias_comparison()
        elif tool_selection == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or type 'exit' to quit.\n")


if __name__ == "__main__":
    main()
