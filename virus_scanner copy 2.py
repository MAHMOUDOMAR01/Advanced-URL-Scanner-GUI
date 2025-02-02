import hashlib
import requests
import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk

# قائمة التوقيعات المعروفة (هاش المحتوى الضار أو URLs)
known_signatures = [
    '5d41402abc4b2a76b9719d911017c592',  # مثال على توقيع MD5 لمحتوى ضار
]

def calculate_md5(content):
    """حساب هاش MD5 لمحتوى الصفحة."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def fetch_url_content(url):
    """جلب محتوى URL."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"فشل في جلب {url}: {e}")
        return None

def scan_url(url):
    """فحص URL للتوقيعات المعروفة أو سلوك مشبوه."""
    content = fetch_url_content(url)
    if not content:
        return "Error"
    
    url_signature = calculate_md5(content)
    if url_signature in known_signatures:
        return "محتوى ضار معروف"
    else:
        return "آمن"

def store_results_in_file(url, status, filename="scan_results.txt"):
    """تخزين نتائج الفحص في ملف نصي."""
    with open(filename, 'a', encoding='utf-8') as f:  # إضافة الترميز UTF-8
        f.write(f"URL: {url}, Status: {status}, Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def display_results_from_file(filename="scan_results.txt"):
    """قراءة وعرض نتائج الفحص من الملف النصي."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # إضافة الترميز UTF-8
            return f.read()
    except FileNotFoundError:
        return "لا توجد نتائج فحص سابقة."

def start_scan():
    url = url_entry.get()
    if url:
        status = scan_url(url)
        store_results_in_file(url, status)
        
        # تحديث نتائج الفحص داخل مربع النتائج
        result_text.delete(1.0, tk.END)  # مسح النتائج السابقة
        if status == "آمن":
            result_text.tag_configure("safe", foreground="green")
            icon_path = "image/safe_icon.png"
        else:
            result_text.tag_configure("danger", foreground="red")
            icon_path = "image/danger_icon.png"

        # إضافة الأيقونة
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((40, 40), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        result_text.image_create(tk.END, image=icon_photo)
        result_text.insert(tk.END, f" URL: {url} - Status: {status}\n", "safe" if status == "آمن" else "danger")
        result_text.image = icon_photo  # الاحتفاظ بالمرجع للأيقونة

        url_entry.delete(0, tk.END)  # مسح حقل الإدخال بعد الفحص
    else:
        messagebox.showwarning("خطأ في الإدخال", "يرجى إدخال URL صالح.")

def show_previous_results():
    results = display_results_from_file()
    result_text.insert(tk.END, f"\nنتائج سابقة:\n{results}\n")

def clear_results():
    """مسح صندوق النتائج."""
    result_text.delete(1.0, tk.END)

def create_gui():
    global root, url_entry, result_text  # جعل المتغيرات العالمية

    root = tk.Tk()
    root.title("فاحص الروابط المتقدم")

    # تعيين حجم النافذة ولون الخلفية
    root.geometry("800x800")
    root.configure(bg="#2E2E2E")  # لون داكن

    # إضافة الشعار
    logo_image = Image.open("image/logo.png")  # تأكد من وضع صورة الشعار في نفس مجلد السكربت
    logo_image = logo_image.resize((750, 400), Image.Resampling.LANCZOS)  # تغيير حجم الشعار حسب الحاجة
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(root, image=logo_photo, bg="#2E2E2E")
    logo_label.image = logo_photo  # الاحتفاظ بالمرجع للصورة
    logo_label.pack(pady=10)

    # إدخال URL بحجم أكبر ونص بديل
    url_entry_frame = tk.Frame(root, bg="#2E2E2E")
    url_entry_frame.pack(pady=10)
    url_label = tk.Label(url_entry_frame, text="قم بادخال الرابط :", font=("Arial", 14), bg="#2E2E2E", fg="white")
    url_label.pack(side=tk.LEFT, padx=10)
    url_entry = tk.Entry(url_entry_frame, width=50, font=("Arial", 14), bg="#3C3C3C", fg="white")
    url_entry.pack(side=tk.LEFT)

    # إطار للأزرار
    button_frame = tk.Frame(root, bg="#2E2E2E")
    button_frame.pack(pady=20)

    scan_button = tk.Button(button_frame, text="فحص URL", command=start_scan, font=("Arial", 12), width=12, bg="#4CAF50", fg="white")
    scan_button.grid(row=0, column=0, padx=10)

    clear_button = tk.Button(button_frame, text="مسح النتائج", command=clear_results, font=("Arial", 12), width=12, bg="#f44336", fg="white")
    clear_button.grid(row=0, column=1, padx=10)

    show_results_button = tk.Button(button_frame, text="النتائج السابقة", command=show_previous_results, font=("Arial", 12), width=12, bg="#2196F3", fg="white")
    show_results_button.grid(row=0, column=2, padx=10)

    # صندوق نص متدحرج لعرض النتائج
    result_text = scrolledtext.ScrolledText(root, width=70, height=15, font=("Arial", 12), wrap=tk.WORD, bg="#3C3C3C", fg="white")
    result_text.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
