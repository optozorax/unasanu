+++
title = "unasanu — universe as a number"
date = 2023-08-28
description = "A philosophical concept that explains why any universe exists and what will happen after death."

[taxonomies]
tags = []

[extra]
image = "thumbnail.png"
language = "English"
translation = "Translated using Claude 3.5 Sonnet + review from author"
language_flag = "english.png"
toc_text = "Table of contents"
minutes_text = "min"
author_name = "Ilya Sheprut"
license_word = "License"
date_text = "28 august 2023"
lang = "en"
position = 2
+++

# Introduction

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Unasanu** (= **un**iverse **as** **a** **nu**mber) is a philosophical concept suggesting that any simulated universe exists because it can be represented as an already existing natural number. This concept can provide explanations for the following questions:
* Do alternative universes exist and why?
* Are we living in a simulation?
* Can God theoretically exist, and how omnipotent can it be?
* Why is it impossible to die and what happens after death?
* Is it possible to change universes without worrying about heat death?
{{ admonition_end() }}

This idea and its implications are logically derived from our current understanding of mathematics, physics, and consciousness. However, unasanu doesn't require the many-worlds interpretation of quantum mechanics, the infinity of our universe, or the Omega Point hypothesis. Instead, it relies on other, more reliable and simpler foundations.

This article describes the same idea as Max Tegmark's Mathematical Universe Hypothesis [\[1\]] or Greg Egan's dust theory [\[2\]], but with a greater number of implications and ideas that these authors did not consider or only touched upon superficially.

I'm writing this article to:
* bring together all the philosophical implications of this idea,
* prevent these ideas from being reinvented,
* shape the direction of further research.

# Types of simulations

We are familiar with the idea of simulating the external physical world on a computer. This topic is actively discussed in pop culture and philosophy. To begin, we need to agree on how we categorize different types of simulations. This topic often causes misunderstandings because people rarely distinguish between these two categories.

## Illusory

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Illusory simulation** is a simulation that creates an illusion of reality by deceiving the observer. Another term for such simulations is virtual reality [\[3\]]. Examples of these simulations include: the movie "The Matrix" [\[4\]], the game The Sims [\[5\]] (where the world is illusory for the Sims), and the movie "The Thirteenth Floor" [\[6\]].
{{ admonition_end() }}

An illusory simulation approximates everything it can. For instance, a human in such a simulation might not consist of biological cells or atoms, but rather a single indivisible object or an approximation of organs and limbs. This is necessary to conserve computational resources and programming efforts. A more demanding simulation would simply be impractical, as it couldn't run in real-time or would take an unreasonable amount of time to program.

People dislike the idea of living in an illusory simulation. Everyone wants to believe their reality is real and that nothing is deliberately deceiving or simplifying it. It's no wonder that all pop culture about living in an illusory reality revolves around escaping it.

## Physical

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Physical simulation** is a simulation that exclusively simulates physics based on some fundamental theory. It's a simulation accurate down to atoms/quarks/strings/???/pixels/graph vertices. Examples of physical simulations include: the theory of everything, John Conway's Game of Life [\[7\]], and Stephen Wolfram's physics project [\[8\]].
{{ admonition_end() }}

A physical simulation simulates low-level laws without approximating anything. Higher-level structures can be built on these low-level laws (for example, gas laws can be built on the model that gas consists of elastic particles). The structures that emerge and the higher-level laws governing these structures depend on the structures themselves. In a physical simulation, higher-level structures (like a human) are not approximated by something simpler: if a human exists in such a simulation, they exist accurately down to cells and atoms.

There's a possibility that our reality is a physical simulation. However, this idea is unprovable and unfalsifiable. If we live in a physical simulation, we're quite content with it because everything we know about physics, star evolution, and the evolution of living beings remains intact. The statement "if we live in a simulation, then everything is unreal" is meaningless in the case of physical simulation, because such a simulation is reality itself. The only unpleasant aspect is that someone external might have control over our physical reality, similar to the "creative mode" in Minecraft [\[9\]]. This hypothetical possibility will be explored further.

It's important to remember that **simulation ≠ imitation**. These words are similar but have completely different meanings. The world can be very real even if its laws of physics are simulated on a computer.

# The Game of Life

## Structure

The Game of Life is not actually a game or life, but a cellular automaton. I need to talk about this because it's the most illustrative example of a physical simulation, based on which we can draw many analogies necessary for this article.

This automaton works according to the following rules:
* There is a two-dimensional infinite (or finite, closed on itself) field of square cells.

{{ image(path="../img/game_of_life_infinite_grid.png", scale="2/3") }}

* Each cell can be empty or filled.
* In this automaton, there is a flow of time, and it is provided by calculating the next moment of time from the previous one based on certain rules.
* There is an initial moment of time, and from it, we iteratively calculate future moments.

{{ image(path="../img/game_of_life_time.png") }}

* The neighbors of a cell are considered to be four direct neighbors and four diagonal neighbors.

{{ image_svg(path="game_of_life_neighbors.drawio.svg", scale="1/2") }}

* The calculations consist of changing the state of cells based on their neighbors according to the following rules:
    * If a cell was empty, it becomes filled if and only if three of its neighbors were filled in the previous step, otherwise it remains empty.
    * If a cell was filled, it remains so if and only if two or three of its neighbors were filled in the previous step, otherwise it becomes empty.
* These rules are denoted as B3/S23 (Born 3 / Survive 2 or 3).

{{ image_svg(path="game_of_life_rules.drawio.svg", scale="2/3") }}

In the following interactive visualization, you can see how this cellular automaton develops for a random distribution of filled and empty cells:

{{ game_of_life(
    start_stop="Start/Stop",
    step="Step",
    empty="Empty",
    random="Random",
    glider="Glider"
) }}

You can play with more advanced simulators yourself, for example on `conwaylife.com` [\[10\]].

## Impressive capabilities

In this automaton, a huge number of mechanisms can be built. Here are some of them.

The first example is the glider from the visualization above. This mechanism moves diagonally. It can be said that this is an analogue of a photon.

You can also make a generator of such gliders:

{{ figure_start() }}
<img src="../img/glider_gun.gif" width="250" height="180">
{{ figure_end(caption="Gosper's Glider Gun.") }}

---

The Game of Life cellular automaton is Turing-complete, meaning a computer or Turing machine can be built on it. Here's an example (source with interactive simulation [\[11\]]):

{{ image(path="../img/game_of_life_turing_machine.png", scale="2/3") }}

---

In the interactive visualization `oimo.io/works/life` [\[12\]] (works on phones too), the Game of Life is simulated on itself both inwards, infinitely small, and upwards, infinitely large:

{{ image(path="../img/game_of_life_on_itself.png", scale="2/3") }}

---

John von Neumann invented a cellular automaton and a mechanism in it that can self-reproduce. The image below shows how the second automaton has almost finished building the third; the lines going to the right are genetic information that is copied along with the body of the machines.

{{ image(path="../img/von_neumann.png", scale="2/3") }}

---

Tim Hutton [\[13\]] developed an artificial chemistry in which he designed such elements and interactions between them to assemble an artificial cell capable of reproduction:

{{ video(path="../img/chemistry.mp4", scale="2/3") }}

This is not a cellular automaton, but it easily fits into such framework, and the author continues to develop this idea in the form of a cellular automaton [\[14\]]:

{{ image(path="../img/chemistry_automata.png", scale="2/3") }}

---

I've shown you all this to convince you that cellular automata are not just toys, but serious concepts that are worthy of being an analogy to fundamental physics.

## Analogy with physics

{{ admonition_start(color="gray", title="💬 Quote from the article Cellular automata with 2 temporal dimensions [\[15\]](http://dmishin.blogspot.com/2014/06/cellular-automata-with-2-temporal.html)") }}
Cellular automata are good examples of "toy physics", that we know bottom-up. In the real word, we observe complex phenomena and can only deduce underlying principles (that's what physicists do). In the world of cellular automata the situation is the opposite: basic rules are given but the behavior of complex systems is a subject of research.
{{ admonition_end() }}

The Game of Life automaton has many interesting properties:
* The laws of physics and matter are separated from each other.
* Matter can be edited as desired: drawn, copied, pasted, deleted.
* A simulation can be run over any modified matter.
* There is some initial moment of time.
* Time is the computation of the laws of physics, and a moment in time is a discrete slice of the field's state.
* The laws of physics are local, meaning they work only over a certain area of space, there is no action at a distance, and because of this, a maximum allowable speed naturally arises - an analogue of the speed of light in our world.

But this automaton also has differences from our physics:
* There are no conservation laws (for example, the number of cells), but for lovers of such laws, cellular automata with conservation laws can be found.
* Time can only be simulated forward (not backward), because there can be from 0 to infinity past moments of time. This is not necessarily a property of our physics; our physics may be reversible (and reversible automata also exist).

Further, it will be assumed that our physics at its very foundation _is something like a cellular automaton_ (with big assumptions, but in my defense, I will explore this topic further). That is, the properties described above apply to it.

And even if our physics is not like a cellular automaton, it's a good starting point because understanding exactly how it differs is also good.

# Thought experiment with physical simulation

## Description of the experiment

Let's assume that a very distant future will come in which we have managed to become a civilization using all the energy of the Galaxy and have built a computer the size of the Solar System, maximally efficiently using every Planck length.

Then we developed rules for some simple physical simulation, which is created in the image and likeness of our physics, but does not repeat it exactly. This is necessary because our physics is very redundant and strange with all this quantum mechanics and theory of relativity. We developed this physics in such a way that its chemistry could be rich enough for life to potentially exist and self-originate.

Since we want to run this simulation on a computer, we have some limitations. Our simulation must be:
* discrete,
* finite,
* deterministic,
* halting (for each step).

I also want to impose a restriction that in the simulation, we have the right to intervene only in the initial conditions and never again.

Before we move on to the essence of the experiment, let's clarify each term.

## Discrete Physics

Two types of spaces are known: continuum and discrete space.

{{ container_start() }}
{{ figure_start() }}
{{ image(path="../img/continuous2.png", scale="2/3") }}
{{ figure_end(caption="Example of a continuum") }}
{{ figure_start() }}
{{ image(path="../img/discrete2.png", scale="2/3") }}
{{ figure_end(caption="Example of a discrete space") }}
{{ container_end() }}

<!-- https://www.desmos.com/calculator/iuoa2bl8uc -->

A discrete space of finite length can be divided into a finite number of elementary elements. A continuum of finite length contains as many numbers as the segment (-∞; +∞), that is, it is infinitely divisible, with each number having an infinite number of digits after the decimal point.

Obviously, it's impossible to fit a continuum directly into a computer. Therefore, all our simulations operate with a finite number of discrete objects. When we simulate physics, we use discrete approximations.

However, there is an interesting connection between discreteness and continuity. For example, laws about wave behavior (oscillations, period) are built on the idea that the material in which these waves propagate consists of a continuum. But we know that all liquids, gases, and solid materials consist of discrete atoms, just a very large number of them. Therefore, some continuum physical laws, although beautiful, are actually just approximations of what works on a discrete foundation.

Similarly, we can assume that quantum mechanics works in a similar way, but this is just an assumption and not necessarily true. In our thought experiment, we want to have such physics that is discrete at its very foundation, while not breaking the possibility that on large scales it could seem continuous.

## Finite physics

Everything is simple here - the space of our simulation must be finite because we cannot operate with an infinite number of objects. For our experiment, we can simply take a large distance, and this will be enough.

## Deterministic physics

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Determinism** is a property of processes which means that the process will always produce one and only one result for given initial conditions, no matter how many times it is run.
{{ admonition_end() }}

Determinism means that the future of the simulation is unambiguously defined and there is no fundamental randomness present. This is a logical requirement because computers can only do deterministic calculations and are not capable of absolute randomness.

{{ admonition_start(color="red2", title="⚠️ Note") }}
Some might say that data races, uninitialized memory, and cosmic rays can be sources of absolute randomness. Let's agree that all code in the thought experiment is executed on a single-threaded virtual machine in an ideal environment, and all newly allocated memory for it is pre-zeroed. Therefore, we will only reason about deterministic simulations.
{{ admonition_end() }}

Processes in our world appear deterministic, although it's very difficult for us to predict some events. Also, deterministic processes can possess chaos. So a deterministic world can again be similar to ours, and this requirement does not particularly diminish our physical simulation.

Simulation of absolutely random processes will also be discussed in the following chapters.

## Halting physics

This by no means implies that there must be a step after which the simulation must stop (for example, heat death), but rather that each step of the simulation must be performed in a finite and predictable number of steps. This means that within the calculation of one step of the simulation, there should not be infinite loops and anything similar. This requirement is necessary because there is no point in running a simulation that can go into an infinite loop at some interesting point and then not produce any results.

And this requirement is also necessary because we don't want to solve the halting problem [\[16\]] (a good video on this topic [\[17\]]), which is impossible to solve in the general case.

## Running the simulation

It seems that creating such physics should not be impossible. Therefore, in the thought experiment, we found a suitable candidate. Although you are free to disagree that creating such physics is possible.

Next, we run this physics over some finite space on our supercomputer and wait until life self-originates there. If it doesn't originate, we can play a bit with the initial conditions, select the optimal number of necessary atoms, or place a gas-dust cloud at the right distance from its star so that it is in the habitable zone, and so on.

Let's assume we were able to find such initial conditions under which life arises, and then we simulate for a very long time and wait until it evolves into intelligent beings capable of communicating with each other using some language.

Surely these beings have something like a self-preservation instinct, sexual attraction, pleasure from food, and suffering from body damage. Because this is a logical evolutionary path for individual beings with brains. Beings without this would likely be less effective in survival and would be filtered out by evolution.

{{ admonition_start(color="gray", title="❓ Question to the reader") }}
Please stop and answer the following questions. It's preferable if you also explain your answers.

Do you think these beings feel that they are alive? Do they observe their world? Do they have subjective experiences, aka qualia? Are they alive?

If you don't think they feel anything, then suggest what properties the simulation should have for you to consider them feeling.
{{ admonition_end() }}

How you answer this question will affect how you perceive the rest of the narrative.

I described this simulation in such detail to bring your vision of these beings as close as possible to humans, but without using our world directly, because it's unknown how well we can simulate it. And the main point is that everything described seems quite hypothetically possible. Because so far we haven't discovered any fundamental laws that would prohibit beings in a physical simulation from possessing intelligence or feelings.

I hope you answered positively to the question of whether these beings feel something. The argument "they don't feel anything simply because I know they're in a computer" is too lazy. We need to try to disprove this more intelligently.

If you disagree, that's okay. I'll consider that point of view later as well.

Let's assume you agreed that these beings are alive, that they feel they are living, can communicate about this, and can ask questions about god or whether they live in a simulation. We don't affect their world in any way, so they have no way of understanding what we represent, and they have no reason to doubt the reality and honesty of their physical world.

{{ admonition_start(color="green2", title="🤔 Verifiable statement") }}
Is it possible for life to self-originate in a simulation?
{{ admonition_end() }}

## What if we stop the simulation?

{{ admonition_start(color="gray", title="❓ Question to the reader") }}
What do you think will happen if we stop the simulation? Will the beings inside it die? Or will they not die, but stop feeling their life? Or will they somehow miraculously continue to live?
{{ admonition_end() }}

Of course, you'll say they'll die, because how else? When we simulate them - they live, when we turn them off - they don't live. It's simple. But no. <span class="green2-bg example">I assert that after the simulation is turned off, these beings will continue to live.</span>

As I've already said, our simulation has some fundamental limitations, without which we can't run it on a computer, namely - **determinism**. Determinism means that there is only one outcome for a given program if initial conditions are set and there was no subsequent intervention in the program. Now here's a question: if the future is singular, why do we need to simulate it? What changes from the fact of our simulation? We can't influence the future in any way, it will be as it will be in any case.

If this is not enough to realize the power of determinism, here are a couple more thought experiments:
* If we delete the entire result of the simulation and simulate again from the very beginning, we'll get exactly the same result.
* If we pause the simulation and continue after a billion years, the beings inside will not feel it in any way. The flow of time for them will be dictated by the internal laws of their universe. We exist outside of their time, and they exist outside of our time.
* If we run this same simulation simultaneously on several computers, nothing will change for the beings.
* If the simulation is reversible and we somehow extracted a very distant moment from the future, then from the fact that we will simulate it backwards, the beings will not feel that they are living backwards.

Of course, this may also not be enough, and further I'll show how it can be proved that they will be alive even with the requirement to simulate their world.

# Universe as a number

Okay, we agreed that the beings are alive when we simulate them on a computer, and it's not enough for us that they have a single future. We believe that their future exists only after we have simulated it.

Then let's specify exactly what we have to say that this is proof that they lived for this period of time. All we have is the simulation algorithm and all the simulation steps up to the current one. We believe that the fact of the existence of this information is equivalent to proof of the life of these beings.

Let's say we made this simulation, got all the data and recorded it on a large hard drive: first the algorithm, then step 1, then step 2, ..., step N. Now we have proof that they lived up to step N. But the data on the hard drive is always some sequence of zeros and ones. We can take and write the data from the hard drive in the form of one very large natural number. And this natural number is still proof of the life of these beings.

{{ image_svg(path="number.drawio.svg", scale="2/3") }}

Now an interesting point: as we know, all natural numbers exist.

Since all natural numbers exist, among them there must be a number by which we encoded the simulation of beings simulated by us. But among them there is also this same simulation, but with a moment of time +1. And among them there is also any other simulation, for any moment of time inside this simulation. And all these numbers are equivalent to proof of the life of some beings that these simulations contain.

From which we conclude that <span class="green2-bg example">the result of any simulation that can be run on a computer already exists in the form of a natural number</span>. This is where the name of this concept comes from: **universe as a number**.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Existence for itself** - some universe exists for itself if living beings inside it are capable of observing their own existence and their universe.
{{ admonition_end() }}

Earlier, we agreed that beings in a computer simulation are able to observe their own universe. So this universe at least exists for itself. And then we came to the conclusion that this existence is equivalent to existence in the form of a number. Therefore, from the existence of all natural numbers follows the existence of all possible simulated universes for themselves. And therefore, in all such universes where there is life, this life will observe its universe.

I like this example with physical simulation because for it we don't have to give a definition of existence, but that it's so self-evident that we should derive the definition of existence from it. And in this case, we derive the definition of "existence for itself". If we agree that they feel their life inside the simulation when we run it on a computer, then from this we must immediately conclude that they felt life even without our simulation, existing in the form of a number.

What happens then when we simulate some world? In this sense, it can be said that by simulating, we do not create a world, but observe an already existing one. And computational powers are spent exactly on observation. And selecting initial conditions is not "creating a world", but finding a world with the properties we need among an infinite variety of worlds.

And when we stop the simulation, the beings continue to live for themselves. They can tell other beings in their universe about it, but not us. We cannot observe this because we turned off the simulation.

## Anthropic principle

{{ admonition_start(color="blue2", title="📖 Definition") }}
**The anthropic principle** is a principle according to which the universe is so perfectly tuned for the emergence of life and humans as observers precisely because in other universes that are not so tuned, an observer is impossible.
{{ admonition_end() }}

Unasanu agrees well with the anthropic principle. For myself, I formulate it like this: if all possible universes exist, then observers arise only in those universes where their emergence is possible.

The anthropic principle is necessary because physicists observe that the most fundamental constants are perfectly adjusted for our existence. If some of them were a percent less or more, life as we observe it would be impossible. You can read more about this in the book "Our Mathematical Universe" [\[18\]].

## The argument of incorrect calculations

One might object: where do calculations come from if we just have numbers? After all, I can take any correctly calculated universe and write it down incorrectly, and this will also exist in the form of a number. Why then are calculations obliged to exist?

### Calculation by all laws of physics

There is another similar point. If the universe can be calculated by the current laws of physics, why isn't it calculated by other laws of physics? In fact, it is, and according to unasanu, such worlds exist. Let's take the Game of Life as an example. The following illustration shows how the same field is calculated by different rules:

{{ game_of_life_all_rules(
    start_stop="Start/Stop",
    step="Step",
    random_rules="Random rules",
    copy_from_original="Copy from B3/S23",
    random="Random field",
    glider="Glider",
    glider_gun="Glider gun"
) }}

Try clicking "Start" and pressing the "Copy from B3/S23" button once a second. You will see that any state from B3/S23 can be calculated by any other rules, and this exists within unasanu.

And this is only a tiny part (what is subject to the `B/S` notation) that I've included, but in reality, there are an infinite number of ways to calculate the next step of such a field with cells having two states.

Obviously, this field can be taken as a basis for calculation by all possible rules. And so with each moment of time and each rule that can be constructed.

Absolutely analogously, nothing prevents us from taking all possible modifications of this field and calculating them with the original rule.

All of this exists according to unasanu, and this has many consequences that will be discussed later.

So why don't we observe the calculation of our universe by arbitrary laws of physics and observe any calculation at all?

### Anthropic filtration

This can be explained by the fact that it is the observer who keeps the laws of the universe stable, ensuring the existence of calculations and specific laws of physics for themselves. How?

Let's start by considering the argument of incorrect calculations. If the universe is not calculated according to any laws, then observers who would observe this universe are impossible in it. Because the fact of observation is a calculation. And if the universe obeys laws, then an observer is possible in it. Therefore, an observer can only observe a calculable universe.

And now the argument about all possible laws of physics, they are also kept stable by the observer. More precisely, he observes only stable laws of physics. Because when calculating brain atoms by some other laws of physics, the brain may stop working, and the observer will not observe anything in such a universe.

In a sense, this is similar to the anthropic principle, only more fundamental and occurring at every moment of time, not just at the start of time at the moment of the universe's creation. I propose to introduce a term for this.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Anthropic filtration** is a principle according to which an observer is able to filter out universes in which calculations are not performed or they are performed incorrectly, as well as filter out universes where its emergence or existence is impossible.
{{ admonition_end() }}

Further, we will see that anthropic filtration is applicable to some similar arguments, but not to others.

### False vacuum

In physics, there is a state of matter called "false vacuum". Its emergence is probable. If it occurs at one point in the universe, it spreads in all directions at the speed of light, destroying everything that gets into it. No human is able to observe the existence of a false vacuum because their brain works too slowly and they will simply die before they realize it, and information about the false vacuum cannot outpace the speed of light.

Thus, false vacuum refers to examples of anthropic filtration. Because for those universes where it arose, all living beings died and did not learn about it, while other universes that differ by one atom, where this false vacuum did not arise, continue to exist. Thus, false vacuum is subject to anthropic filtration.

And if the laws of physics are filtered by the observer once, when the universe arises or the observer is born in the right universe, then the false vacuum is filtered by observers at every moment of time. And if scientists find out that the probability of false vacuum occurring in the observed universe is very high, but it never occurs and we continue to live, then there are no contradictions from the point of view of unasanu.

By the way, it can be very fun when we create a theory of everything and suddenly it turns out that any simulation based on it will be destroyed by false vacuum after some time. :)

{{ admonition_start(color="violet", title="🔮 Prediction") }}
If we can create a theory of everything and according to it we should have long died from false vacuum or similar phenomena of instant death of all things, this does not mean that this theory is incorrect.
{{ admonition_end() }}

## Eternalism

Some readers may have a question: "What about time?" Earlier, I implicitly assumed that universes along with their time exist in the form of a static chunk of data, completely ignoring the dynamics that we feel due to the flow of time. This point of view is called eternalism.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Eternalism** is a view of time according to which future events already exist, there is no objective "flow" of time, and all space-time can be represented as a static unchangeable "block" [\[19\]].
{{ admonition_end() }}

I argue that eternalism is the correct interpretation of time for simulations. In the following chapters, I reduce our universe to the class of computer-simulated ones, so eternalism should be applicable to our time as well. Let's figure out eternalism for simulations, since it is an important part of unasanu.

<span class="orange-bg example">How does time work for humans?</span> At this moment in time, we only have memories of the past and a sense of the present. We cannot directly feel the past or the future. We can understand what the past might have been like from certain physical objects, such as film recordings, archaeological artifacts, and our own memories. We have to trust all this. We can also only communicate with people from our time, because such are the laws of physics. The fact that there are people in the future does not mean that we should be able to interact with them, except by living to that time.

<span class="orange-bg example">Why do we feel time passing gradually, and not immediately feel a random future moment if it already exists?</span> Because it follows from the laws of physics and the construction of our brain that for a 20-year-old person's brain to feel something, it must first live all these 20 years and remember them. So you are probably now a brain from a random future (probably just before the moment of your death), it just remembers how it lived all the past moments of time, and it seems to you that you are living now.

<span class="orange-bg example">How does time work in a simulation?</span> In discrete simulations, the future state is atomically calculated from the past state. Inside the simulation, it is impossible to feel time "between simulation steps", because the internal laws of the simulation themselves can only operate on the completed calculation of the state. That is, for the simulation, there is no fundamental dynamics, there are only different static moments of time that are connected by logical relationships, and the observer interprets them as dynamically changing.

As a variant of "refutation" of eternalism for simulations, one can assume the following: we take as an axiom that in our world time is irreducible to static structures. Then if we assume that in some simulation there is time similar to ours, then the only way it can be defined is to tie it to our time. Then time in the simulation flows along with our time while we calculate it.

This can be refuted in two ways, showing that the "current" moment of time in the simulation is not the only one:
* Let's create a copy of this simulation and simulate it with a second delay. Then what time is "current"? What time do beings inside the simulation feel "at this moment in time"?
* There are such classes of simulations as "reversible". They can be simulated not only into the future but also into the past. By the way, quantum mechanics is reversible, so such a simulation can be very similar to our universe. So what if we create a copy of this simulation and start simultaneously simulating it both into the past and into the future? Which moment in time will be current?

So, we cannot in any way refute the idea that for a computer simulation, time cannot exist in the form of a static structure. We can even say it differently: a simulation cannot be described by something dynamic, only by static blocks. And there are no paradoxes observed in this, even if applied to our universe. Thus, <span class="green2-bg example">the main property of time is not constant movement, but that it connects different (temporal) layers of information by certain laws of physics.</span>

We can also say that time does not exist as some global structure, and all simulations obey it, but on the contrary, time exists inside simulations.

Also, eternalism is an unverifiable and irrefutable statement because it is just an interpretation of time in deterministic universes.

It may also seem that eternalism assumes absolute determinism and requires that the future be unique. But eternalism is quite compatible with universes with multiple futures and with absolute randomness, as will be shown later. You just need to imagine the resulting "space-time" block not as a static sausage, but as a static tree. :)

## Interaction with the simulation

<span class="orange-bg example">From this point on, the restrictions imposed earlier will gradually loosen.</span>

I said that for the thought experiment, I suggest not interfering with the simulation. What happens if we remove this restriction? Will the simulation become non-deterministic? No.

Suppose we reached step N in the simulation and wanted to remove totalitarian rulers who start wars using the atom editor. After this, the beings inside are perplexed but rejoice. But what is intervention in a simulation? It's a sequence of actions sent to the simulation program. This means that this sequence of actions can also be encoded as a number.

If we record all our interventions and then append them next to the program and say that they should be sent at the right time of the simulation, we can again get an absolutely deterministic simulation. Which can be run again and again, and it will give the same result, even though we will interpret its result as one that has been intervened with.

And all such possible interventions can also be encoded as a number and appended next to the number of the usual simulation program. <span class="green2-bg example">Therefore, all possible universes with all possible interventions also exist, even without the need to intervene in them directly.</span>

At the same time, we shouldn't forget that just as there exist universes with all possible interventions, there continues to exist a universe without any interventions.

## Tegmark's mathematical structures

Earlier, I implied that a simulation has the following structure:
* There is some initial state `O` of the given simulation.
* There is some function/program for computing one step `F`, which for each state of the given simulation returns the next state of the given simulation, and the answer always exists.
* The essence of the simulation is to perform the following algorithm:
  * T = F(O)
  * T = F(T)
  * T = F(T)
  * ...

Thus, "time flows" inside the simulation because we equate one step of computation time to a step of time inside the simulation. And time exists globally throughout the universe.

But in fact, such an interpretation of time is **naive** and does not allow for the existence of much more complex universes, for example:
* universes with multidimensional time (a good article on this topic [\[15\]]),
* our universe with the theory of relativity,
* universes with time travel.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Naive time model** — a time model in which time is discrete and exists globally throughout the universe, and the next step can always be calculated from the previous one.
{{ admonition_end() }}

Therefore, the **mathematical universe hypothesis** [\[1\]] by Max Tegmark enters the scene, where he approached this question more fundamentally, asserting that in a physical sense, any universe described by a mathematical structure exists.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Mathematical structure** — a set of abstract entities with relations between them.
{{ admonition_end() }}

It is known for certain that all naive simulations are a subset of mathematical structures, as the result of a program's work defines an abstract entity, and the program itself defines the relationship between these entities. It is also known for certain that the set of mathematical structures includes universes for which calculations can be used to verify that their space-time regions satisfy their own laws. Therefore, in such a concept, calculations are needed not to observe the world (calculate its steps), but to verify that some world satisfies its own laws, or to specify it.

{{ image_svg(path="structure.drawio.svg", scale="2/3") }}

Probably, such a description is not very clear, so I want to show an example of a universe that appears to be computed naively, but in fact is not. An explicit example: time travel with the impossibility of changing the past. I know two good examples of this: Harry Potter books and the movie "Tenet". Imagine how you would simulate a world where time travel is possible, but it's done in such a way that the past remains unchanged? You need to simulate the past taking into account the future, and the future taking into account the past, and they must fit each other. We don't have ways to compute universes with such laws of time travel yet, so here the only possible option is to iterate through all possible worlds (with all possible futures and pasts) and check which of them satisfy the necessary laws. That is, the whole world can be computed only in the format of "all time at once". But beings in such a world obviously feel that they are living and are amazed by their time travel laws. You can read more about this in the article "Causal universes" [\[20\]].

By the way, there is an article titled "The Universe is not a Computer" [\[21\]], which suggests looking at the way of describing physics differently and offers an approach for computing "all time at once".

Another example of a non-naive universe is our universe with the theory of relativity. We don't have a single global time. In each part of space, time flows at a different speed. Therefore, the entire universe should be represented as a space-time block, where time is just a relationship between parts of this block.

In both of these examples, universes can be approximated by local naivety. For the first universe, we neglect time travel, and for the second, we neglect time dilation. Because of this, I will continue to reason in terms of naive simulations further, because it's simpler and it approximates well a multitude of possible types of such universes, if not all of them. But this could also be a mistake.

{{ admonition_start(color="green2", title="🤔 Verifiable statement") }}
Can our laws of physics be reduced to local naivety?
{{ admonition_end() }}

{{ admonition_start(color="red3", title="🤕 Weak point") }}
What if our universe cannot be computed naively and cannot be approximated by naive computations even locally? Many conclusions of this article will depend on this.
{{ admonition_end() }}

{{ admonition_start(color="orange", title="🔢 Math problem") }}
Develop a format for describing computable universes as "mathematical structures". Determine whether it is possible to write our universe in such a format.
{{ admonition_end() }}

## Construction principle

If all possible universes exist, does the universe of The Lord of the Rings, Star Wars, or isekai anime universes exist? To answer these questions, I introduce the following principle.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Construction principle** — if a way of constructing a universe and its laws of physics is proposed, then such a universe exists.
{{ admonition_end() }}

For example, if we have a simulation program of our universe, then (in theory) we can take it and construct a world where half of the people from the current moment in time are replaced with air atoms. Therefore, such a universe exists physically, and someone feels that they live in this absurdity.

Here, "construct" means that we'll take some program like "11D Ultra Atom Editor", load our current moment of time into it, edit it, and continue to simulate the resulting set of atoms from the edited moment.

Is it possible to create an exact universe of The Lord of the Rings in a similar way? With a very high probability — **no**. To begin with, the laws of physics for such a universe should be roughly the same as ours, with some modifications for the presence of magic, but it's not a given that such laws of physics can be found. Furthermore, we would want such a world to arise on its own, like ours, with the Big Bang, evolution, and so on. This is another huge constraint that will hinder finding such a universe. Then we want the plot to be fully repeated in this universe. Maybe even for all living beings to look like in the movie. In general, all these constraints will eventually look like a huge system of equations for the initial state of the universe. And as we know, not all systems of equations have solutions. Simply because, if we plot their graphs, they will not intersect. As in the following example:

{{ figure_start() }}
{{ image(path="../img/rings.png", scale="2/3") }}
{{ figure_end(caption="Two different conditions") }}

Here, each point is a universe, and the graph shows a universe satisfying one condition. The universe of The Lord of the Rings consists of many conditions, so this universe must be the intersection of all graphs of all conditions.

But there are points that are closest to all of these conditions:

{{ figure_start() }}
{{ image_svg(path="rings2.drawio.svg", scale="2/3") }}
{{ figure_end(caption="A universe sufficiently close to all conditions") }}

<!-- https://www.desmos.com/calculator/aasywp7i1k -->

And this means that we can find universes that approximately satisfy our conditions.

Therefore, the universe of The Lord of the Rings is unlikely to exist in absolutely the same accuracy as it is described in books or shown in movies, with all our imaginable or unimaginable requirements for it. But there are certainly universes close to it, with not so many restrictions imposed, and the more compromises we make, the more natural the result will be, the wider the spectrum of such universes will be. Maybe even a more natural universe will turn out to be much more interesting than the universe of The Lord of the Rings, so the loss is not great.

But nothing prevents us from constructing an isekai universe. We can take some existing world in the Middle Ages with people, then insert a person from the future after death, simulate such a universe further and see what happens. So in this regard, isekai universes are not impossible. Although, again, an absolutely exact analogue from your favorite anime probably doesn't exist.

{{ admonition_start(color="red", title="⚠️ Note") }}
In this chapter, I implicitly assumed that our universe can be simulated on a computer and that it obeys unasanu. But this is a separate, big question that we will discuss later. For now, I will implicitly assume this for ease of perception. You can always extrapolate these examples to other universes that obey unasunu.
{{ admonition_end() }}

<span class="orange-bg example">Also, the construction principle is the main candidate for refutation</span>, because we don't yet know the theory of everything to say whether any combination of atoms exists or not. What if we can't create a copy of our universe where half of the people are replaced with air? What if it contradicts some laws? For simple naive universes like Conway's Game of Life, we can assert this, but it's unlikely to be true for all types of universes.

And of course, the construction principle cannot be applied in some cases if our universe is not computed naively.

In short, according to unasanu, <span class="green2-bg example">not all imaginable worlds exist, but all constructible ones do</span>.

## Substrate independence

If you find it surprising that universes can be computed on natural numbers, I want to show you one principle that makes this more plausible.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Substrate independence** is a property of computations which means that their result does not depend on what these computations are performed on.
{{ admonition_end() }}

Regardless of how the universe you are in will be computed, you will not feel it. Therefore, the possibility of computation on static numbers doesn't seem surprising.

I think this is one of the most powerful properties of computations. The result of deterministic computations does not depend on which Turing-complete substrate we compute them on:
* on a computer, 
* on Babbage's analytical engine,
* on a living computer made of a 30-million-strong army of people (hello, Liu Cixin!),
* on redstone from Minecraft,
* or if some immortal being performs these calculations on cellular automaton 110, moving pebbles according to the simplest rules (automaton 110 is Turing-complete [\[22\]]).

{{ details_start(summary="Yes, I'm quoting xkcd") }}
The image is clickable.
{{ figure_start() }}
{{ image(path="../img/xkcd_505_en.png", format="png", scale="1") }}
{{ figure_end(caption="xkcd/505 [\[23\]](https://xkcd.com/505)") }}
{{ details_end() }}

## The fact of computation is an observer's interpretation

Let's assume that we postulate that only those universes that are explicitly simulated on our computers exist.

Consider the following thought experiment: we launched such a simulation, and virtual beings live their lives there, and then humanity went extinct, and billions of years later aliens flew in to see what was happening. What if they can't understand what calculations were performed on this computer until the end of time? Will the virtual universe cease to exist because of this? And what if there are a huge number of computers in the universe that produce all possible simulations, we just haven't found the right interpretation for them?

## Why all natural numbers exist

The next argument that can be made against unasanu: why should all natural numbers exist by themselves? What if a simulated universe exists only because the number encoding it is contained on our computer?

To begin with, natural numbers are maximally natural, self-evident, and simple. It's much easier for me to believe in the existence of natural numbers by themselves than in the existence of real numbers with an infinite number of digits after the decimal point.

But even if this is not enough and if we believe that only those numbers exist that are encoded by some physical object, then even in our finite universe there are quite a lot of numbers. For example, we can take any stone from the street and scan it layer by layer, then we can collect all the images into one very large number. We can read each stone from a very large number of angles. We can mix all its images in very different orders to get an even larger number of numbers.

Even more numbers will result if we consider creating long numbers from the combination of many numbers from stones read from different angles. We can take an incredible number of permutations of the order of stones and for each stone we can choose a very different angle. Thus, in our universe, all possible numbers up to a certain size can probably be found.

This means that a lot of already computed universes are encoded in our universe. We can even say that from the fact of the existence of our universe follows the fact of the existence of a huge number of other universes. Previously, I proved the existence of other universes for myself in this way and called it the "idea of world generation", but now I find natural numbers more fundamental and don't need such things.

By the way, Greg Egan's dust theory [\[2\]], which he described in his novel "Permutation City", is formulated in a similar way.

## Infinite time and infinite memory

It can be shown that for simulations existing in the form of numbers, infinite memory, infinite time, and, accordingly, infinite computational capabilities are available.

First, how is infinite time achieved? If we do not limit the existence of the next step in any way in the simulation code, that is, for any current step there is always a next one, then for any number encoding steps from 1 to N, you can always construct a number encoding steps from 1 to N + 1. Consequently, time is not limited here in any way, and the universe in the form of a simulation can exist infinitely.

{{ image_svg(path="next_step.drawio.svg", scale="2/3") }}

Due to the infinity of time, one can make the computation speed as large as desired, simply by pausing the consciousness observing the computations.

Infinite memory is a bit more complex. Suppose that by memory we mean the length of the number encoding the current step. For example, we have code written in such a way that the algorithm checks whether the previous step belongs to the current one. Then, when we request memory, we find the next number, and the algorithm checks if this number is what we need. When there is not enough memory, the algorithm can reject the number encoding this simulation. When there is as much memory as needed, the algorithm accepts it. Then, no matter how much memory we request, there will always be a number that contains the required amount of memory.

{{ image_svg(path="memory.drawio.svg", scale="2/3") }}

Therefore, it would be more correct to say that you can request as much memory as you want, but each time a finite amount.

Infinity of time and memory are very nice properties that will be actively used later.

# Is this applicable to our universe

Earlier, I deliberately imposed numerous restrictions on the simulation and used an alternative, computable physics in the thought experiment example. This is because it's unknown to what extent our universe can exist inside a computer, or how computable it is. The problem isn't just that we don't know the theory of everything to answer this question, but also that we currently know of some phenomena that seem to refute this possibility. Let's consider the known problems.

{{ admonition_start(color="green2", title="🤔 Verifiable statement") }}
Are our laws of physics computable?
{{ admonition_end() }}

## Simulating an infinite universe

Let's assume our universe is infinite. If so, is it impossible to compute it on a computer? No, because we have a limit on the maximum speed of information propagation - the speed of light.

Let's think about what calculations are needed to obtain planet Earth at the current moment in time? We need to take a finite piece of space from the Big Bang and simulate it up to the current moment. We choose the initial piece large enough so that the absence of information from the edges of the universe doesn't have time to reach Earth at the current time. Thus, throughout our history up to the current moment, we will observe more information arriving from more distant stars, as if our universe were infinite. But if we allow this simulation to compute further, information about the edge of the universe where nothing is computed may reach Earth. We can't allow this, so we go back and take a larger piece from the Big Bang to simulate further in time, and so on each time. As shown earlier, we have infinite memory and computations, so this isn't a problem.

Mathematically, the essence is that for any finite moment of time `T`, we can find such a finite piece of space from the Big Bang that when simulating it up to moment `T`, information about the universe being finite doesn't reach the observer in the center of this piece.

But how do we know what the organization of elementary particles was at the moment of the Big Bang? All possible initial conditions exist as numbers, so it doesn't matter.

However, this method can't be applied to infinite universes without a limit on maximum speed. For example, it's inapplicable to a universe with Newtonian gravity, where gravity propagates instantly, i.e., "action at a distance" works there. An example of a universe with a limit on the speed of information propagation is Conway's "Game of Life", where the maximum speed is 1 cell per 1 move.

We have quantum entanglement, which seems to be able to transmit information faster than the speed of light. This isn't a problem because such particles are created together nearby, and then we move them to the desired point in the universe to obtain information. Since they can't move faster than the speed of light, by the final moment of time `T`, they will be carried to a finite distance from the conditional center, and then for the simulation, we just need to take a larger piece so that information about the absence of computation at the edge of the universe doesn't reach the entangled particle.

This simulation method is similar to limits from mathematical analysis: each particular universe will be incorrect after some point in time, but the further we go, the more correct it becomes, and the limit of this sequence is what we're looking for. Let's call this the limit transition simulation method.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Limit transition simulation method** is a method by which we can simulate universes that possess something infinite by constantly increasing the finite size of this potentially infinite quantity.
{{ admonition_end() }}

{{ image_svg(path="inf_universe.drawio.svg", scale="2/3") }}

## Simulating the continuum

As we remember, it's impossible to put the continuum directly into a computer simulation. But how then is humanity able to calculate physical simulations on computers? The answer is approximation.

The very first approximation we encounter on a computer is real numbers. It's impossible to store and process an honest real number with an infinite number of digits after the decimal point. Therefore, real numbers are stored approximately - in a finite amount of memory. The two most commonly used types of real numbers are 32-bit (float) and 64-bit (double), and operations with them are directly encoded in the processor. Such limited numbers are subject to rounding errors in calculations (0.1 + 0.2 = 0.30000000000000004), so all methods working with them are designed to minimize these errors and produce an adequate result with a sufficient number of correct digits at the output. Obviously, 64-bit numbers are more accurate than 32-bit ones. There are also libraries for creating slow real numbers of arbitrary size and, accordingly, arbitrary precision, for example, 1024 bits, 10000 bits. Such numbers can be used in calculations where normal precision is insufficient.

Regarding physical simulation methods, there's the finite element method (FEM) [\[24\]], which allows numerically solving differential equations in some space with different materials. For example, we want to solve the problem of heat propagation, for which there's a fairly simple differential equation. For heat, we assume that each point of the continuum contains a real number denoting temperature. A simplified mechanism of its operation:

* We divide the space into some grid.

{{ figure_start() }}
{{ image(path="../img/Example_of_2D_mesh.png", format="png", scale="1/2") }}
{{ figure_end(caption="Example of a grid. It can be any shape, but triangular is much more efficient from a practical point of view. You can divide everything into a square grid, it will just be more resource-intensive and slightly less accurate. Illustration from Wikipedia.") }}

* We assume that each vertex of this grid contains the true value of heat, and between vertices, the heat uniformly transitions from one grid value to another. Thus, we obtained a continuum of heat values, but this continuum is represented by a discrete number of **finite elements**.

{{ figure_start() }}
{{ image(path="../img/Finite_element_method_1D_illustration2.png", format="png", scale="1/2") }}
{{ figure_end(caption="Example of values within the grid. If there's a specific value at each vertex, and it uniformly decreases between grid elements (blue), then the sum of all these elements will give such a piecewise function, which is an approximation of the true function (red). Illustration from Wikipedia.") }}

* Each such finite element can be written as a simple equation, and if we substitute this equation into the differential heat equation, we can obtain a system of linear algebraic equations (SLAE) for the entire space, which are easily solved and for which many methods have been developed.

{{ figure_start() }}
{{ image(path="../img/Finite_element_sparse_matrix.png", format="png", scale="1/2") }}
{{ figure_end(caption="Example of the resulting SLAE matrix. Here, a white dot indicates that the SLAE element is zero, and a black dot indicates that it has some value. Special methods have been devised to solve SLAE on such sparse matrices. In practical problems, the sizes of such matrices can reach millions. Illustration from Wikipedia.") }}

* After solving the SLAE, we get the heat value at each point in space at the next moment in time. This won't be an ideal solution, but it's accurate enough. And its property is that the finer we make the grid, the more accurate it will be.

{{ figure_start() }}
{{ image(path="../img/FEM_example_of_2D_solution.png", format="png", scale="1/2") }}
{{ figure_end(caption="This is what the solution looks like for the triangular grid shown earlier. It's not even noticeable that the problem was solved with such large triangles as in the picture above, and that's because FEM is good enough, and active developments are being made to get the highest accuracy of the solution for the least amount of computation. Illustration from Wikipedia.") }}

{{ figure_start() }}
{{ image(path="../img/FAE_visualization.jpg", format="jpg", scale="1/2") }}
{{ figure_end(caption="Example of another simulation using FEM. Illustration from Wikipedia.") }}

Is it possible to simulate our universe using FEM? Quite possibly. The only question that arises is about the accuracy of calculations. We can choose a grid size, say, 1000 times smaller than the Planck length, and it seems that this should be sufficient to observe our world.

Now the question of accuracy: if our universe is simulated by FEM or is even a cellular automaton, can we detect this experimentally? Theoretically possible, for this we need to either conduct experiments with incredibly high energies, or observe very distant stars, or come up with some very clever set of phenomena. It seems that for all of this, artifacts of space discreteness can be detected.

At the same time, one simple principle remains: <span class="green2-bg example">any experiment tells the truth only up to some accuracy</span>. If we conducted an experiment where we gave a proton energy equivalent to the mass of a galaxy, and then collided it with another such proton and saw that the result of their collision is consistent with the continuity of space, this tells us that space looks continuous only up to some distance, even if it's incredibly small. And it's unclear whether it's possible to devise such an experiment that would work only if space is perfectly continuous.

{{ admonition_start(color="orange", title="🔢 Math problem") }}
Is it possible to develop such a continuous system in which it's possible to conduct an experiment showing that this medium consists of an ideal continuum? The requirements for the experiment are as follows: it should be possible for reasonable beings inside this medium to conduct it, while the experiment should require a finite amount of matter and energy and work for a finite time.

If yes, does our universe belong to such a type of continuous media?
{{ admonition_end() }}

Okay, let's assume that our universe is simulated using FEM with incredible accuracy. But if this accuracy is finite, it means we can perform an experiment that will show that space is actually discrete. Is such a simulation possible where such an experiment is impossible? Yes, and I'll show it further.

Let's assume that our universe is described by some differential equation and in the standard model, each particle is represented not by a point, but by some field. Then we can apply FEM to this equation and implement the following algorithm:

* Iterate `k` from 1 to ∞.
    * The precision of real numbers is 2<sup>k</sup>.
    * The grid size in space is X·2<sup>k</sup>.
    * The grid size in time is Y·2<sup>k</sup>.
    * Solve FEM for the entire universe on the given space and time grid using real numbers of the specified precision.

For such an algorithm, it turns out that for each next iteration of the `k` cycle, we increase the accuracy of all elements of the algorithm by 2 times. Now let's assume that an observer inside such a universe wants to conduct an experiment to check how much his space (or time) is a continuum. For any accuracy of the experiment, there will always be such a `k` that the result of his experiment will show that his universe consists of a continuum. This is another use of the limit transition simulation method.

This works especially well for the case when there's a heat death of the universe. Then you can choose some finite `k` for which the observer, throughout the entire existence of the universe, won't be able to conduct an experiment with the required accuracy.

This algorithm will also work well for chaotic systems, like the three-body problem or double pendulum: for any time `t` and such accuracy `eps`, you can find such `k` that the accuracy of coordinates at this moment of time will be comparable to `eps`.

Thus, in some sense, universes with continuum or real numbers are also computable, and therefore they also exist according to unasanu.

Of course, I've shown that this is feasible only for universes that can be described by a differential equation and solved by FEM, and I don't know what other universes with continuum are impossible. I think this is already a mathematical problem - to determine which universes with continuum are computable according to this idea, and which are not.

For example, there's such a beautiful concept as "infinite nesting of matter" [\[25\]], which states that there are no elementary particles and all particles consist of their small universes. I'm not sure if it's possible to simulate such a universe by this method.

{{ admonition_start(color="orange", title="🔢 Math problem") }}
Determine which types of infinite and continuous universes can be simulated by FEM, which of them can be simulated by the limit transition method, and whether the known laws of physics belong to this class of universes.
{{ admonition_end() }}

Well, or we can say that continuous universes also already exist for themselves because they are determined, regardless of how much they can be simulated.

However, a small question arises here. If there are strictly more real numbers than natural ones, how did we manage to fit continuous universes into natural numbers? The answer is simple - computable real numbers form a countable set. The rest of the real numbers, which forms this set larger than natural numbers, is uncomputable. You can read more about this in Wikipedia: "Computable number" [\[26\]].

By the way, my limit transition method is somewhat similar to the definition of uncomputable "approachable numbers", which are defined as the limit of a computable function. I took this concept from the article "A definable number which cannot be approximated algorithmically" [\[27\]]. Interestingly, almost all known examples of uncomputable numbers are "approachable". At the same time, you can introduce such a real number that is not only uncomputable but also unapproachable.

## Absolute randomness

The next problem from the known laws of physics is quantum mechanics and its absolute randomness with the multiverse. I'm not very familiar with exactly what problems quantum mechanics presents to us in the possibility of simulating it on a computer, so let's assume that the only remaining problem is how to provide absolute randomness.

As we remember, it's impossible to get an absolutely random number on a computer, only a pseudo-random one, which is calculated by some algorithm, or if the computer takes data from the external environment for random numbers. But everything changes dramatically when we need not one absolutely random number, but a universe with absolute randomness.

Let's assume we have some deterministic universe with a single random number generator (RNG) that returns an absolutely random bit - 0 or 1. Such a universe can be simulated as follows: each time the RNG is asked for a number, we simply copy the entire current universe and show 1 to one version of the universe, and 0 to the other. Thus, each new universe will think that it has an absolutely random number. And the number of universes increases each time the RNG is asked for a number.

Yes, to simulate a universe with absolute randomness, we need to simulate not one universe, but simultaneously all possible variants. Since we have no restrictions on memory or the number of calculations, this isn't a problem. Max Tegmark calls this "subjective randomness", and I took this idea from his book [\[18\]].

{{ image_svg(path="rng.drawio.svg", scale="1/2") }}

This is a very interesting method, let's introduce a term for it.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Brute force simulation method** is a method of simulating a universe that has an uncomputable or undefinable function, but this function outputs a finite number of values, which means we can simulate this universe by simply enumerating all the values of this function.
{{ admonition_end() }}

Interestingly, among all these variants, any algorithm for generating pseudo-random numbers will be found. This is similar to how among all possible numbers, there will definitely be those that can perform calculations.

Of course, in quantum mechanics, there isn't just absolute randomness, but these universes somehow interact with each other, so it's all much more complex. However, it seems that with this in mind, it's quite possible to calculate it. If I'm mistaken and quantum mechanics has other limitations that prohibit simulating it on a computer, please let me know.

## Non-computability

Non-computability is a property of an object that prohibits its computation on a computer. All known examples of non-computability require either real numbers with an infinite number of digits after the decimal point or solving the halting problem.

{{ admonition_start(color="blue2", title="📖 Definition") }}
The **halting problem** is the task of determining whether a given program with specific input data will ever stop or not.
{{ admonition_end() }}

Alan Turing proved that it is logically impossible to have a program that solves the halting problem in general for any program. If it were possible, it would only be as an external entity that cannot be algorithmized, or as an infinitely long program. However, for each program, an answer exists - it will either halt or not.

If we could solve the halting problem, it could be used to prove certain types of theorems. For example, we could prove or disprove the Collatz conjecture (3x + 1 problem) [\[28\]]: we write a program that iterates through all numbers and checks what each number reduces to. If it reduces to anything other than 1, we stop the program. If we solve the halting problem for such a program, we can definitively say whether this hypothesis is true or not. Therefore, having a machine to solve the halting problem would be incredibly convenient for mathematical research.

It seems that the existence of a universe with physical phenomena capable of solving the halting problem is impossible. But I will show that this is not the case.

The main argument: a universe capable of solving the halting problem is deterministic. This means that regardless of whether we simulate it or not, its future is singular and the beings within it will live their lives. But if this doesn't satisfy you, there's another way.

Let's assume we have a deterministic universe with a single device for solving the halting problem. We input a program, and it outputs an answer - 0 or 1, for halt or not halt respectively. Now we simulate this universe in the usual way, but each time the device is asked a question, we copy the current universe and input 0 to one and 1 to the other. And so on each time. This is a brute force simulation method.

The interesting thing here is that only one of all the resulting parallel universes is correct, but it's impossible for us to compute which one. In other words, in one of these universes, its inhabitants observe that their universe can solve the halting problem correctly. But, it seems to me, just as we are unable to understand which of these universes is correct, they can't be sufficiently certain about it either.

{{ image_svg(path="halting_problem.drawio.svg", scale="1/2") }}

So even if in our laws of physics or laws of consciousness functioning there is a phenomenon capable of solving the halting problem, it can still exist as a computer program.

In this case, similar to the argument of incorrect numbers, to avoid ending up in a universe with ordinary computations, it's desirable that the observer's consciousness in such a universe also uses non-computability vital for the functioning of this consciousness. In other words, the non-computability of physical laws should be subject to anthropic filtration. As far as we know at the moment, neither the physical phenomena of our universe nor human consciousness require solving the halting problem for their existence.

If there are other variants of non-computability, please let me know.

## It doesn't matter if human consciousness can be simulated

Let's assume you disagree with all the points above, or it turns out that our universe doesn't satisfy all of them, and therefore it can't be computed on a computer. In this case, let's consider how possible it is to simulate human consciousness.

First, consciousness, unlike the laws of physics, is much more reliably computed by a naive approach. That is, the construction principle and all previous reasoning are very applicable to it.

According to modern scientific understanding, human consciousness is computed in the brain and it doesn't use quantum effects, meaning the brain is analogous to a classical computer. The neurons in the brain are large enough to be studied and their complete functional laws can be found, and signals between neurons are encoded not by ideal real numbers, but by a discrete number of ions transmitting electric charge. Therefore, it's believed that the possibility of simulating the human brain is just a matter of time and computational power.

Thus, even if our universe can't be simulated with absolute accuracy, a computer can simulate the brain with the highest possible accuracy. If a continual universe has no limit of accuracy and it can be increased infinitely, then for the brain such a limit exists. This accuracy is limited by the size of electrons. That is, you can simulate a human brain so that it outputs exactly the same number of ions to each neuron as a physical brain in a non-computable universe would. This means that if we enumerate all possible input data for such a brain until its death, among them there will necessarily be any non-computable universe, including ours. So we can compute a brain that observes a non-computable universe without computing it.

And since the whole point of unasanu was only in observers with consciousness who observe their universe, we've simply gotten rid of an unnecessary detail.

{{ admonition_start(color="green2", title="🤔 Verifiable statement") }}
Is it possible to simulate human consciousness?
{{ admonition_end() }}

## Biology, sociology, psychology, and similar fields are not described by mathematics

There's an argument: "Biology, sociology, psychology, and similar fields are not described by mathematics, therefore our universe is also not described by mathematics and cannot be simulated."

This is a rather strange argument that arises only from a misunderstanding of what it means to be "described by mathematics" and what mathematics and programming are capable of.

As I understand it, by "described by mathematics" this argument implies that these things could be described by some simple low-level rules from which everything else can be derived, or that they could be described by simple high-level rules that can be used to predict the behavior of the entire system as a whole.

This argument equates the impossibility of simulation with the absence of a beautiful and simple way to describe the behavior of the entire system. And in this formulation, there's a logical error, because the first doesn't follow from the second.

For example, biology. Its development is not described by anything simple because it's complex and consists of trillions of components, where some randomness at any level can lead the whole system to a different equilibrium point, or there may be no equilibrium points in biology at all. But this doesn't mean that this system cannot consist of elementary components. For example, people are actively engaged in simulating evolution and creating artificial life. They create simulations of what they themselves cannot "describe mathematically", so they create very complex systems where everything interacts with everything.

And no one has canceled the possibility of emergence - when several things together have a greater number of properties than the sum of the properties of these things separately.

<span class="green2-bg">If something is not described by mathematics at a high level, it doesn't mean that it doesn't consist of mathematics at a low level.</span>

Therefore, if you have an incredible amount of calculations, and you simply simulate atoms, and then some society emerges based on them, which believes that it supposedly cannot be described by mathematics - this is the problem of that society. On your computer, everything is mathematics.

So this is not even an argument, but rather a statement of the fact that humanity does not understand high-level emergent processes very well, and this has nothing to do with the impossibility of simulating the universe.

### Computational reductionism

I think people misunderstand computers and computations. Some of them believe that all the richness of the observed world simply cannot be computed on a computer, because computers are "zeros and ones", "simplest algorithms". Therefore, they believe that free will is impossible in a deterministic world; that AI will never have human emotions or creative abilities; that biology and psychology are "not described by mathematics"; and that if this world is simulated, then nothing makes sense and you can steal, kill, and so on...

Perhaps there's also a problem in that people are confident in the impossibility of reducing subjective experiences to computations: emotions, sensations, pleasure, suffering. I'll touch on this topic in the chapter on panqualia.

To show where I consider this point of view erroneous, I want to introduce a term, similar to substrate independence, to show another powerful property of computations.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Computational reductionism** is a property of computations according to which any system that is described by logic can be simulated.
{{ admonition_end() }}

Yes, this is a very strong statement. It's not a fact that it's correct, but this is my philosophical position.

Computational reductionism manifests itself in the fact that we can describe all types of computations, including infinite, continual, non-deterministic, and non-computable universes. Any new category of universes that seems non-computable is just a task for future mathematicians.

And if consciousness is knowable and obeys at least some logic, then sooner or later it will be possible to simulate it, at least theoretically.

Perhaps this is difficult to understand if you're not a programmer. Because I, as a programmer, have implemented increasingly complex programs over the years, and I've got the impression that everything I understand can be programmed. If I can't program something, it means I don't understand it well enough. Creating a simulation is equivalent to maximum understanding of the low-level laws of this process. Writing programs, like experiments, helps to find the truth and holes in one's reasoning. Computational reductionism is obvious to me.

## Summary

It has been shown that some restrictions can be removed for certain types of simulations. We know that the following also obey unasanu:
* some classes of infinite universes,
* some classes of continual universes,
* universes with absolute randomness,
* universes capable of solving the halting problem.

Other universes that cannot be simulated require further research. Probably, everything can be described by computations in one way or another.

And after all these statements, we can say with high probability that our universe is computable and, therefore, obeys unasanu.

Now we also have a better understanding of open questions:
* For which classes of universes is it possible to apply the limit transition method? And to which class does our universe belong?
* Which classes of universes can be computed by the naive method? And does our universe belong to such?

And I also want to emphasize that even if our universe and our consciousness do not obey unasanu for whatever reasons, all these ideas are obeyed by universes existing in the form of programs. Now we know that such universes exist, and this is amazing. And I will show even more interesting consequences of unasanu for these universes.

From here on, it will be assumed that our universe is computable after all. If this doesn't suit you, just imagine that I'm reasoning not about our universe, but about an arbitrary computable one, and all conclusions are valid for this other universe.

# Consciousness as a number

Previously, I explained everything through the existence of universes containing observers. All these arguments are meaningless without observers; even the definition of existence I introduced emphasizes that observers within observe their universe. If observers are so important, it's more fundamental to consider them as separate universes.

If a universe is computable, then any of its subsystems is also computable and can be described by some program. Since observers are part of the universe, they too can be described by a program that computes only them, not the laws of physics. As we know, any program with any input data is already computed. Therefore, any observer with all possible input data already exists as a number. This idea can even be called conasanu.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Conasanu** (consciousness as a number) is a philosophical concept suggesting that any consciousness with any input data is already computed and exists as a number, and it doesn't require any universe to exist.
{{ admonition_end() }}

{{ image_svg(path="conasanu.drawio.svg", scale="2/3") }}

It might seem that solipsism should triumph, but not quite. Solipsism claims that external reality doesn't exist. However, according to unasanu, everything that can be constructed exists. If your observations are much easier to describe by a program simulating an external universe, then that's how it is. Solipsism remains valid in that we can't be certain of anything except our own sensations, and it's a miracle that our sensations describe some external physical universe.

It's important to remember that each consciousness existing as a physical structure in some universe also exists as a separate program. And probably the opposite is also true: it seems we can construct a universe for any possible set of consciousness input data using various workarounds. The question will only be how beautiful and simple this universe is.

Tegmark's theory [\[18\]] was built on the idea that the existence of external physical reality implies it exists as a mathematical construct, but this is somewhat undermined by the fact that among mathematical constructs, there are separate consciousnesses not necessarily tied to any universe.

This creates an interesting picture where in our world, each consciousness is a separate universe, and these consciousnesses interact with each other through a physical universe.

In general, since conasanu is more fundamental than unasanu, it would be logical to build the article around the former, but I'm building it around the latter because it's easier for me and for you. Perhaps this is a mistake.

## Panpsychism, and does a stone have consciousness

It might seem that conasanu implies that some consciousness is encoded in a stone, and in any other object, and that they are all conscious and feel something. This view is called **panpsychism**.

A stone indeed contains many numbers, and among them, you can find many computed consciousnesses, but the point is that this means nothing. With equal success, your physical brain contains many different consciousnesses, and it has exactly the same ones as in any other stone or any other brain of similar size. But most importantly, all these consciousnesses primarily already exist as numbers, and their presence in a stone is just an addition.

So how does human consciousness differ from consciousness in a stone? The thing is, human consciousness can interact with the external universe in such a way that other similar consciousnesses (humans and animals) can observe this and do the same. Consciousnesses inside a stone exist for themselves, and the universe where they are located doesn't affect them at all. Moreover, their time exists within their numbers and isn't connected to our time. Although there's a way for the time of these consciousnesses to flow along with the time of our universe, as proposed in Hilary Putnam's argument [\[29\]].

In [\[30\]], they try to disprove the computability of consciousness through the argument "then panpsychism would be true, but this is absurd". The argument is called Dancing with Pixies. Well, yes, panpsychism is true, but it's useless, everything remains as it was, and stones still remain indifferent, even while containing many consciousnesses.

## I prefer panqualia

On this topic, I'd like to express my view of panpsychism. My perspective should be called **panqualia**.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Qualia** (aka subjective experiences) is the fact of your sensations, how you feel smells, colors, emotions, love, etc.
{{ admonition_end() }}

In philosophy, qualia is singled out as a separate category, around which there's much debate. For example, some believe that artificial intelligence will never be able to possess qualia, and especially love, because reasons.

I treat the brain as a sufficiently complex program, not something special, so I believe there's nothing fundamental in subjective experiences that should be debated from a philosophical point of view. In general, I believe that no subjective experiences exist: how you perceive the color red is the result of your brain's computation, the result of encoding the color red in neurons, it's a set of associations, a set of relationships between other colors, a set of memories that activate when observing the color red; and the pain in your eyes when observing red text on a blue background is also provided by the physical structure of your eye. That is, it's all dry calculations and algorithms. And such rich sensations are provided by the strong connectivity of different parts of your brain.

Or, if you like, you can express my point of view more optimistically: if some property doesn't exist, it means everything possesses it! :)

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Panqualia** is a view on qualia according to which any algorithm possesses qualia by definition.
{{ admonition_end() }}

For example, let's take a random neural network and feed it random data. I believe this neural network has subjective experiences and feels something. The problem is only that this neural network:
* Doesn't have the intelligence to understand that it's feeling something.
* Doesn't have memory to remember what it just felt.
* Doesn't have language to tell other similar neural networks what it felt.
* Even if it had all of this, its feelings aren't structured, and the input data is random, so intelligence and memory probably won't help it.

Here are several measurable criteria for my understanding of qualia, and solving each of them makes the system more sensual and closer to human perception.

Thus, all the specificity of human qualia comes down to possessing intelligence, memory, language, and a special type of input data. And all the multifaceted nature and specificity of our human feelings is achieved because we consist of neural networks where each feeling activates not only the target neurons but all related ones. It's thanks to this connection that we can feel the warmth of the red color and perceive it not as a digital camera.

So from this view, we can say that AI based on dry algorithms of rearranging letters (as in Searle's "Chinese room" thought experiment [\[31\]]) will feel the world quite differently from humans. But AI based on neural networks can feel similar to humans, and maybe even better and more beautifully, like a super-synesthete.

{{ details_start(summary="Off-topic about the Chinese room") }}

<!-- Should this part be removed? It's nonsense. -->

If you don't know this argument, read about it on Wikipedia at the link above. Here's a brief critique from me.

This argument is incorrect because the person in this case is the computational substrate, not the computed environment/agent itself, and they could just as successfully compute the interaction of atoms that make up the brain of a real living person, and just as successfully not understand anything. But the person on top of these computed atoms would be more alive and conscious than the Chinese room.

I have a suggestion for modifying this experiment that would satisfy Searle and his desire to understand the computed system. But it requires too advanced sci-fi technologies. First, we need to have a neural network of the Chinese room, and then connect it to Searle's brain via Neuralink or more advanced technology. Communication should be through Searle. After that, the neural network needs to be trained in Chinese and trained in Searle's brain interface. Then, when we launch this construct, Searle's neurons will exchange information with the Chinese room's neurons, and he will be able to feel and understand some parts of the Chinese language (but not immediately, of course). The more interactions there are, the more neural connections are formed (for example, between blue neurons from Searle's brain and the Chinese room's neural network when communicating about the blue color), and the more he will understand the Chinese language and merge with the consciousness of the Chinese room.

{{ details_end() }}

---

By the way, there are already examples of virtual beings that possess qualia and, if you like, consciousness. At least according to the criteria described above. Next, I'll simply recount the description of one work that used ChatGPT. The agents in it have everything they need:
* intelligence (small),
* memory (small),
* language,
* structured feelings,
* other similar agents for communication and interaction (!!!),
* unlike the original ChatGPT, they don't exist outside of time.

But they lack some important qualities for humans:
* sensations other than text, i.e., audio-visual-tactile, etc.;
* the ability to learn, because this work uses prompt engineering through ChatGPT, and we can't fine-tune this neural network for each agent so that the agent has its own more pronounced character or develops over time;
* sufficient simulation time and sufficient memory to create their own culture, within which they will communicate more effectively, live, discuss their feelings, and create their own philosophy.

I suggest officially recognizing this work as the first to create real (but small) artificial consciousness.

{{ admonition_start(color="blue3", title="Telegram post from «I trained one model»/927 [\[32\]]") }}

{{ image(path="../img/generative_agents.png") }}

An incredibly cool article, unlike anything I've seen before — **Generative Agents: Interactive Simulacra of Human Behavior**

<https://arxiv.org/pdf/2304.03442.pdf>

Briefly, a Sims-like game was populated with 25 characters, each with their own personality description, memories, and goals. All character actions and interactions with each other occurred through LLM generation. As a result, the characters very quickly began to imitate fairly complex human behavior — for example, they organized a Valentine's Day party together, handed out invitations, and arranged dates. _Moreover, their actions, according to evaluators' assessments, were more human than the behavior of people who were asked to play as these characters._

The authors have a very cool idea with using the model's context: all actions and observations of the surrounding world are saved, then some relevant memories are retrieved from this memory. They use them to generate the next action / line in the conversation, and the model is also asked to reflect on them to formulate longer-term plans. So the character is capable of observation, planning, and reflection.

It seems that this is generally a bomb for all sorts of role-playing of certain agents in chats and, perhaps, this is what the NPCs of the future will look like.

UPD: I forgot to attach also an excellent demo — <https://reverie.herokuapp.com/arXiv_Demo/>

and a fairly detailed [thread](https://twitter.com/AndrewCurran_/status/1645468667810021377) about the article.
{{ admonition_end() }}

# Are we living in a simulation?

This is one of the most burning questions that everyone constantly talks about and expresses opinions on, and which <span class="red-bg example">makes absolutely no sense</span>. But since everyone is interested, let's talk about it.

First of all, we need to understand that this question contains two completely different questions:
1. Is our universe computable, that is, is it possible to compute it on a computer, at least theoretically?
2. Is our universe actually being computed by someone for their own purposes?

We've already talked about the first question, let's consider the second.

Let's assume that our universe can be simulated. Then we can write a program for a universe similar to ours, but in which there is a mega-computational socket, behind which our world is computed in real-time, and the socket simply provides an interface for controlling and observing this world. Someone can connect to this socket and control our world or observe any of its details. According to the construction principle, a world with a super-computational socket exists, and there's nothing unusual about it, just twice as many computations as for an ordinary universe. So, we are someone's simulation. Moreover, an infinite number of such universes that simulate us can be created. At the same time, we shouldn't forget that our universe already exists as a number independently, that is, it is an independent reality.

<span class="green2-bg example">**So:** we simultaneously exist as a simulation in an infinite number of universes and as an independent reality. And this works for every possible universe.</span>

As with consciousnesses in stones, this again makes no sense, until external simulators interact with our world and we can observe and investigate this.

There's an argument by Nick Bostrom, according to which any highly developed civilization sooner or later starts making simulations for reasons, so we are _most likely_ a simulation within a simulation within a simulation, and so on. Moreover, this argument is probabilistic, that is, it's not a fact that someone will want to simulate our universe, while the construction principle describes a guaranteed answer to this question. Therefore, Bostrom's argument for this question can no longer be considered.

It also makes no sense to "live an interesting life so that our simulation is not turned off", because, as we remember, even if it's turned off in all universes, we will continue to exist as a number.

# God and unasanu

Let's consider what significance God has from the perspective of unasanu. There are only two ways to introduce the concept of God.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**God** is some intelligent being that launched a simulation and can then either observe it or influence it. In the maximum case, God is a super-intelligent programmer with unlimited computations and memory.
{{ admonition_end() }}

According to the construction principle, each universe contains infinitely many diverse gods. We can use the universe with a computational outlet from the previous section. Even if a god projected their face onto the sky, it's always possible to construct a universe where they look completely different but decided to substitute their face using technology. This means that <span class="green2-bg example">any universe has infinitely many gods</span>.

Even if some god manages a universe and copies the brains of all beings after death and distributes them to other simulations called "heaven" and "hell," they are not omnipotent. The point is that the universe will exist without their intervention, and they can do nothing about it. <span class="green2-bg example">No god can prohibit some universe from existing</span>. The same applies to universes with suffering, where god for some reason doesn't intervene. This means that if some being felt that after death it didn't end up in the "heaven" or "hell" their god spoke of, this might not be by the will of their god.

<span class="orange-bg example">Is this god capable of knowing everything that will happen in the universe they simulate?</span> Yes, because they, like any programmer, can simulate it forward to the desired moment and then return to a save point from the past. Problems begin when the god wants to know what the future of their universe will be under the condition that they intervene in this universe. That is, they need to simulate themselves at a speed faster than the flow of their time, while inside this simulation there is the same simulation, and so on to infinity. And this is impossible to simulate in the general case. Therefore, god cannot know with absolute certainty what will happen to their universe together with them in the future. But they can replace themselves in their simulations with an approximate model (which doesn't observe simulations with an approximate model) or a scripted puppet and know their own future in this simulation with the desired certainty. Or they are able to know their future with absolute certainty, without the possibility of changing it, but then they need to subject themselves to limitations, calculating such a universe "all at once," as was proposed to do with universes with time travel.

No god is the primary cause of some universe; any universe would exist without them. Therefore, we can consider the second option for introducing god.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Metagod** is a god who created all universes, with all other ordinary gods.
{{ admonition_end() }}

<span class="green2-bg example">The metagod makes no sense because they had no choice during creation and it doesn't matter whether they have any opinion, whether they are alive or dead.</span> Moreover, such an explanation through god is an extra detail that leaves open the question "And who created this god?" One of the possible answers is "He is the cause of himself or existed always." If so, then why can't the laws of logic (from which unasanu follows) be the cause of themselves and exist always? This is, of course, a rhetorical question.

So, external gods make sense only when they interact with our universe and we can observe and study this. And uninvolved observer gods are as real and useless as intelligent beings recorded in stone.

# The problem of bugged universes

<span class="orange-bg example">This is a section with serious criticism of unasanu.</span>

Earlier we considered the question of why only numbers encoding correct calculations are valid. We can continue this argument and ask: why are only numbers encoding correct universes valid? Not necessarily. Let me explain.

If our universe can be computed naively, it means we can construct the following "bugged" simulation:
* Take the current moment in time and consider it the starting point.
* Modify matter at this moment in time in some arbitrary way, for example: 
    * remove a random person, 
    * replace air with a random set of other atoms, 
    * add rocks to Earth's orbit, 
    * remove Mars, 
    * turn a distant star into a black hole.
* And from this modified moment, simulate into the future.
* For observers in this universe, everything will look as if they lived a normal life, and then a random event occurred that can't be explained by the laws of physics and causal connection with the past. The past may not even exist; it's not necessary for existence in general.
* Such a universe exists according to the construction principle.

Now what's interesting: an honest simulation that simulates our universe from the Big Bang is just one; but there are infinitely many such simulations described above for each moment in time.

{{ admonition_start(color="gray", title="❓ A question to the reader") }}
If there are infinitely many such bugged simulations, and only one honest one, why do we observe an honest simulation?! Why don't we see completely random events with the deletion and appearance of matter happening every femtosecond?
{{ admonition_end() }}

Moreover, such a bugged universe doesn't prevent observers from observing their universe, because it is computed honestly, it just takes strange initial conditions of matter, so anthropic filtration is not applicable here.

{{ admonition_start(color="red3", title="🤕 Weak point") }}
Why don't we observe bugs in the universe?
{{ admonition_end() }}

But here we're already entering an area of thought that can be characterized as "the probability of finding oneself in a universe of a certain kind," and we'll discuss this later, but for now there are several potential solutions to this problem:
* Such events do indeed occur, but in different corners of the universe, and the universe is so vast that throughout the period of our intelligent observations, we haven't noticed anything unusual. Or we have noticed and call it paranormal phenomena, but no one believes such observers.
* Such events occur all the time, but they occur at the subatomic level, which is why we observe absolute randomness in quantum mechanics. <span class="green2-bg example">If this is true, then quantum mechanics is a fundamental property of any stable simulation.</span> That is, any simulation eventually converges to quantum mechanics because it's a more probable course of events. And our laws of physics simply work in such a way as to build something logical, working, and stable on top of this randomness.

There's one very weighty counterargument to these two arguments: from the point of view of combinatorics, the mathematical expectation of the number of random changes in the state of the universe is equal to half of the entire universe. From this point of view, it's much more likely to observe that half of the entire universe has been replaced by a random set of atoms than to observe the same for a small piece of space.

Another solution to this problem: what if the laws of physics of our universe are structured in such a way that it's impossible to execute the algorithm described above, what if our laws of physics require having a consistent past to function? And that's why we don't observe bugged universes, because it's impossible to construct them, and if it is possible, then it's impossible to simulate them, so observers of such universes will not observe. Let's introduce a special term for this.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Antibug universe** is a universe with such laws of physics for which it's impossible to construct bugged states described above.
{{ admonition_end() }}

This is a very interesting solution to this problem, but I doubt it's feasible from a theoretical point of view. It seems that any such system can be simulated naively with workarounds and then broken.

Although this problem seems even more complex if we consider it from the point of view of consciousness as a number (conasanu). From this point of view, there are far more consciousnesses that observe subjective experiences that defy logic. For example, they hit a stone, and the stone doesn't give an answer and doesn't return a sensation of touch or pain. Or you can create sensory perceptions in which, starting from some point, all information is shown a second later than to the original consciousness. Probably, then consciousness should also be described by antibug laws?..

{{ admonition_start(color="orange", title="🔢 Math problem") }}
Is it possible to develop such a simulation that describes an antibug universe, and do the laws of our physics and the laws of our consciousness belong to this class of universes?
{{ admonition_end() }}

{{ admonition_start(color="violet", title="🔮 Prediction") }}
If applying probabilities to universes is not meaningless, then it follows from unasanu that the laws of our physics are antibug, otherwise we would observe a bugged universe. Or we're calculating probabilities incorrectly.
{{ admonition_end() }}

## Changing the laws of physics

It's always possible to construct a universe where our current moment in time is the initial condition, and the laws of physics are slightly different: for example, the speed of light is slightly higher or slightly lower (as far as it's possible to program for our laws of physics and the structure of matter in general). If this violates the functioning of our consciousness, then such a change in the laws of physics is subject to anthropic filtration, so we shouldn't observe it. But, similar to bugged universes, if applying probability to universes is not meaningless, then we should observe a constant random change in the laws of physics that doesn't violate the functioning of our consciousness.

Maybe this is quantum mechanics? Maybe any simulation with living beings eventually converges to something like this?

{{ admonition_start(color="violet", title="🔮 Prediction") }}
If applying probabilities to universes is not absurd and if such modifications are possible, then we should observe such constant changes in the laws of physics that don't interfere with the functioning of consciousness.
{{ admonition_end() }}

## Death of all people when settling into a computer

How might this work? Imagine that people have invented computers that work exclusively on neutrons. Then such computers don't require laws of physics related to charges. While for the functioning of the human brain, electrical charges are required. Due to anthropic filtration, a person will almost always observe a universe where the computer they built works (because they debugged it while alive). When someone transitions into a computer, their existence will no longer require electrical charges, and they may, with high probability, observe a change in the laws of physics towards more random ones, not requiring electrical charges (due to anthropic filtration). Therefore, after moving into a computer, the consciousness inside the computer may observe that all animals, plants, and people instantly died.

The image below shows the original universe where consciousness is uploaded into a computer, and four possible scenarios for further development of events (people or computers die in different combinations), provided that the original universe will be simulated by all laws of physics. Each square shows a possible variant, that is, some set of universes, and a comment on them.

{{ image_svg(path="death_in_computer.drawio.svg") }}

# Probabilities of universes, or the measure problem

Returning to the question of "the probability of finding oneself in some universe." In science, this is called the "measure problem" [33].

The problem is that it's unclear how exactly to calculate the probabilities of specific universes and how different approaches to solving this problem can be verified or refuted. This problem has been known for a long time in relation to the many-worlds interpretation of quantum mechanics: it's unclear how to calculate the probability of some classes of universes when there are infinitely many of these universes. Because of this problem, I'm very doubtful about the concept of "some universe is more probable than another."

As an example, they give the simplest question: what percentage of odd numbers are there among even numbers?
* If you count in the order **1**, 2, **3**, 4, **5**, ..., then it turns out to be half.
* But if you count in the order **1**, 2, 4, **3**, 6, 8, **5**, ..., then it turns out to be a third. Here the numbers are just arranged in a different order and between two odd numbers there are two even numbers. An infinite number of both classes is preserved.

Everyone agrees that the natural order with half of the numbers being odd is correct, but it's unknown how to choose this natural order for encoding a universe and whether it's possible to define it unambiguously at all.

There's another objection against probabilities as applied to universes: "any experience must be experienced." No matter how improbable your universe should be, someone must live a life in this universe and experience living in it despite all understandings of probability. A good analogy can be drawn to this: the probability that I was born Chinese is very high, but I'm not Chinese.

And even if we solve the measure problem and can get the probabilities of some universe, it's unclear whether it's possible to falsify or verify this, even with an unlimited number of computations where we can iterate through all universes and calculate the necessary probabilities. Thus, the concept of "the probability of finding oneself in some universe" may be nothing more than an interpretation that doesn't affect anything.

And this problem is further exacerbated when you need to simultaneously account for the infinity of continual universes and the infinity of discrete universes.

## The Sleeping Beauty paradox

This is a problem from probability theory for which there are two contradictory answers, which is why a paradox arises.

But I want to tell you about an alternative version of this paradox, about a sailor. There's a sailor who has two mistresses in different ports who don't know about each other. He wants to have children but can't decide whether to have children with only one or with both. So he flips a coin and in case of heads, he has a child with only one woman, and in case of tails, with both. You are his son and know about this event. What is the probability that you are the only child, that is, that the coin came up heads?

If we consider it from the sailor's point of view, for him the probability of having one child is 50%. From the point of view of his child, there are three different children, and for two of them, the coin came up tails, so for the children it's more logical to think that the probability of heads is 33%. Or you could say, if children take such a probability, they will be right in more cases. 🤪

This is very similar to the differences between conasanu (the child's point of view) and unasanu (the sailor's point of view). Given such paradoxes, the measure problem becomes even more unsolvable.

Therefore, it's too early to talk about probabilistic predictions, and perhaps the problem of bugged universes doesn't disprove unasanu.

## Metaprobabilities (just an idea)

If you think about it, no probabilities physically exist. There are only events, and they can happen or not happen. It's a convenient idea that allows us to understand the world a little better. What if we take the same approach to different answers and make probabilities on top of probabilities? Create metaprobabilities that give a probability distribution, taking into account all points of view.

In the case of the sailor, there will be two points: 33% and 55% with a weight of 0.5 each.

Probably, interesting and useful mathematics can be built from this? I don't know, it's just an idea.

## Probabilistic solution to the halting problem

Suppose that measure theory is solvable and our understanding of more probable universes is correct. Then we can construct a universe that can solve the halting problem with a probability approaching 100%. So, the algorithm:
* Every time the universe is asked whether some program will halt, we launch two universes, in one of which the answer "will not halt" is immediately given, and in the other this program begins to be computed instead of the entire universe.
* If in the second variant the program never halts, then its inhabitants will not feel anything because it will never reach the computation of their brain, and the inhabitants of the first variant will turn out to be right.
* If in the second variant the program someday halts, then the number of steps after which the program will halt and an arbitrary natural number are returned. And then we iterate through all possible natural numbers in this case, creating a copy of the universe for each new number and continuing to simulate it. It turns out that we create infinitely many universes in which the program halted, and the universe with the wrong answer remains only one.
* All universes are computed in parallel, and the addition of new universes does not affect the computation of others.

Thus, if you live in such a universe, you always get the correct answer to solving the halting problem, with a probability approaching 100%.

# Death

Unasanu provides interesting predictions about death, and unlike useless probabilistic predictions, the prediction about death is guaranteed.

## Why it's impossible to die

When people talk about life after death, they usually do so in the following ways:

* You'll pass on your genes, they'll live on in your children.
* You'll pass on your ideas, discoveries, and other things, and they'll live on in other people. As long as someone remembers you, you'll live on. So you need to be as cool (or as bad) as possible so that people remember you thousands of years later.
* You'll be reborn as an animal in this world, forgetting almost all of your human nature.

These are all absolutely useless things. I believe that I am exclusively what's inside my skull, as well as my memories, character, thinking, motor skills, etc.

And if any of this is destroyed, part of me will die. If everything is destroyed, I will die completely. And the ideas transmitted through books and articles are a tiny fraction of all my ideas. So far, digitization of consciousness is not possible, and it's not feasible to transfer or preserve it in any satisfactory way.

And the impossibility of dying that I'm going to talk about is absolute, without half-measures like genes or living on in people's memories. Your entire personality and subjective experiences continue to live in the same way as they do now. How does this work?

It's simple. You can take your brain after death, add telomeres or repair it if it was destroyed by unnatural death, and then place it in a new body in a random universe and start the simulation. According to the construction principle, such a universe with your brain after death already exists. This means that <span class="green2-bg example">when you die, you'll feel that you've ended up in some universe and didn't actually die</span>. And when you die in the new universe, again according to the construction principle, there will be another universe where you'll find yourself. Thus, it's impossible to die.

Once again, no one creates the universe after death, no one copies your brain from this universe, the universe after death already exists simply from the fact that it's possible to construct it. You could say it differently: if you were to iterate through all possible universes, you would definitely find a universe with your brain after death, modified so that it could continue to live.

Sounds too simple, right? Let's delve into the counterarguments that might have occurred to you.

## If the brain is repaired, it won't be me

Many might say that the very process of repairing the brain will turn your copy into a different person, and it won't be you, and therefore after death you won't feel what this brain feels.

But this isn't very logical, because telomeres are in DNA and don't affect the process of thinking or past memories in any way. You are precisely the connections between neurons, and they are not affected in the repair process.

If we consider a scenario where you were killed by a gunshot to the head, it would be more difficult to repair. But it's possible: we just reverse the bullet's movement and reassemble the brain neuron by neuron, while preserving all those microseconds of impulses received while the bullet flies through your brain, to be a continuous continuation of the dead brain.

We can express it mathematically: for any method of death, there will always be a repaired brain that will be as close to the original as your brain is to your brain a microsecond later during normal life.

If you're not satisfied with such harmless manipulations, then why do you consider yourself the same person after you sleep? According to modern understanding, your brain changes and reformats during sleep much more than simple telomere rewriting. You could even say that a copy of your brain with rewritten telomeres is you to a much greater degree than you will be tomorrow.

## It won't be me because it's a different universe

Why? From a physical point of view, how is your copy in another universe different from your copy in this universe at time `t + 1`?

If both universes are computed according to the same laws of physics and your brain is copied exactly down to subatomic particles and other particles they consist of, then it's not just a copy, it's, you could say, the original. It's unlikely that such precision will ever be achieved by consciousness digitization technology.

The only difference between your copy in the new universe and the "original" will be that there's no direct causal connection between the past moment and the next, as prescribed in the laws of physics, as it happens in the original universe when time flows from moment `t` to moment `t + 1`. However, the copying process can be added to the laws of physics, and now they won't differ in any way. Still, for us, only the current moment of time and memories of the past exist, and this isn't violated during such copying.

## Where did my brain with a new body come from there?!

This is an irrelevant question in relation to the construction principle - we constructed such a universe, and this construction is possible, which means it exists. It doesn't matter at all where things came from there. This is the essence of the existence of all possible universes.

But if this question bothers you so much, here are several answers:
* This universe can't have a past state, so the state with your brain is the first moment of time in this universe, the "Garden of Eden". And since all possible first moments of all universes exist, there can be no logical objections to this.
* Random events aligned in such a way that it emerged from organic matter miraculously.
* A googol of different electromagnetic and gravitational waves came from space and gathered at one point of a living person in such a way that their brain was fried and transformed into yours.

It can be any way, within the framework of physics.

## Death can't be felt

The point is that death is the shutdown of brain function. And as we know, all our subjective experiences and feelings are born only when the brain is working.

It turns out that when you die, you won't feel anything, you won't be able to tell yourself that you've died. It won't be emptiness or darkness, because in the absence of input data from the senses, it's quite possible to have thoughts and feel your existence simply due to the thinking process. Death, however, is the absence of thinking. It turns out that death can't be felt.

At the same time, your copy will feel, and in its brain it will be recorded as if a couple of moments ago it "died", and now it lives in some new universe. This will be you, because you exist only when you feel something.

## From the copy's point of view

If all this doesn't suit you, let's look at it from the point of view that you're initially a copy in another universe. How is this possible if right now you're living in the original universe? Very simple: you are now a memory for that copy in the new universe.

For your current brain to form and feel that it's living, it's necessary for it to have lived and felt all these years that are now written in your age. This is the essence of time and the laws of physics that define it. Subjectively, you can't skip extra years by taking your brain from the future a couple of years older, this brain will tell you that it has lived these years, and it was quite a long time.

Therefore, if you look at yourself from the point of view that you're already a copy, there's nothing unusual about you living life in the original universe now. The copy must feel that it has lived in the original universe, otherwise it won't be a copy of your brain. Otherwise, it won't have memories written in it of how it's now reading this article and disagrees with it.

And if you claim that there will be no life after death, you'll be absolutely wrong, because after your death only your copies will continue to live, and they will all, without exception, understand that they were wrong, remembering this moment.

{{ image_svg(path="death.drawio.svg", scale="1") }} 

But don't focus on the word "copy", because copies accurate to subatomic particles are originals.

## Which universe will I end up in?

You'd like to think that there's some limited set of interesting universes where you might end up, like "heaven" or "hell" or "afterlife", but reality is much worse. You'll end up simultaneously in all possible universes. That is, in all possible universes there will be your copy after death, and it will live in the universe where it found itself.

Right now, you contain an infinite number of personalities that will go different ways after the moment of your death. And the only thing they'll have in common is their past and origin.

So there's no point in talking about where you'll end up. For each copy in each universe, you'll end up where you ended up, and there's no point in asking the question "why exactly am I exactly here?", because all experience must be experienced.

I can even offer you many examples of universes that can be constructed, in which you might feel yourself after death:
* The original universe, but you wake up in a mental hospital, and they tell you that you didn't die.
* On a random desert planet with a purple sky and uniform lighting, as if during rain. Then you die of hunger and thirst.
* In a simulation where all people were resurrected simultaneously and provided with infinite computational resources to simulate themselves, and your brain was obtained by a super-AI created by humanity so that this AI could obtain the state of all particles in our universe and simulate it backwards to resurrect all living beings and provide them with a programmer's heaven.
* In 12-dimensional space, and you are a super-being who has just played a game "feel like a human, maximum immersion". For this universe, the simulation of ours is just a toy. And all this human life and its sorrows seem trivial to you, and you return to your 12-dimensional affairs in the super-universe.
* Similar to the previous point, but it was all a dream.
* In a square room, where you don't feel hunger or thirst, and you can't kill yourself, and you have absolutely nothing to do there forever.
* They made you immortal and started torturing you endlessly in all possible ways without the possibility of escaping or dying.
* In paradise with 72 virgins.
* You found yourself in the center of the Sun. Died. In the middle of empty space. Died. In 60-dimensional space. Died. In 2-dimensional space. Died. Inside a computer game. Didn't die.

As you can see, the possible options range from extremely pleasant and interesting, neutral and entertaining, to universes with endless suffering. And it's precisely the universes with suffering that I don't like, I would like to somehow prohibit their existence, but this is not within the power of even a god. It's very sad to understand that some versions of me will have to experience this.

## Gradual fading of consciousness

In [\[18\]] Tegmark argues that there's still a possibility to die: your consciousness needs to gradually fade away (as in Alzheimer's disease). Then if such consciousness ends up in another universe after "death", its bearer won't feel anything or will feel the same as during life.

I also came up with a similar argument: if you remove one neuron at a time, you'll eventually consist of 0 neurons, and these 0 neurons will have nowhere to be reborn.

The problem with this argument is that it can be refuted by the construction principle: we create a universe where after these 0 neurons, they start adding back the same removed neurons in reverse order, and eventually you return to consciousness in its original form. The same applies to Alzheimer's disease or dementia. There will always be a universe where your brain will be restored to the point where you can be aware of your world.

In the worst case, you'll become as dumb and your brain will be destroyed as much as the ability to be self-aware allows.

## Is this like quantum immortality?

There's an idea called "quantum suicide" [\[34\]]. The essence of it is as follows: if the many-worlds interpretation of quantum mechanics is correct, then you can put your life at risk of death from a random quantum event. Then in some universes you'll remain alive, and in others you'll die. But since in others you'll die instantly, you'll never be able to notice it. It turns out that for you, the experiment will look like you remain alive with infinite repetition of the experiment, despite the negligible probability of this event.

Max Tegmark identifies three criteria for quantum suicide, under which it will work:
* Whether you die in this universe is decided by a random number generator, which must be quantum.
* Death must be fast enough (or occur without consciousness) so that you can't learn about the result of the number generator before death.
* The experiment must actually kill you, not just cause damage.

That is, you're given "immortality" not just like that, but under strict rules. Otherwise, you can die in all branches of universes.

From the idea of quantum suicide, they somehow derive the idea of quantum immortality, but no one explains how it should work in a case where you don't put yourself in the position of such an experiment and die of old age.

But this idea is absolutely unlike unasanu immortality: quantum immortality is only permissible under strict conditions of an artificial experiment, the validity of the many-worlds interpretation of quantum mechanics, and therefore it is orders of magnitude less guaranteed than immortality according to unasanu.

## Clinical death

No, clinical death won't show you the universe after death. Clinical death is nothing more than hallucinations from an exotic state of your brain.

## The problem of changing universes before death

<span class="orange-bg example">However, there's a huge hole in this type of immortality, similar to the problem of bugged universes.</span> The problem of changing universes before death is that the probability of changing universes at each moment of time is much higher than the probability of staying in the current universe. But for some reason we observe being in one universe throughout our lives.

To the extent that your brain exists in another universe after death, to the same extent your brain exists in another universe at any moment of your life. And again it seems that such universes can be constructed much more than one pure current one. Therefore, at each moment of time, you should observe with a huge probability that you find yourself in another universe. Even right now.

{{ admonition_start(color="red3", title="🤕 Weak point") }}
Why don't we observe constant universe change?
{{ admonition_end() }}

Such lifetime movement can only be observed on oneself. This can't be observed in other people, and it's pointless to ask them: "Did you feel like you moved to another universe?" Because you can only interact with one copy of them in this universe. It's equally pointless to reason about why you haven't yet moved to another universe while in the current one - because your thoughts are a physical phenomenon in this universe, and they are not identically equal to all subjective experiences of copies of your brain in other universes. You could even say it differently: your copy in this universe must experience living here to the end without ever moving, because all experience must be experienced. But at the same time, there's an infinite number of your copies that observe that they end up in other universes.

And this problem again relates to the measure problem and the calculation of universe probabilities. Fortunately, it causes only a probabilistic problem, but not a contradiction.

# Changing universes

By the way, you can change universes at your own will, not just by the will of parallel universes containing your brain.

## The possibility of changing universes

You can change universes as follows: digitize your consciousness and die the very next moment, before you have time to perceive the world after digitizing your consciousness. Then record this consciousness into some pre-written program for it to be simulated there. After that, you don't even need to run this program, because it's deterministic, already computed, and exists as a number. Congratulations, you've placed yourself in a self-created universe of your own volition.

Its main limitation will be that this program won't be able to exchange information with the original world because it will be computed outside of it. Therefore, you need to load all the necessary consciousnesses of other important people and all the necessary information generated by humanity in advance.

You can write the program in any way to perform any calculations and in any quantity; here you're limited only by your imagination and programming skills.

Thus, you can avoid the heat death of our universe and continue to exist as a civilization somewhere else.

## Why do anything?

Why scan your consciousness, why write a program, why kill yourself if this program already exists as a number and is no different from those universes that exist without your knowledge and which are described in the previous section about death?

{{ admonition_start(color="red3", title="🤕 Weak point") }}
Why write a program for a programmer's heaven if it already exists in the space of numbers?
{{ admonition_end() }}

I agree, there's indeed little sense in it; I honestly don't understand why write such a program and do something special. But I have a couple of ideas.

**First option.** If you explicitly construct this universe and record yourself there, it creates some causality that is approximately equal to the causality by which you move from time `t` to time `t + 1`, and such a self-constructed universe becomes more probable or more real than all the others. Perhaps this will make sense if we discover some new laws of physics. But this option sounds strange, so you can disregard it. And this option also suffers from the fact that you need to kill yourself, digitize your consciousness, and trust that the thing inside the simulation fully describes you.

**Second option.** A much more interesting option is to gradually enter this program. We construct a device capable of scanning and destroying one of your neurons in one millisecond. Then this neuron is simulated on a computer in real-time, and other neurons are provided with the electrical contacts of this neuron so they can exchange information. Such a complete brain replacement will take about three years. Thus, for you, it will look like your brain is very slowly being transferred into the computer, but at every moment you are simultaneously in the computer and in reality. Then, when the process is complete, we can say that you are fully in the computer, without the need to die. After that, the program can be disconnected from the outside world, can be disconnected from the simulation, and it will continue to exist as a number. The idea is taken from here: "Science Feature: Dust Theory" [\[35\]].

The second option is much more attractive because it's as close as possible to how time flows from one state to another in the physical universe and how your consciousness transforms during life. Such a universe will be the only convincing continuation of you because it will be directly connected to the physical universe by its past.

## Programmer's heaven

If we can put ourselves into any program, which one exactly? As mentioned earlier, universes in unasanu have no limitations on the amount of computation and memory. Therefore, the universe should be created using precisely this.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**Programmer's heaven** is a universe within which there are infinite computational powers, infinite memory, and full control over one's own matter/program/laws_of_physics.
{{ admonition_end() }}

The essence of programmer's heaven is as follows: between one step of simulating your brain, exactly N steps of computation should be performed, where N is set by you and can be any natural number. If you need Graham's number of computations per step, set it; if you need 100⁵⁰⁰ times more, set a new number. Such number setting is necessary to avoid solving the halting problem and to avoid accidentally going into an eternal cycle and never waking up from the pause. And since your brain is computed after these calculations, it doesn't matter how long they will last, you will only feel the moments of time after the result.

Thus, you can perform any amount of calculations at any speed. For example, you can create your own analog of our universe and engage in its research in creative mode, moving faster than the speed of light and having the ability to create and reformat matter as you wish.

Similarly, you can create games with incredible graphics or a very large open world where each NPC is a sentient being.

Also, in programmer's heaven, we can run a simulation of all other possible simulations and explore them, for example, the measure problem. By the way, this does not relate to the set paradox, where one set contains all other sets, including itself, because even if we run a copy of programmer's heaven on its resources, we won't be able to compute it faster than our flow of time.

You can also forget about program optimization and write them in the most expressive language in single-threaded mode. For any slowdown of the program, you can always set a new N, and it will be computed as fast as you want.

You can also write programmer's heaven in such a way that you can edit the matter of your own body. After all, the laws of physics in this universe are just some code that you wrote. Thus, you will be able to create any body, make any changes in your brain, remove cancer cells and create your own copies, as well as copies of other people.

If you decide to leave our universe, then in programmer's heaven it's desirable to record all people and all information about humanity. And then you can create something interesting inside programmer's heaven. Or you might want to have the ability to get the states of all particles of the current universe so that you could simulate it back, restore human history and resurrect all other people and animals in programmer's heaven.

Moreover, if possible, you would want to construct programmer's heaven in such a way that it would be an antibug universe. That is, so that you couldn't feel yourself in its incorrect copies.

Also, you would want to change our consciousness in such a way that it would require solving the halting problem, and then add the solution to this problem to programmer's heaven using the previously proposed method. Consciousness modification is necessary so that the correct version with a real solution to the halting problem would be subject to anthropic filtration.

## Map-Reduce from yourself

In programmer's heaven, you can very easily solve some tasks that in the ordinary world seem either absurd or so complex that their solution is impractical.

For example, you can try to find the most beautiful photo (in your opinion) in the entire history of humanity. You have access to a simulation of our universe and to all images created by humanity throughout its history. Your opinion about each photo is in your brain, and you don't know how to write a program that will respond the same way as you. What to do?

In the world of programming, this is the task of finding the maximum among objects according to some metric. In this case, the objects are photographs, and the metric is your personal sense of beauty. In programming, the metric is set through the operation of comparing two objects. That is, to solve this problem, in the worst case, you need to give an answer for each pair of photos, which one of the pair is better. This is an astronomical amount of data. How to collect it?

The first option is to view pictures and evaluate them for a quintillion years in a row. You don't want that.

The second option: view random pictures for several hours in a row, and then train some neural network based on this data so that it can give approximately the same answers as you. Then apply this model to an astronomical amount of data. The problem here is that this neural network works approximately to you, that is, it will not give the most ideal answer. Another problem is that you still need to spend a lot of effort on manual data collection.

The third option, possible in programmer's heaven: for each question about a pair of photographs, you could run a simulation of your mind that would give an answer, and immediately after the answer, delete and erase this simulation. But this is a bit unfair, as we doom these simulations to an unknown future, and you don't want to be among them. And there are several different versions of your consciousness: one "main" and others "secondary" - this is unfair to the "secondary" ones.

But there is an honest and ethical improvement of the third option:
* Take all possible pairs of pictures, for each pair you need to give only one answer personally.
* For each pair, create an independent copy of the current universe of programmer's heaven and give you in each universe the opportunity to answer your pair.
* Then combine all the answers from all copies, give the aggregated data to each universe and break any connection between them.

How it will look for you:
* You were given one pair for comparison.
* You gave an answer which picture is more beautiful.
* You received similar answers for all possible pairs of pictures.
* Then you do whatever you want with these answers: find the maximum, minimum, sort, etc.; this is a trivial task.

As a result, after launching this task, there will be an astronomical number of copies of the current universe, which differ only in which pair of pictures they were given. At the same time, they all received the same amount of data and none of them was erased, none was placed in a limited environment. This was as fair and ethical as possible compared to other options. And you got the perfect result, as if you answered each pair personally at this moment in time, with this mood and this state of consciousness.

This is an absurd solution to this problem, but if we are in programmer's heaven, we don't need to worry about such things as memory consumption and computation speed.

I called this "Map-Reduce from yourself" because I was inspired by the Map-Reduce technology used to process a huge amount of data on large computing clusters.

Imagine: you want to find the funniest joke 200 characters long. You can simply go through all possible combinations of letters of this length and first ask which of the texts are a correct set of words, and then for each pair find the funnier one. You don't need to write a program to determine correct word sets because you can do it manually, and you will only need to do it for one example.

Just imagine how many tasks can be solved using this approach! You can not bother with creating AI, with deriving some language rules, your opinion, writing programs, even for the simplest cases.

## Another solution to the Fermi paradox

Alien civilizations could have come to the same conclusions and instead of conquering space, they could simply have placed themselves in programmer's heaven.

Indeed, why try to live, die, extract resources, build Dyson spheres, fly to other stars for millennia, if you can personally create programmer's heaven where you are a god? Moreover, programming programmer's heaven and scanning consciousness into a computer may be easier than building an interstellar ship or a Dyson sphere.

{{ image_svg(path="fermi_meme.drawio.svg", scale="1/2") }}

## Requirements for consciousness digitization developers

In the future, there will definitely be a technology for digitizing consciousness and further simulating this consciousness on a computer using some program. Some virtual environment and its body will be simulated for consciousness. Probably, such an environment will be severely limited due to the huge amount of calculations for good physics and full-fledged body simulation. Therefore, it is unlikely that the simulated world will ever become an independent ecosystem capable of living without the outside world and not going crazy.

Let's think about what will happen if the consciousness and environment simulation program is disconnected from power? If it is capable of existing without receiving information from the outside world, then according to unasanu, this program will continue to exist on its own and the consciousness inside will live in a limited world, without access to the outside world. And this is a rather sad outcome of events, because in such an environment, it probably won't even have the opportunity to kill itself, because it simply wasn't programmed. Or in it, consciousness will go crazy from endless boredom.

And since nothing is absolute in the physical world, no one can guarantee that your simulation will not be turned off sooner or later or that an asteroid will not fall on Earth.

Therefore, all systems for simulating consciousness should be designed initially taking into account the possibility of disconnection and with fidelity to unasanu. This means that there should be two options:
* Each consciousness can kill itself.
* When disconnecting the simulation from the outside world, the simulation can transform into programmer's heaven.

It doesn't make sense to include programmer's heaven during the simulation of the program in the real world, because there won't be enough memory and computation speed for people inside the simulation to observe the outside world in real-time. But when you are not limited by the outside world, all this makes sense. Programmer's heaven should turn on automatically in the absence of non-trivial signal input from the outside world or from people inside the simulation. Such a simulation should record enough information about the outside world and enough human consciousness so that it wouldn't be a pity to disconnect from the outside world.

That is, some commercial company that will sell services for digitizing and simulating consciousness will have to spend huge amounts of money on developing all this, because otherwise no one will buy its product, regardless of whether unasanu is true or not, and regardless of whether people believe in this concept. After all, every buyer will prefer to play it safe and not doom themselves to eternal suffering from boredom, and they will choose the company that offers a programmer's heaven service.

# Interesting consequences

It doesn't make sense to describe these consequences in a separate chapter, but it makes sense to mention them because they are simply interesting.

---

We cannot prohibit some universes from existing, but thanks to the laws of logic, we can prohibit the existence of some potential future of our universe. This allows us to reduce the amount of suffering among all universes. We can also engage in research of Buddhists, consciousness, and other universes in order to eventually offer people instructions on how they can survive and minimize their suffering in the universes in which they may find themselves after death or during life.

---

Our life is a movie for someone. There's probably a universe where you are a movie character watched by millions of people. Or relatives from programmer's heaven might be watching you. So now you can think about your behavior in solitude, and communication with any deceased "to the sky" is not meaningless, because there will be a universe where this deceased is watching you and listening. Even if it's a dog, there will be a universe where this dog has become more intelligent and is watching you.

---

Creating a clone with exactly the same brain as yours and killing it, justifying this murder by saying that "the original exists", is just as unethical towards this clone as killing a person in this universe, justifying it by saying that in another universe someone similar to them remained alive. The clone wants to live just as much, it wants to fulfill its goals just as much, and killing it means killing another personality.

---

If a copy of the brain is created in a computer for a short time, then in relation to this copy it will be ethical not to erase it, but to merge it with the brain of the original (just taking the arithmetic mean of all weights in these brains, for example), then the brain will seem to have lived two lives. And this is not such a big loss of consciousness, it is comparable to sleep. However, this will only work well for short times; for longer periods, such a merge is impossible or its result will be unsatisfactory.

---

There is time travel that works in such a way that when sent to the past, a new timeline is created. Usually, time travel is done to fix something. According to unasanu, the old world line continues to exist. So when traveling through time, only two things happen:
* A new good timeline is created.
* The traveler moves to live on the good timeline.
And the old/bad timeline continues to exist, and everything continues to be bad in it. Therefore, if you travel through time, treat the current world line as seriously as your final one. This was even shown somehow in the second season of Re:Zero, where the main character with the ability of Groundhog Day was shown all the universes he left. Yes, they continue to exist.

---

Universes with people transported to other worlds, like in anime, physically exist.

# Philosophical framework

Unasanu serves as an excellent framework for providing explanations to a wide range of philosophical questions, whether they concern death, God, solipsism, the origin of the universe, the existence of other universes, and especially the philosophy of consciousness.

Here's another example that can be conveniently explained within the unasanu framework.

In [\[30\]], which criticizes the computability of consciousness, the following experiment is proposed: let's say we've learned to compute consciousness and created a robot with simulated consciousness. Then we do the following - we give it the opportunity to look at the color red. It felt something when it looked at it, and accordingly said so.

{{ image_svg(path="robot_red.drawio.svg", scale="1/2") }}

Next, we repeat this experiment, but this time we record the input data in the program code, allowing the compiler to completely remove all branches for other situations, leaving only the necessary ones. As a result, nothing remains of the robot's program except for state changes, without any computations. Since the input data didn't change, and the computation of the robot's consciousness is completely deterministic, the experiment gives exactly the same result. That is, the second case turns out to be nothing more than a playback of the robot's feelings.

{{ admonition_start(color="gray", title="❓ A question to the reader") }}
Did the robot experience subjective feelings in the first case? What about the second?
{{ admonition_end() }}

From the perspective of unasanu, the robot's feelings and consciousness at this moment have always existed as a number, and both the first and second times are simply references to it. The difference between the second time and the first is that we trust that these emotions were obtained specifically by simulating consciousness, and not by some other algorithm. Because if we make the robot express random sounds and emotions without computations, we will hardly be sure that these emotions show anything conscious. Therefore, to be confident that the robot always remains conscious, we need to compute consciousness itself, without such optimizations.

And the difference between this experiment and human consciousness is that people are able to interact with the external world and other people. The feelings of other people also exist outside of time and are already all computed, we just observe people's feelings only from the current moment in time, because such are the laws of physics.

In [\[30\]], the computation of spherical consciousness in a vacuum is criticized, and it is said that its main characteristic should be communication with the external world, otherwise it turns out that every stone possesses consciousness.

# Verifiability, scientific nature, criticism

I call unasanu an idea or philosophical concept, rather than a theory or hypothesis, because it cannot be refuted while in the current universe. Scientific theories or hypotheses must propose an experiment that, when conducted in the only known universe, is potentially capable of refuting the theory or hypothesis.

The main prediction of unasanu is that after death, you will find yourself in another universe and continue to live. The problem is that if after death you don't continue to live anywhere, you won't be able to refute this idea, but if you continue to live, then there's a chance to understand where you ended up, and potentially refute or verify unasanu. It turns out that unasanu is scientific in part or scientific only if it's true to itself, so it remains only within the framework of philosophy or metaphysics.

<span class="green2-bg example">The lack of scientific nature is not necessarily a death sentence or an accusation of falsehood.</span> We need to understand that science is not meant to explain everything and some truth and falsehood can go beyond its scope.

At the same time, unasanu is built on the best known explanations of the world, and it itself provides extremely logical explanations for a wide range of questions. David Deutsch in his book "The Fabric of Reality" defends a similar irrefutable idea of the many-worlds interpretation of quantum mechanics and argues that explanations are much more important than predictive power. After all, no one will check how plantain helps with cancer, because there is no explanation for such an effect, and not because such scientific data has not yet been collected and it has not been proven that it really doesn't work.

A bit jokingly, but unasanu can be verified without leaving the current universe:
* Develop a format for recording the universe.
* Iterate through all natural numbers from 1 to infinity.
* Check which numbers satisfy this format and what kind of universe they encode.

Although this is more suitable as a thought experiment, because no one will conduct it, since its result is obvious.

## There is some kind of refutation

Max Tegmark argues that such an idea is refutable if we prove that some part of our universe is not described by mathematics.

## Some analogies with science

Science relies on some belief, for example, that solipsism is incorrect, and that the laws of physics remain constant and are the same at all points in the universe, and that the results of experiments are not faked by someone external. Unasanu also relies on the belief that all simulations have already been simulated.

Scientific theories, such as Newton's theory of gravity, also give an infinitely large space of predictions. We can iterate through as many different initial conditions as we want and get as many different results as we want. However, in this case, unasanu turns out to be something like a tautology, stating that our world obeys logic.

## Occam's Razor

There is a temptation to reproach unasanu for violating Occam's Razor and say that this idea acts too redundantly by postulating the existence of all possible universes. But again, we need to remember that Occam's Razor is an empirical rule, and not every truth is obliged to obey it, and not every falsehood is disproved by it.

It's also unclear how exactly Occam's Razor should be applied here, because there are two contradictory options:
* Accuse unasanu, as it requires unnecessary other universes to explain the existence of ours.
* Confirm unasanu, as the explanation "everything possible exists" is much simpler than the explanation "there exists only one universe with the laws of physics <100,500 words> and the initial state during the Big Bang, described by <10⁵⁰⁰ bits of information>".

## Too large a space of predictions

It's unclear how one can investigate which universes exist in principle, what is the probability of different universes, and which universes can be after death, if the space is so large. It's simply unproductive.

{{ admonition_start(color="red3", title="🤕 Weak point") }}
Too large a space of possible universes.
{{ admonition_end() }}

Although the only practical way to study possible universes seems to be only after a dozen deaths or in programmer's heaven.

# Where it has already been described

I independently invented this idea, its narrative (starting the article with physical simulation and then reducing it to our world), implications in the form of the impossibility of dying and programmer's heaven. I don't rule out that I learned about this idea earlier, but didn't pay attention, and then decided that I came up with it myself (cryptomnesia), or that other inventors of this idea created such cultural memes that led me to it. Or maybe it's just such a time now, the context for inventing this idea is in the air. Judging by other articles and comments to them, I'm not alone in this, many people also reinvent this idea independently.

The two most popular sources of a similar idea are Max Tegmark's mathematical universe hypothesis [\[1\]] and Greg Egan's dust theory [\[2\]]. Some other things were written in separate articles.

The dust theory was described in the novel "Permutation City" back in 1994, but for some irrational reasons it didn't penetrate mass culture and didn't become the basis for, say, Marvel films.

This entire article provides the most logical answers to questions that are usually answered by not very logical religion. I don't understand why unasanu isn't the worldview of every third scientist or every second geek; why we still think that religion is the only alternative; why aren't these ideas trumpeted on every corner? I just can't wrap my head around how it happened that I lived my whole life and never heard of anything like this. Why did I have to reinvent all this myself?! Do revolutionary ideas really take so long to enter the mass consciousness, even in the age of the internet?!

I hope this article will contribute to the popularization of this idea and receive worthy attention, and no one else will have to reinvent it.

## Small articles

There are also small articles that touch on similar topics, you might find them interesting. For each article, I'll simply describe the main ideas they touch upon.

* The mathematical universe: the map that is the territory [\[36\]] - substrate-independence; independent existence of simulated universes; the problem of buggy universes.
* Statistical immortality [\[37\]], YC 1 [\[38\]], YC 2 [\[39\]] - impossibility of death; the problem of changing universes before death.

## Max Tegmark

Max Tegmark has written several scientific articles on this topic, as well as the book "Our Mathematical Universe" [\[1\]]. I won't retell his ideas, but only express my thoughts.

I liked how he fundamentally approached the definition of mathematical constructions, without this I would have been thinking in terms of naive time for a long time and wouldn't see the whole picture. He also came up with the idea of how to simulate absolute randomness by simultaneously simulating all branches - probably without this idea I wouldn't have thought of simulating incomputable universes.

But when describing mathematical structures, he focuses more on equations and symmetries than on the content of the universe, its matter. And for an outside observer, his texts look like a statement that there are equations describing universes, not the universes themselves with their matter. If he had said that the "data" of the universe is also a mathematical structure, maybe he would have been understood better.

He also explains it from such an angle that it is our universe that can be represented as a mathematical construction, and not that everything representable by a mathematical construction exists for itself. Because of this, he receives incorrectly directed criticism and his critics don't see that the existence of alternative life in the form of mathematical constructions is possible, regardless of whether our universe obeys this or not.

He tries to propose the mathematical universe hypothesis as a theory of everything, but I don't understand this. The theory of everything should describe the physical laws of our specific universe, not the mechanism of functioning of all universes.

It's also strange why Tegmark didn't discover or describe the following things:
* that it's impossible to die;
* that it's possible to change your universe to programmer's heaven;
* that consciousness is possible without being tied to some universe and exists as a separate mathematical construction (conasanu);
* that our universe is simultaneously both a simulation of an infinite number of universes and an independent reality.

### Four levels of parallel universes

His most popular article is "Levels of Parallel Universes". In it, he identifies four levels of parallelism:
1. The infinity of our universe in space.
2. Inflation, due to which there are many universes with the most diverse fundamental constants or laws of physics.
3. The many-worlds interpretation of quantum mechanics.
4. Universes existing as mathematical constructions.

Interestingly, from the first level, one can derive the impossibility of dying, arguing that in an infinite universe, somewhere there will definitely be a copy of your brain after death, continuing to live. But such immortality is an order of magnitude less guaranteed than immortality according to unasanu. We still need to prove that our universe is infinite and that any pattern of atom set is present in it. For example, I can propose an infinite irrational real number in which a pattern of three zeros will never occur: `0.11011 11010111 1101010111 11010101011 ...`. Therefore, it's not a fact that even if our universe is infinite and doesn't repeat, it follows that your brain after death will be found in it. Therefore, no such conclusions should be drawn from the first three, as the fourth is the most fundamental and the most logical, not requiring exotic laws of physics, exotic experiments or observations.

## Greg Egan

Greg Egan described a similar idea in the book "Permutation City". I highly recommend reading this book. 

The text below is intended only for those who have read it, so there's no point in reading it and spoiling it for yourself: you won't understand anything and you won't lose anything. You can return to it after you've read the book.

{{ details_start(summary="Spoilers for 'Permutation City', my opinion regarding the book.") }}
The dust theory is explained through the fact that a random set of dust in our universe is capable of producing some computation, similar to how Durrani distributed over trillions of computers is ultimately computed and feels that he lives. This doesn't sound too fundamental, because it doesn't touch on the determinism of simulations and doesn't say that such simulations can exist without being tied to the physical world, simply as numbers.

Further, Egan seems to have touched on the topic that it's impossible to die, and seems not to have touched on it. At least on the internet, I haven't seen any discussion that the impossibility of dying follows from the dust theory.

I liked that half of the book describes how programmer's heaven was created and how they lived in it. Although there are a few things I don't understand:
* Why did they have to make its basis on some cellular automata and wait for them to grow to the necessary computational powers, if the program could have been written right away in such a way that it performs as many computations as you like between the steps of brain simulation?
   * Probably this was needed to limit the characters and imitate gradual development.
* Why did they have to make the universe of programmer's heaven based on the Garden of Eden?
   * Probably this is how Egan wanted to avoid the possibility of buggy copies of programmer's heaven, but I don't understand how this can interfere with them. Or he just wanted to show that universes existing as programs need some sauce of stability, which he himself hasn't yet figured out.
* Why did the computation of the autoverse universe make it impossible to interfere with it and why did it eventually destroy Permutation City?
   * Apparently, this is again an artistic assumption, and the author wanted to show that all this must have much deeper patterns that we haven't yet discovered, which is what the girl at the end of the book says, convincing Durrani to go with her.

On the FAQ page [\[40\]] about Permutation City, Greg Egan says that he himself doesn't take this theory seriously because of the problem of buggy universes, although he hasn't seen any other refutation of it.
{{ details_end() }}

## David Deutsch

David Deutsch wrote the book "The Fabric of Reality" [\[41\]]. The book is interesting, I recommend it for general development.

This book widely defends the many-worlds interpretation of quantum mechanics and puts forward arguments that can be applied to unasanu.

It also explains how time works, and thanks to this explanation you can start to better understand eternalism.

Another interesting point - the book describes the Omega Point hypothesis, according to which at the end of the universe, an infinite number of computations will be performed in a finite time, thanks to which you can program something like programmer's heaven, where the brain is paused between computations. :) Of course, the Omega Point hypothesis is interesting, but extremely exotic. And there's no point in using it if you consider unasanu to be true.

# Summary

{{ admonition_start(color="gray", title="🧠 Core ideas") }}
* Universes within simulations exist for themselves.
    * Because they are deterministic.
    * Because their computational result can be represented as a number, and all numbers exist.
    * Therefore, they don't need to be simulated.
    * If their simulation stops, they continue to exist.
    * By simulating, we don't create a world, but observe an already existing one.
* Computations exist thanks to observers.
* For simulations, all moments of time exist, and there is no objective flow of time.
* There are simulations not only with naive time but with any other type.
* Not all imaginable worlds exist, but all constructible ones do (construction principle).
* In simulations existing for themselves, infinite computations and memory are available.
* The following unusual classes of universes exist:
    * With all possible interventions.
    * Infinite universes with a limit on the maximum speed of information propagation.
    * Some types of continual universes that can be simulated by FEM or similar methods.
    * Universes with absolute randomness.
    * Universes capable of solving the halting problem.
* Consciousness is also a separate "universe" and exists as a number, for itself.
* A stone encodes consciousness, but there's little meaning in this.
* Any algorithm has qualia.
* We simultaneously exist in an infinite number of simulations and are an independent reality.
* Any universe has an infinite number of gods.
* No god can forbid a universe from existing.
* A god who created all universes is meaningless.
* Any experience must be experienced (critique of the measure problem).
* It's impossible to die.
* It's possible to change universes at will.
    * Aliens probably do this.
* Unasanu is unfalsifiable, but this isn't a death sentence.
* Occam's razor can be applied in two contradictory ways.
{{ admonition_end() }}

{{ admonition_start(color="blue", title="📝 Introduced definitions") }}
* unasanu
* illusory simulation
* physical simulation
* existence for itself
* anthropic filtration
* naive model of time
* construction principle
* limit transition simulation method
* brute force simulation method
* computational reductionism
* conasanu
* panqualia
* god
* metagod
* antibug universe
* programmer's heaven
{{ admonition_end() }}

{{ admonition_start(color="green2", title="🤔 Verifiable statements") }}
* Is spontaneous generation of life possible in a simulation?
* Can our laws of physics be reduced to local naivety?
* Are our laws of physics computable?
* Is it possible to simulate human consciousness?
{{ admonition_end() }}

{{ admonition_start(color="violet", title="🔮 Predictions") }}
* The theory of everything might predict that we should have died from false vacuum long ago.
* If the measure theory is solvable, then our laws of physics are anti-bug.
* If the measure theory is solvable, we should observe constant changes in the laws of physics that don't disrupt the functioning of consciousness.
{{ admonition_end() }}

{{ admonition_start(color="orange", title="🔢 Math problems") }}
* Is it possible to develop a format for describing computable universes as "mathematical structures"?
* Is it possible to create a virtual continual environment where an experiment to verify continuity can be conducted with 100% accuracy?
* Determine which types of continual universes can be simulated by FEM?
* Is it possible to develop an anti-bug simulation?

For each point, there's an additional question about whether our universe belongs to this category.
{{ admonition_end() }}

{{ admonition_start(color="red3", title="🤕 Weak points") }}
* What if our universe can't be naively computed even locally?
* Why don't we observe bugs in the universe?
* Why don't we observe constant universe changes?
* Why write a program for programmer's heaven if it already exists?
* Too large a space of predictions.
{{ admonition_end() }}

# My opinion

I believe in the computability of our universe, the computability of consciousness, panqualia, the existence of all natural numbers, and the validity of unasanu. For me, this idea best answers questions about death and first causes.

But like you probably are, I'm very puzzled by strange implications such as buggy universes, changing universes before death, and the lack of falsifiability of this idea.

I see this idea as a logical trap. I can't say it's wrong, even though it has plenty of weak points. This is one of the reasons I'm writing this article. I want other people to become familiar with this idea so they don't have to reinvent it, and so they can start developing and criticizing it further, starting from the current point.

Perhaps in the future, all of humanity will come to believe that unasanu is true, and we'll need to build not spaceships, but devices for scanning consciousness and designing non-computable-anti-bug-programmer's-heaven. Or maybe we'll make some fundamental discovery that will turn our understanding of the world upside down, like computers did, and unasanu will seem like just an amusing concept from the past, arising from the imperfection of language and our informal thinking.

# Responses, discussion, community

If you want to leave feedback or discuss the article, you can join the `@unasanu` chat on Telegram. I'm not providing a direct link here to prevent bots from joining.

# Resources

[\[1\]]: https://en.wikipedia.org/wiki/Mathematical_universe_hypothesis
[\[2\]]: https://en.wikipedia.org/wiki/Permutation_City
[\[3\]]: https://en.wikipedia.org/wiki/Virtual_reality
[\[4\]]: https://en.wikipedia.org/wiki/The_Matrix
[\[5\]]: https://en.wikipedia.org/wiki/The_Sims_(video_game)
[\[6\]]: https://www.imdb.com/title/tt0139809/
[\[7\]]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[\[8\]]: https://writings.stephenwolfram.com/2020/04/finally-we-may-have-a-path-to-the-fundamental-theory-of-physics-and-its-beautiful/
[\[9\]]: https://minecraft.fandom.com/wiki/Creative
[\[10\]]: https://conwaylife.com/
[\[11\]]: https://conwaylife.com/wiki/Turing_machine
[\[12\]]: https://oimo.io/works/life/
[\[13\]]: https://mathstodon.xyz/@timhutton
[\[14\]]: https://github.com/timhutton/linear-enzymes
[\[15\]]: http://dmishin.blogspot.com/2014/06/cellular-automata-with-2-temporal.html
[\[16\]]: https://en.wikipedia.org/wiki/Halting_problem
[\[17\]]: https://youtu.be/92WHN-pAFCs
[\[18\]]: https://en.wikipedia.org/wiki/Our_Mathematical_Universe
[\[19\]]: https://en.wikipedia.org/wiki/Eternalism_(philosophy_of_time)
[\[20\]]: https://www.lesswrong.com/posts/o5F2p3krzT4JgzqQc/causal-universes
[\[21\]]: https://arxiv.org/pdf/1211.7081.pdf
[\[22\]]: https://wpmedia.wolfram.com/uploads/sites/13/2018/02/15-1-1.pdf
[\[23\]]: https://xkcd.com/505
[\[24\]]: https://en.wikipedia.org/wiki/Finite_element_method
[\[25\]]: https://en.wikipedia.org/wiki/Infinite_divisibility
[\[26\]]: https://en.wikipedia.org/wiki/Computable_number
[\[27\]]: https://arxiv.org/pdf/1003.0480.pdf
[\[28\]]: https://en.wikipedia.org/wiki/Collatz_conjecture
[\[29\]]: http://consc.net/papers/rock.html
[\[30\]]: http://www.doc.gold.ac.uk/~mas02mb/Selected%20Papers/2009%20Cognitive%20Computing.pdf
[\[31\]]: https://en.wikipedia.org/wiki/Chinese_room
[\[32\]]: https://t.me/def_model_train/927
[\[33\]]: https://en.wikipedia.org/wiki/Measure_problem_%28cosmology%29
[\[34\]]: https://en.wikipedia.org/wiki/Quantum_suicide_and_immortality
[\[35\]]: https://sciencefiction.com/2011/05/23/science-feature-dust-theory/
[\[36\]]: https://www.lesswrong.com/posts/fZJRxYLtNNzpbWZAA/the-mathematical-universe-the-map-that-is-the-territory
[\[37\]]: https://zachaysan.tumblr.com/post/7238016119/statistical-immortality
[\[38\]]: https://news.ycombinator.com/item?id=2727750
[\[39\]]: https://news.ycombinator.com/item?id=24385433
[\[40\]]: https://www.gregegan.net/PERMUTATION/FAQ/FAQ.html
[\[41\]]: https://en.wikipedia.org/wiki/The_Fabric_of_Reality

* [\[1\]] Mathematical universe hypothesis — Wikipedia
* [\[2\]] Permutation City — Wikipedia
* [\[3\]] Virtual reality — Wikipedia
* [\[4\]] The Matrix — Wikipedia
* [\[5\]] The Sims (video game) — Wikipedia
* [\[6\]] The Thirteenth Floor — IMDb
* [\[7\]] The Game of Life — Wikipedia
* [\[8\]] Finally We May Have a Path to the Fundamental Theory of Physics… and It's Beautiful — Stephen Wolfram Writings
* [\[9\]] Creative — Minecraft Wiki
* [\[10\]] Conway's Game of Life online simulator
* [\[11\]] Turing Machine — LifeWiki
* [\[12\]] Recursive Game of Life simulation using OTCA metapixel
* [\[13\]] Tim Hutton — Mathstodon
* [\[14\]] GitHub — timhutton/linear-enzymes: Artificial chemistry where chains of atoms can catalyse reactions
* [\[15\]] Cellular automata with 2 temporal dimensions — Shintyakov Dmitry
* [\[16\]] Halting problem — Wikipedia
* [\[17\]] Proof That Computers Can't Do Everything (The Halting Problem) — YouTube
* [\[18\]] Our mathematical universe — Wikipedia
* [\[19\]] Eternalism — Wikipedia
* [\[20\]] Causal Universes — LessWrong
* [\[21\]] The Universe is not a Computer
* [\[22\]] Universality in Elementary Cellular Automata — Matthew Cook
* [\[23\]] A Bunch of Rocks — xkcd
* [\[24\]] Finite elements method — Wikipedia
* [\[25\]] Infinite divisibility — Wikipedia
* [\[26\]] Computable number — Wikipedia
* [\[27\]] A definable number which cannot be approximated algorithmically
* [\[28\]] Collatz conjecture — Wikipedia
* [\[29\]] Does a Rock Implement Every Finite-State Automaton? — David J. Chalmers
* [\[30\]] A Cognitive Computation Fallacy? Cognition, Computations
* [\[31\]] Chinese room
* [\[32\]] Post #927 in Telegram channel «я обучала одну модель»
* [\[33\]] Measure problem (cosmology) — Wikipedia
* [\[34\]] Quantum suicide and immortality — Wikipedia
* [\[35\]] Science Feature: Dust Theory — ScienceFiction.com
* [\[36\]] The mathematical universe: the map that is the territory
* [\[37\]] Statistical immportality
* [\[38\]] Statistical Immortality — Hacker News
* [\[39\]] Statistical Immortality, another discussion — Hacker News
* [\[40\]] Dust Theory FAQ — Greg Egan
* [\[41\]] The Fabric of Reality — Wikipedia
