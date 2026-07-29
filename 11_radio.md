# Micro:bit Radio

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rvymAr6WqrQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Radio lets devices send and receive messages without wires. BBC micro:bits can use radio waves to communicate with each other.

```{admonition} Documentation
:class: important
All the radio functions can be found in the **[BBC micro:bit MicroPython Radio documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html)**.
```

## How does the radio work

Imagine you and a friend are standing on opposite sides of the classroom. You each have a torch and agree on a code. By turning your torch on and off, you can send "HELLO" to your friend. They can send a message back in the same way. You have communicated without using wires.

Radio communication works in a similar way, but it uses radio waves instead of light. Radio waves are invisible. A sender changes the radio wave to carry information, and a receiver reads that information from the wave. The micro:bit handles most of this for us, so our code can focus on the message we want to send.

## Sending a message

You need at least two micro:bits to send and receive messages. Each micro:bit can be a sender, a receiver, or both.

When a micro:bit receives a message, it is placed in a message **queue**. A computer queue works like a queue of people. New messages join the end of the queue, and the oldest message is used first. The micro:bit queue has limited space. If the queue is full, new messages are ignored.

## Example

The example below shows how radio messages work. One micro:bit sends a message, and the other micro:bit displays an image. 

On two seprate micro:bits:
1. Stop and close the current **main.py** file.
2. open the **main.py** file in the **16_radio** folder in Thonny. 
   
You should see the code below:

```{literalinclude} ./python_files/16_radio/main.py
:linenos:
```

## Radio Exercise 1

On two separate micro:bits:
1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **16_radio_exercise_1** folder in Thonny.
3. Write code to move an image between two micro:bits when one micro:bit is shaken.

## Radio Exercise 2

On two separate micro:bits:
1. Stop and close the current **main.py** file. 
2. Open the **main.py** file in the **16_radio_exercise_2** folder in Thonny.
3. Write code to use the micro:bit radio feature to send a private yes or no answer.
   - Choose either **yes** or **no** and send it to another micro:bit.
   - Display the answer on the other micro:bit for half a second.
   - Use **[`radio.config`](https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html#radio.config)** to choose a group so other nearby micro:bits do not receive your message.

## Radio Exercise 3

On one micro:bit:
1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **16_radio_exercise_3/inside** folder in Thonny.
3. Write code to display the indoor temperature when button **A** is pressed.

On a differnt micro:bit:
1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **16_radio_exercise_3/outside** folder in Thonny.
3. Write code to take a temperature reading and transmit it every 5 seconds.

 Place the outside micro:bit outside and the inside micro:bit inside. When you press button **A** on the inside micro:bit, it should display the temperature reading from the inside micro:bit. When you press button **B**, it should display the outdoor temperature.