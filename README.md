Cucumber uses a semi official package in Python called [Behave](https://behave.readthedocs.io/en/latest/tutorial/)

How to run:
- Create a [virtual environment](https://docs.python.org/3/library/venv.html) by running `python -m venv .`
- Activate virtual environment by running `./Scripts/activate` (you'll also have to run this for new terminal sessions also to activate the environment)
- Install dependencies `pip install behave python-dotenv mailosaur`
- Copy `.env.example` to `.env` and fill in the details
- Update the contact details in `features/mail.feature` and `features/sms.feature`
- Run the command `behave` to test

Useful notes:
- Must use unrestricted Mailosaur API key for quickstart
- You cannot have a feature/step named `email` or a circular dependency will be created with the Mailosaur package
- The SMS/Emails being tested must have been sent recently
