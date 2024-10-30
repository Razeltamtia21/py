# Daftar pertanyaan, pilihan, dan jawaban
questions = [
    {
        "question": "Apa ibu kota dari Indonesia?",
        "choices": ["a. Jakarta", "b. Surabaya", "c. Bandung", "d. Medan"],
        "answer": "a"
    },
    {
        "question": "Berapa hasil dari 5 + 7?",
        "choices": ["a. 10", "b. 12", "c. 13", "d. 14"],
        "answer": "b"
    },
    {
        "question": "Siapa presiden pertama Indonesia?",
        "choices": ["a. Soeharto", "b. Megawati", "c. Soekarno", "d. Joko Widodo"],
        "answer": "c"
    }
]

# Fungsi menjalankan kuis
def run_quiz():
    print("=== Kuis Pilihan Ganda ===")
    score = 0
    for i, question in enumerate(questions):
        print(f"\nPertanyaan {i + 1}: {question['question']}")
        for choice in question["choices"]:
            print(choice)
        
        answer = input("Jawaban Anda (a/b/c/d): ").lower()
        
        # Cek jawaban
        if answer == question["answer"]:
            print("Benar!")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah '{question['answer']}'")
    
    # Tampilkan skor akhir
    print(f"\nKuis selesai! Skor Anda: {score} dari {len(questions)}")

# Menjalankan kuis
run_quiz()
