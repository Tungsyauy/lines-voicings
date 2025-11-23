# score_generator.py
import subprocess
import os

def convert_to_lilypond_note(note):
    # Extract the note name and octave (e.g., "C5" -> "C", 5)
    note_name = note[:-1]  # Everything except the last character (e.g., "C" or "Bb")
    octave = int(note[-1])  # Last character is the octave (e.g., 5)
    
    # Convert note name to LilyPond format
    if len(note_name) == 1:  # Simple note (e.g., "C", "D")
        lilypond_note = note_name.lower()
    else:  # Sharp or flat note (e.g., "F#", "Bb")
        base_note = note_name[0].lower()  # "F" or "B"
        accidental = note_name[1]  # "#" or "b"
        if accidental == "#":
            lilypond_note = base_note + "is"  # "fis" for F#, "cis" for C#
        else:  # accidental == "b"
            lilypond_note = base_note + "es"  # "bes" for Bb, "es" for Eb
    
    # Convert octave to LilyPond format (middle C is C4, or c' in LilyPond)
    # In LilyPond, c (no apostrophe) is C3, so we adjust relative to C3
    octave_diff = octave - 3  # Relative to C3 (c in LilyPond)
    if octave_diff >= 0:
        octave_mark = "'" * octave_diff  # Higher octaves use '
    else:
        octave_mark = "," * abs(octave_diff)  # Lower octaves use ,
    
    # Add duration (eighth note)
    return f"{lilypond_note}{octave_mark}8"

def generate_score_ly(phrase, partial=False, phrase_length=9):
    if partial:
        # For partial display: show first note, last note of each cell
        if phrase_length < 5:
            raise ValueError("Phrase must have at least 5 notes for partial display")
        if phrase_length == 9:  # Standard 7sus4 or major phrase (5 + 4 notes)
            notes = [phrase[0], phrase[4], phrase[8]]  # Start, end of left, end of right
            lilypond_notes_list = [convert_to_lilypond_note(note) for note in notes]
            lilypond_notes = f"{lilypond_notes_list[0]} r8 r8 r8 {lilypond_notes_list[1]} r8 r8 r8 {lilypond_notes_list[2]}"
        elif phrase_length == 17:  # Long 25 major (5 + 4 + 4 + 4 notes)
            notes = [phrase[0], phrase[4], phrase[8], phrase[12], phrase[16]]  # Start, end of each cell
            lilypond_notes_list = [convert_to_lilypond_note(note) for note in notes]
            lilypond_notes = f"{lilypond_notes_list[0]} r8 r8 r8 {lilypond_notes_list[1]} r8 r8 r8 {lilypond_notes_list[2]} r8 r8 r8 {lilypond_notes_list[3]} r8 r8 r8 {lilypond_notes_list[4]}"
        else:
            # Generic case: first note, last note of first cell, and last note
            notes = [phrase[0], phrase[4], phrase[-1]]
            lilypond_notes_list = [convert_to_lilypond_note(note) for note in notes]
            lilypond_notes = f"{lilypond_notes_list[0]} r8 r8 r8 {lilypond_notes_list[1]} r8 r8 r8 {lilypond_notes_list[2]}"
    else:
        # For full display: show all notes
        notes = phrase
        lilypond_notes = " ".join(convert_to_lilypond_note(note) for note in notes)
    
    # Debugging: Print the phrase and notes
    print(f"Generating score {'partial' if partial else 'full'}: phrase={phrase}, notes={notes}, lilypond_notes={lilypond_notes}")
    # LilyPond file content with adjusted paper size and line-width
    content = f"""
\\version "2.24.0"
\\paper {{
  #(set-paper-size '(cons (* 8 in) (* 2.5 in)))  % Adjusted paper size: 8 inches wide, 2.5 inches tall
  indent = 0\\mm
  left-margin = 0\\mm
  right-margin = 0\\mm
  top-margin = 0\\mm
  bottom-margin = 0\\mm
  line-width = 200\\mm  % Reduced to make the staff less wide
  ragged-right = ##f
  system-count = 1
}}
\\score {{
  \\new Staff {{
    \\override Staff.StaffSymbol.thickness = #0.5
    \\set Staff.fontSize = #2  % Increased font size for larger notes
    \\override Staff.StaffSymbol.staff-space = #1.0
    \\clef treble
    \\key c \\major
    {lilypond_notes}
  }}
  \\layout {{
    \\context {{
      \\Staff
      \\override VerticalAxisGroup.staff-staff-spacing = #'((basic-distance . 0) (minimum-distance . 0) (padding . 0))
    }}
  }}
}}
"""
    filename = "score.ly" if not partial else "score_partial.ly"
    with open(filename, "w") as f:
        f.write(content)
    # Debugging: Print the content of the generated file
    print(f"Generated {filename} content:\n{content}")
    return filename

def generate_score_png(phrase):
    filename = generate_score_ly(phrase)
    try:
        result = subprocess.run(["lilypond", "--png", "-o", "score", filename], check=True, capture_output=True, text=True)
        print(f"LilyPond output for score: stdout={result.stdout}, stderr={result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"LilyPond error for score: stdout={e.stdout}, stderr={e.stderr}")
        raise
    if not os.path.exists("score.png"):
        raise FileNotFoundError("score.png was not generated")
    return "score.png"

def generate_partial_score_png(phrase, phrase_length):
    filename = generate_score_ly(phrase, partial=True, phrase_length=phrase_length)
    try:
        result = subprocess.run(["lilypond", "--png", "-o", "score_partial", filename], check=True, capture_output=True, text=True)
        print(f"LilyPond output for score_partial: stdout={result.stdout}, stderr={result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"LilyPond error for score_partial: stdout={e.stdout}, stderr={e.stderr}")
        raise
    if not os.path.exists("score_partial.png"):
        raise FileNotFoundError("score_partial.png was not generated")
    return "score_partial.png"

def cleanup_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)