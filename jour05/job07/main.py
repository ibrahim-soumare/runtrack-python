def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
           
            notes_arrondies.append(note)
        else:
            
            difference = 5 - (note % 5)
            if difference < 3:
                note_arrondie = note + difference
            else:
                note_arrondie = note

            notes_arrondies.append(min(note_arrondie, 100))

    return notes_arrondies


notes_originales = [35, 82, 67, 93, 45]
notes_arrondies = arrondir_notes(notes_originales)


print("Notes originales :", notes_originales)
print("Notes arrondies  :", notes_arrondies)