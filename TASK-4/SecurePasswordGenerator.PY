# Secure Password Generator with Multilingual Support
import random
import string
import tkinter as tk
from tkinter import ttk, messagebox


# Function to generate a secure password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong", "#27ae60"
    elif length >= 8 and (has_upper or has_lower) and has_digit:
        return "Moderate", "#f39c12"
    else:
        return "Weak", "#e74c3c"


# Event handler for generating password
def generate_password_event():
    try:
        # Get the entered length
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text=texts['positive_number_error'], fg="red")
            return

        # Generate password
        password = generate_password(length)

        # Display password
        output_option = output_var.get()
        if output_option == "Terminal":
            print(f"Generated Password: {password}")
            result_label.config(text=texts['terminal_message'], fg="green")
        elif output_option == "Pop-Up":
            messagebox.showinfo("Secure Password Generator", f"{texts['Pop-Up_message']}: {password}")
            result_label.config(text=texts['Pop-Up_success'], fg="green")
        else:
            result_label.config(text=texts['select_output'], fg="red")

        # Show password strength
        strength, color = check_password_strength(password)
        strength_label.config(text=f"{texts['strength']}: {strength}", fg=color)

        # Enable the copy button
        copy_button.config(state="normal")
        copy_button.password = password

    except ValueError:
        result_label.config(text=texts['valid_number_error'], fg="red")


# Function to copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(copy_button.password)
    root.update()
    result_label.config(text=texts['copy_message'], fg="green")


# Function to update the UI text based on the selected language
def update_language(event=None):
    selected_language = language_var.get()
    global texts
    texts = translations[selected_language]

    header_label.config(text=texts['header'])
    length_label.config(text=texts['enter_length'])
    output_label.config(text=texts['select_output_label'])
    generate_button.config(text=texts['generate_button'])
    copy_button.config(text=texts['copy_button'])
    footer_label.config(text=texts['footer'])


# Translations for multilingual support
translations = {
    "English": {
        "header": "🔒 Secure Password Generator",
        "enter_length": "Enter Password Length:",
        "select_output_label": "Select Output Method:",
        "generate_button": "Generate Password",
        "copy_button": "Copy to Clipboard",
        "footer": "Your passwords are safe with us!",
        "positive_number_error": "Length must be a positive number.",
        "terminal_message": "Password displayed in terminal.",
        "Pop-Up_message": "Generated Password",
        "Pop-Up_success": "Password displayed in Pop-Up.",
        "select_output": "Please select an output method.",
        "valid_number_error": "Please enter a valid number.",
        "copy_message": "Password copied to clipboard!",
        "strength": "Password Strength",
    },
     "Spanish": {
        "header": "🔒 Generador de Contraseñas Seguras",
        "enter_length": "Ingrese la Longitud de la Contraseña:",
        "select_output_label": "Seleccione el Método de Salida:",
        "generate_button": "Generar Contraseña",
        "copy_button": "Copiar al Portapapeles",
        "footer": "¡Tus contraseñas están seguras con nosotros!",
        "positive_number_error": "La longitud debe ser un número positivo.",
        "terminal_message": "Contraseña mostrada en la terminal.",
        "Pop-Up_message": "Contraseña Generada",
        "Pop-Up_success": "Contraseña mostrada en un cuadro de diálogo.",
        "select_output": "Por favor seleccione un método de salida.",
        "valid_number_error": "Por favor ingrese un número válido.",
        "copy_message": "¡Contraseña copiada al portapapeles!",
        "strength": "Fortaleza de la Contraseña",
    },
    "French": {
        "header": "🔒 Générateur de Mots de Passe Sécurisés",
        "enter_length": "Entrez la Longueur du Mot de Passe:",
        "select_output_label": "Sélectionnez la Méthode de Sortie:",
        "generate_button": "Générer un Mot de Passe",
        "copy_button": "Copier dans le Presse-papiers",
        "footer": "Vos mots de passe sont en sécurité avec nous!",
        "positive_number_error": "La longueur doit être un nombre positif.",
        "terminal_message": "Mot de passe affiché dans le terminal.",
        "Pop-Up_message": "Mot de Passe Généré",
        "Pop-Up_success": "Mot de passe affiché dans une fenêtre contextuelle.",
        "select_output": "Veuillez sélectionner une méthode de sortie.",
        "valid_number_error": "Veuillez entrer un nombre valide.",
        "copy_message": "Mot de passe copié dans le presse-papiers!",
        "strength": "Force du Mot de Passe",
    },
    "German": {
        "header": "🔒 Sicherer Passwortgenerator",
        "enter_length": "Geben Sie die Passwortlänge ein:",
        "select_output_label": "Wählen Sie die Ausgabemethode:",
        "generate_button": "Passwort generieren",
        "copy_button": "In die Zwischenablage kopieren",
        "footer": "Ihre Passwörter sind bei uns sicher!",
        "positive_number_error": "Die Länge muss eine positive Zahl sein.",
        "terminal_message": "Passwort im Terminal angezeigt.",
        "Pop-Up_message": "Generiertes Passwort",
        "Pop-Up_success": "Passwort in Pop-Up angezeigt.",
        "select_output": "Bitte wählen Sie eine Ausgabemethode.",
        "valid_number_error": "Bitte geben Sie eine gültige Zahl ein.",
        "copy_message": "Passwort in die Zwischenablage kopiert!",
        "strength": "Passwortstärke",
    },
    "Chinese": {
        "header": "🔒 安全密码生成器",
        "enter_length": "输入密码长度:",
        "select_output_label": "选择输出方式:",
        "generate_button": "生成密码",
        "copy_button": "复制到剪贴板",
        "footer": "您的密码在我们这里是安全的!",
        "positive_number_error": "长度必须是正数。",
        "terminal_message": "密码在终端中显示。",
        "Pop-Up_message": "生成的密码",
        "Pop-Up_success": "密码在弹出窗口中显示。",
        "select_output": "请选择输出方式。",
        "valid_number_error": "请输入有效的数字。",
        "copy_message": "密码已复制到剪贴板!",
        "strength": "密码强度",
    },
    "Russian": {
        "header": "🔒 Генератор Безопасных Паролей",
        "enter_length": "Введите Длину Пароля:",
        "select_output_label": "Выберите Метод Вывода:",
        "generate_button": "Сгенерировать Пароль",
        "copy_button": "Скопировать в Буфер Обмена",
        "footer": "Ваши пароли в безопасности у нас!",
        "positive_number_error": "Длина должна быть положительным числом.",
        "terminal_message": "Пароль отображен в терминале.",
        "Pop-Up_message": "Сгенерированный Пароль",
        "Pop-Up_success": "Пароль отображен в всплывающем окне.",
        "select_output": "Пожалуйста, выберите метод вывода.",
        "valid_number_error": "Пожалуйста, введите действительное число.",
        "copy_message": "Пароль скопирован в буфер обмена!",
        "strength": "Сила Пароля",
    },
    "Japanese": {
        "header": "🔒 セキュアパスワードジェネレーター",
        "enter_length": "パスワードの長さを入力してください:",
        "select_output_label": "出力方法を選択してください:",
        "generate_button": "パスワードを生成",
        "copy_button": "クリップボードにコピー",
        "footer": "あなたのパスワードは私たちの安全です!",
        "positive_number_error": "長さは正の数でなければなりません。",
        "terminal_message": "ターミナルにパスワードが表示されました。",
        "Pop-Up_message": "生成されたパスワード",
        "Pop-Up_success": "ポップアップにパスワードが表示されました。",
        "select_output": "出力方法を選択してください。",
        "valid_number_error": "有効な数字を入力してください。",
        "copy_message": "パスワードがクリップボードにコピーされました!",
        "strength": "パスワードの強度",
    },
    "Korean": {
        "header": "🔒 안전한 비밀번호 생성기",
        "enter_length": "비밀번호 길이를 입력하세요:",
        "select_output_label": "출력 방법 선택:",
        "generate_button": "비밀번호 생성",
        "copy_button": "클립보드에 복사",
        "footer": "당신의 비밀번호는 우리와 함께 안전합니다!",
        "positive_number_error": "길이는 양수여야 합니다.",
        "terminal_message": "터미널에 비밀번호가 표시됩니다.",
        "Pop-Up_message": "생성된 비밀번호",
        "Pop-Up_success": "팝업에 비밀번호가 표시됩니다.",
        "select_output": "출력 방법을 선택하세요.",
        "valid_number_error": "유효한 숫자를 입력하세요.",
        "copy_message": "비밀번호가 클립보드에 복사되었습니다!",
        "strength": "비밀번호 강도",
    },
    "Hindi": {
        "header": "🔒 सुरक्षित पासवर्ड जनरेटर",
        "enter_length": "पासवर्ड की लंबाई दर्ज करें:",
        "select_output_label": "आउटपुट विधि चुनें:",
        "generate_button": "पासवर्ड जनरेट करें",
        "copy_button": "क्लिपबोर्ड पर कॉपी करें",
        "footer": "आपके पासवर्ड हमारे साथ सुरक्षित हैं!",
        "positive_number_error": "लंबाई एक सकारात्मक संख्या होनी चाहिए।",
        "terminal_message": "टर्मिनल में पासवर्ड प्रदर्शित किया गया।",
        "Pop-Up_message": "जनरेटेड पासवर्ड",
        "Pop-Up_success": "पॉप-अप में पासवर्ड प्रदर्शित किया गया।",
        "select_output": "कृपया एक आउटपुट विधि चुनें।",
        "valid_number_error": "कृपया एक मान्य संख्या दर्ज करें।",
        "copy_message": "पासवर्ड क्लिपबोर्ड पर कॉपी किया गया!",
        "strength": "पासवर्ड की ताकत",
    }
    # Additional translations omitted for brevity
}

# Create the main tkinter window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Language selection dropdown
language_var = tk.StringVar(value="English")
language_label = tk.Label(root, text="Language:", font=("Helvetica", 10), bg="#1e1e1e", fg="#ffffff")
language_label.pack(pady=5)
language_menu = ttk.Combobox(root, textvariable=language_var, state="readonly", values=list(translations.keys()), width=15)
language_menu.pack(pady=5)
language_menu.bind("<<ComboboxSelected>>", update_language)

# Create a header
header_label = tk.Label(root, text="🔒 Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="#00ffcc")
header_label.pack(pady=10)

# Input field for password length
length_label = tk.Label(root, text="Enter Password Length:", font=("Helvetica", 12), bg="#1e1e1e", fg="#ffffff")
length_label.pack(pady=5)
length_entry = ttk.Entry(root, width=35)
length_entry.pack(pady=5)

# Output method dropdown
output_var = tk.StringVar(value="Select Output")
output_label = tk.Label(root, text="Select Output Method:", font=("Helvetica", 12), bg="#1e1e1e", fg="#ffffff")
output_label.pack(pady=5)
output_menu = ttk.Combobox(root, textvariable=output_var, state="readonly", values=["Terminal", "Pop-Up"], width=32)
output_menu.pack(pady=5)

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_event)
generate_button.pack(pady=10)
generate_button.configure(style="Futuristic.TButton")

# Copy button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)
copy_button.configure(style="Futuristic.TButton")

# Password strength label
strength_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#1e1e1e", fg="#ffffff")
strength_label.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"), bg="#1e1e1e", wraplength=450, fg="#ffffff")
result_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Your passwords are safe with us!", font=("Helvetica", 10, "italic"), bg="#1e1e1e", fg="#7f8c8d")
footer_label.pack(side="bottom", pady=10)

# Set initial language
update_language()

# Run the application
root.mainloop()
