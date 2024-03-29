import tkinter as tk

bagansakit=[
    [0,1,2,3,9], #20,21,22,23,29
    [0,1,2,4,10], #20,21,22,24,30
    [0,1,2,5,6,9], #20,21,22,25,26,29
    [1,7,11], #21,27,31
    [8,2,5,12] #28,22,25,32
]
bagangejala = [
    [1, 2, 4, 5],
    [4, 5, 6],
    [4, 7],
    [4, 8, 9],
    [8, 10],
    [4, 5, 9, 11],
    [4, 8, 11, 12],
    [4, 13],
    [1, 2, 3, 4],
    [14, 15],
    [14, 16],
    [14, 17],
    [18, 19]
]
penyakit = [
    "Staphylococcus aureus",
    "Jamur beracun",
    "Salmonellae",
    "Clostridium botulinum",
    "Campylobacter"
]

txtgejala = [
    "1. Sering mengalami buang air besar (> 2 kali)?",
    "2. Mengalami berak encer?",
    "3. Mengalami berak berdarah?",
    "4. Merasa lesu dan tidak bergairah?",
    "5. Tidak selera makan?",
    "6. Merasa mual dan sering muntah (lebih dari 1 kali) ?",
    "7. Merasa sakit di bagian perut ?",
    "8. Tekanan darah anda rendah ?",
    "9. Anda merasa pusing ?",
    "10. Anda mengalami pingsan ?",
    "11. Suhu badan anda tinggi ?",
    "12. Mengalami luka di bagian tertentu ?",
    "13. Tidak dapat menggerakkan anggota badan tertentu ?",
    "14. Pernah memakan sesuatu ?",
    "15. Memakan daging ?",
    "16. Memakan jamur ?",
    "17. Memakan makanan kaleng ?",
    "18. Membeli susu ?",
    "19. Meminum susu ?"
]

def process_gejala():
    sakit = [0] * len(bagangejala)
    target = [0] * len(bagansakit)

    for i in range(len(bagangejala)):
        tmp = 0.0
        for j in range(len(bagangejala[i])):
            if checkboxes[bagangejala[i][j] - 1].get() == 1:
                tmp += 100 / len(bagangejala[i])
        sakit[i] = tmp

    for i in range(len(bagansakit)):
        tmp = 0.0
        for j in range(len(bagansakit[i])):
            tmp += sakit[bagansakit[i][j]] / len(bagansakit[i])
        target[i] = tmp

    persenmax = max(target)
    imax = target.index(persenmax)

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Hasil:\n")
    for i in range(len(penyakit)):
        output.insert(tk.END, f"{penyakit[i]} : {target[i]:.2f} %\n")
    if persenmax >= float(threshold.get()):
        output.insert(tk.END, f"Diagnosa: {penyakit[imax]}")
    else:
        output.insert(tk.END, "Tidak ada diagnosis yang memenuhi threshold.")


root = tk.Tk()
root.title("Diagnosa Penyakit Gastro Usus")

threshold_label = tk.Label(root, text="Threshold (%):")
threshold_label.grid(row=0, column=0, padx=5, pady=5)
threshold = tk.Entry(root)
threshold.insert(tk.END, "20")
threshold.grid(row=0, column=1, padx=5, pady=5)

checkboxes = []
for i, gejala in enumerate(txtgejala):
    checkbox = tk.IntVar()
    tk.Checkbutton(root, text=gejala, variable=checkbox).grid(row=i+1, column=0, columnspan=2, sticky="w")
    checkboxes.append(checkbox)

process_button = tk.Button(root, text="Proses", command=process_gejala)
process_button.grid(row=len(txtgejala)+1, column=0, columnspan=2, pady=10)

output = tk.Text(root, height=10, width=50)
output.grid(row=len(txtgejala)+2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
