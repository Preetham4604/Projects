🔐 Cyber Password Strength Checker

A modern Cybersecurity Password Strength Analyzer built with Python (Tkinter) that evaluates password strength, calculates entropy, checks for leaked passwords via the Have I Been Pwned API, and helps users generate secure passwords.

This project combines cryptography, API integration, and GUI development — perfect for showcasing applied cybersecurity and Python GUI skills.


🚀 Features

✅ Password Strength Analysis
Analyzes passwords based on length, diversity, and complexity rules.

✅ Entropy Calculation
Estimates the theoretical randomness (in bits) of the password.

✅ Leak Detection (HIBP API)
Verifies if the password has been exposed in known data breaches.

✅ Password Generator
Creates random, secure passwords with configurable character diversity.

✅ Cyber-Themed GUI
Interactive Tkinter interface with neon visuals and dynamic color-coded feedback.

✅ No Password Storage
Passwords are analyzed in-memory only — nothing is stored for security.


💡 How Password Strength Is Calculated

The tool uses a dual evaluation method combining a rule-based scoring system (points) and entropy-based measurement.
This ensures both structural and statistical strength are analyzed.

1. Rule-Based Scoring (Points System)

  Each password earns points for meeting common cybersecurity best practices:


🔸Length ≥ 8	+1	Minimum secure length 

🔸Contains both uppercase & lowercase letters	+1	Improves character diversity

🔸Contains at least one digit	+1	Adds numerical complexity

🔸Contains at least one special symbol (!@#$%^&*...)	+1	Makes patterns harder to predict

🔸Length ≥ 12 	+1	Bonus for extended length



2. Entropy Calculation (Mathematical Strength)

Entropy measures how unpredictable or random a password is — it represents the number of bits of information per character combination.
Formula used:


**Entropy=Length×log2(CharacterSetSize)**

Entropy (bits)	Theoretical Strength

🔸0–28	❌ Very Weak

🔸28–35	⚠️ Weak

🔸36–59	🟡 Medium

🔸60–127	🟢 Strong

🔸128+	💪 Very Strong


3. Relationship Between Points and Entropy

While both methods assess strength, they focus on different aspects:

Aspect	Points System	Entropy Calculation
Focus	Follows best practices	Measures randomness
Method	Rule-based (checks for diversity & length)	Mathematical (based on combinations)
Output	Discrete (1–5 points)	Continuous (bits)
Strength Type	Structural	Statistical
Limitation	Can misjudge random strings	May overrate predictable ones


🔸 Example Comparisons

Password	Points	Entropy (bits)	Strength Analysis

abc123	2	~31 bits	Weak — short and predictable

Password123!	4	~69 bits	Medium — diverse but common

qwertyuiop!@#	4	~78 bits	Strong mathematically, but pattern-based

X9v@P7k$Rt2&	5	~94 bits	Very Strong — random & complex

Tr0ub4dor&3	4	~67 bits	Strong, but semi-patterned

correcthorsebatterystaple	3	~104 bits	High entropy, but simple words

^Zg9!nT3pQ%f2sB@	5	~107 bits	Excellent — high points and high entropy.




💡 Insight:

A long passphrase can achieve high entropy even with fewer point-based rules.

A short but complex password can achieve high points and strong entropy.

The most secure passwords are both diverse and random — scoring high in both systems.



⚠️ Important Note

Higher entropy doesn’t always mean better real-world security — passwords like Password123! may have decent entropy but are common and predictable.
Entropy only measures mathematical randomness, while the point system ensures strong composition and unpredictability.
✅ Best practice: combine both — length + randomness + diversity.


🛠️ Tech Stack

Language: Python 3.10+

GUI Framework: Tkinter

Libraries:

requests → API requests (HIBP check)

Pillow → Background image

hashlib, math, random, re, string → Core logic

API: Have I Been Pwned (Password Range API)



⚙️ Installation & Usage

1️⃣ Clone the repository

git clone https://github.com/your-username/CyberPasswordChecker.git

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
python password_checker.py
