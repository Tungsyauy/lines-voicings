# Bebop Practice Program

## Overview
The Bebop Practice Program is an interactive web application designed to help jazz musicians practice bebop phrases across various chord progressions and keys. It generates musical phrases based on user-selected parameters and displays them in standard music notation. The program is particularly useful for jazz improvisers looking to expand their vocabulary of bebop lines.

## Installation and Setup

### Running Locally
1. Clone or download this repository to your local machine
2. Navigate to the project directory
3. You can run the application using any local web server. For example:
   - Using Python:
     ```
     python -m http.server 8000
     ```
   - Using Node.js (with http-server installed):
     ```
     npx http-server
     ```
4. Open your browser and navigate to `http://localhost:8000` (or the appropriate port)

### Requirements
- Modern web browser with JavaScript enabled
- No additional dependencies needed (all libraries are included)

## Features

### Practice Modes
- **Random Mode**: Generates phrases in randomly cycling keys
- **Designate Mode**: Allows selection of a specific key for practice

### Phrase Types
The application supports multiple phrase types and chord progressions:

- **7sus4**: Phrases over 7sus4 chords with options for:
  - Minor
  - Dominant
  - Half-diminished (ø7)
  - Altered
  - Random (cycles through different chord types)

- **Major**: Phrases in major keys

- **25 Progressions**: Various ii-V-I and related progressions
  - Major 25 (ii-V-I)
  - Minor 25 (iiø7-V7-i)
  - Backdoor 25 (IV-bVII7-I)
  - Tritone Substitution 25 (both major and minor variants)
  - II7 to bII (tritone substitution)

- **Other Common Jazz Progressions**:
  - IV to iv (major to minor subdominant)
  - Turnaround progressions (I-VI7-ii-V7)
  - Rhythm Changes bars 5-6 (I7-IV7-#IVdim)
  - II7 to ii (secondary dominant resolution)
  - iii to biii° (diatonic to diminished movement)
  - vi to II7b9 (minor to altered dominant)
  - IV7 to #iv° (subdominant to diminished)
  - #ivø7 to VII7 (half-diminished to dominant)

### Phrase Length Options
- **Short**: Concise musical phrases
- **Long**: Extended musical phrases with more development

### Interactive Learning Features
- **Progressive Reveal**: Phrases initially display with the second half hidden as rests, allowing users to:
  1. View the first half of the phrase
  2. Attempt to complete the phrase themselves
  3. Reveal the full phrase to check their answer
  - This approach encourages active learning and prediction skills

- **Keyboard Navigation**: Support for keyboard shortcuts:
  - Enter/Space: Toggle between partial and full phrase view
  - Escape/Delete/Backspace: Navigate backward through screens

### Responsive Design
- Optimized for both mobile and desktop use
- Automatic orientation handling for mobile devices
- Prevents unwanted zooming and scaling for better usability

## How to Use

1. **Start**: Click "Login" on the welcome screen (no actual authentication required)
2. **Select Mode**: Choose between Random or Designate mode
3. **Select Key** (if in Designate mode): Choose from all 12 keys
4. **Select Phrase Type**: Choose from various chord progressions and phrase types
5. **Select Chord Type** (for 7sus4): Choose the specific chord quality
6. **Select Length**: Choose between short or long phrases
7. **Practice**: 
   - View the partial phrase
   - Try to predict/play the continuation
   - Click "Show Full" to reveal the complete phrase
   - Click "Generate Next" to create a new phrase

## Technical Implementation
The application uses:
- HTML5, CSS3, and JavaScript
- ABC notation for music rendering (via abcjs library)
- Custom algorithms for musical phrase generation based on bebop vocabulary
- Cell-based phrase construction mimicking jazz language patterns

## Educational Approach
The program is built on a pedagogical approach that:
- Presents idiomatic jazz language in context
- Encourages active learning through the partial-reveal mechanism
- Provides systematic exposure to different harmonic contexts
- Allows focused practice on specific progressions or comprehensive review

## Credits
Made by tsy (tungsyauy@gmail.com) 