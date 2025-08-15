import json
import os.path

FILENAME = "notes.json"

class Note:
    def __init__(self, note_id, note_text):
        self.id = note_id
        self.text = note_text
    def to_dict(self): # Konverze objektu na slovník pro uložení do JSON
        return {"id": self.id, "text": self.text}
    def from_dict(data): # Načtení objektu z JSON slovníku
        return Note(data["id"], data["text"])

class Notebook: # Třída
    def __init__(self):
        self.notes = []
        self.load_notes()

    def add_note(self, text): # Metoda
        new_id = max([note.id for note in self.notes], default=0) + 1
        new_note = Note(new_id, text)
        self.notes.append(new_note)
        self.save_notes()
        print("Note added.")

    def save_notes(self):
        with open(FILENAME, "w") as f:
            json.dump([note.to_dict() for note in self.notes], f, indent=2)

    def load_notes(self):
        if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
            with open(FILENAME, "r") as f:
                data = json.load(f)
                self.notes = [Note.from_dict(note) for note in data]
        else:
            self.notes = []

    def delete_notes(self):
        note_id = input("Type the ID of the note you want to delete: ")
        for note in self.notes:
            if note.id == int(note_id):
                self.notes.remove(note)
                self.save_notes()
                print("Note deleted.")
                return

def main():
    notebook = Notebook()

    while True:
        print("\nNotes book")
        print("1. Show notes")
        print("2. Create new note")
        print("3. Delete note")
        print("4. Close")
        choice = input("Choose what you want to do: ")

        if choice == "1":
            if not notebook.notes:
                print("There's no notes!")
            else:
                for note in notebook.notes:
                    print(f"[{note.id}] {note.text}")
        elif choice == "2":
            text = input("Type your text: ")
            notebook.add_note(text)

        elif choice == "3":
            notebook.delete_notes()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()