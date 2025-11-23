# score_generator.py
import subprocess
import os

def convert_to_lilypond_note(note):
    note_name = note[:-1]
    octave = int(note[-1])
    
    if len(note_name) == 1:
        lilypond_note = note_name.lower()
    else:
        base_note = note_name[0].lower()
        accidental = note_name[1]
        if accidental == "#":
            lilypond_note = base_note + "is"
        else:
            lilypond_note = base_note + "es"
    
    octave_diff = octave - 3
    if octave_diff >= 0:
        octave_mark = "'" * octave_diff
    else:
        octave_mark = "," * abs(octave_diff)
    
    return f"{lilypond_note}{octave_mark}8"

def generate_score_ly(phrase, partial=False, phrase_length=9):
    if partial:
        if phrase_length < 5:
            raise ValueError("Phrase must have at least 5 notes for partial display")
        if phrase_length == 9:
            notes = [phrase[0], phrase[4], phrase[8]]
            lilypond_notes_list = [convert_to_lilypond_note(note) for note in notes]
            lilypond_notes = f"{lilypond_notes_list[0]} r8 r8 r8 {lilypond_notes_list[1]} r8 r8 r8 {lilypond_notes_list[2]}"
        elif phrase_length == 17:
            notes = [phrase[0], phrase[4], phrase[8], phrase[12], phrase[16]]
            lilypond_notes_list = [convert_to_lilypond_note(note) for note in notes]
            lilypond_notes = f"{lilypond_notes_list[0]} r8 r8 r8 {lilypond_notes_list[1]} r8 r8 r8 {lilypond_notes_list[2]} r8 r8 r8 {lilypond_notes_list[3]} r8 r8 r8 {lilypond_notes_list[4]}"
        else:
            notes = [phrase[0], phrase[4], phrase[-1]]
            lilypond_notes_list = [convert_to_lilypond_note(note) for note in notes]
            lilypond_notes = f"{lilypond_notes_list[0]} r8 r8 r8 {lilypond_notes_list[1]} r8 r8 r8 {lilypond_notes_list[2]}"
    else:
        notes = phrase
        lilypond_notes = " ".join(convert_to_lilypond_note(note) for note in notes)
    
    print(f"Generating score {'partial' if partial else 'full'}: phrase={phrase}, notes={notes}, lilypond_notes={lilypond_notes}")
    content = f"""
\\version "2.24.0"
\\paper {{
  #(set-paper-size '(cons (* 8 in) (* 2.5 in)))
  indent = 0\\mm
  left-margin = 0\\mm
  right-margin = 0\\mm
  top-margin = 0\\mm
  bottom-margin = 0\\mm
  line-width = 200\\mm
  ragged-right = ##f
  system-count = 1
}}
\\score {{
  \\new Staff {{
    \\override Staff.StaffSymbol.thickness = #0.5
    \\set Staff.fontSize = #2
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