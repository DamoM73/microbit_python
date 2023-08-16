# Micro:bit Radio

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rvymAr6WqrQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Radio is a way of sending and receiving messages and BBC micro:bits can use radio waves to communicate with each other.

```{admonition} Documentation
:class: important
All the sound functions can be at **[BBC micro:bit MicroPython Radio documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html)**.
```

## How does the radio work

Imagine you and a friend standing on opposite sides of the classroom. You each have a torch, and a Morse Code. By turning your torch on and off you can transmit "HELLO" to your friend using Morse Code (.... . .-.. .-.. ---). They can reply "HI" (.... ..). You have just communicated wirelessly using the electromagnetic radiation spectrum, the visible part of it we call light.

Computer wireless interaction uses radio waves, which are an invisible part of the electromagnetic radiation spectrum. In a wireless broadcast a transmitter changes one of the radio waves properties in such a way that information can be encoded. Just like turning the torch on an off change one of the properties of the light. When radio waves encounter an electrical conductor (i.e. an aerial), the information in the waves can be extracted and transformed back into its original form.

## Sending a message

You will need at least two micro:bits to send and receive messages. Each micro:bit can operate as the sender and the receiver.

When a micro:bit receives a message, it is put onto a message **queue**. Computer queues work exactly the same way as queues in real life. Items get added to the end of the queue, and the next item to be used is the item at the start of the queue. This means the 'next' item to be used is the oldest item. The micro:bit has a limited queue size. If the queue is full any new incoming messages are ignored.

## Example

Below is example code for how radios work. This code uses one micro:bit to display an emoji on a different micro:bit, so you need to have the code running on two micro:bits.

```{literalinclude} ./python_files/radio_example/main.py
:linenos:
```

## Radio Exercises

1. Teleport a duck between micro:bits when a micro:bit is shaken
2. Use micro:bit’s radio feature to answer questions in secret. 
   - Choose either a yes or no response and send it to another micro:bit to display for half a second. 
   - Use **[`radio.config`](https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html#radio.config)** to ensure no one else can read your message.
3. Use two micro:bits to display the outdoor and indoor temperatures. 
   - The **outdoor micro:bit** should take a temperature reading and transmit it very 5 seconds. 
   - The **indoor micro:bit** should display the indoor tempo when button **A** is pressed or the outside temperature when button **B** is pressed.