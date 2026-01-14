# Semantic Alignment Report: Projects 0001-0100
Validating that Hardware and Key Parameters from the Problem Statement are present in all 3 Key Sections.
*Note*: 'Missing' in Block section implies neither the direct term nor its functional block counterpart (e.g. 'Button' vs 'pico_gpio_read') was found.

| ID | Hardware / Params | 6️⃣ Blocks (HW Only) | 8️⃣ Guide | 🔟 Code | Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0001 | LED, 2 | ✅ | ✅ | ✅ | ✅ |
| 0002 | LED, 0.2, 1.0 | ✅ | Missing: 0.2, 1.0 | Missing: 0.2, 1.0 | ⚠️ Mismatch |
| 0003 | LED, Button, Switch | Missing: Button, Switch | Missing: Button, Switch | Missing: Button, Switch | ⚠️ Mismatch |
| 0004 | LED, 3, 1 | ✅ | ✅ | ✅ | ✅ |
| 0005 | LED, Button | ✅ | ✅ | Missing: Button | ⚠️ Mismatch |
| 0006 | LED, Button, Switch | ✅ | ✅ | ✅ | ✅ |
| 0007 | LED, Button, 0.1 | ✅ | ✅ | ✅ | ✅ |
| 0008 | LED, 5 | ✅ | ✅ | ✅ | ✅ |
| 0009 | LED, LDR | Missing: LDR | ✅ | ✅ | ⚠️ Mismatch |
| 0010 | LED | ✅ | ✅ | ✅ | ✅ |
| 0011 | Button | ✅ | ✅ | ✅ | ✅ |
| 0012 | LED, Button, 0.1, 1 | ✅ | ✅ | ✅ | ✅ |
| 0013 | LED, Button, Switch, 1 | ✅ | ✅ | Missing: Switch | ⚠️ Mismatch |
| 0014 | LED, Button | ✅ | ✅ | ✅ | ✅ |
| 0015 | Button | ✅ | ✅ | ✅ | ✅ |
| 0016 | LED, Button, Switch | ✅ | ✅ | Missing: Switch | ⚠️ Mismatch |
| 0017 | LED, Button, 3 | ✅ | ✅ | ✅ | ✅ |
| 0018 | LED, Button | ✅ | ✅ | ✅ | ✅ |
| 0019 | LED, Button, 10 | ✅ | ✅ | ✅ | ✅ |
| 0020 | Button, 0.05 | ✅ | ✅ | ✅ | ✅ |
| 0021 | Buzzer, 0.5 | ✅ | ✅ | ✅ | ✅ |
| 0022 | LED, Buzzer | ✅ | ✅ | ✅ | ✅ |
| 0023 | Button, Buzzer | ✅ | ✅ | ✅ | ✅ |
| 0024 | Buzzer | ✅ | ✅ | ✅ | ✅ |
| 0025 | Button, Buzzer | ✅ | ✅ | ✅ | ✅ |
| 0026 | Button, Buzzer, Switch | ✅ | ✅ | Missing: Switch | ⚠️ Mismatch |
| 0027 | Button, Buzzer, 0.2, 1 | ✅ | Missing: 0.2 | Missing: 0.2 | ⚠️ Mismatch |
| 0028 | Button, Buzzer | ✅ | ✅ | ✅ | ✅ |
| 0029 | Buzzer, LDR | ✅ | ✅ | ✅ | ✅ |
| 0030 | Buzzer | ✅ | ✅ | ✅ | ✅ |
| 0031 | Motor, 3 | ✅ | ✅ | ✅ | ✅ |
| 0032 | Motor, 0.5 | ✅ | ✅ | ✅ | ✅ |
| 0033 | Button, Motor | ✅ | ✅ | ✅ | ✅ |
| 0034 | Button, Motor, 3 | ✅ | ✅ | ✅ | ✅ |
| 0035 | Button, Motor | ✅ | ✅ | Missing: Motor | ⚠️ Mismatch |
| 0036 | Button, Motor, 5 | ✅ | Missing: 5 | ✅ | ⚠️ Mismatch |
| 0037 | Motor, 2 | ✅ | Missing: 2 | ✅ | ⚠️ Mismatch |
| 0038 | Button, Motor, 4 | ✅ | Missing: 4 | ✅ | ⚠️ Mismatch |
| 0039 | Motor, Temp | Missing: Temp | ✅ | ✅ | ⚠️ Mismatch |
| 0040 | Motor, 3 | ✅ | ✅ | ✅ | ✅ |
| 0041 | LED, 5, 2 | ✅ | Missing: 5, 2 | ✅ | ⚠️ Mismatch |
| 0042 | None | ✅ | ✅ | ✅ | ✅ |
| 0043 | Button | ✅ | ✅ | ✅ | ✅ |
| 0044 | None | ✅ | ✅ | ✅ | ✅ |
| 0045 | Button, 5 | ✅ | Missing: 5 | ✅ | ⚠️ Mismatch |
| 0046 | LDR, Switch | Missing: LDR | ✅ | ✅ | ⚠️ Mismatch |
| 0047 | LED, Button, 3 | ✅ | ✅ | Missing: Button | ⚠️ Mismatch |
| 0048 | LED, Button | ✅ | ✅ | ✅ | ✅ |
| 0049 | LED, Ultrasonic | Missing: Ultrasonic | ✅ | ✅ | ⚠️ Mismatch |
| 0050 | LED | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0051 | LED | ✅ | ✅ | ✅ | ✅ |
| 0052 | LED, 5 | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0053 | LED, Button, Switch | ✅ | ✅ | Missing: Button, Switch | ⚠️ Mismatch |
| 0054 | LED, RGB | Missing: RGB | Missing: LED | Missing: RGB | ⚠️ Mismatch |
| 0055 | LED | ✅ | ✅ | ✅ | ✅ |
| 0056 | LED, LDR | Missing: LDR | Missing: LED, LDR | ✅ | ⚠️ Mismatch |
| 0057 | LED, Ultrasonic, RGB | Missing: Ultrasonic, RGB | Missing: LED, Ultrasonic, RGB | ✅ | ⚠️ Mismatch |
| 0058 | LED, LDR, 2 | ✅ | Missing: LED, LDR | ✅ | ⚠️ Mismatch |
| 0059 | LED, Button, 15 | ✅ | Missing: Button, 15 | ✅ | ⚠️ Mismatch |
| 0060 | LED, LDR | ✅ | Missing: LED, LDR | ✅ | ⚠️ Mismatch |
| 0061 | Button, Buzzer, 0.5 | ✅ | Missing: 0.5 | Missing: 0.5 | ⚠️ Mismatch |
| 0062 | LED, Button, Buzzer, 5 | ✅ | Missing: 5 | ✅ | ⚠️ Mismatch |
| 0063 | Button, Buzzer, Switch | ✅ | ✅ | Missing: Switch | ⚠️ Mismatch |
| 0064 | Button, Buzzer | ✅ | Missing: Buzzer | ✅ | ⚠️ Mismatch |
| 0065 | Button | ✅ | ✅ | ✅ | ✅ |
| 0066 | LED, Button, Buzzer, 3, 2 | ✅ | Missing: LED, Buzzer | ✅ | ⚠️ Mismatch |
| 0067 | Buzzer, Switch, 10 | ✅ | Missing: Buzzer, 10 | Missing: Switch | ⚠️ Mismatch |
| 0068 | Button, Buzzer | ✅ | Missing: Buzzer | ✅ | ⚠️ Mismatch |
| 0069 | Buzzer, Ultrasonic, 3 | Missing: Ultrasonic | Missing: Buzzer, 3 | ✅ | ⚠️ Mismatch |
| 0070 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0071 | LED, Button, 3 | ✅ | Missing: LED, 3 | ✅ | ⚠️ Mismatch |
| 0072 | LED, Button, 0.1, 0.5 | ✅ | Missing: 0.1, 0.5 | ✅ | ⚠️ Mismatch |
| 0073 | Button, 10 | ✅ | Missing: 10 | ✅ | ⚠️ Mismatch |
| 0074 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0075 | Button, Buzzer | ✅ | Missing: Buzzer | ✅ | ⚠️ Mismatch |
| 0076 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0077 | Button, Buzzer | ✅ | Missing: Buzzer | ✅ | ⚠️ Mismatch |
| 0078 | LED, Button, RGB | Missing: RGB | Missing: RGB | ✅ | ⚠️ Mismatch |
| 0079 | LED, Ultrasonic | Missing: Ultrasonic | Missing: LED, Ultrasonic | ✅ | ⚠️ Mismatch |
| 0080 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0081 | Button | ✅ | ✅ | ✅ | ✅ |
| 0082 | LED, Button, 3, 5 | ✅ | Missing: LED, 5 | Missing: 3 | ⚠️ Mismatch |
| 0083 | Button | ✅ | ✅ | ✅ | ✅ |
| 0084 | LED, Button, Display | Missing: Display | Missing: LED, Display | Missing: Display | ⚠️ Mismatch |
| 0085 | Display | ✅ | Missing: Display | ✅ | ⚠️ Mismatch |
| 0086 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0087 | Button, Buzzer, 1 | ✅ | ✅ | ✅ | ✅ |
| 0088 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0089 | LDR | ✅ | Missing: LDR | ✅ | ⚠️ Mismatch |
| 0090 | Display | ✅ | ✅ | ✅ | ✅ |
| 0091 | LED | ✅ | ✅ | ✅ | ✅ |
| 0092 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0093 | Button, Buzzer, 0.2, 0.6 | ✅ | Missing: Buzzer, 0.2, 0.6 | Missing: Button, 0.6 | ⚠️ Mismatch |
| 0094 | LED | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0095 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0096 | LED, LDR | ✅ | Missing: LED, LDR | ✅ | ⚠️ Mismatch |
| 0097 | LED, Button | ✅ | Missing: LED | ✅ | ⚠️ Mismatch |
| 0098 | Button, 3 | ✅ | Missing: 3 | ✅ | ⚠️ Mismatch |
| 0099 | LED, 10 | ✅ | ✅ | ✅ | ✅ |
| 0100 | Buzzer | ✅ | ✅ | ✅ | ✅ |
