import os
import dotenv

dotenv.load_dotenv(verbose=True)

dotenv_path = os.path.join(__file__, ".env")
dotenv.load_dotenv(dotenv_path)

NAGASE_TOKEN = os.environ.get("NAGASE_TOKEN")
NAGASE_ID = os.environ.get("NAGASE_ID")
NAGASE_PASSWORD = os.environ.get("NAGASE_PASSWORD")
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")
ICLOUD_ADDRESS = os.environ.get("ICLOUD_ADDRESS")
