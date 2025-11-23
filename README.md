# Lines & Voicings

A unified music practice suite combining bebop line practice and chord voicing practice in one seamless application.

## Overview

Lines & Voicings is an interactive web application designed to help jazz musicians practice both bebop lines and chord voicings. The application consists of two integrated programs:

- **Lines**: Bebop Practice Program - Practice bebop phrases across various chord progressions and keys
- **Voicings**: Chord Practice Program - Practice dominant 7th chord voicings and variations

## Features

### Lines Program
- **Practice Modes**: Random or Designate key selection
- **Multiple Phrase Types**: 7sus4, Major, 25s, IV to iv, Turnaround, Rhythm Changes, and more
- **Progressive Reveal**: Learn phrases by first seeing partial phrases, then revealing the full phrase
- **Responsive Design**: Optimized for both mobile and desktop

### Voicings Program
- **Chord Types**: X7, X7sus4, X7#11, X7b13#9, X7b9, and Random
- **Audio Playback**: Listen to chord voicings before seeing them
- **Visual Notation**: See chord voicings in standard music notation
- **Interactive Learning**: Generate, listen, and practice chord voicings

## Installation and Setup

### Running Locally

1. Clone or download this repository to your local machine
2. Navigate to the project directory
3. Run the included Python server:
   ```bash
   python3 server.py
   ```
   The server will start on port 8004 by default
4. Open your browser and navigate to `http://localhost:8004`

### Alternative: Using Python's Built-in Server

```bash
python3 -m http.server 8004
```

### Requirements
- Python 3.x (for the server)
- Modern web browser with JavaScript enabled
- No additional dependencies needed (all libraries are included via CDN)

## Project Structure

```
lines-voicings/
├── index.html              # Main entry point
├── lines.html              # Bebop Practice Program
├── app.js                  # Lines program logic
├── data.js                 # Musical data structures
├── music-utils.js          # Music utility functions
├── phrase-generator.js     # Phrase generation logic
├── styles.css              # Main stylesheet
├── server.py               # Local development server
├── Chord Practice Program/ # Voicings program
│   ├── index.html
│   ├── app.js
│   ├── styles.css
│   └── audio/              # Chord audio files
└── README.md
```

## How to Use

1. **Start the Application**: Run the server and open the main page
2. **Choose Program**: 
   - Click "Lines" for bebop phrase practice
   - Click "Voicings" for chord voicing practice
3. **Navigate**: Use the return arrows in the bottom-right corner to navigate back to the main menu
4. **Practice**: Follow the on-screen instructions for each program

## Technical Implementation

- **Frontend**: HTML5, CSS3, JavaScript
- **Music Rendering**: ABC notation via abcjs library
- **Server**: Python HTTP server for local development
- **Design**: Glassmorphism UI with responsive layout

## Credits

Made by tsy  
Contact: tungsyauy@gmail.com
