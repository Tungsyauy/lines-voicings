# Dominant 7th Chord Practice Program

A web-based chord practice application for studying dominant 7th chord voicings with dual-staff notation display.

## Features

- **Dual-Staff Display**: Shows chords with both treble and bass clef using ABC.js
- **Multiple Chord Types**: 
  - X7: Basic dominant 7th chord
  - X7sus4: Suspended 4th dominant chord
  - X7#11: Sharp 11 dominant chord
  - X7b13#9: Flat 13 sharp 9 dominant chord
  - X7b9: Flat 9 dominant chord
- **Transposition**: Transpose chords to all 12 keys
- **Responsive Design**: Works on desktop and mobile devices
- **Glassmorphism UI**: Modern, elegant user interface

## Chord Data Structure

Each chord is defined with the following structure:
```javascript
'ChordName': [leftHandNotes..., '|', rightHandNotes...]
```

Where `|` separates left hand (bass clef) from right hand (treble clef) notes.

### Example Chord Voicings (in C):
- **C7**: `['C3', 'Bb3', '|', 'E4', 'A4', 'D5']`
- **C7sus4**: `['C3', 'F3', 'Bb3', '|', 'D4', 'A4']`
- **C7#11**: `['C3', 'E3', 'Bb3', '|', 'D4', 'F#4', 'A4']`
- **C7b13#9**: `['C3', 'Bb3', '|', 'E4', 'Ab4', 'Eb5']`
- **C7b9**: `['C3', 'Bb3', '|', 'C#4', 'E4', 'F#4', 'A4']`

## Technical Implementation

### Technologies Used
1. **HTML**: Basic page structure
2. **CSS**: Glassmorphism styling with responsive design
3. **JavaScript**: Core application logic
4. **ABC.js**: Music notation rendering library

### Key Functions
- `drawStaff(notes)`: Renders dual-staff notation using ABC.js
- `convertToABCWithAccidentals(notes)`: Converts note arrays to ABC notation format
- `transposeChord(notes, semitones, key)`: Transposes chords to different keys
- `adjustChordOctave(chord, key)`: Automatically adjusts octaves for optimal readability

### ABC.js Dual-Staff Syntax
```javascript
const abcNotation = `X:1
L:1/4
K:C
V:1 clef=treble
[${rightHandABC.join('')}]4
V:2 clef=bass
[${leftHandABC.join('')}]4`;
```

## Usage

1. Open `index.html` in a web browser
2. Click "Start Practice" to begin
3. Choose a chord type or select "Random"
4. Use "Generate Chord" to display new chord voicings
5. Use "Transpose" to change keys randomly

## File Structure

```
Chord Practice Program/
├── index.html          # Main HTML file
├── styles.css          # Styling with glassmorphism design
├── app.js             # Main application logic
└── README.md          # This documentation file
```

## Browser Compatibility

- Modern browsers with JavaScript enabled
- Requires internet connection for ABC.js library
- Optimized for both desktop and mobile viewing

## Development Notes

This program follows the same architectural patterns as the Messiaen chord practice program, with the key difference being the chord data structure that uses the `|` separator to distinguish between left and right hand voicings for dual-staff display.


