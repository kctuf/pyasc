import base64
from tkinter import *
from tkinter import messagebox


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def saveencryptnotes():
    tite = title_entry.get()
    message = input_text.get("1.0", END)
    master_secret = master_secret_input.get()

    if len(tite) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="Hata", message="Tüm bilgileri girin")
    else:
        message_encrypted = encode(master_secret, message)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{tite}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f"\n{tite}\n{message_encrypted}")
        finally:
            title_entry.delete(0, END)
            master_secret_input.delete(0, END)
            input_text.delete("1.0", END)


def decrypt_notes():
    message_enrypted = input_text.get("1.0", END)
    master_secret = master_secret_input.get()

    if len(message_enrypted) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="Hata", message="Eksik bilgi")
    else:
        try:
            decrypted_message = decode(master_secret, message_enrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showwarning(title="Error",message="bu msj çözüldü")

# UI
window = Tk()
window.title("Gizli Notlar")
window.config(padx=30, pady=30)

photo = PhotoImage(file="photo.png", )
photolablel = Label(image=photo)

canvas = Canvas(height=300, width=300)
canvas.create_image(0, 0, image=photo)
canvas.pack()

title_info_label = Label(text="Başlık Gir")
title_info_label.pack(padx=5, pady=5)

title_entry = Entry(width=30)
title_entry.pack()

input_info_label = Label(text="Gizli Bilgi Gir")
input_info_label.pack()

input_text = Text(width=30, height=15)
input_text.pack()

master_secret_Label = Label(text="Anahtar Gir")
master_secret_Label.pack()

master_secret_input = Entry(width=30)
master_secret_input.pack()

save_button = Button(text="Save&Encrypt", command=saveencryptnotes)
save_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt_notes)
decrypt_button.pack()

window.mainloop()
