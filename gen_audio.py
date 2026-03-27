import os
from openai import OpenAI

client = OpenAI()

letter_text = """Dear Trish.

I have started this letter a hundred times in my head. On the quiet mornings when the world is still and the grief sits down beside me like it always does. On the hard days when everything feels like too much. On the days when I pick up my phone just to hear your voice and remember that somebody out there truly understands. Every time I tried to find the right words, I came back to the same truth — there are no perfect words for what we carry. But there is something between us that does not need perfect words. It just needs to be said.

I hate how we met. I need you to know that. I hate it with everything in me. Two mommas — one in Tennessee, one in New Hampshire — and the thing that brought us together was the worst thing either of us has ever survived. Child loss. The kind of grief that does not have a name big enough to hold it. The kind that changes the shape of everything — your mornings, your breathing, the way a song hits you, the way you look at a photograph, the way you wake up and for one half-second forget, and then remember again. We did not sign up for this. We did not choose this sorority. We would choose our children over anything, over everything, without a single hesitation. We would trade every friendship, every good thing, every blessing — just to have them back. And that is something only another angel momma truly understands.

But here we are. And here is what I know with everything I have: God did not put you in my path by accident. Out of all the people in this world, He gave me you. A woman who does not flinch from the pain. A woman who says their names without being asked. A woman who shows up from New Hampshire when people right here in Tennessee have not. That is not a coincidence. That is grace.

Lucas. Ryan. Our boys. Gone from our arms but never — not for one single second — gone from our hearts. Lucas, my son, who left a hole in this world that nothing will ever fill. And Ryan, your son — twenty-four years old, and always, always your baby. That is what people who have not lost a child do not understand. They think the age changes the grief. It does not. A mother's love does not have an expiration date. It does not shrink with the years. It does not care how tall they grew or how old they got. He was yours from his very first breath, and he is yours still. From feet to wings too soon. That is what it is. That is what it will always be.

And yet — here we are. Still standing. Still breathing. Still showing up for each other. Only one call away.

You have been that call for me, Trish. On the days when the weight of everything comes crashing back — the grief, the business, the surgery, the fight, all of it piling up at once — you are the one I know I can reach. You do not try to fix it. You do not tell me it gets easier. You just show up. You sit in it with me. And that is the rarest, most precious thing one human being can do for another. I hope you know — from the bottom of everything I have — that I am that call for you too. Tennessee to New Hampshire. States apart. It does not matter. We show up. We always have. We always will.

This is not the friendship either of us would have chosen. We would have chosen our boys. We would choose them every time. But since we are here — since we are in this sorority neither of us ever wanted to join — I am grateful, deeply and completely grateful, that it is you beside me. That out of everyone in this world, it is your voice on the other end of the line. That it is your name I see on my phone and feel my whole chest settle just a little.

Two mommas. Two boys in heaven. One bond that death, distance, and time will never touch. That is what we are. That is what we will always be.

I love you, Trish. From hell and back — and I mean that in the truest, most sacred way. We have both been there. We both know what that road looks like. And we walked it, and we are still here, and we found each other on the way. That is not nothing. That is everything.

Thank you for Ryan — for every story you have shared about him, for every time his name came up and you let me know him a little through your love for him.

Thank you for Lucas — for honoring him, for saying his name, for never treating my grief like something to get over or move past.

Thank you for showing up from New Hampshire when most people right here in Tennessee have not.

Thank you for being only one call away, every single time.

Thank you for being my family when I needed one most.

Our boys are watching over us. I believe that with everything I have. And I think they are glad their mommas found each other. I think they are glad we did not have to carry this alone.

Lucas and Ryan — from feet to wings too soon. But never, ever forgotten. And their mommas — still here, still standing, still only one call away.

All my love, always — Serena."""

print("Generating audio with OpenAI TTS (nova)...")
response = client.audio.speech.create(
    model="tts-1-hd",
    voice="shimmer",
    input=letter_text,
    speed=0.92
)

output_path = "/home/ubuntu/letter-to-trish/letter-reading.mp3"
response.stream_to_file(output_path)
print(f"Audio saved to {output_path}")

# Check file size
size = os.path.getsize(output_path)
print(f"File size: {size / 1024 / 1024:.2f} MB")
