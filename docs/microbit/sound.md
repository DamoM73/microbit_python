# Sound

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/r53PjFwyAhw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The micro:bit v2 has a built-in speaker that plays tunes, tones and robotic speech, and a microphone that measures how loud it is.

Possible uses:

- game sound effects
- alarms
- talking projects
- sound-activated lights

## Connect it

The speaker and microphone are built into the micro:bit v2, so there is nothing to connect.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- The microphone is on the front of the board. The LED next to it lights up while the microphone is in use.

![microphone location](../assets/microphone.png)

## Set it up

Volume and the microphone are part of the `microbit` library. Music and speech each need their own module:

```python linenums="1"
from microbit import *
import music
import speech
```

Only import the modules your program uses.

### Writing notes

Custom tunes are lists of notes written as strings: `NOTE[octave][:duration]`

- **note** → `C` to `B`. Add `#` for sharp or `b` for flat. `R` is a rest (silence).
- **octave** → `0` (very low) to `8` (very high). Octave `4` contains middle C.
- **duration** → a higher number lasts longer. `4` lasts twice as long as `2`.

For example, `"A1:4"` is note A, octave 1, duration 4.

### Speech pitch

`speech.sing()` sets the pitch of each sound with `#` and a pitch number before the phoneme. The chart shows which pitch numbers match which notes.

![speech-pitch](../assets/speech-pitch.jpg)

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `set_volume(level)` | `level`: 0–255 | none | Sets the speaker volume |
| `music.play(music)` | `music`: built-in tune or list of notes | none | Plays a tune |
| `music.pitch(frequency, duration)` | `frequency`: Hz<br>`duration`: ms | none | Plays a tone at a frequency |
| `speech.say(words, pitch=64, speed=72)` | `words`: English string | none | Speaks English words |
| `speech.pronounce(phonemes)` | `phonemes`: phoneme string | none | Speaks exact sounds written as phonemes |
| `speech.sing(phonemes)` | `phonemes`: phonemes with pitch numbers | none | Sings phonemes at set pitches |
| `microphone.current_event()` | none | `SoundEvent` | `SoundEvent.LOUD` or `SoundEvent.QUIET` |
| `microphone.sound_level()` | none | int (0–255) | How loud the sound is |

### `set_volume()`

```python linenums="1"
--8<-- "examples/microbit/sound/set_volume/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `music` module
    - line 5 → starts an endless loop
    - line 6 → sets the volume to the loudest (`255`)
    - line 7 → plays the built-in `BA_DING` sound
    - line 8 → sets the volume much quieter (`50`)
    - line 9 → plays `BA_DING` again
    - line 10 → waits 1 second before the loop repeats

### `music.play()` — built-in tunes

The micro:bit has many [built-in tunes](https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#built-in-melodies).

```python linenums="1"
--8<-- "examples/microbit/sound/play_builtin/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `music` module
    - line 5 → starts an endless loop
    - line 6 → plays the built-in tune `NYAN`
    - line 7 → waits 500 milliseconds before the loop repeats

### `music.play()` — custom tunes

```python linenums="1"
--8<-- "examples/microbit/sound/play_custom/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `music` module
    - lines 5–8 → stores the notes of "Frère Jacques" in a list called `tune`
    - line 11 → starts an endless loop
    - line 12 → plays the notes in `tune`
    - line 13 → waits 500 milliseconds before the loop repeats

### `music.pitch()`

Plays tones that aren't musical notes, such as sirens and sound effects. `440` Hz is the note A that musicians tune to.

```python linenums="1"
--8<-- "examples/microbit/sound/pitch/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `music` module
    - line 5 → starts an endless loop
    - line 6 → steps `freq` up from `880` to `1760` in steps of `16`
    - line 7 → plays `freq` for 20 milliseconds
    - line 8 → steps `freq` back down from `1760` to `880` in steps of `-16`
    - line 9 → plays `freq` for 20 milliseconds

### `speech.say()`

Change the voice with `pitch` (higher number = lower voice) and `speed` (higher number = slower). The speech sounds robotic because it uses a simple speech synthesiser.

```python linenums="1"
--8<-- "examples/microbit/sound/say/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `speech` module
    - line 5 → starts an endless loop
    - line 6 → says "Hello world" with a slightly slower, higher voice than the default
    - line 7 → waits 1 second before the loop repeats

### `speech.pronounce()`

When `say()` doesn't sound right, write the word the way it sounds using [phonemes](https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html#phonemes). `speech.translate()` gives you a starting point to edit.

```python linenums="1"
--8<-- "examples/microbit/sound/pronounce/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `speech` module
    - line 5 → starts an endless loop
    - line 6 → speaks the phonemes for "Moreton Bay Boys' College"
    - line 7 → waits 1 second before the loop repeats

### `speech.sing()`

To make a note last longer, repeat its vowel sounds, for example `"DOWWWWWW"`.

```python linenums="1"
--8<-- "examples/microbit/sound/sing/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 2 → imports the `speech` module
    - lines 5–6 → stores the notes of a scale (doh, re, mi…) in a list. Each string is a pitch number (such as `#115`) followed by the sound to sing.
    - line 7 → joins the list into one string called `song`
    - line 10 → starts an endless loop
    - line 11 → sings `song`
    - line 12 → waits 1 second before the loop repeats

### `microphone.current_event()`

```python linenums="1"
--8<-- "examples/microbit/sound/current_event/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → checks if the sound has just changed from quiet to loud
    - line 6 → if it has, shows a big heart
    - line 7 → keeps the big heart on for 200 milliseconds
    - line 8 → if it hasn't…
    - line 9 → …shows a small heart

### `microphone.sound_level()`

```python linenums="1"
--8<-- "examples/microbit/sound/sound_level/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the sound level and stores it in `level`
    - line 6 → scrolls the sound level across the display
    - line 7 → waits 500 milliseconds before the loop repeats

## Documentation

- [BBC micro:bit MicroPython — music](https://microbit-micropython.readthedocs.io/en/v2-docs/music.html)
- [BBC micro:bit MicroPython — speech](https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html)
- [BBC micro:bit MicroPython — microphone](https://microbit-micropython.readthedocs.io/en/v2-docs/microphone.html)
- [BBC micro:bit MicroPython — set_volume](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html#microbit.set_volume)

## Exercises

Starter files are in the `sound` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#sound) page.

### Exercise 1

Starter: `sound/ex1_my_tune`

Create a program that plays your own tune.

### Exercise 2

Starter: `sound/ex2_college_song`

Create a program that sings the College Song.

### Exercise 3

Starter: `sound/ex3_sound_meter`

Light up the display based on how loud the sound is: more LEDs for louder sounds.
