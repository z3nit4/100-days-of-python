"""
Secure Login System (With Exception Handling)

Requirements:
    Program should:
    - Store a correct username & password
    - Allow 3 login attempts
    - Handle:
        Empty input, KeyboardInterrupt (Ctrl + C) & Unexpected errors
    - Lock account after too many attempts
    - Use: 
        try, except, else & finally
"""

credentials = {} # Store user's creds once registered

while True:
    # Main Menu
    print("\n--- Secure Login ---")
    print("Welcome. Select 1 to login if you're a returning user. Otherwise, select 2 to register.")
    print("1. Login")
    print("2. Register")
    choice = input("Choose an option: ")


    # ---------------- REGISTER USER ----------------
    if choice == "2":
        try:
            # Collect new user's creds
            print("\n--- Secure Login ---")
            username = input("Enter a Username: ")
            password = input("Enter a Password: ")
            
            # Store creds in dictionary
            credentials = {
            'Username':username,
            'Password':password
            }
            
            print("Registration successful! You may now login.")

        # Handle empty input
        except ValueError as e:
                        print("Error:", e)

        # Handle Ctrl+C safely
        except KeyboardInterrupt:
            print("\nLogin cancelled by user.")
            break
        
        # Catch any unexpected errors
        except Exception as e:
            print("Unexpected error occurred:", e)
        

    # ---------------- LOGIN USER ----------------
    elif choice == "1":
        
         # Reset attempts each time login is selected
        attempts = 3
        
         # Login loop (limited attempts)
        while attempts > 0:
            try:
                print("\n--- Secure Login ---")
                
                user = input("Enter username: ").strip()
                passw = input("Enter password: ").strip()

                # Prevent empty username or password
                if not user or not passw:
                    raise ValueError("Username and password cannot be empty.")

                # Check if entered creds match stored creds
                if user == credentials['Username'] and passw == credentials['Password']:
                    print("********* Login successful!********")
                    break # Exit login loop on success
    
                else:
                    attempts -= 1 # Decrease attempts for wrong credentials
                    print(f"Incorrect credentials. Attempts left: {attempts}")

            except ValueError as e:
                print("Error:", e)

            except KeyboardInterrupt:
                print("\nLogin cancelled by user.")
                break

            except Exception as e:
                print("Unexpected error occurred:", e)

            finally:
                # Runs after every login attempt
                print("Attempt processed.")
        
        if attempts == 0:
                    print("Account locked. Too many failed attempts.")