🔐 ZIP Password Cracker (Brute Force)
A Python + Flask-based educational tool to demonstrate brute-force password cracking on ZIP files using a wordlist.
This project showcases how weak ZIP file protection can be broken by systematically trying all possible passwords.


📸 Demo Screenshot:

1.Crack the Zip file password --> https://github.com/Apoorvaguttedar/ZipCracker-BruteForce-v1/blob/main/snapshots/Check_zipfile.png

2.Add Zipfile-->https://github.com/Apoorvaguttedar/ZipCracker-BruteForce-v1/blob/main/snapshots/Add_ZipFile.png

3.Add Password-->https://github.com/Apoorvaguttedar/ZipCracker-BruteForce-v1/blob/main/snapshots/Add_passwordlist.png

4.Password Cracked -->https://github.com/Apoorvaguttedar/ZipCracker-BruteForce-v1/blob/main/snapshots/Password%20cracked.png




🚀 Features
Upload any password-protected .zip file.
Upload a custom wordlist to try potential passwords.
See real-time results including:
* Found password (if any)
* Number of attempts
* Time taken
Styled in a terminal-style hacker UI for immersive experience.





🧠 Technologies Used
Python 3
Flask (Web framework)
HTML/CSS (Hacker-themed frontend)
zipfile (Standard Python module for ZIP handling)



📁 Folder Structure
zip-cracker/
├── app.py               # Flask backend
├── zip_cracker.py       # Core logic for cracking ZIP
├── templates/
│   └── index.html       # HTML UI
├── static/
│   └── style.css        # CSS styling (hacker theme)
├── uploads/             # Uploaded files (auto-generated)
├── README.md            # You're reading it!





🛠️ How to Run
1 Install Flask:
pip install flask
2 Start the App:
python app.py
3 Visit in Browser:
http://localhost:5000





🔎 How It Works
Takes the uploaded .zip file and reads passwords from the provided wordlist file.
Tries each password one by one until the ZIP opens successfully or the list is exhausted.
Displays cracking result with attempts and time stats.





📂 Sample Wordlist Format
Your wordlist.txt should contain one password per line:
python-repl
Copy code
123456
qwerty
letmein
password123
hunter2 etc...





⚠️ Disclaimer
This project is for educational and ethical purposes only.
Do not use this tool on files you do not own or have explicit permission to test.
Unauthorized password cracking is illegal and unethical.





