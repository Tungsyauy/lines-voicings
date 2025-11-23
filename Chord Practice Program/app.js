// app.js - Main application logic for the Dominant 7th Chord Practice Program

// Detect base path for GitHub Pages compatibility
// If the site is hosted at a subdirectory (e.g., /chord-practice-program/), 
// we need to include that in our paths
const getBasePath = () => {
    const path = window.location.pathname;
    // Remove trailing slash and filename to get base directory
    const basePath = path.substring(0, path.lastIndexOf('/') + 1);
    return basePath;
};

const BASE_PATH = getBasePath();
console.log('🌐 Base path detected:', BASE_PATH);

// Application state
let appState = {
    currentScreen: 'chord-type',
    selectedChordType: 'random',
    currentChord: null,
    currentKey: 'C',
    keySequences: {}, // Key sequences for each chord type
    currentSequenceKey: null, // Current chord type being used
    isListeningMode: false, // Whether we're in listening mode (audio played, waiting for show chord)
    pendingChordData: null, // Chord data waiting to be displayed
    lastAudioChordName: null // The last chord name that successfully played audio
};

// Simple test to see if JavaScript is working
console.log('🧪 JavaScript is working - app state initialized');

// Define valid key names
const validKeys = [
    // Sharp keys (use sharps in chord symbols)
    'C', 'G', 'D', 'A', 'E', 'B', 'F#',
    // Flat keys (use flats in chord symbols)  
    'F', 'Bb', 'Eb', 'Ab', 'Db'
];

// Pitch mapping for transposition
const pitchClasses = {
    "C": 0, "Db": 1, "C#": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4,
    "F": 5, "Gb": 6, "F#": 6, "G": 7, "Ab": 8, "G#": 8, "A": 9,
    "Bb": 10, "A#": 10, "B": 11
};

// Chord voicings in C (from bottom to top) - Adjusted for F4 limit
const chordVoicings = {
    'C7': ['C2', 'Bb2', '|', 'E3', 'A3', 'D4'],
    'C7sus4': ['C2', 'F2', 'Bb2', '|', 'D3', 'A3'],
    'C7#11': ['C2', 'E2', 'Bb2', '|', 'D3', 'F#3', 'A3'],
    'C7b13#9': ['C2', 'Bb2', '|', 'E3', 'Ab3', 'Eb4'],
    'C7b9': ['C2', 'Bb2', '|', 'E3', 'A3', 'C#4']
};

// Available chord types
const chordTypes = ['C7', 'C7sus4', 'C7#11', 'C7b13#9', 'C7b9'];

// Audio file mapping for all chord types
const audioFiles = {
    // X7 chords
    'A7': 'audio/A7.mp3',
    'Ab7': 'audio/Ab7.mp3',
    'B7': 'audio/B7.mp3',
    'Bb7': 'audio/Bb7.mp3',
    'C7': 'audio/C7.mp3',
    'D7': 'audio/D7.mp3',
    'Db7': 'audio/Db7.mp3',
    'E7': 'audio/E7.mp3',
    'Eb7': 'audio/Eb7.mp3',
    'F#7': 'audio/F#7.mp3',
    'F7': 'audio/F7.mp3',
    'G7': 'audio/G7.mp3',
    // X7sus4 chords
    'A7sus4': 'audio/A7sus4.mp3',
    'Ab7sus4': 'audio/Ab7sus4.mp3',
    'B7sus4': 'audio/B7sus4.mp3',
    'Bb7sus4': 'audio/Bb7sus4.mp3',
    'C7sus4': 'audio/C7sus4.mp3',
    'D7sus4': 'audio/D7sus4.mp3',
    'Db7sus4': 'audio/Db7sus4.mp3',
    'E7sus4': 'audio/E7sus4.mp3',
    'Eb7sus4': 'audio/Eb7sus4.mp3',
    'F#7sus4': 'audio/F#7sus4.mp3',
    'F7sus4': 'audio/F7sus4.mp3',
    'G7sus4': 'audio/G7sus4.mp3',
    // X7#11 chords
    'A7#11': 'audio/A7#11.mp3',
    'Ab7#11': 'audio/Ab7#11.mp3',
    'B7#11': 'audio/B7#11.mp3',
    'Bb7#11': 'audio/Bb7#11.mp3',
    'C7#11': 'audio/C7#11.mp3',
    'D7#11': 'audio/D7#11.mp3',
    'Db7#11': 'audio/Db7#11.mp3',
    'E7#11': 'audio/E7#11.mp3',
    'Eb7#11': 'audio/Eb7#11.mp3',
    'F#7#11': 'audio/F#7#11.mp3',
    'F7#11': 'audio/F7#11.mp3',
    'G7#11': 'audio/G7#11.mp3',
    // X7b13#9 chords
    'A7b13#9': 'audio/A7b13#9.mp3',
    'Ab7b13#9': 'audio/Ab7b13#9.mp3',
    'B7b13#9': 'audio/B7b13#9.mp3',
    'Bb7b13#9': 'audio/Bb7b13#9.mp3',
    'C7b13#9': 'audio/C7b13#9.mp3',
    'D7b13#9': 'audio/D7b13#9.mp3',
    'Db7b13#9': 'audio/Db7b13#9.mp3',
    'E7b13#9': 'audio/E7b13#9.mp3',
    'Eb7b13#9': 'audio/Eb7b13#9.mp3',
    'F#7b13#9': 'audio/F#7b13#9.mp3',
    'F7b13#9': 'audio/F7b13#9.mp3',
    'G7b13#9': 'audio/G7b13#9.mp3',
    // X7b9 chords
    'A7b9': 'audio/A7b9.mp3',
    'Ab7b9': 'audio/Ab7b9.mp3',
    'B7b9': 'audio/B7b9.mp3',
    'Bb7b9': 'audio/Bb7b9.mp3',
    'C7b9': 'audio/C7b9.mp3',
    'D7b9': 'audio/D7b9.mp3',
    'Db7b9': 'audio/Db7b9.mp3',
    'E7b9': 'audio/E7b9.mp3',
    'Eb7b9': 'audio/Eb7b9.mp3',
    'F#7b9': 'audio/F#7b9.mp3',
    'F7b9': 'audio/F7b9.mp3',
    'G7b9': 'audio/G7b9.mp3'
};

// Verify audioFiles object is loaded
console.log('🎵 Audio files loaded. Total entries:', Object.keys(audioFiles).length);
console.log('🎵 Sample keys:', Object.keys(audioFiles).slice(0, 5));
console.log('🎵 F7b9 in audioFiles:', 'F7b9' in audioFiles, audioFiles['F7b9']);

// Fisher-Yates shuffle algorithm
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

// Generate a new shuffled sequence of keys for a specific chord type
function generateNewKeySequence(chordType) {
    const sequenceKey = chordType || 'default';
    appState.keySequences[sequenceKey] = {
        sequence: shuffleArray(validKeys),
        index: 0
    };
    console.log(`🎲 Generated new key sequence for ${sequenceKey}:`, appState.keySequences[sequenceKey].sequence);
}

// Get the next key from the sequence for the current chord type
function getNextKey(chordType) {
    const sequenceKey = chordType || 'default';
    
    // If we don't have a sequence for this chord type or reached the end, generate a new one
    if (!appState.keySequences[sequenceKey] || 
        appState.keySequences[sequenceKey].index >= appState.keySequences[sequenceKey].sequence.length) {
        generateNewKeySequence(sequenceKey);
    }
    
    const sequence = appState.keySequences[sequenceKey];
    const nextKey = sequence.sequence[sequence.index];
    sequence.index++;
    
    console.log(`🎯 Next key from sequence for ${sequenceKey}: ${nextKey} (${sequence.index}/${sequence.sequence.length})`);
    return nextKey;
}

// Play audio for a chord if available
function playChordAudio(chordName) {
    console.log('🎵 Attempting to play audio for:', chordName);
    console.log('🎵 audioFiles object exists:', typeof audioFiles !== 'undefined');
    console.log('🎵 Looking for key in audioFiles:', chordName);
    console.log('🎵 Available keys in audioFiles:', Object.keys(audioFiles).slice(0, 10), '...');
    console.log('🎵 audioFiles[chordName]:', audioFiles[chordName]);
    
    if (audioFiles[chordName]) {
        const audio = document.getElementById('chord-audio');
        if (!audio) {
            console.warn('🎵 Audio element not found');
            return;
        }

        // Stop any current playback and clear previous source
        audio.pause();
        audio.currentTime = 0;
        
        // Construct full path with base path for GitHub Pages compatibility
        const audioPath = audioFiles[chordName];
        // Combine base path with audio path (base path already ends with /)
        const fullPath = BASE_PATH + audioPath;
        // Encode the URL properly (especially for F#7 which has # in filename)
        // Replace # with %23 in the path (needed for F#7.mp3, F#7#11.mp3, etc.)
        const encodedPath = fullPath.replace(/#/g, '%23');
        console.log('🎵 Loading audio from:', encodedPath);
        
        // Set up event handlers
        const onCanPlay = () => {
            console.log('🎵 Audio file loaded and ready:', encodedPath);
            appState.lastAudioChordName = chordName;
            updatePlayAgainButtonState();
            
            // Play the audio
            const playPromise = audio.play();
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    console.log('🎵 Audio playing successfully for:', chordName);
                }).catch(error => {
                    console.error('❌ Error playing audio:', error);
                    console.log('🔇 Audio failed to play, but still waiting for Show Chord click');
                });
            }
        };
        
        const onError = (event) => {
            console.error('❌ Error loading audio file:', encodedPath);
            console.error('Error details:', event);
            console.error('Audio element state:', {
                src: audio.src,
                networkState: audio.networkState,
                readyState: audio.readyState,
                error: audio.error
            });
            console.log('🔇 Audio failed to load, but still waiting for Show Chord click');
            appState.lastAudioChordName = null;
            updatePlayAgainButtonState();
        };
        
        // Remove any existing listeners first (cleanup)
        // Create wrapper functions to ensure we can remove the exact same function reference
        const wrappedOnCanPlay = onCanPlay;
        const wrappedOnError = onError;
        
        // Clear previous source and wait a tiny bit before setting new one
        audio.src = '';
        
        // Use setTimeout to ensure the previous source is fully cleared
        setTimeout(() => {
            // Set up new event listeners (using once: true for automatic cleanup)
            audio.addEventListener('canplaythrough', wrappedOnCanPlay, { once: true });
            audio.addEventListener('loadeddata', wrappedOnCanPlay, { once: true }); // Fallback for faster loading
            audio.addEventListener('error', wrappedOnError, { once: true });
            
            // Set the source - this will trigger loading
            audio.src = encodedPath;
            console.log('🎵 Set audio src to:', audio.src);
            
            // Explicitly trigger loading
            try {
                audio.load();
                console.log('🎵 Called audio.load()');
            } catch (e) {
                console.warn('Warning during audio.load():', e);
            }
        }, 10); // Small delay to ensure previous source is cleared
    } else {
        console.log('🔇 No audio file available for:', chordName, '- but still waiting for Show Chord click');
        appState.lastAudioChordName = null;
        updatePlayAgainButtonState();
    }
}

function updatePlayAgainButtonState() {
    const playAgainBtn = document.getElementById('play-again-btn');
    if (!playAgainBtn) {
        return;
    }

    if (appState.lastAudioChordName && audioFiles[appState.lastAudioChordName]) {
        playAgainBtn.disabled = false;
    } else {
        playAgainBtn.disabled = true;
    }
}

// Show the pending chord (called after audio or immediately if no audio)
function showPendingChord() {
    if (appState.pendingChordData) {
        const { chordName, selectedChordType } = appState.pendingChordData;
        
        // Display the chord
        displayChord(chordName, selectedChordType);
        
        // Reset listening mode
        appState.isListeningMode = false;
        appState.pendingChordData = null;
        
        // Reset button text
        const generateBtn = document.getElementById('generate-chord-btn');
        if (generateBtn) {
            generateBtn.textContent = 'Generate Chord';
        }
        
        console.log('📋 Chord displayed:', chordName);
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    preventZoomAndScaling();
});

// Comprehensive zoom and scaling prevention
function preventZoomAndScaling() {
    // Prevent pinch zoom on the entire document
    document.addEventListener('touchstart', function(event) {
        if (event.touches.length > 1) {
            event.preventDefault();
        }
    }, { passive: false });

    document.addEventListener('touchmove', function(event) {
        if (event.touches.length > 1) {
            event.preventDefault();
        }
    }, { passive: false });

    document.addEventListener('touchend', function(event) {
        if (event.touches.length > 1) {
            event.preventDefault();
        }
    }, { passive: false });

    // Prevent double-tap zoom
    let lastTouchEnd = 0;
    document.addEventListener('touchend', function(event) {
        const now = (new Date()).getTime();
        if (now - lastTouchEnd <= 300) {
            event.preventDefault();
        }
        lastTouchEnd = now;
    }, { passive: false });

    // Prevent zoom with keyboard shortcuts
    document.addEventListener('keydown', function(event) {
        if ((event.ctrlKey || event.metaKey) && (event.key === '+' || event.key === '-' || event.key === '0')) {
            event.preventDefault();
        }
    });

    // Prevent context menu on long press
    document.addEventListener('contextmenu', function(event) {
        event.preventDefault();
    });
}

function initializeApp() {
    setupEventListeners();
    showScreen('chord-type');
    updatePlayAgainButtonState();
}

function setupEventListeners() {
    // Chord type selection is now the first screen

    // Chord type selection
    document.getElementById('random-btn').addEventListener('click', () => {
        appState.selectedChordType = 'random';
        showScreen('chord-practice');
        generateChord();
    });

    document.getElementById('c7-btn').addEventListener('click', () => {
        appState.selectedChordType = 'C7';
        showScreen('chord-practice');
        generateChord();
    });

    document.getElementById('c7sus4-btn').addEventListener('click', () => {
        appState.selectedChordType = 'C7sus4';
        showScreen('chord-practice');
        generateChord();
    });

    document.getElementById('c7sharp11-btn').addEventListener('click', () => {
        appState.selectedChordType = 'C7#11';
        showScreen('chord-practice');
        generateChord();
    });

    document.getElementById('c7b13sharp9-btn').addEventListener('click', () => {
        appState.selectedChordType = 'C7b13#9';
        showScreen('chord-practice');
        generateChord();
    });

    document.getElementById('c7b9-btn').addEventListener('click', () => {
        appState.selectedChordType = 'C7b9';
        showScreen('chord-practice');
        generateChord();
    });

    // Return arrows - chord-type-return now goes to main page via HTML link

    document.getElementById('chord-practice-return').addEventListener('click', () => {
        showScreen('chord-type');
    });

    // Chord practice controls
    document.getElementById('generate-chord-btn').addEventListener('click', generateChord);

    const playAgainBtn = document.getElementById('play-again-btn');
    if (playAgainBtn) {
        playAgainBtn.addEventListener('click', () => {
            if (appState.lastAudioChordName) {
                playChordAudio(appState.lastAudioChordName);
            }
        });
    }
}

function showScreen(screenName) {
    // Hide all screens
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.add('hidden');
    });
    
    // Show the requested screen
    const targetScreen = document.getElementById(`${screenName}-screen`);
    if (targetScreen) {
        targetScreen.classList.remove('hidden');
        appState.currentScreen = screenName;
        
        // If showing chord practice screen, ensure it's clean
        if (screenName === 'chord-practice') {
            console.log('🎯 Showing chord practice screen');
            const chordDisplay = document.getElementById('chord-display');
            const notation = document.getElementById('notation');
            if (chordDisplay) chordDisplay.textContent = 'Click "Generate Chord" to start';
            if (notation) notation.innerHTML = '';
            appState.lastAudioChordName = null;
            updatePlayAgainButtonState();
        }
    }
}

function generateChord() {
    const generateBtn = document.getElementById('generate-chord-btn');
    
    // If we're in listening mode, this click means "Show Chord"
    if (appState.isListeningMode) {
        console.log('🎯 Show Chord button clicked');
        showPendingChord();
        return;
    }
    
    console.log('🎯 Generate Chord button clicked');
    
    // Select chord type first
    let selectedChordType;
    if (appState.selectedChordType === 'random') {
        selectedChordType = chordTypes[Math.floor(Math.random() * chordTypes.length)];
    } else {
        selectedChordType = appState.selectedChordType;
    }
    
    // Get the next key from the shuffled sequence for this chord type
    const nextKey = getNextKey(selectedChordType);
    appState.currentKey = nextKey;
    
    // Create chord name with current key
    const chordName = selectedChordType.replace('C', appState.currentKey);
    
    // Store current chord
    appState.currentChord = {
        type: selectedChordType,
        name: chordName,
        key: appState.currentKey
    };
    
    // 按照要求：和弦不会立即显示，先清空显示
    document.getElementById('chord-display').textContent = 'Listen to the chord...';
    document.getElementById('notation').innerHTML = '';
    
    // Store chord data for later display
    appState.pendingChordData = { chordName, selectedChordType };
    
    // 按照要求：先播放音频，然后按钮变为Show Chord
    playChordAudio(chordName);
    
    // 按照要求：按钮变为Show Chord
    appState.isListeningMode = true;
    generateBtn.textContent = 'Show Chord';
    console.log('🎵 Audio played, waiting for Show Chord click for:', chordName);
}


function transposeNote(note, semitones, key, chordType = null, isRightHand = false) {
    const pitch = note.slice(0, -1);
    const octave = parseInt(note.slice(-1));
    const pitchClass = pitchClasses[pitch];
    
    // Handle invalid notes
    if (pitchClass === undefined || isNaN(octave)) {
        console.error('Invalid note in transposeNote:', note);
        return note;
    }
    
    // Fix JavaScript modulo behavior for negative numbers
    const newPitch = ((pitchClass + semitones) % 12 + 12) % 12;
    const newOctave = octave + Math.floor((pitchClass + semitones) / 12);
    
    // Use key-aware note representation with chord type consideration
    const preferredNoteName = getNoteRepresentation(newPitch, key, chordType, isRightHand);
    
    return `${preferredNoteName}${newOctave}`;
}

function transposeChord(notes, semitones, key, chordType = null) {
    let isRightHand = false;
    return notes.map(note => {
        if (note === '|') {
            isRightHand = true; // After separator, we're in right hand territory
            return note;
        }
        return transposeNote(note, semitones, key, chordType, isRightHand);
    });
}

// Key-based note representation system
const PITCH_CLASSES_SHARP = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
                             6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"};
const PITCH_CLASSES_FLAT = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
                            6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"};
const FLAT_KEYS = new Set(["Db", "Ab", "Eb", "Bb", "F"]);
const SHARP_KEYS = new Set(["F#", "B", "E", "A", "D", "G", "C"]);

// Get the appropriate note representation based on key and chord type (Enhanced from Messiaen)
function getNoteRepresentation(pitchClass, key, chordType = null, isRightHand = false) {
    console.log(`🔍 getNoteRepresentation called with: pitchClass=${pitchClass}, key=${key}, chordType=${chordType}, isRightHand=${isRightHand}`);
    
    // Special rule for B7#11 and F#7#11 - use flats ONLY for right hand notes
    if (chordType === 'C7#11' && (key === 'B' || key === 'F#') && isRightHand) {
        console.log(`🎯 Special rule: ${key}7#11 chord - using flats for RIGHT HAND only`);
        return PITCH_CLASSES_FLAT[pitchClass];
    }
    
    // Special rules for 7b9 chords - right hand notation preferences
    if (chordType === 'C7b9' && isRightHand) {
        if (key === 'F' || key === 'G') {
            console.log(`🎯 Special rule: ${key}7b9 chord - using sharps for RIGHT HAND only`);
            return PITCH_CLASSES_SHARP[pitchClass];
        } else if (key === 'F#' || key === 'E' || key === 'B') {
            console.log(`🎯 Special rule: ${key}7b9 chord - using flats for RIGHT HAND only`);
            return PITCH_CLASSES_FLAT[pitchClass];
        }
    }
    
    // Special rules for dominant 7th chords based on chord type
    if (chordType === 'C7' || chordType === 'C7sus4' || chordType === 'C7#11') {
        // Regular dominant chords: use standard key-based logic
        if (FLAT_KEYS.has(key)) {
            return PITCH_CLASSES_FLAT[pitchClass];
        } else if (SHARP_KEYS.has(key)) {
            return PITCH_CLASSES_SHARP[pitchClass];
        }
    } else if (chordType === 'C7b13#9' || chordType === 'C7b9') {
        // Altered dominant chords: prefer flats for altered tensions
        const alteredFlatKeys = new Set(["Db", "Ab", "Eb", "Bb", "F", "C", "G"]);
        const alteredSharpKeys = new Set(["D", "A", "E", "B", "F#"]);
        
        if (alteredFlatKeys.has(key)) {
            return PITCH_CLASSES_FLAT[pitchClass];
        } else if (alteredSharpKeys.has(key)) {
            return PITCH_CLASSES_SHARP[pitchClass];
        }
    }
    
    // Fallback to regular key-aware logic
    if (FLAT_KEYS.has(key)) {
        return PITCH_CLASSES_FLAT[pitchClass];
    } else if (SHARP_KEYS.has(key)) {
        return PITCH_CLASSES_SHARP[pitchClass];
    } else {
        // Default to sharps for unknown keys
        return PITCH_CLASSES_SHARP[pitchClass];
    }
}

// Note to pitch conversion
function noteToPitch(note) {
    const pitchClasses = {
        "C": 0, "Db": 1, "C#": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4,
        "F": 5, "Gb": 6, "F#": 6, "G": 7, "Ab": 8, "G#": 8, "A": 9,
        "Bb": 10, "A#": 10, "B": 11
    };
    
    // Validate the note input
    if (!note || typeof note !== 'string') {
        console.error('Invalid note input:', note);
        return [undefined, undefined];
    }
    
    const name = note.slice(0, -1);
    const octaveStr = note.slice(-1);
    const octave = parseInt(octaveStr);
    
    // Validate the note name and octave
    if (!(name in pitchClasses)) {
        console.error('Invalid note name:', name, 'in note:', note);
        return [undefined, undefined];
    }
    
    if (isNaN(octave)) {
        console.error('Invalid octave:', octaveStr, 'in note:', note);
        return [undefined, undefined];
    }
    
    return [pitchClasses[name], octave];
}

// Octave limit constants (B1 to F4 range) - Modified for right hand limit
const D2_PITCH = 11 + (1 * 12); // B1 = 23
const F4_PITCH = 5 + (4 * 12); // F4 = 53 (new right hand limit)

// Left hand (bass clef) range constraints (B1 to G#3)
const LEFT_HAND_LOW = 11 + (1 * 12); // B1 = 23
const LEFT_HAND_HIGH = 8 + (3 * 12); // G#3 = 44

// Check if left hand (bass clef) part is within required range (B1 to G#3)
function isLeftHandInRange(chord) {
    // Find the separator to identify left hand notes
    const separatorIndex = chord.indexOf('|');
    if (separatorIndex === -1) {
        // No separator means this is not a dual-staff chord, so no left hand constraint
        return true;
    }
    
    // Get left hand notes (before the separator)
    const leftHandNotes = chord.slice(0, separatorIndex);
    
    for (const note of leftHandNotes) {
        const [pitchClass, octave] = noteToPitch(note);
        if (pitchClass === undefined || octave === undefined) continue;
        
        const absolutePitch = pitchClass + (octave * 12);
        if (absolutePitch < LEFT_HAND_LOW || absolutePitch > LEFT_HAND_HIGH) {
            return false;
        }
    }
    
    return true;
}

// Check if chord is within comfortable reading range (B1 to F4)
function isChordInRange(chord) {
    for (const note of chord) {
        if (note === '|') continue; // Skip separator
        
        const [pitchClass, octave] = noteToPitch(note);
        if (pitchClass === undefined || octave === undefined) {
            continue;
        }
        const absolutePitch = pitchClass + (octave * 12);
        
        if (absolutePitch < D2_PITCH || absolutePitch > F4_PITCH) {
            return false;
        }
    }
    return true;
}

// Automatically adjust chord octave if it's too high or too low
function adjustChordOctave(chord, key, chordType = null) {
    console.log('Adjusting chord octave for:', chord);
    
    let currentChord = [...chord];
    let totalOctaveShift = 0;
    let maxAttempts = 5; // Prevent infinite loops
    let attempts = 0;
    
    while (attempts < maxAttempts) {
        attempts++;
        console.log(`Adjustment attempt ${attempts}:`, currentChord);
        
        // Check if any note is out of range
        let hasHighNotes = false;
        let hasLowNotes = false;
        let hasLeftHandRangeIssues = false;
        
        for (const note of currentChord) {
            if (note === '|') continue; // Skip separator
            
            const [pitchClass, octave] = noteToPitch(note);
            if (pitchClass === undefined || octave === undefined) continue;
            
            const absolutePitch = pitchClass + (octave * 12);
            if (absolutePitch > F4_PITCH) {
                hasHighNotes = true;
            }
            if (absolutePitch < D2_PITCH) {
                hasLowNotes = true;
            }
        }
        
        // Check left hand range constraint for dual-staff chords
        if (currentChord.includes('|')) {
            if (!isLeftHandInRange(currentChord)) {
                hasLeftHandRangeIssues = true;
            }
        }
        
        // If all notes are in range and all constraints are satisfied, we're done
        if (!hasHighNotes && !hasLowNotes && !hasLeftHandRangeIssues) {
            if (totalOctaveShift === 0) {
                console.log('No octave adjustment needed - chord is already in range');
            } else {
                console.log(`Final adjustment complete: total shift = ${totalOctaveShift} octave(s)`);
            }
            return currentChord;
        }
        
        // Determine octave shift based on out-of-range notes
        let octaveShift = 0;
        if (hasHighNotes) {
            octaveShift = -1;
            console.log(`Attempt ${attempts}: Chord has high notes, transposing down 1 octave`);
        } else if (hasLowNotes) {
            octaveShift = 1;
            console.log(`Attempt ${attempts}: Chord has low notes, transposing up 1 octave`);
        } else if (hasLeftHandRangeIssues) {
            // Check if left hand is too high or too low
            const separatorIndex = currentChord.indexOf('|');
            if (separatorIndex !== -1) {
                const leftHandNotes = currentChord.slice(0, separatorIndex);
                let leftHandTooHigh = false;
                let leftHandTooLow = false;
                
                for (const note of leftHandNotes) {
                    const [pitchClass, octave] = noteToPitch(note);
                    if (pitchClass === undefined || octave === undefined) continue;
                    
                    const absolutePitch = pitchClass + (octave * 12);
                    if (absolutePitch > LEFT_HAND_HIGH) {
                        leftHandTooHigh = true;
                    } else if (absolutePitch < LEFT_HAND_LOW) {
                        leftHandTooLow = true;
                    }
                }
                
                if (leftHandTooHigh) {
                    octaveShift = -1;
                    console.log(`Attempt ${attempts}: Left hand too high, transposing down 1 octave`);
                } else if (leftHandTooLow) {
                    octaveShift = 1;
                    console.log(`Attempt ${attempts}: Left hand too low, transposing up 1 octave`);
                }
            }
        }
        
        // Apply octave shift
        let isRightHandInAdjust = false;
        currentChord = currentChord.map(note => {
            if (note === '|') {
                isRightHandInAdjust = true;
                return note;
            }
            
            const [pitchClass, octave] = noteToPitch(note);
            if (pitchClass === undefined || octave === undefined) return note;
            
            const newOctave = octave + octaveShift;
            
            // Use key-aware note representation
            const pitchName = getNoteRepresentation(pitchClass, key, chordType, isRightHandInAdjust);
            
            return `${pitchName}${newOctave}`;
        });
        
        totalOctaveShift += octaveShift;
        console.log(`After attempt ${attempts}:`, currentChord);
    }
    
    // If we exceeded max attempts, return the best we could do
    console.warn(`Warning: Exceeded maximum octave adjustment attempts (${maxAttempts}). Returning best result.`);
    return currentChord;
}

// Fix enharmonic conflicts (same pitch, different names) within the same octave
function fixEnharmonicConflictsEnhanced(chord, key = "C", chordType = null) {
    console.log(`Enhanced letter name conflict check for chord in key ${key}:`, chord);
    
    // Group notes by octave
    const notesByOctave = {};
    chord.forEach(note => {
        if (note === '|') return; // Skip separator
        
        const [pitchClass, octave] = noteToPitch(note);
        if (pitchClass !== undefined && octave !== undefined) {
            const letterName = note[0]; // Extract letter name (C, D, E, F, G, A, B)
            if (!notesByOctave[octave]) notesByOctave[octave] = [];
            notesByOctave[octave].push({ note, pitchClass, letterName });
        }
    });
    
    // Check each octave for conflicts
    let hasConflicts = false;
    let isRightHandInFix = false;
    const fixedChord = chord.map(note => {
        if (note === '|') {
            isRightHandInFix = true;
            return note;
        }
        
        const [pitchClass, octave] = noteToPitch(note);
        if (pitchClass === undefined || octave === undefined) return note;
        
        const letterName = note[0];
        const sameOctaveNotes = notesByOctave[octave] || [];
        
        // Look for letter name conflicts in the same octave
        const conflictingNote = sameOctaveNotes.find(n => 
            n.letterName === letterName && n.note !== note
        );
        
        if (conflictingNote) {
            hasConflicts = true;
            console.log(`Letter name conflict detected: ${note} and ${conflictingNote.note} both use letter '${letterName}' in octave ${octave}`);
            
            // Use key-aware note representation
            const preferredNoteName = getNoteRepresentation(pitchClass, key, chordType, isRightHandInFix);
            const alternative = preferredNoteName + octave;
            
            console.log(`Converting ${note} to ${alternative} (key-aware representation for ${key})`);
            return alternative;
        }
        
        // Also check for exact pitch class conflicts (enharmonic equivalents)
        const enharmonicConflict = sameOctaveNotes.find(n => 
            n.pitchClass === pitchClass && n.note !== note
        );
        
        if (enharmonicConflict) {
            hasConflicts = true;
            console.log(`Enharmonic conflict detected: ${note} and ${enharmonicConflict.note} are the same pitch in octave ${octave}`);
            
            // Use key-aware note representation
            const preferredNoteName = getNoteRepresentation(pitchClass, key, chordType, isRightHandInFix);
            const alternative = preferredNoteName + octave;
            
            console.log(`Converting ${note} to ${alternative} (key-aware representation for ${key})`);
            return alternative;
        }
        
        return note;
    });
    
    if (hasConflicts) {
        console.log(`Fixed conflicts using ${key} key preferences:`, fixedChord);
    } else {
        console.log('No conflicts found');
    }
    
    return fixedChord;
}

// Draw staff function with proper ABC.js rendering
function drawStaff(notes) {
    // Clear previous content
    const notationDiv = document.getElementById('notation');
    notationDiv.innerHTML = '';
    
    // Check if this chord has hand separation
    const hasHandSeparation = notes.includes('|');
    
    if (hasHandSeparation) {
        // Split notes into left and right hand
        const separatorIndex = notes.indexOf('|');
        const leftHandNotes = notes.slice(0, separatorIndex);
        const rightHandNotes = notes.slice(separatorIndex + 1);
        
        // Convert notes to ABC format
        const leftHandABC = convertToABCWithAccidentals(leftHandNotes);
        const rightHandABC = convertToABCWithAccidentals(rightHandNotes);
        
        console.log(`🎼 Original notes:`, notes);
        console.log(`🎼 Left hand (bass):`, leftHandNotes);
        console.log(`🎼 Right hand (treble):`, rightHandNotes);
        console.log(`🎼 Left hand ABC:`, leftHandABC);
        console.log(`🎼 Right hand ABC:`, rightHandABC);
        
        // Create ABC notation with two staves
        const abcNotation = `X:1
L:1/4
K:C
V:1 clef=treble
[${rightHandABC.join('')}]4
V:2 clef=bass
[${leftHandABC.join('')}]4`;
        
        console.log(`🎼 ABC notation:`, abcNotation);
        
        // Render with ABC.js
        try {
            ABCJS.renderAbc(notationDiv, abcNotation, {
                responsive: "resize",
                scale: 1.0,
                staffwidth: 450,
                paddingleft: 15,
                paddingright: 15,
                paddingtop: 15,
                paddingbottom: 15,
                viewportHorizontal: true,
                viewportVertical: true,
                add_classes: true,
                format: {
                    titlefont: "serif 14",
                    gchordfont: "serif 10",
                    vocalfont: "serif 11",
                    annotationfont: "serif 10",
                    historyfont: "serif 14",
                    infofont: "serif 10",
                    measurefont: "serif 10",
                    partsfont: "serif 10",
                    repeatfont: "serif 10",
                    textfont: "serif 10",
                    voicefont: "serif 10",
                    wordsfont: "serif 10"
                },
                wrap: {
                    minSpacing: 1.6,
                    maxSpacing: 2.4,
                    preferredMeasuresPerLine: 16
                }
            });
            
            console.log(`✅ ABC.js rendered successfully with two staves`);
            console.log(`Staff drawn successfully with notes:`, notes);
            
            // Apply post-render styling for two-staff chords
            setTimeout(() => {
                const svg = notationDiv.querySelector('svg');
                if (svg) {
                    // Keep two-staff chords centered
                    svg.style.marginLeft = 'auto';
                    svg.style.marginRight = 'auto';
                    svg.style.display = 'block';
                    svg.style.float = 'none';
                    
                    // Apply the white filter
                    svg.style.filter = 'brightness(0) invert(1) drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3))';
                    
                    console.log('🎯 Two-staff chord staff styled!');
                }
            }, 100);
        } catch (error) {
            console.error(`❌ Error rendering ABC:`, error);
            notationDiv.innerHTML = `<p style="color: red;">Error rendering staff: ${error.message}</p>`;
        }
    } else {
        // Single staff rendering (if needed for future chord types)
        const abcNotes = convertToABCWithAccidentals(notes);
        
        const abcNotation = `X:1
L:1/4
K:C
V:1 clef=treble
[${abcNotes.join('')}]4`;
        
        try {
            ABCJS.renderAbc(notationDiv, abcNotation, {
                responsive: "resize",
                scale: 1.0,
                staffwidth: 450,
                paddingleft: 15,
                paddingright: 15,
                paddingtop: 15,
                paddingbottom: 15,
                viewportHorizontal: true,
                viewportVertical: true,
                add_classes: true
            });
            
            setTimeout(() => {
                const svg = notationDiv.querySelector('svg');
                if (svg) {
                    svg.style.filter = 'brightness(0) invert(1) drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3))';
                }
            }, 100);
        } catch (error) {
            console.error(`❌ Error rendering ABC:`, error);
            notationDiv.innerHTML = `<p style="color: red;">Error rendering staff: ${error.message}</p>`;
        }
    }
}

// Convert notes to ABC notation with proper accidental handling
function convertToABCWithAccidentals(notes) {
    const accidentalState = {}; // Track accidentals by pitch class AND octave
    
    return notes.map(note => {
        // Skip separator characters
        if (note === '|') {
            return null;
        }
        
        const noteName = note.slice(0, -1);
        const octave = parseInt(note.slice(-1));
        
        const pitchClass = noteName[0]; // Base pitch class (C, D, E, F, G, A, B)
        const currentAccidental = noteName.length > 1 ? noteName[1] : null;
        
        // Create key that includes both pitch class and octave
        const accidentalKey = `${pitchClass}${octave}`;
        
        let baseNote = pitchClass.toLowerCase();
        let accidentalSymbol = "";
        
        // Determine what accidental symbol to use based on current state
        if (currentAccidental === "#") {
            if (accidentalState[accidentalKey] !== "#") {
                accidentalSymbol = "^"; // Sharp
                accidentalState[accidentalKey] = "#";
            }
        } else if (currentAccidental === "b") {
            if (accidentalState[accidentalKey] !== "b") {
                accidentalSymbol = "_"; // Flat
                accidentalState[accidentalKey] = "b";
            }
        } else {
            // Natural note - only add natural sign if we need to cancel a previous accidental
            if (accidentalState[accidentalKey] === "#" || accidentalState[accidentalKey] === "b") {
                accidentalSymbol = "="; // Natural (cancels previous accidental)
                accidentalState[accidentalKey] = "natural";
            }
        }
        
        // Apply accidental symbol
        if (accidentalSymbol) {
            baseNote = accidentalSymbol + baseNote;
        }
        
        // Handle octaves relative to octave 4 (middle octave in ABC)
        if (octave >= 5) {
            // Higher octaves use apostrophes
            const apostrophes = "'".repeat(octave - 4);
            baseNote = baseNote + apostrophes;
        } else if (octave === 4) {
            // Octave 4 stays as is (lowercase)
            baseNote = baseNote;
        } else if (octave === 3) {
            // Octave 3 uses uppercase
            baseNote = baseNote.toUpperCase();
        } else if (octave <= 2) {
            // Lower octaves use commas
            baseNote = baseNote.toUpperCase();
            const commas = ",".repeat(3 - octave);
            baseNote = baseNote + commas;
        }
        
        return baseNote;
    }).filter(note => note !== null); // Remove null values (separators)
}

// Function to display a chord
function displayChord(chordName, chordType) {
    console.log('🎯 Displaying chord:', chordName, 'Type:', chordType);
    
    // Get the original voicing in C
    const originalVoicing = chordVoicings[chordType];
    if (!originalVoicing) {
        console.error('No original voicing found for chord type:', chordType);
        return;
    }
    
    // Calculate transposition semitones
    const transpositionSemitones = pitchClasses[appState.currentKey];
    if (transpositionSemitones === undefined) {
        console.error('Invalid key for transposition:', appState.currentKey);
        return;
    }
    
    // Transpose the voicing
    let transposedVoicing;
    if (appState.currentKey === 'C') {
        transposedVoicing = [...originalVoicing];
    } else {
        transposedVoicing = transposeChord(originalVoicing, transpositionSemitones, appState.currentKey, chordType);
    }
    
    // Apply intelligent octave adjustment if needed (with Messiaen-style range constraints)
    const octaveAdjustedVoicing = adjustChordOctave(transposedVoicing, appState.currentKey, chordType);
    
    // Fix enharmonic conflicts within the same octave (Messiaen-style)
    const enharmonicFixedVoicing = fixEnharmonicConflictsEnhanced(octaveAdjustedVoicing, appState.currentKey, chordType);
    
    // Display results
    document.getElementById('chord-display').textContent = chordName;
    
    // Draw the chord on staff
    drawStaff(enharmonicFixedVoicing);
    
    console.log('Final voicing:', enharmonicFixedVoicing);
}
