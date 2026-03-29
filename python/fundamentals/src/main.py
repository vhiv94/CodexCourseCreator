
# Study Log CLI
def main():

    # Define a title variable
    title = "Study Log CLI"

    # Define a log filename variable
    log_filename = "study_log.txt"

    # Print a welcome message
    print(f"{title}\n{'-' * len(title)}\n{log_filename}")

    title = input("Enter the title of your study log: ")
    clean = title.strip()
    print(clean)


if __name__ == "__main__":
    main()