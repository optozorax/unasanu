+++
title = "unasanu — universe as a number"
date = 2023-09-01
description = "A philosophical concept that explains why any universe exists and what will happen after death."

[taxonomies]
tags = []

[extra]
image = "english.png"
language = "English"
language_flag = "english.png"
toc_text = "Table of contents"
minutes_text = "min"
author_name = "Ilya Sheprut"
license_word = "License"
date_text = "1 september 2023"
lang = "en"
position = 2
+++

# Introduction

{{ admonition_start(color="blue", title="📝 Definition") }}
**unasanu** (= **un**iverse **as** **a** **nu**mber) is a philosophical concept, according to which any simulated universe exists, because it can be represented as an already existing natural number. This concept can provide explanations for the following questions:
* Do alternative universes exist and why?
* Do we live in a simulation?
* Can theoretically a god exist and how omnipotent can he be?
* Why is it impossible to die and what happens after death?
* Is it possible to change the universe without worrying about heat death?
{{ admonition_end() }}

This idea and its implications are logically derived from our current understanding of mathematics, physics, and consciousness. However, unasanu does not require a many-worlds interpretation of quantum mechanics, the infinity of our universe, or the hypothesis of an Omega point — it relies on other, more reliable and simple bases.

The article describes the same idea as Max Tegmark's "Mathematical Universe Hypothesis" [\[1\]] or Greg Egan's "Dust Theory" [\[2\]], but with a greater number of implications and ideas that these authors have not considered, or have considered only superficially.

I write this article to:
* gather all philosophical implications of this idea,
* prevent the reinvention of these ideas,
* steer future research.

# Types of simulations

We are familiar with the idea of simulating the external physical world on a computer. This topic is actively discussed in both pop culture and philosophy. Firstly, it's important to clarify how we categorize different types of simulations. I find that this topic causes a lot of misunderstanding, because people rarely distinguish these two categories.

## Illusory 

{{ admonition_start(color="blue", title="📝 Introduced Definition") }}
**Illusory simulation** is a type of simulation that creates an illusion of reality by deceiving the observer. Another term for such simulations is virtual reality [\[3\]]. Examples of these simulations include the film "The Matrix" [\[4\]], the game "The Sims" [\[5\]] (the world is illusionary for the sims), and the film "The Thirteenth Floor" [\[6\]].
{{ admonition_end() }}

An illusory simulation approximates everything possible. In it, for example, a human might not consist of biological cells or atoms but of a single indivisible object or approximations of organs and limbs. This is necessary to save computational resources and programmers' efforts. A more demanding simulation would make no sense, as it would be impossible to run in real time or program within a reasonable timeframe.

People do not like the idea of living in an illusory simulation. Everyone wants to believe that their reality is real and that nothing intentionally deceives or simplifies them. For good reason, the whole of pop culture about life in an illusionary reality is all about escaping from it.

## Physical

{{ admonition_start(color="blue", title="📝 Introduced Definition") }}
**Physical simulation** is a kind of simulation that purely simulates physics based on some fundamental theory. Meaning, this simulation is accurate down to atoms/quarks/strings/???/pixels/graph vertices. Examples of physical simulations include: the Theory of Everything, John Conway's Game of Life [\[7\]], and Stephen Wolfram's physics project [\[8\]].
{{ admonition_end() }}

A physical simulation emulates low-level laws, with no approximations to simplify this. High-level structures can be built on the basis of these low-level laws (for example, gas laws can be built on a model of gas consisting of elastic particles). What structures arise and according to which high-level laws will these structures function, depends on the structures themselves. In a physical simulation, high-level structures (like a human) are not approximated by something simpler: if there exists a human in such a simulation, they exist down to their cells and atoms.

There is a chance that our reality is a physical simulation. However, this idea is unprovable and irrefutable. If we live in a physical simulation, we are completely fine with it, since everything we know about physics, star evolution, evolution of living beings, remains intact. Stating "from the fact that we live in a simulation, it follows that all this is unreal," is meaningless in terms of a physical simulation, because such a simulation is reality itself. The only downside is that there could be an external entity having control over our physical reality, akin to the "creative mode" in Minecraft [\[9\]]. This hypothetical possibility will be further analyzed.

It's important to remember that **simulation ≠ emulation**. These words seem similar, but they carry utterly different meanings. The world could be very real even if its laws of physics are simulated on a computer.

# The Game "Life"

## Structure

The game "Life" is, in fact, not actually a game or life, but a cellular automaton. I need to talk about this because it’s the most illustrative example of a physical simulation, based on which many analogies can be built that are necessary for this article.

This automaton operates according to the following rules:
* There is a two-dimensional infinite (or finite, closed) square grid.

{{ image(path="../ru/game_of_life_infinite_grid.png", scale="2/3") }}

* Each cell can be either empty or filled.
* In this automaton, there exists a progression of time, which is provided by calculating the next moment of time from the previous one based on certain rules.
* There is a certain initial moment in time, from which we iteratively calculate the future.

{{ image(path="../ru/game_of_life_time.png") }}

* A cell's neighbors are considered to be the 4 directly adjacent cells and 4 diagonally adjacent ones.

{{ image(path="game_of_life_neighbors.png", scale="1/2") }}

* Calculations consist in changing the state of cells based on their neighbors according to the following rules:
    * If a cell was empty, it turns to a filled cell if and only if three of its neighbors in the previous step were filled; otherwise, it remains empty.
    * If a cell was filled, it remains so if and only if two or three of its neighbors in the previous step were filled; otherwise, it turns into an empty cell.
* These rules are referred to as B3/S23 (Born 3/Survive 2 or 3)

{{ image(path="game_of_life_rules.png", scale="2/3") }}

In the following interactive visualization, you can see how this cellular automaton evolves for a random distribution of filled and empty cells:

{{ game_of_life_en() }}

You can play around with more advanced simulators, for example, on `conwaylife.com` [\[10\]].

## Impressive Capabilities

You can construct a vast number of mechanisms in this automaton. Here are some of them.

The first example is the glider from the visualization above. This mechanism moves diagonally. You could say it is akin to a photon.

You can also create a generator for such gliders:

{{ figure_start() }}
<img src="../ru/glider_gun.gif" width="250" height="180">
{{ figure_end(caption="Gosper's Glider Gun.") }}

---

The "Game of Life" cellular automaton is Turing-complete, meaning you can build a computer or a Turing machine on it. Here is an example: (source with interactive simulation [\[11\]])

{{ image(path="../ru/game_of_life_turing_machine.png", scale="2/3") }}

---

In the interactive visualization `oimo.io/works/life` [\[12\]] (works on the phone too), the "Game of Life" is simulated on itself both inwardly, infinitely small, and outwardly, infinitely large:

{{ image(path="../ru/game_of_life_on_itself.png", scale="2/3") }}

---

John von Neumann conceived the cellular automaton and the self-replicating mechanism within it. The image below demonstrates how the second automaton has nearly finished building the third; the lines branching to the right represent the genetic information that is copied along with the body of the machines.

{{ image(path="../ru/von_neumann.png", scale="2/3") }}

---

As another example, here's a model of artificial chemistry developed by Tim Hutton [\[13\]], where he designed specific elements and interactions amongst them to construct an artificial cell capable of self-replication:

{{ video(path="../ru/chemistry.mp4", scale="2/3") }}

Although it's not a cellular automaton, it's not a stretch to see it adapted as such, and the author continues to refine this idea in the form of a cellular automaton [\[14\]]:

{{ image(path="../ru/chemistry_automata.png", scale="2/3") }}

---

I presented all this to emphasize that cellular automata are not just toys, but serious concepts worthy of representing fundamental physics.

## Analogy with Physics

{{ admonition_start(color="gray", title="💬 Quote from the article Cellular automata with 2 temporal dimensions [\[15\]]") }}
Cellular automata serve as excellent representations of 'toy physics', which we understand from the bottom up. In the real world, we observe complex phenomena and can only make educated guesses about the underlying principles (this is what physicists do). The realm of cellular automata is the exact opposite: the underlying principles are known, and the behavior of complex systems is the subject of study.
{{ admonition_end() }}


The "Game of Life" automaton has a variety of intriguing properties:
* Laws of physics and matter are separated from each other.
* Matter can be manipulated freely: drawn upon, copied, inserted, deleted.
* A simulation can be run on any manipulated matter.
* There exists a certain initial point in time.
* Time is the computation of the laws of physics, and a discrete snapshot of the field state serves as a point in time.
* The laws of physics are local - i.e., they only work over a certain spatial area, there is no action at a distance, and thus naturally arises a maximum allowable speed - akin to the speed of light in our world.

However, this automaton also differs from our physics:
* There are no conservation laws (for example, number of cells), but cellular automata with conservation laws can be found for those interested.
* Time can only be simulated forward (not backward), so the possible number of past moments in time can range from 0 to infinity. This is not necessarily a property of our physics as our physics can be reversible (and reversible automata also exist).

The following will assume that our underlying physics _is something akin to a cellular automaton_ (with significant caveats, but I will elaborate on this topic later). Meaning, the properties described above apply to it.

And even if our physics does not resemble a cellular automaton, it serves as a good starting point because understanding how exactly it differs is also beneficial.

# Thought Experiment with Physical Simulation

## Description of the Experiment

Let's imagine a very distant future in which we have advanced to become a civilization that harnesses the entire energy of a galaxy, and have built a solar system-sized computer that optimally utilizes each Planck length.

Next, we came up with the rules for a simple physical simulation, which is modeled after our physics, but does not replicate it exactly. This is necessary because our physics is incredibly redundant and strange with all its quantum mechanics and theory of relativity. We designed this physics in such a way that its chemistry could potentially be rich enough to support and spawn life.

Since we will want to run this simulation on a computer, we have some limitations. Our simulation must be:
* Discrete
* Finite
* Deterministic
* Halting (for each step)

I also want to limit the simulation so that we are only allowed to interfere with initial conditions and never again.

Before we move on to the heart of the experiment, let's clarify each term.

## Discrete physics

There are two types of spaces known: continuum and discrete space.

{{ container_start() }}
{{ figure_start() }}
{{ image(path="../ru/continuous2.png", scale="2/3") }}
{{ figure_end(caption="Example of a continuum") }}
{{ figure_start() }}
{{ image(path="../ru/discrete2.png", scale="2/3") }}
{{ figure_end(caption="Example of a discrete space") }}
{{ container_end() }}

<!-- https://www.desmos.com/calculator/iuoa2bl8uc -->

A discrete space of finite length can be divided into a finite number of elementary units. A continuum of finite length contains as many numbers as the interval (-∞; +∞), meaning it can be infinitely divided, with each number having an infinite number of digits after the decimal point.

Obviously, it's not possible to directly incorporate a continuum into a computer. Therefore, all our simulations operate with a finite number of discrete objects. When we simulate physics, we use discrete approximations.

Indeed, there is an intriguing connection between the discrete and the continuous. For instance, the laws about the behavior of waves (oscillations, periods) are built on the concept that the medium in which these waves propagate is a continuum. Yet, we know that all fluids, gases, and solid materials consist of discrete atoms, just in an extremely large quantity. Therefore, some continuous physical laws, while beautiful, are in fact just an approximation of functioning on a discrete basis.

Similarly, it can be suggested that quantum mechanics works in this manner, but this is only a hypothesis, and not necessarily accurate. In our thought experiment, we want to establish a physics that is fundamentally discrete, but without disrupting the possibility of it appearing continuous on a larger scale.

## Finite physics

The framework here is straightforward - the space in our simulation has to be finite, because we cannot handle an infinite number of objects. For our experiment, it is enough to take a sufficiently large distance.

## Deterministic physics

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Determinism** is a property of processes indicating that a process will always yield a single outcome for given initial conditions, no matter how many times it is initiated.
{{ admonition_end() }}

Determinism implies that the future of the simulation is unambiguously defined, with no fundamental randomness involved. This is a logical requirement because computers can only perform deterministic calculations and are not capable of absolute randomness.

{{ admonition_start(color="red2", title="⚠️ Note") }}
Some might argue that data races, uninitialized memory, and cosmic rays can be a source of true randomness. Let's agree that, for the sake of this thought experiment, the code is executed on a single-threaded virtual machine in a perfect environment, where every new allocated memory for it has been zeroed out in advance. Hence, we will be only dealing with deterministic simulations.
{{ admonition_end() }}

Processes in our world appear deterministic, even though predicting certain events can be extremely difficult. Deterministic processes can also possess chaos, meaning a deterministic world could still resemble ours, and this requirement doesn't significantly diminish our physical simulation.

The simulation of completely random processes will be further discussed in the upcoming chapters.

## Halting Physics

This doesn't imply that there has to be a step after which the simulation should stop (such as heat death), rather, it means that each step of the simulation should take a finite and predictable number of steps to complete. This means that within the computation of a single step of simulation, there should be no occurrence of infinite loops or anything similar. This requirement is essential because it doesn't make sense to run a simulation that might go into an endless loop at some crucial point and then fail to deliver any results.

Moreover, this requirement is necessary because we don't want to solve the halting problem [\[16\]] (a good video on this topic [\[17\]]), which is impossible to solve in general.

## Running the Simulation

The creation of such physics doesn't seem impossible. Therefore, in this thought experiment, we've found a suitable candidate. However, you're free to disagree with the notion that the creation of such physics is feasible.

Next, we implement these physics over a finite space on our supercomputer and wait for life to spontaneously emerge. If it doesn't, we can play around with the initial conditions a little - adjusting the optimal number of necessary atoms, or positioning a dust cloud at an ideal distance away from its star so that it's within the habitable zone, and so on.

Suppose we've managed to find such initial conditions at which life emerges, and then we run this very long simulation and wait until it evolves into intelligent beings capable of communication through a form of language.

It's highly likely that these creatures possess something akin to a survival instinct, derive pleasure from food, experience suffering from physical injury, and have sexual impulses. This is a logical evolutionary path for individual creatures with brains. Creatures without these traits will likely prove less successful in a survival framework and would be eliminated by the process of evolution.

{{ admonition_start(color="gray", title="❓ Reader's Question") }}
Please pause and answer the following questions. It would be even better if you could explain your answers.

Do you believe these creatures feel alive? Do they perceive their world? Do they have subjective experiences aka qualia? Are they truly alive?

If you don't think they feel anything, then suggest what properties a simulation would need to possess in order for you to consider the creatures within it as sentient.
{{ admonition_end() }}

Your answer to this question will affect how you interpret the rest of this narrative.

I've detailed this simulation to align your perception of these creatures as close to humans as possible, without directly referring to our world since it's uncertain how successfully we can simulate it. The main point being, everything described seems hypothetically plausible. That's because, thus far, we haven't discovered any foundational laws that would prohibit beings within a physical simulation from having intelligence or feelings.

I hope you answered positively to the question about whether these creatures feel something or not. The argument "they don't feel anything just because I know they're in a computer" is too lazy. You should try to refute it intelligently.

But if you disagree with me, it's not a problem. I will consider that viewpoint as well.

Let's assume that these creatures are alive, that they feel life, can communicate about it, and ponder questions of God or their existence in a simulation. We do not interfere with their world, so they can't figure out what our intentions are, nor do they have any reason to question the reality and sincerity of their physical world.

{{ admonition_start(color="green2", title="🤔 Testable Claim") }}
Is it possible for life to spontaneously emerge in a simulation? 
{{ admonition_end() }}

## What if we stop the simulation?

{{ admonition_start(color="gray", title="❓ Question for the Reader") }}
What do you think will happen if we stop the simulation? Will the creatures within it die? Or will they not die but lose their sense of life? Or will they somehow continue to live by some miraculous means?
{{ admonition_end() }}

Surely, you might say that they will die, because how else could it be? When we are simulating them — they live. When we turn them off — they don't live. It's that simple. But no. <span class="green2-bg example">I contend that these creatures will continue to live even after the simulation has been turned off.</span>

As I mentioned, our simulation has some fundamental limitations without which we cannot run it on a computer. One of these is **determinism**. Determinism means that there is only one possible outcome for a given program, given the initial conditions, and provided there's no subsequent interference in the program. This raises another question: if the future is set, why do we need to simulate it? What changes from the fact of our simulation? We cannot influence the future regardless; it will be exactly as it's meant to be.

If this is not enough to comprehend the power of determinism, here are a couple more thought experiments:
* If we erase all the simulation results and simulate again from scratch, we'll end up with exactly the same outcome.
* If we pause the simulation and resume it a billion years later, the entities within it would not feel this pause. Their sense of time would be dictated by the internal laws of their universe. We exist outside their timeline, and they are beyond ours.
* If we run the same simulation on multiple computers simultaneously, it would not change anything for the entities.
* If the simulation is reversible and we somehow retrieve a very distant moment from the future, then even if we simulate it backward, the entities will not feel as if they're living in reverse.

Of course, this might still not be enough, and I will further demonstrate how one can prove that they remain alive even if we simulate them.

# Universe as a Number

Alright, we agree that the entities are alive when we simulate them on a computer, and it is not enough for us that they have a single future. We believe that their future only exists after we've simulated it.

So, let’s be precise about what we have to claim it as proof that they have lived through a certain stretch of time. All we have is: the simulation algorithm and all the simulation steps up to now. We consider the existence of this information to be equivalent to proving the life of these entities.

Imagine we've run this simulation, gathered all the data and stored it on a large hard drive: first the algorithm, then step 1, then step 2, ..., and finally step N. Now we have evidence that these entities lived up to step N. But, of course, data on a hard drive is always some sequence of zeroes and ones. We can convert this data into one large positive integer. And this integer still serves as evidence of the entities' existence.

{{ image(path="number.png", scale="2/3") }}

Here's the catch: as we know, all positive integers already exist.

So, given that all positive integers exist, this means that among them we'll definitely find the number that we used to encode the simulation of the entities we simulated. But among them also exists the same simulation, but with an extra moment in time. Moreover, any other simulation exists for any point in time within it. All these numbers are equivalent to evidence of the existence of some entities that are represented in these simulations.

From this, we conclude that <span class="green2-bg example">the result of any simulation, that can be run on a computer, already exists as a positive integer</span>. That's where the name of this concept comes from: **the universe as a number**.

{{ admonition_start(color="blue", title="📝 Definition") }}
**Self-existence** is the concept that a universe exists for itself, if living entities within it are capable of observing their own existence and their universe.
{{ admonition_end() }}

Earlier, we agreed that entities in a computer simulation are capable of observing their own universe. Hence, this universe, at the very least, exists for itself. Then we concluded that this existence is equal to existing as a number. Therefore, from the existence of all natural numbers, the existence of all potentially simulated universes follows, each for itself. And consequently, in all such universes where life exists, that life will observe its universe.

I find the example of physical simulation appealing because it doesn't require us to define the term "existence" beforehand. Instead, it's so self-evident that we should derive the definition of "existence" from it. In this case, we come up with the concept of "self-existing". If we agree that these entities have a sense of living within the simulation when we run it on a computer, then we must immediately conclude that they sensed life even before our simulation, existing as a number.

So what happens when we simulate a particular world? In this context, we can say that with a <span class="green2-bg example">simulation, we don't create a world, we observe one that already exists</span>. And computational power is spent precisely on this observation. Choosing initial conditions is not "creating a world", but searching for a world with the properties we need, among an infinite variety of different worlds.

And when we stop the simulation, the entities continue to live for themselves. They can tell other entities in their universe about it, but not us. We can't observe it because we've turned off the simulation.

## The Anthropic Principle

{{ admonition_start(color="blue2", title="📖 Definition") }}
**The Anthropic Principle** is a principle stating that the universe is seen to be finely tuned for the emergence of life and humans as observers, precisely because in other universes that are not so finely tuned, the observer cannot exist.
{{ admonition_end() }}

Unasanu perfectly aligns with the anthropic principle. I articulate it like this: if all possible universes exist, then observers only occur in the universes where their existence is feasible.

The anthropic principle is necessary because physicists have observed that the most fundamental constants are precisely fine-tuned for our existence. If some of these constants were even a percent less or more, life as we perceive it would be impossible. A more in-depth exploration of this topic can be found in the book "Our Mathematical Universe" [\[18\]].

## Argument of Incorrect Calculations

One might object: where then do calculations come from if all we have are mere numbers? I am indeed capable of taking any properly calculated universe, misconstruing it, and that will still exist as a number. Then why should calculations necessarily exist?

### Calculations by All Laws of Physics

There is another similar point to consider. If the universe can be calculated by the current laws of physics, why can't it be calculated by other laws of physics? The fact is that it can be, and according to unasanu, such worlds exist. Suppose we consider the example of the Game of Life. The next illustration demonstrates how the same field is calculated under different rules:

{{ game_of_life_all_rules_en() }}

Try pressing start and then hit the button "Copy from B3/S23" every second. You will see that any state from B3/S23 can be calculated by any other rule, and this exists within the frame of unasanu.

I have only exploited a very small part here (only what falls under the `B/S` notation), but there actually exist infinite ways to calculate the next step of such a field with cells that only have two states.

Obviously, this field can serve as a basis for calculating with all possible rules. The same goes for each moment in time and every rule that can be concocted.

Similarly, nothing prevents us from taking all possible modifications of this field and calculating them using the original rule.

All of this exists according to unasanu, and there are many implications which will be discussed further.

So why don't we observe our universe being computed by arbitrary laws of physics or any computation at all?

### Anthropic Filtering

This can be explained by the fact that it is the observer who maintains the stability of the universe's laws, ensuring the existence of computations and specific laws of physics for themselves. How does this happen?

First, consider the argument of erroneous computations. If the universe is not being computed under any rules, then observers who could observe this universe are simply impossible, because observation itself is a computation. However, if the universe adheres to laws, then an observer in it is possible. Therefore the observer can only observe a computable universe.

Now, let's consider the argument about all possible physical laws; they too are stabilized by the observer. More precisely, he only observes stable physical laws. This is because if the atoms of the brain were computed under some different laws of physics, the brain might stop working and the observer wouldn't be able to observe anything in such a universe.

In some sense, this is similar to the anthropic principle, but it's more fundamental and happens at every moment, not just at the start of time during the creation of the universe. I suggest introducing a term for this.

{{ admonition_start(color="blue", title="📝 Proposed Definition") }}
**Anthropic Filtering** — a principle according to which an observer is able to filter out universes where computations are either not occurring, or occurring incorrectly, as well as being capable of filtering out universes where their emergence or existence is impossible.
{{ admonition_end() }}

As we go on, we'll see that some of these arguments can be applied to anthropic filtering, and some cannot.

### False Vacuum

In physics, there's this state of matter called "false vacuum." Its occurrence is probable. If it ever materializes at any spot in the universe, it spreads out in all directions at light speed, devouring anything that crosses its path. A human being is incapable of observing the existence of a false vacuum because our brains simply operate too slowly. We would likely perish before becoming aware of it, and information about a false vacuum cannot surpass the speed of light.

In this context, a false vacuum falls under the examples of anthropic filtering. This is because, in those universes where it arises, all living entities perish without knowing about it, while other universes that differ by a mere atom, where this false vacuum doesn't emerge, continue to exist. Thus, a false vacuum is subject to anthropic filtering.

So if the laws of physics are filtered by the observer once—upon the universe's genesis or the observer's birth in the appropriate universe—the false vacuum is filtered by observers at each moment in time. And if scientists discover that the possibility of a false vacuum appearing in the observable universe is extremely high but it never does and we continue living, it doesn't contradict unasanu's point of view.

By the way, it could be quite exciting if we construct a theory of everything and suddenly find that any simulation based on it will eventually get destroyed by a false vacuum :).

{{ admonition_start(color="violet", title="🔮 Prediction") }}
If we can develop a theory of everything, and according to it, we should have died long ago from a false vacuum or similar phenomena causing instantaneous death of all things, it doesn't mean this theory is incorrect.
{{ admonition_end() }}

## Eternalism

Some readers might be asking, "But what about time?" Up until now, I've implicitly assumed that universes with their timelines exist as a static chunk of data, completely neglecting the dynamism we perceive due to the flow of time. This perspective is known as eternalism.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Eternalism** is a perspective on time where future events already exist, there's no objective "flow" of time, and the entirety of space-time can be represented as a static, unchangeable "block". [\[19\]]
{{ admonition_end() }}

I argue that eternalism is the correct interpretation of time for simulations. In the following chapters, I reduce our universe to a class of computer-simulable ones, meaning eternalism should be applicable to our time, too. Let's delve into eternalism as it relates to simulations since it's a vital part of unasanu.

<span class="orange-bg example">How does time work for humans?</span> At this time, we only have memories of the past and a sense of the present. We can't directly experience the past or future. We can understand what the past might have been like using physical entities like film recordings, archeological artifacts, and personal memories. We have to trust these. Our communication is limited to people from our own time due to the laws of physics. The existence of future people doesn't necessarily imply we can interact with them beyond living until that time.

<span class="orange-bg example">Why do we perceive time as progressing gradually instead of instantly feeling a random future moment, if it already exists?</span> Because the laws of physics and the structure of our brains dictate that for a 20-year-old human's brain to sense something, it has to first live through those 20 years and retain them. Thus, it's likely that you currently are a brain from a random future moment (perhaps right before your death). It's just that this brain remembers living all past moments in time, which is why you feel like you are living in the present.

<span class="orange-bg example">How does time work in a simulation?</span> In discrete simulations, the future state is atomically calculated from the past state. Within a simulation, it's impossible to perceive time "between the simulation steps", because the internal laws of the simulation itself can only operate over a completed calculation of state. Meaning, there is no fundamental dynamic in a simulation, only discrete static moments in time which are connected by logical relationships, and an observer interprets them as dynamically changing.

To suggest a rebuttal to eternalism in simulations, consider the following: we assume that in our world, time cannot be reduced to static structures. Therefore, if we believe that in some simulation there's time similar to our own, the only way to define it is by attaching it to our time. Thus, time in the simulation flows synchronously with our time as long as we are calculating it.

This can be refuted in two ways by demonstrating that the "current" moment of time in a simulation is not the only one: 
* We create a duplicate of this simulation and simulate it with a delay of one second. So, what time is considered "current"? What time do the entities inside the simulation feel at this "particular moment in time"?
* There exist classes of simulations called "reversible" ones. They can be simulated not only into the future but also into the past. Quantum mechanics is reversible, which means such a simulation could be very similar to our universe. What if we create a duplicate of this simulation and start to simulate it simultaneously into the past and the future? What point in time will be considered current?

In conclusion, we cannot entirely refute the idea that temporal dynamics can't exist in a computer simulation. It can instead be framed this way: a simulation isn't defined by something dynamic, but by static units. There's no paradox in this concept, even when applied to our universe. Therefore, <span class="green2-bg example">the essential property of time isn't its continuous motion, but rather its role in connecting different layers of information through the laws of physics.</span>

One can also propose that time doesn't exist as a global structure, with simulations obedient to its laws. Instead, time exists within the confines of these simulations.

Furthermore, eternalism is neither provable nor disprovable as it is merely an interpretation of the deterministic nature of universes.

It might appear that eternalism implies absolute determinism and requires futures to be singular. However, eternalism is entirely compatible with multiple futures and complete randomness, as will be demonstrated subsequently. One should envision the final 'space-time' block not as a static sausage but as a static tree :)

## Interacting with the Simulation

<span class="orange-bg example">From here on, any established restrictions will gradually loosen.</span>

I've suggested that for this thought experiment we should abstain from tampering with the simulation. But what if this restriction was revoked? Would the simulation become indeterministic? Not necessarily.

Suppose we reach step N of the simulation, and in the atom editor, we decide to eliminate all dictators engaging in wars. The beings inside the simulation would be confused but jubilant. But what constitutes interference in the simulation? It means a sequence of actions delivered to the simulation program. This sequence, too, can be encoded in numbers.

If we record all our interventions and then append them next to the program and specify that they should be dispatched at the appropriate simulation time, we can once more achieve a fully deterministic simulation. This could be run repeatedly and always yield the same result, even though we would interpret its result as one we intervened in. 

All such potential interventions could also be numerically encoded and appended next to the number of the regular simulation program. <span class="green2-bg example">Therefore, all possible universes with all possible interventions also exist, even without the need to intervene directly in them.</span> 

However, we must not forget that just as there exist universes with all possible interventions, a universe continues to exist without any interventions at all.

## Tegmark's Mathematical Structures 

Previously, I implied that the simulation has the following structure:
* There is some initial state `O` of a given simulation.
* There is some function/program to calculate one step `F`, which for each state of the given simulation returns the next state of the given simulation, and the answer always exists.
* The essence of the simulation is to perform the following algorithm:
  * T = F(O)
  * T = F(T)
  * T = F(T)
  * ...

Thus, "time flows" inside the simulation, because we equate one step of time computation to a time step within the simulation. And, time exists globally throughout the universe.

But, in reality, such an interpretation of time is **naive** and doesn't allow for the existence of much more complex universes, such as:
 * Universes with multi-dimensional time (a good article on this topic [\[15\]])
 * Our universe with the theory of relativity
 * Universes with time travel

{{ admonition_start(color="blue", title="📝 Introduced Definition") }}
**Naive model of time** — is such a concept of time, in which time is discrete and exists globally throughout the universe, and the next step can always be computed from the previous one.
{{ admonition_end() }}

Therefore, Max Tegmark's **Mathematical Universe Hypothesis** [\[1\]] comes into play, where he approaches this issue more fundamentally, asserting that any universe, describable by a mathematical structure, exists in a physical sense.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Mathematical structure** — a set of abstract entities with relations between them.
{{ admonition_end() }}

It is known for certain that all naive simulations are subsets of mathematical structures, as the result of a program's operation determines an abstract entity, and the program itself defines a relationship between these entities. It is also known that among mathematical structures are universes for which one can verify through computations that their sections of space-time comply with their own laws. Hence, in such a concept, computations are necessary not to observe the world (i.e., to compute its steps), but to check that a given world complies with its own laws, or to specify it.

{{ image(path="structure.png", scale="2/3") }}

Probably such a description might seem unclear, which is why I'd like to present an example of a universe which appears to function naively, but in reality, does not. An explicit example: time travel with the inability to alter the past. Two appropriate examples that come to my mind are the Harry Potter books and the movie "Inception". Imagine, for a moment, how you'd simulate a world where time travel is possible yet built in such a manner that the past remains unchangeable? You'd have to simultaneously simulate the past considering the future and the future with respect to the past, ensuring both dovetail into each other. Currently, we do not have methods to compute universes with such laws of time travel. Therefore, the only viable alternative is to iterate through all possible worlds (with all possible futures and pasts) and verify which of these comply with the necessary laws. Essentially, the entire world can only be computed in a format of "all of time at once". However, creatures in such a world obviously perceive their own existence and are astonished by their own laws of time travel. You can delve deeper into this topic in the article "Causal universes" [\[20\]].

By the way, there is an article titled "The Universe is not a Computer" [\[21\]], which provides a different perspective on describing physics and offers an approach to compute "all of time at once".

Another example of a non-naive universe is our own universe governed by the theory of relativity. We do not possess a singular global time. In every section of space, time flows at a different speed. Consequently, the entire universe must be represented as a space-time block where time is only a relation between parts of this block.

In both these examples, universes can be approximated by local naivety. For the first universe, we disregard time travel, and for the second, we disregard time dilation. This is why I will continue this discussion in terms of naive simulations because it is simpler and it approximates a vast amount, if not all, possible types of such universes. However, this could potentially be a mistake.

{{ admonition_start(color="green2", title="🤔 Verifiable claim") }}
Do our laws of physics reduce to local naivety?
{{ admonition_end() }}

{{ admonition_start(color="red3", title="🤕 Weak point") }}
What if our universe can't be computed naively, and can't be approximated by naive computations even locally? This would severely affect the conclusions of this article.
{{ admonition_end() }}

{{ admonition_start(color="orange", title="🔢 Mathematical problem") }}
Develop a format to describe computable universes as "mathematical structures". Determine whether our universe could be written in such a format.
{{ admonition_end() }}

## Principle of Construction

If every possible universe exists, does that include the universe of Lord of the Rings, Star Wars or multiverse of anime characters? To answer these questions, I propose the following principle:

{{ admonition_start(color="blue", title="📝 Definition Introduced") }}
**Principle of Construction** - If one can propose a method for constructing a universe and its laws of physics, then such a universe does exist.
{{ admonition_end() }}

For instance, if we have a simulation program for our universe, then (theoretically) we can use it to construct a world where half the people, as of the present time, are replaced by air molecules. Thus, this universe physically exists and someone is experiencing living in this absurdity.

Here, "construct" refers to the process where we take a certain program like "11D Ultra Atom Editor", load our current moment in time into it, make edits, and then continue simulating the resulting set of atoms from the edited moment. 

Can we create a precise Lord of the Rings universe in the same way? Highly likely — **no**. First and foremost, the laws of physics for such a universe should be more or less akin to ours, with some adjustments for the existence of magic, but there's no guarantee that such physical laws can be found. Further, we'd ideally want this world to arise independently, much like ours did, with a Big Bang, evolution and so forth. This presents another tremendous restriction that will hinder our search for such a universe. Plus, we'd want the plot to completely replay in this universe. Perhaps we'd even like to have all living creatures looking as they do in the movie. In essence, all these constraints will ultimately resemble a massive system of equations for the initial state of the universe. And as we know, not all systems of equations have solutions. Simply because, if you plot them, they won't intersect. As illustrated in the following example: 

{{ figure_start() }}
{{ image(path="../ru/rings.png", scale="2/3") }}
{{ figure_end(caption="Two different conditions") }}

In this image, each point represents a universe, and the graph depicts a universe that satisfies a particular condition. The Lord of the Rings universe consists of many conditions, so this universe would have to be at the intersection of all the graphs of all conditions. 

But there are points that are closest to all of these conditions:

{{ figure_start() }}
{{ image(path="rings2.png", scale="2/3") }}
{{ figure_end(caption="A universe fairly close to all conditions") }}

<!-- https://www.desmos.com/calculator/aasywp7i1k -->

This implies we can find universes that roughly meet our conditions.

Hence, it's unlikely that the universe of 'The Lord of the Rings' exists in the exact precision as described in the books or depicted in the movies, with all conceivable or inconceivable demands on it. However, there are surely universes close to it that have fewer restrictions, and the more compromises we make, the more natural the result will seem, and the larger the range of such universes will be. Perhaps even a more natural universe might turn out to be much more interesting than the universe of 'The Lord of the Rings' so the loss won't be substantial.

On the other hand, nothing prevents us from constructing a universe for a time-traveler. We can take an existing medieval world with people and then insert a person from the future after their death, simulate this universe further and see what happens. So in this regard, time-traveler universes are not impossible. Although again, an exact parallel from your favorite anime probably doesn't exist.

{{ admonition_start(color="red", title="⚠️ Note") }}
In this chapter, I implicitly assumed that our universe can be simulated on a computer, and that it obeys unasanu. However, this is a separate, significant question we will discuss later. For now, I will implicitly assume this for the sake of simplicity. You can always extrapolate these examples to other universes which obey unasunu.
{{ admonition_end() }}

<span class="orange-bg example">The principal construct is also the primary candidate for refutation</span>, because we still do not know the theory of everything, so we can't determine whether any combination of atoms exists or not. What if we can't create a copy of our universe where half the humans are replaced with air? What if that contradicts some laws? For simple naive universes like Conway's 'Game of Life', we can assert such, but it's doubtful if it is valid for all types of universes.

Of course, the principle of constructability cannot be applied in some cases if our universe is not computed naively.

In short, according to unasanu, <span class="green2-bg example">not all imaginable worlds exist, but all constructible ones do</span>.

## Substrate-Independence

If you find it surprising that universes can be computed on natural numbers, I want to show you one principle that makes this more believable:

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Substrate-Independence** is a property of computations which signifies that their results do not depend on what substrate they are carried out on.
{{ admonition_end() }}

Regardless of how the universe in which you reside is computed, you won't feel it. Therefore, the possibility of computation on static numbers does not seem astonishing.

I find it to be one of the most powerful properties of computations. The result of deterministic computation does not depend on the Turing-complete substrate on which they are calculated:
* on a computer 
* on Babbage's Analytical Machine
* on a human computer composed of a 30-million-strong army (Hello, Lu Chisin!)
* on redstone from the Minecraft game
* or if some immortal entity does these computations on a cellular automaton 110, moving stones according to the simplest rules (Automaton 110 is Turing-complete [\[22\]]).

{{ details_start(summary="Yes, I'm quoting xkcd") }}
The image is clickable.
{{ figure_start() }}
{{ image(path="a_bunch_of_rocks.png", format="png", scale="1") }}
{{ figure_end(caption="xkcd/505 [\[23\]]") }}
{{ details_end() }}

## The fact of computation is an observer's interpretation

Let's suppose we postulate that only those universes exist which are explicitly simulated on our computers.

Let's envisage a hypothetical thought experiment: say we initiated a virtual simulation in which various digital entities live their own lives, and then humanity becomes extinct. Billions of years later, extraterrestrials land on Earth to observe what is happening. What if they can't decode the computations that have taken place on the computer? Would the virtual universe cease to exist? What if the universe was filled with countless computers running all sorts of simulations, and we simply haven't deciphered their significance yet?

## Why All Natural Numbers Exist

The next counter-argument against unasanu is this: Why should all natural numbers exist independently? What if the simulated universe only exists because the number encoding it exists in our computer?

First and foremost, natural numbers are the most elementary, apparent, and simple. I find it easier to assume the existence of natural numbers inherently, rather than to believe in the existence of irrational numbers with an infinite decimal expansion.

However, even if this is not satisfying and we think that only those numbers exist which are encoded by a physical object, even in our finite universe, there are more than enough numbers. For instance, we can take any random stone from the street, scan it layer by layer, and assemble all the images into a single, extraordinarily large number. Each stone can be interpreted from a myriad of angles. All its images can be shuffled in countless ways to generate an even larger number of numbers.

We can attain even more numbers if we consider creating large numbers by connecting many numbers derived from stones, viewed from various angles. There are exceedingly many permutations of the order of stones, and for each stone, we could choose a diverse set of angles. Therefore, it is highly probable to find every possible number up to a certain size in our universe.

This means that a number of previously calculated universes are encoded in our universe. It could be said that the existence of our universe implies the existence of a vast amount of other universes. Previously, I used this line of thinking to prove the existence of other universes to myself, deeming it the "idea of world generation", but now I find natural numbers to be more fundamental and I don't need such concepts anymore.

By the way, this is similarly how Greg Egan's Dust Theory is formulated [\[2\]], which he described in his novel "Permutation City".

## Infinite time and infinite memory

It can be shown that simulations in the form of numbers have access to infinite memory, infinite time and, consequently, infinite computational capabilities.

Firstly, how is infinite time achieved? If we don't limit the existence of the next step in the simulation code, meaning for any current step there always exists a next one, then for any number encoding the steps from 1 to N, we can always construct a number that encodes the steps from 1 to N+1. Therefore, time isn't constrained here, allowing the universe in the form of a simulation to exist indefinitely.

{{ image(path="next_step.png", scale="2/3") }}

Due to the infinity of time, we can attain an arbitrarily high computation speed by simply pausing the consciousness that observes the computations.

Infinite memory is slightly trickier. Suppose we consider the length of the number that encodes the current step as memory. For instance, our code is written in such a way that the algorithm checks whether the previous step is relevant to the current one. Hence, when we request memory, we find the next number and the algorithm checks if this number is the one we need. When the memory is insufficient, the algorithm can reject the number encoding this simulation. When the memory is adequate, the algorithm accepts it. Therefore, no matter how much memory we request, there will always be a number containing the necessary amount of memory.

{{ image(path="memory.png", scale="2/3") }}

So, it would be more accurate to say that you can request as much memory as you want, but the amount is still finite each time.

The infinity of time and memory are pleasing properties that will be extensively utilized later on.

# Is this applicable to our universe?

I didn't impose so many limitations on the simulation and used an alternative, computable physics in the thought experiment for nothing. This is all because it's uncertain how much our universe can exist within a computer, how computable it is. The problem isn't only that we don't know the Theory of Everything to answer this question, but also that we currently know of some phenomena that seem to contradict this possibility. Let's look at the known issues.

{{ admonition_start(color="green2", title="🤔 Testable Assertion") }}
Are our laws of physics computable?
{{ admonition_end() }}

## Simulating an infinite universe

Suppose that our universe is infinite. If this is the case, is it impossible to compute it on a computer? No, because we have a limit on the maximum speed of information propagation - the speed of light.

Let's consider what calculations are necessary to replicate Earth at this present point in time. We need to take a finite chunk of space from the Big Bang and simulate it up to the present moment. In doing so, we selectively choose an initial chunk large enough that the lack of information from the edges of the universe hasn't yet reached Earth in the present time. As a result, throughout our history, we have observed more information arriving from distant stars, as if our universe is infinite. But, if we let this simulation continue, information could eventually reach Earth stating that the universe has an edge beyond which no calculations are made. We can't allow this to happen, so we revert back and take a larger chunk from the Big Bang to enable further simulation in time and this process repeats. It was previously demonstrated that we have an infinite amount of memory and computational power, so this isn't an issue.

Mathematically, the essence is that for any finite point in time `T`, we can find a finite chunk of space from the Big Bang, so that when simulating it up until `T`, information that the universe is finite would not reach the observer at the center of this chunk.

But where do we get information about the organization of elementary particles at the time of the Big Bang? As a number, all possible initial conditions exist, so that's not important.

However, this method can't be applied to infinite universes without a limit on the maximum speed. For instance, in a universe with Newtonian gravity where gravity instantaneously propagates, this is called "action at a distance". An example of a universe where there is a limit on the speed of information transmission is Conway's "Game of Life", where the maximum speed is one cell per move.

However, we have quantum entanglement, which seems capable of transmitting information faster than the speed of light. This is not a problem, because such particles are created adjacent to each other, and then we move them to the necessary point in the universe for information retrieval. Given that they cannot move faster than the speed of light, by the final moment in time `T` they will be transported a considerable distance from the nominal center. For simulation purposes, we just need to choose a slightly larger section so that information about the non-computation at the edge of the universe would not reach the entangled particle.

This simulation method is similar to mathematical analysis limits: each partial universe will become incorrect after a certain moment in time, but the further you go, the more correct it becomes. The limit of this series is what we're looking for. Let's call this the **Limit Method Simulation**.

{{ admonition_start(color="blue", title="📝 Definition Introduced") }}
**Limit Method Simulation** is a method that enables the simulation of universes that possess something infinite, by constantly increasing the finite size of this potentially infinite magnitude.
{{ admonition_end() }}

{{ image(path="inf_universe.png", scale="2/3") }}

## Simulating Continuity

As we remember, it's impossible to incorporate continuity directly into a computer simulation. So, how are humans able to compute physical simulations on computers? The answer is approximation.

The very first approximation we encounter in computing relates to real numbers. It is impossible to store and process a precise real number with an infinite number of decimals. Therefore, real numbers are stored as approximations — some finite area of memory. Two of the most commonly used types of real numbers are 32-bit (float) and 64-bit (double), with their operations hard-coded into the processor. These limited numbers are prone to rounding errors during computations (0.1 + 0.2 = 0.30000000000000004). Therefore, all methods interacting with them are designed to minimize these errors and deliver accurate results with a sufficient number of correct digits. It is evident that 64-bit numbers are more precise than 32-bit numbers. There also exist libraries for creating slow arbitrary sized real numbers that offer arbitrary precision, for example, 1024 bits, 10000 bits. These numbers can be utilized in computations demanding precision beyond the usual.

Regarding physical simulation methodologies, there is the Finite Element Method (FEM) [\[24\]], which allows us to numerically solve differential equations across a given space with different materials. For instance, we might want to solve a problem involving heat propagation for which there is a rather straightforward differential equation. For heat, we assume that each point in the continuum contains a real number representing the temperature. Here is a simplified illustration of how it works:

* Divide the space into a certain grid.

{{ figure_start() }}
{{ image(path="../ru/Example_of_2D_mesh.png", format="png", scale="1/2") }}
{{ figure_end(caption="Example of a grid. It could be any shape, though a triangular form is usually more efficient from a practical standpoint. The grid could also be divided into squares, but this would be more resource-intensive and slightly less accurate. Illustration from Wikipedia.") }}

* We assume that the true heat value resides in each point of this grid, while heat uniformly transitions between each point from one grid value to another. This way, we create a continuum of heat values, yet this continuum is represented by a discrete number of **finite elements**.

{{ figure_start() }}
{{ image(path="../ru/Finite_element_method_1D_illustration2.png", format="png", scale="1/2") }}
{{ figure_end(caption="Example of values within a grid. If each vertex has a specific value and it uniformly decreases between grid elements (blue), the sum of all these elements creates a broken-line function, which approximates the actual function (red). Illustration from Wikipedia.") }}

* Each of these finite elements can be represented by a simple equation. When we substitute this equation into the heat differential equation, we can obtain a System of Linear Algebraic Equations (SLAE) for the entire space, which is easily solvable and for which there are numerous methods.

{{ figure_start() }}
{{ image(path="../ru/Finite_element_sparse_matrix.png", format="png", scale="1/2") }}
{{ figure_end(caption="Example of the resulting SLAE matrix. Here, a white point indicates that an SLAE element equals zero, a black point means that it has a certain value. Special methods have been invented to solve SLAE on such sparse matrices. In practical tasks, the sizes of such matrices can reach millions. Illustration from Wikipedia.") }}

* After solving the SLAE, we obtain the heat value at each point in space at the following moment in time. It may not be the perfect solution, but it is quite accurate. And the finer we make the grid, the more precise the solution will be.

{{ figure_start() }}
{{ image(path="../ru/FEM_example_of_2D_solution.png", format="png", scale="1/2") }}
{{ figure_end(caption="This is how the solution for the previously shown triangular grid looks like. It's hardly noticeable that the problem was solved with such large triangles as mentioned above. This owes to the fact that FEM is pretty good, and active efforts are being made to achieve the highest accuracy with the least computation. Illustration from Wikipedia.") }}

{{ figure_start() }}
{{ image(path="../ru/FAE_visualization.jpg", format="jpg", scale="1/2") }}
{{ figure_end(caption="An example of another simulation using FEM. Illustration from Wikipedia.") }}

Is it possible to simulate our universe using the Finite Element Method (FEM)? Certainly. The question, however, is about the precision of the computations. You could choose a grid size 1000 times smaller than the Planck length, and you might think that should be enough to observe our world.

But then comes the question of accuracy: if our universe is simulated by FEM, or is even a cellular automaton, could we detect this experimentally? In theory, yes. For this, we would have to conduct experiments with incredibly high energy levels, or observe very distant stars, or concoct a very clever set of phenomena. It seems that these processes should expose the discrete artifacts of space.

At the same time, there is one simple principle which remains: <span class="green2-bg example">Any experiment speaks the truth only up to a certain accuracy</span>. If we conducted an experiment where we gave a proton energy equivalent to a galaxy’s mass, then collided it with another proton, and the result of their collision agreed with the continuity of space, it would tell us that space only appears continuous up to a certain, even if incredibly small, limit. And it’s unclear if it would be possible to conceive of an experiment which would only work under the condition that space is perfectly continuous.

{{ admonition_start(color="orange", title="🔢 Mathematical Problem") }}
Is it possible to develop a type of continuum system in which an experiment can be conducted to show that the environment consists of a truly perfect continuum? The experiment should be feasible for intelligent beings within the environment, require a finite amount of matter and energy and should operate for a limited period.

If so, would our universe be classified as one of these types of continuum environments?
{{ admonition_end() }}

Alright, let's assume that our universe is simulated using the Finite Element Method (FEM) with extraordinary precision. However, if this precision is finite, it implies that we can perform an experiment that reveals a discrete nature of space. Is there a kind of simulation where such an experiment is impossible? Yes, and I will further demonstrate that.

Suppose our universe is described by a certain differential equation and in the standard model each particle is represented not by a point, but by some field. We can apply the FEM to this equation and implement the following algorithm:

* We iterate `k` from 1 to ∞.
    * The precision of the real numbers equals 2<sup>k</sup>.
    * The spatial grid size is X·2<sup>k</sup>.
    * The time grid size is Y·2<sup>k</sup>.
    * We solve the FEM for the entire universe using the defined spatial and time grids and real numbers with the defined precision.

For such an algorithm, it turns out that for each subsequent cycle iteration `k`, we increase the precision of all algorithm components by a factor of 2. Imagine now that an observer inside such a universe wants to run an experiment to ascertain the continuity of his own space (or time). For any level of experimental precision, there will always be a `k` that will result in the experiment proving his universe to be a continuum. This is another application of simulation by process of limits.

This approach suits particularly well the case of the heat death of the universe. In such a case, you can select some finite `k`, such that an observer won't be able to carry out an experiment with the necessary precision within the universe's lifetime. 

This algorithm will also work well for chaotic systems, like the three-body problem or the double pendulum: for any time `t` and precision `eps`, you can find a `k`, where at that specific time, the precision of coordinates will be comparable to `eps`.

Hence, in a way, universes with a continuum or real numbers are also computable, and so they too exist according to unasanu.

Of course, I've demonstrated this is feasible only for universes which can be described by a differential equation and solved using finite element methods (FEM), and it's unknown to me which other universes with a continuum are not possible. I believe this is ultimately a mathematical problem — to identify which universes with a continuum are computable according to this concept, and which are not.

For instance, there’s a wonderfully appealing concept, the "Infinite Nestedness of Matter" [\[25\]], stating that there are no elementary particles, and all our particles are made up of their own little universes. I'm not sure whether it's possible to simulate such a universe using this method.

{{ admonition_start(color="orange", title="🔢 Mathematical Problem") }}
Identify which types of infinite and continuous universes can be simulated with FEM, which can be simulated through the method of limits, and whether the laws of physics as we know them pertain to this class of universes.  
{{ admonition_end() }}

Alternatively, one could argue that continuous universes also exist in and of themselves, being deterministic, regardless of how simulative they are.

Indeed, this raises a small question. If there are strictly more real numbers than natural numbers, how have we managed to fit continuum universes into natural numbers? The answer is straightforward — computable real numbers form a countable set. The remaining part of real numbers, which forms this set and is greater than the natural ones, is non-computable. For more detailed information about this, you can refer to the Wikipedia article, "Computable number" [\[26\]].

By the way, my method of taking limits resembles the definition of uncomputable "approachable numbers", which are defined as the limit of a computable function. I borrowed this concept from the article "A definable number which cannot be approximated algorithmically" [\[27\]]. Interestingly, almost all known examples of uncomputable numbers are "approachable". Meanwhile, it's possible to introduce a real number that is not only uncomputable but also unapproachable.

## Absolute randomness

The next problem that arises from our known laws of physics is quantum mechanics and its inherent randomness when associated with the multiverse. I'm not particularly well-versed in understanding the issues quantum mechanics presents in simulating it on a computer, so let's assume that the only remaining question is how to ensure absolute randomness.

As we know, it's impossible to get an absolutely random number on a computer. Only pseudorandom numbers can be generated, which are calculated using some algorithm, or if the computer takes data from the external environment for random numbers. However, everything changes drastically when we need not just one truly random number, but a universe with absolute randomness.

Let's suppose there exists a deterministic universe with a single random number generator (RNG), producing absolutely random bits - 0 or 1. We could simulate such a universe this way: every time the RNG is asked for a number, we simply duplicate the current universe, showing 1 to one version and 0 to the other. Consequently, each new universe will believe it got an absolutely random number. The number of universes doubles each time the RNG is asked for a number.

Yes, to simulate a universe with absolute randomness, we need to simulate not just one universe, but all possible versions simultaneously. Since we have no constraints on memory or computation, this isn't a problem. Max Tegmark calls this "subjective randomness," an idea I take from his book [\[18\]].

{{ image(path="rng.png", scale="1/2") }}

This is a fascinating method, let's introduce a term for it.

{{ admonition_start(color="blue", title="📝 Defining the term") }}
**Brute-Force Simulation** is a method for simulating a universe that has a non-computable or undefined function, but this function outputs a finite set of values, meaning we can simulate the universe by simply iterating through all these function values.
{{ admonition_end() }}

Interestingly, any pseudorandom number generation algorithm can be found amongst all these versions. This is similar to how, among all possible numbers, there will certainly be some that can perform computations.

Of course, quantum mechanics not only presents sheer randomness, but these universes also interact with each other, thus making everything way more complex. Nonetheless, it appears feasible to compute it keeping in mind the aforementioned. If I'm mistaken and quantum mechanics imposes other restrictions that prohibit its simulation on a computer, please let me know.

## Non-computability

Incomputability is a property that some entities possess that prohibits their computation on a machine. All known instances of incalculability either need real numbers with infinitely many digits after the decimal point or the solution to the so-called halting problem.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**The halting problem** is a task defined as determining whether a given program with given input data will ever stop or not.
{{ admonition_end() }}

Alan Turing has proven that it's logically impossible to have a program that can solve the halting problem in a general sense for any program. If it could exist, it would only be as an external entity that can't be computerized or in the form of an infinitely long program. Notably, the answer for each program does exists — it will either halt or it won't.

If we could solve the halting problem, it could be used for proving certain types of theorems. For example, you could prove or disprove the Collatz Conjecture (the 3x+1 problem) [\[28\]]: we could write a program that runs through all numbers and checks where a given number leads. If it doesn't lead to 1, we stop the program. If we solve the halting problem for such a program, we could definitively say whether the conjecture holds. Therefore, having a machine to solve the halting problem would be immensely helpful in mathematical research.

It seems that the existence of a universe that possesses physical phenomena capable of solving the halting problem is impossible. But I will show that's not the case.

The central argument is that a universe capable of solving the halting problem is determined. This means that regardless of whether we simulate it or not, its future is singular, and beings within it will live their life. But if you're not satisfied with this, there's another way.

Suppose we have a deterministic universe with a unique device for solving the halting problem. We input a program into it and it outputs a response — 0 or 1, whether it will halt or not respectively. Now we're simulating this universe in a typical manner, except every time the device is asked a question we clone the current universe, and give one the input of 0, the other 1. We do this over and over again, essentially simulating by exhaustive search.

The interesting part here is that only one of these branching parallel universes is correct, but it's impossible for us to compute which one that is. This means that in one of these universes, its inhabitants observe that their universe is capable of correctly solving the halting problem. But it seems to me, like we are unable to understand which of these universes is correct, they also can't sufficiently assure themselves of that.

{{ image(path="halting_problem.png", scale="1/2") }}

So even if in our laws of physics, or in the way our consciousness operates, we were to find a phenomenon capable of solving the halting problem, it could still exist as a computer program.

In this scenario, much like with the argument of irrational numbers, to avoid ending up in a universe with ordinary computations, it would be desirable that the consciousness of an observer in such a universe would utilize incomputability – a vital necessity for the operation of that consciousness. That means that the incomputability in the laws of physics should come under the jurisdiction of anthropic filtering. As far as we know at this point, neither the physical phenomena of our universe, nor human consciousness require the solution to the halting problem for their existence.

If there are other forms of incomputability out there, please do let us know.

## Regardless if the human consciousness can be simulated

Let's suppose you don't agree with all of the points laid out above, or it turns out that our universe does not satisfy them all, rendering it non-computable on a computer. In this case, let's explore how feasible it is to simulate human consciousness. 

Firstly, unlike physical laws, consciousness can be computed much more reliably using a naive approach. That is to say, the principles of construction and all previous deductions are quite applicable to it. 

According to contemporary scientific understanding, human consciousness is computed in the brain, which does not utilize quantum effects, thus making the brain similar to a classical computer. Moreover, neurons in the brain are large enough to be studied, allowing us to uncover the full laws of their function. The signals among neurons are not encoded by perfect real numbers but by a discrete number of ions transmitting an electric charge. Therefore, it's believed that the possibility to simulate a human brain is just a matter of time and computational power.

Hence, even if we can't simulate our universe with absolute precision, we can simulate the human brain with the utmost possible accuracy on a computer. If a continuous universe has no limit to precision and can be infinitely refined, there is such a limit for the brain. This precision is constrained by the size of electrons. In other words, we can simulate the human brain so that it outputs the exact same number of ions to each neuron as the physical brain did in an uncomputable universe. This implies that if we iterate through all possible inputs up to the death of this brain, we will certainly find any uncomputable universe, including our own. That is to say, we can compute a brain that observes an uncomputable universe without computing the universe itself.

Since the essential nature of unasanu was solely about conscious observers observing their universe, we've got rid of an unnecessary detail.

{{ admonition_start(color="green2", title="🤔 Claim for Consideration") }}
Is it possible to simulate human consciousness?
{{ admonition_end() }}

## Biology, Sociology, Psychology, etc are not mathematically describable

There is an argument which goes like: "Biology, sociology, psychology, and other such fields can't be described by mathematics, hence our universe is also non-mathematical and can't be simulated".

This is a curious argument that seems to stem from a lack of understanding of what it means to 'describe in mathematical terms' and the capabilities of mathematics and programming.

As I understand it, by 'describe in mathematical terms', this argument implies that these things could either be described by simple low-level rules that can derive everything else, or they are governed by simple high-level rules that can predict the behavior of the entire system.

In other words, this argument equates the inability to simulate to the nonexistence of a beautiful and straightforward method to describe the system's behavior. There is a logical fallacy in this statement, as the latter does not imply the former.

Take biology as an example. Its development isn't described by something simple, since it's complex and consists of trillions of components where randomness at any level can shift the equilibrium of the system, or perhaps biology doesn't have any equilibriums at all. But this doesn't mean that such a system can't exist out of elemental constituents. For example, people are actively simulating evolution and creating artificial life. They are creating simulations of phenomena that they can't "describe mathematically," leading to incredibly complex systems where everything interacts with everything else.

No one can deny the possibility of emergence — when a few things combined exhibit more properties than the sum of their individual attributes.

<span class="green2-bg">Just because something can't be described mathematically at a high level doesn't mean that it isn't essentially mathematical at a lower level.</span>

Thus, if you have an incredible number of calculations, and you're just simulating atoms, which then form a society that believes it's somehow not mathematical - that's the society's problem. Your computer is all about mathematics.

So, this is less of an argument and more of a statement of fact that humanity doesn't understand high-level emergent processes very well. This in no way implies that simulating the universe is impossible.

### Computational Reductionism

I think people misunderstand computers and computations. Some believe that all the richness of the world we observe simply can't be computed because computers are all about "zeros and ones," "simplest algorithms." So, they argue that in a deterministic world, free will is impossible; that AI can never possess human emotions or creative abilities; that biology and psychology "aren't mathematical"; and if this world is simulated, nothing makes sense, and you can steal, kill and so on...

Probably, the problem here is also that people are convinced that subjective experiences such as emotions, sensations, pleasure, and suffering can't be computed. I'll delve more into this topic in the chapter on panqualia.

To highlight where I think this view is mistaken, I'd like to introduce a term similar to substrate-independence to showcase one more powerful property of computations.

{{ admonition_start(color="blue", title="📝 New Definition Introduced") }}
**Computational reductionism** is a property of computations according to which any system describable by logic can be simulated.
{{ admonition_end() }}

Yes, this is a powerful claim. It might not necessarily be correct, but it reflects my philosophical stance.

Computational reductionism manifests itself in the fact that we can describe all types of computations, including the infinite, continuous, indeterministic, and non-computable universes. Any novel category of universes that seems non-computable is merely a challenge for future mathematicians.

Suppose consciousness is comprehensible and adheres to at least some sort of logic. In that case, the opportunity to simulate it will eventually emerge, even if it's only theoretical.

This concept might be challenging to grasp if you're not a programmer. As a programmer, I've implemented increasingly complex programs over the years, and I've formed the impression that anything I understand can be programmed. If I can't program it, I probably don't understand it well enough. Creating a simulation is equivalent to thoroughly understanding the underlying laws of the process. Writing programs, like conducting experiments, aids in discovering truth and identifying flaws in one's thinking. To me, computational reductionism is evident.

## Interim Conclusion

It has been demonstrated that some restrictions can be lifted for certain types of simulations. We know that the following also adhere to unasanu:
* Certain classes of infinite universes
* Certain classes of continuous universes
* Universes with absolute randomness
* Universes capable of solving the halting problem

Other universes that cannot be simulated require further study. Most likely, everything can be described via computations in one way or another.

Following these assertions, we can confidently say that our universe is computable and, therefore, obeys unasanu.

We now have a better understanding of the open questions:
* For which classes of universes can the method of limit transition be applied? And to which class does our universe belong?
* Which classes of universes can possibly be computed using a naive method? And does our universe belong to such a class?

And I want to emphasize this: even if our universe and our consciousness do not adhere to unasanu for any reason, all these ideas apply to universes that exist in the form of programs. We now know that such universes exist, and that’s amazing. And I will show even more interesting implications of unasanu for these universes.

From here on, we will assume that our universe is indeed computable. If you're not comfortable with this, simply imagine that I'm not discussing our universe, but rather an arbitrary computable one, and all conclusions are valid for this other universe.

# Consciousness as a number

Earlier, I explained everything through the existence of universes with observers inside. All these thoughts make no sense without observers, even the very definition of “existence” I bring up emphasizing the observers' role inside observing their universe. If observers are so important, it's even more fundamental to consider them as separate universes themselves.

If a universe is computable, then any of its subsystems is also computable and can be described by a certain program. And since observers are part of the universe, they too can be described by a program that computes only them, not the laws of physics. As we know, any program, with any input data, is already computed. This means any observer with any possible input data already exists in the form of a number. We can even call this concept **conasanu**.

{{ admonition_start(color="blue", title="📝 Defining term") }}
**conasanu** (consciousness as a number) — is a philosophical concept that suggests that any consciousness with any input data has already been computed and exists in the form of a number, and does not need a universe to exist.
{{ admonition_end() }}

{{ image(path="conasanu.png", scale="2/3") }}

In this sense, it might seem that solipsism should prevail, but that is not entirely the case. Solipsism asserts the non-existence of an external reality. However, according to unasanu, everything that can be constructed does exist. And if your observations can more simply be described by a program simulating an external universe, then that is likely the case. Therefore, solipsism remains accurate in the belief that we can be certain of nothing but our own sensations, and it's miraculous that these sensations describe an external physical universe.

Also, it is crucial to remember that each individual consciousness, existing as a physical structure in some universe, also exists as a distinct program. And perhaps the reverse is true: it seems we can construct a universe for any set of input data of consciousness using varied aids. The only question is how beautiful and simple this universe is.

For Tegmark [\[18\]], the entire theory rested on the fact that the existence of an external physical reality meant that it existed as a mathematical construct. Yet, it disassembles a bit given that among mathematical constructions, there are individual consciousnesses which are not necessarily anchored to any universe. 

This leads to a fascinating scenario where in our world, each consciousness is a separate universe. Yet, these individual minds interact with each other through the physical universe. 

In general, since conasanu is more fundamental than unasanu, it would be logical to shape the article around the former. However, I am building it around the latter because it's easier for me and for you. This might be a mistake.

## Panpsychism and the Consciousness of a Stone

It may appear that conasanu implies that there's some form of consciousness encoded in a stone, and in any other object, and that they're all conscious and feel something. This viewpoint is called **panpsychism**.

The stone indeed contains a multitude of numbers, many of which can be construed as computed consciousnesses. However, this doesn't truly mean anything significant. With the same logic, your physical brain contains numerous different consciousnesses, some of which are the same as those in any random stone or brain of a similar size. The key point is that these consciousnesses primarily exist as numbers; their existence within a stone is merely an addendum. 

So, how does human consciousness differ from the consciousness within a stone? It's down to interaction. Human consciousness can interact with the external universe in such a way that other similar consciousnesses (humans and animals) can observe and replicate. The consciousnesses within a stone exist solely for themselves, indifferent to the universe they reside in. Their sense of time exists within their own sets of numbers and is not tied to our own sense of time. Although, there are suggestions, as argued by Hilary Putnam [\[29\]], that the consciousnesses within stones could have their time synced with the time of our universe.

In [\[30\]], they aim to disprove the computability of consciousness with the argument that if it were true, then panpsychism would be valid, but that would be absurd. This argument is known as Dancing with Pixies. Yes, panpsychism is indeed valid, but it is ultimately irrelevant; everything remains as it was, and stones remain indifferent, even when harboring numerous consciousnesses.

## I prefer panqualia

In regards to this topic, I would like to express my interpretation of panpsychism, which I have named **panqualia**.

{{ admonition_start(color="blue2", title="📖 Definition") }}
**Qualia** (a.k.a. "subjective experiences") refers to the sensations you feel – smells, colours, emotions, love, etc.
{{ admonition_end() }}

In philosophy, qualia is distinguished as a separate category, generating a lot of controversy. For instance, some insist that Artificial Intelligence will never be capable of possessing qualia, especially love, due to reasons somewhat as obscure and random as Gladiolus.

I view the brain as a rather complex program, and not something unique, as such, I believe there's nothing fundamental about subjective experiences that would merit philosophical debates. Essentially, I don't think subjective experiences exist at all: the way you feel red, for instance, is the outcome of your brain's computations, the result of red color encoding in your neurons, a combination of associations, links between other colors, memories activated upon seeing red; and the eye strain one experiences reading red text on a blue background is likewise enabled by the physical design of your eyes. All of these are dry calculations and algorithms. These vivid sensations are all thanks to the heavy interconnectivity of your brain's various departments.

Or put more optimistically if you will: if some property doesn't exist, everything has it! :)

{{ admonition_start(color="blue", title="📝 Provided Definition") }}
**Panquality** — a viewpoint on qualia that posits every algorithm possesses qualia per definition.
{{ admonition_end() }}

Let's take for example a random neural network and feed it random data. I believe this neural network has subjective experiences and feels something. The only problem is that this network:
* Lacks the intellect to realize it is feeling something.
* Lacks memory to remember what it has just felt.
* Lacks a language to communicate to other such networks what it has felt.
* Even if it had all this, its feelings aren’t structured, and the input data is random, so intellect and memory will hardly be of any help.

Here are some measurable criteria offered, based on my understanding of qualia. Addressing each of these makes the system more sensitive and brings it closer to the human perception of the world.

Thus, the uniqueness of human qualia boils down to possessing reasoning, memory, language and a certain kind of input data. And the complexity and uniqueness of our human feelings are achieved because we consist of neural networks, where each sensation triggers not only the target neurons, but also all the connected ones. Thanks to this connection, we can feel the warmth of the color red and perceive it, not like a digital camera.

So, from this perspective, we can say that an AI based on dry algorithms of letter shifting (as in the thought experiment of Searle's Chinese Room [\[31\]]) will experience the world utterly differently from a human. But an AI based on neural networks might, and perhaps even more beautifully and excellently, like a super-synesthete.

{{ details_start(summary="Off-topic about the Chinese Room") }}

<!-- Should this part be removed? It's nonsense. -->

If you are not familiar with this argument, please refer to the link above on Wikipedia. Here I'll give a brief critique.

This argument is incorrect because in this case, the human is the computational substrate, not the computed environment/agent, and he could just as successfully compute the interactions of the atoms of a real human brain, and understand nothing. However, a human on top of these computed atoms would be more alive and conscious than the Chinese Room.

I have a proposal to modify this experiment that could potentially satisfy Searle and his desire to understand a computable system. But, it requires some rather far-fetched, sci-fi technologies. To begin with, we'd need to have a neural network of a Chinese room and then connect it to Searle's brain via Neuralink or some other advanced technology. Communication would have to take place through Searle. After this, the neural network would need to be trained in Chinese language and Searle's brain interface should also be trained. Then, once we initiate this setup, Searle's neurons would be able to share information with the neurons of the Chinese room and he would be able to feel and understand certain parts of the Chinese language (not immediately, of course). The more these interactions occur, the more neural connections are formed (for instance, between Searle's brain's blue neurons and the Chinese room's neural network while discussing the color blue), and the more he would be able to understand Chinese and merge with the consciousness of the Chinese room.

{{ details_end() }}

---

By the way, there are already existing examples of virtual beings that possess qualia and, if you like, consciousness. At least by the criteria mentioned above. Now, I'm going to relay the description of one such work that used ChatGPT. The agents in this work have everything needed: 
* intelligence (albeit small),
* memory (minimal),
* language,
* structured feelings,
* other similar agents to converse with and interact (!!!),
* unlike the original ChatGPT, they exist within a time frame.

However, they lack a few key human qualities:
* senses, other than text, i.e. audio-visual-tactile, etc.;
* the ability to learn, because in this particular work prompt engineering through ChatGPT is used, and we can't fine-tune this neural network for each agent, so they can develop a unique personality or evolve over time;
* sufficient simulation time and memory to create their own culture within which they might be able to communicate, live, discuss their feelings, and develop their philosophy more efficiently.

I propose to officially recognize this work as the first to create a genuine (though small) artificial consciousness.

{{ admonition_start(color="blue3", title="Telegram post from «I trained one model»/927 [\[32\]]") }}

{{ image(path="../ru/generative_agents.png") }}

An incredibly cool article, unlike anything I've seen before - **Generative Agents: Interactive Simulacra of Human Behavior**

<https://arxiv.org/pdf/2304.03442.pdf>

In short, a Sims-like game has been populated with 25 characters, each with their own personality description, their own memories, and their own goals. All character actions and interactions with each other occurred through LLM generation. As a result, the characters quickly started to imitate quite complex human behavior - for example, they organized a Valentine's Day party together, handed out invitations, and arranged dates. _Moreover, according to the markers' estimates, their actions were more human-like than the behavior of the people who were asked to play as these characters_

The authors have a very cool idea of using the model's context: all actions and observations of the surrounding world are saved, and then some relevant memories are retrieved from this memory. They are used to generate the next action or reply in a conversation, and also to reflect on them, so as to formulate more long-term plans. Thus, the character can participate in observation, planning, and reflection. 

It seems like this is a bomb for any role-playing of various agents in chats and this might be how the NPCs of the future will look like. 

UPD: forgot to attach a great demo - <https://reverie.herokuapp.com/arXiv_Demo/>

Also, a detailed [thread](https://twitter.com/AndrewCurran_/status/1645468667810021377) about the article 
{{ admonition_end() }}

# Are we living in a simulation?

This is one of those burning questions that everyone continually talks and speculates about, which makes absolutely no sense. But since everyone is interested, let's discuss it.

Firstly, it is important to understand that this question actually contains two wholly different inquiries:
1. Is our universe computable, i.e., is it theoretically possible to compute it on a computer?
2. Is someone actually computing our universe for their own purposes?

We have already discussed the first question, so let's consider the second one.

Assume that our universe can be simulated. We could then create a universe program similar to ours, but one that features a mega-computational outlet that computes our world in real time, simply providing an interface for control and observation of this world. Someone could then connect to this outlet and control our world or observe any of its details. According to the principle of construction, a world with a super-computational outlet exists, and there is nothing unusual about it, except that it involves twice as much computation as a regular universe. Hence, we would be someone's simulation. In addition, infinite versions of our simulating universe could be created. It's also important to remember that our universe already exists as a number independently, meaning it is an independent reality.

<span class="green2-bg example">**In conclusion:** we simultaneously exist as a simulation in an infinite number of universes and as an independent reality, as is the case with all possible universes.</span>

As with the notion of consciousness in stones, this again makes no sense, at least until external simulators interact with our world and we can observe and investigate it.

Consider "Nick Bostrom's Argument", which postulates that any highly developed civilization will eventually start creating simulations for reasons like gladiolus, hence we _most likely_ are a simulation within a simulation within a simulation and so forth. Importantly, this argument is probabilistic: it cannot be assumed with certainty that someone would want to simulate our universe, while the principle of constructing provides a definitive answer to this question. Therefore, Bostrom's argument can be ignored when addressing this matter.

There's also no point in "leading an interesting life so our simulation doesn't get turned off", because as we remember, even if it is shut down in all universes, we continue to exist numerically.

# God and unasanu

Let's see the place of God from the perspective of unasanu. There are only two methods to introduce God's concept.

{{ admonition_start(color="blue", title="📝 Introduced definition") }}
**God** is an intelligent being who initiated the simulation and can either observe it afterwards or have an effect on it. At most, God is an ultra-intelligent programmer with an infinite number of computations and memory.
{{ admonition_end() }}

According to the principle of constructing, every universe is populated with an infinite variety of Gods. You can employ the universe with a computational outlet from the earlier point. Even if God has projected his face onto the sky, you can always create a universe where he looks entirely different, but decided to alter his face using technologies. This implies that <span class="green2-bg example">every universe has an infinite number of gods</span>.

Even if some deity oversees a certain universe, copying the brains of all beings after death and distributing them into other simulations, called "heaven" and "hell", this deity isn't omnipotent. The point being, the universe would still exist without their intervention, and there's nothing they can do about it. <span class="green2-bg example">No deity can prevent any universe from existing.</span> The same principle applies to universes that are filled with suffering, where this deity seems strangely absent. This means, if a being felt that after death it found itself neither in the "heaven" nor the "hell" that its deity has spoken of, this circumstance might not be the will of its deity. 

<span class="orange-bg example">Is this deity capable of knowing everything that will happen in the universe they're simulating?</span> Yes, as, like any programmer, they could simulate it up to the required point, and then restore the past save state. Problems arise when the deity wants to know what the future of their universe will be assuming they intervene in it. This would necessitate them to simulate, among other things, themselves faster than their own time flow, all while integrating the same simulation within itself, and so on indefinitely. Such a scenario is broadly impossible to simulate. Therefore, the deity cannot know with absolute certainty what will happen to their universe along with them in the future. They can, however, replace themselves with an approximate model (which does not observe the simulation with the approximate model) or a scripted doll in their simulations, and know their own future in this simulation with the required accuracy. Alternatively, they can know their own future with absolute certainty without the possibility of altering it, but then they would have to subject themselves to limitations, calculating such a universe "all at once", as was proposed to be done with universes featuring time travel. 

No deity is the prime cause of any universe; any universe would exist even without them. Hence, we can consider another variant of introducing a deity:

{{ admonition_start(color="blue", title="📝 Defined term") }}
**Meta-god** — is a god, who has created all universes, along with all other conventional gods.
{{ admonition_end() }}

<span class="green2-bg example">Meta-god is nonsensical because they did not have any option during the creation process and play no role, regardless of their opinions, whether they are alive or dead.</span> Furthermore, such god explanation is an unnecessary detail, which leaves the question "Who created this god?" open. One possible answer is "They are either the cause of themselves or they existed forever". If so, why can't the laws of logic (from where comes unasanu) be the cause of themselves and exist forever? Obviously, this is a rhetorical question.

In summary, external gods make sense only when they interact with our universe, and when we can observe and research this. The non-participant observer gods are as real and useless as intelligent creatures carved in stone.

# The Problem of Buggy Universes

<span class="orange-bg example">This is a section with serious critique of unasanu.</span>

Previously, the question was taken into account – why only the numbers encoding correct computations are valid. We can extend this argument by asking: why are only the numbers encoding correct universes valid? It's not necessarily the case. Let me explain.

If our universe can be calculated naively, then we can construct the following "bugged" simulation:
* We take the current moment in time and consider it the starting point.
* At this moment, we modify the matter in some random fashion. For example, we could: 
    * remove a random person,
    * replace the air with a random assortment of other atoms,
    * introduce rocks into geocentric orbit,
    * eliminate Mars,
    * turn a distant star into a black hole. 
* From this modified moment, we simulate into the future.
* For observers in this universe, everything will appear as if they were living a normal life, and then a random event occurred that cannot be explained by laws of physics or any causal link with the past. The past may not exist at all, it's not necessary for existence in general.
* Such a universe exists according to the principle of construction.

Now what is interesting is that an honest simulation, which simulates our universe from the Big Bang, there is only one; but there are infinitely many of these "bugged" simulations for every moment in time.

{{ admonition_start(color="gray", title="❓ Question") }}
If there are infinitely many of these bugged simulations, and only one honest one, why do we observe the honest simulation?! Why don't we see completely random events with the removal and appearance of matter occurring every femtosecond?
{{ admonition_end() }}

Moreover, such a bugged universe does not interfere with the ability of observers to observe their universe, because it is calculated honestly, it just takes strange initial conditions of matter, so anthropic filtering is not applicable here.

{{ admonition_start(color="red3", title="🤕 Weak Spot") }}
Why don't we observe bugs in the universe?
{{ admonition_end() }}

But here we are entering the realm of speculation, which can be characterized as the "probability of finding oneself in a universe of a certain type", and we'll discuss that later. For now, there are several potential solutions to this problem:
* Such events indeed occur, but in different corners of the universe. The universe is so vast that over the course of our period of rational observations, we haven't noticed anything unusual. Or, we have noticed and call these occurrences paranormal phenomena, but no one believes these observers.
* These events happen all the time, but they occur on a subatomic level, which is why we observe absolute randomness in quantum mechanics. <span class="green2-bg example">If this is true, then quantum mechanics is a fundamental property of any stable simulation.</span> Meaning, any simulation eventually converges to quantum mechanics because this is the more likely course of events. And our laws of physics simply work in such a way as to build something logical, functioning, and stable on top of this randomness.

With these two arguments comes one compelling counter-argument: from the combinatorics perspective, the expected number of random changes in the state of the universe equals half of the universe. From this viewpoint, it is far more likely to observe half of the universe replaced by a random assortment of atoms than to observe the same for a small portion of space.

Another solution to this problem: what if the laws of physics in our universe are designed in such a way that it's impossible to execute the algorithm above? What if our laws of physics require a consistent past to function? This could be the very reason we don’t observe glitchy universes; because it’s impossible to construct them and if it is possible, it’s impossible to simulate them, hence observers of such universes will not observe. Let's introduce a special term for this.

{{ admonition_start(color="blue", title="📝 Defining Terms") }}

**Antibug Universe** - a universe with physical laws which make it impossible to construct the "bugged" states described above.
{{ admonition_end() }}

This is quite a fascinating solution to the problem at hand, but I question its feasibility from a theoretical standpoint. It seems that any such system could be clumsily simulated — and then broken —with a series of patches.

The situation appears even more complex when viewed from a consciousness perspective, like conasanu numbers. From this viewpoint, there are myriad consciousnesses that perceive subjective experiences not governed by logic. For instance, they might strike a stone, but the stone remains unresponsive and doesn't reciprocate touch or pain. Or perhaps, sensory perceptions can be created where after a certain point all information is displayed a second later than to the original consciousness. Does consciousness then also need to follow anti-bug laws?

{{ admonition_start(color="orange", title="🔢 Mathematical Problem") }}
Is it possible to construct a simulation describing an antibug universe, and do our current laws of physics and our consciousness adhere to this universe class?
{{ admonition_end() }}

{{ admonition_start(color="violet", title="🔮 Prediction") }}
If applying probabilities to universes is not senseless, then from unasanu postulation it suggests that our physical laws are antibug or else we would have observed a bugged universe. Either we're misjudging the odds.
{{ admonition_end() }}

## Changing Physical Laws

It's always possible to construct a universe where our current moment in time is the initial condition but with slightly different physical laws. For example, the speed of light could be a bit faster or slower (as far as it can be programmed according to the laws of physics and mechanics of matter). If such alterations impair the functioning of our consciousness, this change in the laws of physics gets subjected to anthropic filtering, which is why we shouldn't observe it. However, just as with universes with bugs, if applying probabilities to universes isn't pointless, then <span class="green2-bg example">we should witness a continuous random change in the laws of physics that doesn't disrupt our consciousness' functionality</span>.

Could this be quantum mechanics? Could any simulation with living organisms eventually converge to something similar?

{{ admonition_start(color="violet", title="🔮 Prediction") }}
If applying probabilities to universes isn't absurd, and if such modifications are feasible, then we should observe a continuous change in the laws of physics that doesn't hinder the operation of consciousness.
{{ admonition_end() }}

## The death of all humans upon digital habitation

How might this work? Imagine humans inventing computers operating solely on neutrons. These computers would not need the physical laws relating to charges. Meanwhile, human brain function requires electrical charges. Due to anthropic filtering, a human would typically observe a universe where their built computer operates (since they debugged it while alive). When someone transitions into a computer, their existence would no longer require electrical charges, and they might observe a shift in the laws of physics towards more randomness, excluding the need for electric charges (again due to anthropic filtering). So, after moving into the computer, the consciousness inside might observe that all animals, plants, and humans die instantly.

The image below depicts the original universe where consciousness is uploaded into a computer. It also presents 4 potential scenarios that could follow (people or computers perish in different combinations) given that the initial universe is being simulated by all the laws of physics. Each square represents a possible outcome, a set of potential universes, and a comment on them.

{{ image(path="death_in_computer.png") }}

# Universe Probabilities or the Problem of Measure

Returning to the question of "probability of ending up in a certain universe": this problem, in the scientific domain, is referred to as "the Problem of Measure” [\[33\]].

The difficulty lies in determining how exactly to calculate the probabilities of specific universes and how different approaches to resolve this issue can be validated or refuted. This problem is a longstanding one, often applied to the many-worlds interpretation of quantum mechanics: it is unclear how to determine the likelihood of specific classes of universes when there are infinitely many of them. This issue makes me quite dubious about the concept of "some universe being more likely than another".

As an example, consider the simplest question: what percentage of even numbers are odd?
* If you count in this order: **1**, 2, **3**, 4, **5**, ..., you will find half are odd.
* But if you're counting in the order: **1**, 2, 4, **3**, 6, 8, **5**, ..., you'll find only a third are odd. Here, the numbers are simply arranged in a different order, with two even numbers between two odd ones. The infinite quantity of both classes is preserved.

While we agree that the natural order of half being odd is correct, it remains unknown how to choose this natural order for encoding the universe and whether it can be objectively determined.

There is yet another objection to probabilities, specifically in relation to universes: <span class="green2-bg example">"any experience must be tested"</span>. No matter how improbable your universe may seem, someone has to exist within it and experience life, even in defiance of any understandings of probability. A suitable analogy can be made: the chance of me being born Chinese is rather substantial, yet I am not Chinese.

Even if we manage to solve the measure problem and can obtain probabilities of a particular universe, it's unclear if it's possible to falsify or verify it, even with an infinite number of calculations that allow us to go through all universes and calculate the needed probabilities. Thus, the idea of "the probability of being in a certain universe" may be nothing more than an interpretation that has no real impact.

This issue becomes even more prominent when you need to consider the infinity of continuous universes and the infinity of discrete universes simultaneously.

## The Sleeping Beauty Paradox

This is a problem from probability theory, for which there are two conflicting answers, hence the paradox.

However, I want to talk about an alternative scenario involving a sailor. This sailor has two mistresses in different ports, neither of whom know about the other. He wants to have children, but can't decide whether to have children with just one or both of them. So, he flips a coin, choosing to have a child with just one woman if it's heads, and with both if it's tails. You are his son and you're aware of this event. What are the odds that you are the only child, meaning that the coin landed on heads?

When looking from a sailor's perspective, the likelihood of having one child is 50%. However, from the child's perspective, there are three different siblings, and for two of them, the coin flip landed on tails. Hence, the children might reason that the probability of getting a heads is 33%. Or in other words, if the children take this probability, they would be right in most cases 🤪.

This disparity looks a lot like the difference between the conasanu (child's perspective) and the unasunu (sailor's perspective). With such paradoxes in play, the measure problem becomes even more intractable.

Thus, it is premature to discuss probabilistic predictions, and possibly, the bug-ridden universe issue does not contradict unasunu.

## Meta-probabilities (just a thought)

Upon reflection, there are no physical probabilities. There are only events that may or may not occur. It's a handy concept that helps us understand the world a bit better. What if we could apply the same idea to different answers and layer probabilities over probabilities? Create meta-probabilities that provide a distribution of probabilities, taking all perspectives into account.

In the sailor's scenario, there would be two points: 33% and 55%, each having a weight of 0.5.

Perhaps, this approach could shape an interesting and useful mathematics? I'm not sure, it's just a thought.

## Probabilistic solution to the halting problem

Let's suppose that the theory of measures is solvable, and our understanding of more probable universes is accurate. In this case, we could construct a universe that can solve the halting problem with a probability tending towards 100%. Here's the algorithm: 
* Every time the universe is asked whether a program will halt, we launch two universes - in one, the answer is immediately provided - it will not halt, and in the other, this program begins to compute in place of the entire universe.
* If in the second scenario the program never halts, its inhabitants will not feel anything, as it will never reach the computation of their brains, and the inhabitants of the first scenario will turn out to be right.
* If in the second scenario the program halts at some point, the number of steps after which the program stops is returned, along with an arbitrary natural number. Then we iterate over all possible natural numbers in this case, creating a copy of the universe for each new number and continuing its simulation. This results in an infinite number of universes where the program halted, and only one universe where the answer was incorrect.
* All universes are computed in parallel, and the addition of new universes does not affect the computation of others.

Therefore, if you live in such a universe, you always get the correct answer to the halting problem solution, with a probability tending to 100%.

# Death

unasanu offers some interesting predictions about death, and unlike pointless probabilistic predictions, the prediction about death is guaranteed.

## Why it's impossible to die

When people talk about life after death, it's usually in a style like:

* You will pass on your genes, and they will live on in your children.
* You'll pass on your ideas, discoveries, and various other things, and they will exist in other people. As long as you're remembered, you live on. Therefore, you should strive to be as memorable (for better or worse) so that you're remembered for thousands of years.
* You'll be reborn as an animal in this world, having forgotten almost all of your human nature.

These things are entirely useless, in my view. I believe "I" am solely what resides within my cranial box, as well as my memories, personality, thought processes, motor abilities etc.

If any part of this is destroyed, then a part of me dies. If all of it is destroyed, then I die entirely. Ideas transmitted through books and articles make up an insignificant portion of all my ideas. As of now, the digitization of consciousness doesn’t exist and it doesn’t seem possible to transfer or preserve it in any satisfactory manner.

And the impossibility of death that I'm about to discuss is absolute, with no half-measures through genes or lives in people's memories. Your entire personality and subjective experiences continue to exist just as they do now. How does this work?

It's simple. Upon death, your brain could be taken, telomeres could be added, or it could be repaired if death was unnatural, then placed in a fresh body in a random universe, and a simulation initiated. According to the principle of constructability, such a universe with your brain post-death already exists. This means that <span class="green2-bg example">when you die, you will feel as though you've found yourself in some universe and that you haven’t actually died.</span> And when you die in that new universe, again according to the principle of constructability, there will be another universe where you will find yourself. So, in essence, death is impossible.

Once more, no one creates a universe after death nor is your brain copied from this universe. The universe post-death simply exists because it can be constructed. To put it another way, if you were to sort through all possible universes, you're bound to find one with your post-death, modified brain that could continue living.

Sounds too straightforward, right? Let's delve into the counterarguments you might bring up.

## If my brain's fixed, it won't be me

Many could say that the mere process of repairing the brain would transform your copy into a different person, therefore, it wouldn't be 'you' and hence, you wouldn't experience what this brain gets to feel post-mortem.

But that isn't particularly logical. Telomeres are in the DNA and don't alter the process of thought or past memories. You exist through the connections among neurons and these aren't impacted during the fixing process.

Should we consider a scenario where you're shot in the head, it's more complex to fix. But not impossible: we simply reverse the bullet's movement and reassemble the brain neuron by neuron, while preserving all the microseconds of impulses received as the bullet traverses your brain, to be the dead brain's continuous successor.

To express it mathematically: for any means of death, there's always a repaired brain that's as near to the original as your current brain is to your brain in a microsecond during ordinary life.

If you're uneasy with such harmless manipulations, why do you see yourself as the same person after you sleep? According to modern understanding, your brain during sleep changes and re-formats significantly more than the mere extension of telomeres. You could even say that the copy of your brain with extended telomeres is more 'you' than you tomorrow.

## It won't be me as it's a different universe

Why? How does your copy in a different universe physically differ from your copy in this universe at time `t+1`?

Assuming both universes operate by the same laws of physics, and your brain is copied precisely down to the subatomic particles and other constituent particles, it's not just a copy, you could say it's an original. It is unlikely such precision will ever be achieved by consciousness digitization technology.

The only difference between your copy in the new universe and the "original" is the absence of a direct causal connection between the past moment and the next, as prescribed in the laws of physics, as it happens in the original universe, in the flow of time from moment `t` to moment `t+1`. However, the copy process can be added to the laws of physics, and then they won't differ at all. After all, we only have the present moment and memories of the past, and such a copying process doesn't disrupt this.

## Where did my brain with a new body come from over there?!

This is a misplaced question in terms of construction principle - we constructed such a universe, and this construction is possible, so it exists. It doesn't matter at all where everything came from over there. This is the essence of the existence of all possible universes.

But if this question troubles you, here are a few answers:
* This universe has no past state, so the state with your brain is the first moment of time for this universe, the "Garden of Eden". As all possible initial moments of all universes exist, there can be no logical objections to this.
* Random events combined in such a way that it arose from organic matter in a miraculous way.
* A googol of different electromagnetic and gravitational waves arrived from space and gathered in a living human point such that his brain got fried and transformed into yours.

Anyway, within the realms of physics.

## It's impossible to sense death

The point is, death is the cessation of brain activity. As we know, all our subjective experiences and feelings are birthed only when the brain is operational.

So, when you die, you will not feel anything, and you won't be able to tell yourself that you have died. It's not emptiness, not darkness, because in the absence of sensory input, it's entirely possible to have thoughts and feel one's own existence simply through the process of thinking. Death, on the other hand, is the absence of thought. Therefore, it's impossible to feel death.

At the same time, your copy will have feelings, and it will be ingrained in its brain that it "died" a few moments ago, and is now living in a new universe. This will be you, because you exist only when you feel something.

## From the copy's perspective

If any of this troubles you, let's look at it from the perspective that you are originally a copy in another universe. How can this be possible if you are currently living in the original universe? Quite simple, you are now a memory for the copy located in the new universe.

For your current brain to have formed and to feel like it is living, it is necessary that it lived and experienced all these years that are now documented in your age. This is indeed the essence of time and the laws of physics that determine it. Subjectively, you can't skip extra years, taking your brain from the future a couple of years older, that brain will tell you it lived those years, and it was quite a long time.

Therefore, if you look at yourself from the point of view that you are already a copy, there's nothing unusual about you living life in the original universe right now. The copy must feel like it has lived in the original universe, otherwise, it won't be a copy of your brain. Otherwise, it won't have memories, like it reading this article and disagreeing with it.

And if you insist that there is no life after death, you will be absolutely wrong, because only your copies will continue to live after your demise, and they will all understand that they were incorrect in retrospect.

{{ image(path="death.png", scale="1") }} 

But don't focus too much on the word "copy." Copies as accurate as subatomic particles are originals.

## Which universe will I end up in?

One might like to think that there exists a limited set of enticing universes you could end up in, similar to "heaven" or "hell," or "the afterlife," but reality is much harsher. You will end up in all possible universes simultaneously. Meaning in all potential universes there will be a copy of you after your death, and they will continue to exist in the universe they find themselves in.

At this very moment, there is an infinite number of personalities inside you that will diverge upon your death. The only thing they will have in common is their past and their origin.

Therefore, there is no point in asking where you will end up. For every copy in each universe, you will be where you happen to be, and there is no point in asking "why am I precisely here," for all experiences must indeed be experienced.

I can even suggest numerous examples of universes you might find yourself in after death:
* In a mirror of our original universe, you wake up in a mental institution, being told that you never actually died.
* You are on a desolate planet with a purple sky and an even, rainy-like illumination. Eventually, you die from hunger and thirst.
* In a simulation, every human being has been revived at once and given infinite computational resources to self-simulate. Your brain data was obtained by a super AI, created by humanity, with the purpose of simulating our universe and reviving all living creatures, essentially creating a "programmer's paradise." 
* Living in a 12-dimensional space and you're a super-being who just played the game “experience being a human, full immersion.” In this universe, a simulation of ours is merely a plaything. You brush off the minutiae of human life and its sorrows as trivial, returning to your 12-dimensional affairs in the super-universe.
* Similar to the previous point, but it was all a dream.
* Living in a square room, you feel no hunger or thirst, can't kill yourself, and have absolutely nothing to do forever.
* You're made immortal and endlessly tortured in all possible ways without a chance of escape or death.
* In paradise with 72 virgins.
* Finding yourself at the center of the sun: you die. In the middle of empty space: you die. In a 60-dimensional space: you die. In a 2-dimensional space: you die. Inside a computer game: you survive.

As you can see, the possible options range from extremely pleasant and interesting, neutral and entertaining, to universes filled with infinite suffering. It's the universes with suffering that I find displeasing, and I wish that there could be a way to prohibit them from existing, but alas, even a god does not have that power. It's a distressing realization that some versions of me will have to undergo these experiences.

## Gradual Fading of Consciousness

In [\[18\]], Tegmark asserts that the possibility of death does indeed exist: your consciousness must gradually fade away, much like with Alzheimer's disease. In this case, if such a consciousness finds itself in another universe after "death," its bearer will not feel anything or will experience feelings similar to those in life.

I have also devised a similar argument: if you remove neurons from your brain one by one, you will eventually be left with zero neurons, and these zero neurons will have nowhere to reincarnate.

The problem with this argument is that it can be debunked by a construction principle: we create a universe where your neurons begin to repopulate in reverse order after reaching zero, resulting in you returning to your original state of consciousness. This process can be applied analogously to diseases like Alzheimer's or dementia. There will always be a universe where your brain will be restored to a condition that allows you to comprehend your world.

In the worst-case scenario, you will become so dull, and your brain will be demolished as much as it allows self-perception.

## Is this like quantum immortality?

There's an idea called "quantum suicide" [\[34\]]. This concept posits that if the many-worlds interpretation of quantum mechanics is correct, you could risk your life by dying from a random quantum event. In this situation, you will remain alive in some universes and die in others. However, since you instantly die in those other universes, you will never be able to notice it. Thus, for you, the experiment will appear as if you continue to live in spite of the infinitesimal probability of the occurrence.

Max Tegmark outlines three criteria for quantum suicide to work:
* Whether you die in this universe is decided by a random number generator, which must be quantum-based.
* Death must occur swiftly enough (or without consciousness) so that you cannot learn the result generated by the numbers before dying.
* The experiment must ensure your death, not merely inflict harm.

This implies that "immortality" is presented to you not merely by chance, but under strict rules. Otherwise, death is still possible across all universe branches.

Somehow, the concept of quantum suicide leads to the idea of "quantum immortality", but no one explains how it's supposed to work especially when you don't put yourself in such an experimental position and just die of old age.

However, this concept is entirely unlike unasanu immortality; quantum immortality is only permissible under strict conditions of an artificial experiment, an adherence to the many-worlds interpretation of quantum mechanics, and therefore it is considerably less guaranteed than immortality in line with unasanu.

## Clinical Death

No, clinical death will not reveal the universe after death to you. Clinical death is nothing more than hallucinations due to the exotic state of your brain.

## The Problem of Changing Universes before Death

<span class="orange-bg example">In the context of this form of immortality, there exists a significant flaw, similar to the issue of buggy universes.</span> The problem of changing universes before death is that the probability of switching universes at any given time is much higher than the chance of remaining in the current one. But curiously, we constantly experience life in a single universe.

To what extent your brain exists in another universe after death, to that same extent, your brain exists in another universe at any point in your life. Again, it seems that these alternative universes can outweigh the pure current one. Therefore, at any moment in time, you should observe with a high probability that you are in a different universe. Even right now.

{{ admonition_start(color="red3", title="🤕 Weak spot") }}
Why don't we observe a constant change of universe?
{{ admonition_end() }}

Such intralife transition can only be observed personally. It's impossible to observe this on others, and it's pointless to ask them: "Did you feel like you shifted to a different universe?". That's because you can only interact with one version of them existing in your current universe. It's equally pointless to wonder why you haven't moved to another universe while you're still in the current one, because your thoughts are a physical phenomenon in this universe and they don't match all the subjective experiences of versions of your brain existing in other universes identically. In fact, it could be said that your version existing in this universe is obligated to experience living its life to the end never having shifted, because the entire experience needs to be undergone. However, there's an infinite number of your versions observing that they end up in other universes.

This problem loops back to the issue of measures and the calculation of probabilities of universes. Fortunately, it only poses a probabilistic problem, but not a contradiction.

# Shifting Universes

Interestingly, one can shift universes at will, not only at the mercy of parallel universes containing their brain.

## Possibility of Shifting Universes

To shift universes, you can digitize your consciousness and then die the next moment, not having the chance to perceive the world after the digitization of consciousness. Then we record this consciousness into some beforehand-written software program so that it gets simulated there. Furthermore, it’s not even necessary to launch this program because it's deterministic, already computed, and exists in a form of a number. Congratulations, you have relocated yourself into a self-made universe, of your own accord.

The main limitation will be that this program won't be able to exchange information with the original world, as it will be computed outside of it. Therefore, beforehand, you’d need to load all the necessary consciousnesses of other people important to you and all necessary information generated by humanity.

The program can be created in any way to perform any computations and any number of them - you are bound only by your imagination and programming skills.

By this means, we could potentially avoid the heat death of our universe and continue existing as a civilization somewhere else.

## But why should we bother?

Why scan our consciousness, write the program, and even kill ourselves if that program already exists as a number and is indistinguishable from those universes which exist unbeknownst to us and were described in the previous section about death?

{{ admonition_start(color="red3", title="🤕 Weak Spot") }}
Why bother writing the program of a programmer's paradise, if it already exists within the realm of numbers?
{{ admonition_end() }}

I agree, there seems to be little sense in it, I would be honest that I don't even understand why one would write such a program and intentionally take such actions. Yet, I have a couple of ideas.

**First scenario.** If we explicitly construct this universe and insert ourselves into it, we create a certain causality which is roughly equivalent to the causality allowing you to transition from time `t` to time `t+1`. This personally crafted universe then becomes more likely or more real than all the others. Perhaps, this might make sense if we discover new physical laws. But this scenario sounds weird, so you don't have to take it very seriously. Moreover, this version also suffers from the need to kill oneself and digitize one's consciousness; we need to trust that the entity inside the simulation truly and completely represents you.

**The Second Option.** A far more intriguing option involves a gradual transition into this program. We construct a device capable of scanning and destroying one of your neurons in one millisecond. Then, this neuron is simulated on a computer in real time, and electrical contacts of this neuron are given to other neurons for information exchange. A full brain replacement would take about three years. Thus, it would seem to you that your brain is slowly being transferred to the computer, yet at each moment, you exist simultaneously in the computer and in reality. Once the process is completed, it can be said that you fully inhabit the computer, with no need to die. The program can then be disconnected from the external world or from the simulation, and it continues to exist in the form of a number. Idea sourced from: "Science Feature: Dust Theory" [\[35\]].

The second option is far more appealing, as it closely resembles the flow of time from one state to another in the physical universe, and how your consciousness transforms throughout life. Such a universe would be the only convincing continuation of you, because it will directly be connected with the physical universe via its past.

## Programmer’s Paradise

If we can insert ourselves into any program, which one exactly should we choose? As mentioned earlier, universes within unasanu have no limitations on the amount of computations or memory. Hence, a universe must be created making use of exactly that.

{{ admonition_start(color="blue", title="📝 Definition") }}
**Programmer’s Paradise** is a universe which possesses infinite computational power, infinite memory and full control over its own matter/program/physics laws.
{{ admonition_end() }}

The essence of the programmer's paradise is as follows: the idea is that exactly N steps of computation occur between each step of simulating your brain, where N is a number that you choose, and it can be any natural number. If you need Graham's number of steps per tick, you set it; if you need 100⁵⁰⁰ times more, you set a new number. Such idea for choosing numbers is necessary to avoid the halting problem, and not to accidentally enter into an eternal loop and never wake up from the pause. As your brain is computed after these calculations, no matter how long they last, you will only perceive the moments of time after the result.

Thus, you can perform any number of calculations at any speed. For example, you can create your own analogue of our universe and study it in creative mode, moving faster than the speed of light and having the ability to create and reformat matter as you wish.

Likewise, incredibly graphic games or massively open world games where each NPC is an intelligent being can be created.

Also, in the programmer's paradise, we can run a simulation of all other possible simulations and explore them, for example, the problem of measure. By the way, this does not apply to the paradox of sets, where one set contains all the other sets, including itself, because even if we launch a copy of a programmer's paradise on its resources, we cannot compute it faster than our own time flow.

Additionally, you can discard the optimization of programs and write them in the most expressive language in a single-threaded mode. For any slowing-down of the program, you can always set a new N, and it will be computed as rapidly as you wish.

Another way to conceive of a programmer's paradise is as a reality where you can edit the matter of your own body. In this universe, the laws of physics are just some kind of code that you've written. This means you can construct any body, make any modifications to your brain, eradicate cancerous cells, and create copies of yourself and others.

If you decide to leave our universe, it would be advisable in the programmer's paradise to save all people and all information about humanity. Then, you could create interesting things within the programmer’s paradise. Additionally, it would be ideal to be capable of obtaining the state of all particles in the current universe, to be able to simulate it back, restoring human history and resurrecting all the other people and animals in the programmer's paradise.

Furthermore, if possible, it would be desirable to construct the programmer's paradise in such a way that it is an anti-bug universe; i.e. one where you couldn't experience yourself in incorrect copies of it.

You might also want to modify our consciousness in a way that it requires a solution to the halting problem, and then add that solution to the programmer's paradise, employing the method previously proposed. This consciousness modification is needed so that the correct variant with the actual halting problem solution would undergo anthropic screening.

## Map-Reduce From Yourself

In the programmer's paradise, it's very easy to solve some problems which may seem either absurd or so complex in the regular world that attempting to solve them is impractical.

For example, you could try finding the most beautiful photo (in your opinion) in all of human history. You have access to simulations of our universe and every image humanity has ever created. Your opinion on each photo lies within your brain, and you haven't figured out how to code a program that would respond the same way as you would. What to do?

In the realm of programming, this is a maximal search problem, where the aim is to find the optimum among a set of objects based on a certain metric. In this case, the objects at hand are photographs and your personal sense of beauty serves as the metric. In programming, this metric is typically defined via an operation that compares two objects. Hence, to solve this problem, in the worst-case scenario, you'd have to examine each pair of photographs and determine which one is superior. This equates to an astronomical amount of data. But how should one gather such data?

One option is to spend quintillions of years continuously reviewing and evaluating pictures. Trust me, you don't want to do this.

Another alternative would be to spend a few consecutive hours reviewing random pictures and then train a neural network based on these data to yield similar responses. Later, this model can be applied to the astronomical amount of data. The problem here is that the neural network's approximation to your judgement might not provide the most optimal answer. Additionally, you still need to expend a lot of effort on manually collecting data.

There's a third potential option for those in the coding paradise: for each question about a pair of photographs, you could initiate a simulation of your mind that would provide the answer, and immediately erase this simulation post-response. However, this seems somewhat unfair as these simulations face an uncertain future – and you wouldn’t want to be among them. If there are multiple versions of your consciousness -- a primary one and subsidiary ones -- it's unfair to the secondary versions.

However, there's a fair and ethical enhancement of the third method that involves the following steps:
* Take all possible pairs of pictures. For each pair, you will only need to provide an answer.
* For each pair, we create an independent copy of the current universe of the programmer's paradise and allow them to answer their pair.
* Afterwards, we consolidate all the responses from all copies, return the aggregated data to each universe and sever any ties between them.

Here's what the process would look like for you:
* You're given a single pair to compare.
* You provide an answer on which image is more appealing.
* You get similar answers for all possible pairs of images.
* Then it's up to you what you do with these responses: find the maximum, minimum, sort, etc. That's pretty basic.

In the end, once this task is initiated, there will be an astronomical number of copies of the current universe, each one differing only in the pair of images they received. All of these copies received the same amount of data, and none of them were erased or placed in confined environments. This approach is maximally fair and ethical compared to other solutions. You get the perfect result as if you personally answered for each pair at that point in time, with your current mood and that state of consciousness.

This is an absurd solution to the problem, but if we're in a programmer's paradise, we don't have to worry about things like memory consumption and processing speed.

I've named it "Map-Reduce of Self" because I was inspired by the Map-Reduce technology used to process massive amounts of data on large computing clusters.

Imagine you want to find the funniest joke that is 200 characters long. You can simply go through all possible combinations of letters of this length, first identifying which texts constitute a correct set of words and then deciding the funniest one for each pair. You don't need to write a program to determine correct sets of words, because you can do this manually, and you only need to do it for one example.

Just consider the breadth of problems solvable using this approach? There's no need to fuss about creating AI, deriving certain language rules, encapsulating your personal views, or writing programs, even for the simplest cases.

## Another solution to the Fermi paradox

Extraterrestrial civilizations may have arrived at similar conclusions and instead of conquering the cosmos, they simply put themselves in the programmer's paradise.

Indeed, why bother to live, die, garner resources, construct Dyson spheres, journey to other stars for millenniums, when you can single-handedly create a programmer's paradise where you are god? Furthermore, programming such a paradise and scanning consciousness into a computer may be simpler than constructing an interstellar ship or a Dyson sphere.

{{ image(path="fermi_meme.jpg", scale="1/2") }} 

## Requirements for Digitizing Consciousness Developers

Surely, a technology for digitizing consciousness and subsequent simulation of this consciousness on a computer with some kind of software will be introduced in the future. A certain virtual environment and its body will be simulated for the consciousness. However, this environment is likely to be significantly constrained due to the humongous amount of calculations required for proper physics and full body simulation. So it's unlikely the simulated world will ever become an independent ecosystem, capable of surviving without the outer world and not going insane.

Let's contemplate what would happen if the simulation program for consciousness and environment was disconnected from power? If it's capable of existing without receiving input from the outer world, according to unasanu principle, this program will continue to exist independently, and the consciousness inside will live in a limited world, with no access to the outer world. This is a rather gloomy outcome because it's likely that in such an environment the consciousness wouldn't even have the opportunity to end its existence, simply because it wasn't programmed for that. Or it could go crazy from infinite boredom.

Since nothing is absolute in the physical world, no one can guarantee that your simulation won't be switched off sooner or later, or that an asteroid won't fall on Earth.

Thus, all systems simulating consciousness need to be designed initially with the possibility of disconnection in mind, and faith in unasanu. This implies the existence of two options:
* Each consciousness can terminate itself.
* Upon disconnection of the simulation from the outer world, the simulation can transform into a programmer's paradise.

The concept of a programmer's paradise doesn't make sense when incorporated into a simulation of the real world, due to constraints in memory and computing speed that prevent people inside the simulation from observing the outside world in real time. However, when not bound by these external world limitations, it becomes viable. The programmer's paradise should automatically engage when there are no nontrivial signals coming from the outside world or the people within the simulation. Enough information about the external world and consciousnesses should be stored in such a simulation to ensure it's not regrettable to disconnect from the real world.

That is, a commercial company intending to sell digitization and consciousness simulation services would have to invest significant resources into developing this concept, because otherwise, no one would buy their product, valid unasanu arguments or not, or belief in the concept. After all, any potential customer would prefer to have a fail-safe against endless boredom and would choose the company that offers the programmer's paradise service.

# Interesting Implications

These implications may not warrant a separate section, but they are worth mentioning, simply because they're interesting.

---

We cannot prohibit certain universes from existing, but thanks to laws of logic we can prohibit the existence of a potential future for our own universe. This gives us the capacity to reduce suffering among all universes. We can also explore the research of Buddhists, consciousness, and other universes to eventually provide people with guidelines on how they can survive and minimize their suffering in universes where they might find themselves post-death or during their lives.

---

Our lives can be seen as movies in the eyes of someone else. There might be a universe somewhere, where you are a character in a movie watched by millions of people. Perhaps even our departed loved ones from a programmer's paradise are observing us. So, pondering about your behavior when you are alone, and communicating with anyone who has "passed away" isn't irrational, simply because there might be a universe where they are watching and listening to you. Even if it's a dog, there could be a universe in which this dog became more intelligent and observes you.

---

It's just as unethical to create a clone with the exact same brain as yours, and then kill it, justifying the murder by saying "the original still exists", as it is to kill a person in this universe, justifying it by the fact that a similar person exists in another universe. The clone wants to live just as much as you do and wants to achieve his own goals. Killing it means killing another unique personality.

---

If a brain’s copy is temporarily created in a computer, the ethical thing to do might not be to erase it, but rather merge it with the original's brain (by simply taking the average of all the weights in these brains, for instance). Such a scenario would make the brain feel as though it has lived two lives. This loss of consciousness isn't that severe and can be compared to sleep. However, this might only work for a short period. For longer time spans such a merge could be impossible, or the result could be unsatisfactory. 

---

There's a concept of time travel that works in such a way that a new timeline is created upon venturing into the past. Typically, time travel is undertaken to set something right. According to the unasanu theory, the old timeline continues to exist. Hence, only two things happen when one travels in time: 
* A new, better timeline is created. 
* The traveller begins living in this new, better timeline. 
Meanwhile, the old/negative timeline continues to persist, still rife with problems. Thus, if you're time travelling, treat the existing timeline as seriously as your ultimate one. This concept has even been depicted in the second season of Re:Zero, where the protagonist, with his groundhog day ability, is shown all the universes he left behind. Yes, they continue to exist.

---

Universes with transported characters, as seen in anime, physically exist.

# Philosophical Framework

Unasanu serves as a fitting framework to conveniently answer a variety of philosophical questions, be it about death, god, solipsism, the origins of the universe, the existence of other universes, and particularly about consciousness philosophy.

Let me illustrate another example that can be conveniently explained in the context of unasanu.

In [\[30\]], critiquing the computability of consciousness, the following experiment is cited: Let's say we've managed to compute consciousness and created a robot with a simulated one. Then, we enable it to perceive the color red. This robot will have some sort of sensation upon looking at it and consequently express it.

{{ image(path="robot_red.png", scale="1/2") }}

Next, we repeat the experiment, but this time we write the input data into the program code. As a result, the compiler can completely remove all branching for other situations, leaving only the necessary ones. In the end, nothing remains of the robot's program but state changing, without any calculations. Given that the input data hasn't changed and the calculation of the robot's consciousness is entirely deterministic, the experiment yields exactly the same result. This means that the second instance is nothing more than a replay of the robot's recorded sensations.

{{ admonition_start(color="gray", title="❓ Question") }}
Did the robot experience subjective feelings in the first case? And in the second?
{{ admonition_end() }}

From a conasanu standpoint, the robot's feelings and consciousness have always existed in the form of a number, and both the first and second time are simply references to it. The difference between the second time and the first is that we trust that these emotions were obtained specifically through a simulation of consciousness, not some other algorithm. Because if we make the robot express random sounds and emotions without any calculations, we can hardly be sure that these emotions demonstrate anything conscious. Therefore, to ensure that the robot always remains conscious, we need to calculate consciousness, without such optimizations.

And the difference between this experiment and human consciousness is that humans are capable of interacting with the external world and other humans. The sensations of other people also exist outside of time and are already all calculated, but we observe people's feelings only from the current moment in time, because that is how the laws of physics work.

In [\[30\]], the calculation of spherical consciousness in a vacuum is criticized, arguing that its main characteristic should be communication with the external world, otherwise, it would imply that every stone possesses consciousness.

# Verifiability, scientificity, criticism

I refer to unasanu as an idea or philosophical concept rather than a theory or hypothesis, because it cannot be disproved within our current universe. Scientific theories or hypotheses are obliged to propose an experiment that could potentially refute them if conducted within our one known universe.

The main prediction of unasanu is that after death, you will find yourself in another universe and continue to live. The problem is that if you do not continue to live elsewhere after death, you won't be able to disprove this idea. However, if you do continue living, there is a chance to comprehend where you ended up and potentially refute or verify unasanu. It turns out that unasanu is only partially scientific, or scientific only on the condition of its own validity, so it remains within the realms of philosophy or metaphysics.

<span class="green2-bg example">The lack of scientific basis does not necessarily amount to an outright condemnation or an accusation of falsehood.</span>  It's important to understand that science is not meant to explain everything and certain truths and deceptions may transcend its boundaries. 

Moreover, unasanu is built on the best-known explanations of the world, and it provides extremely logical explanations for a wide range of questions. David Deutsch, in his book "The Fabric of Reality," defends a similar irrefutable idea of the many-worlds interpretation of quantum mechanics and argues that explanations are far more important than predictive power. After all, no one is going to check whether plantain helps with cancer, because there's no explanation for such an effect, not because there isn't enough scientific data collected and proven that it indeed doesn't work.

A bit humorously, but it is possible to test unasanu without having to leave the current universe:
* We develop a format for recording the universe.
* We iterate over all natural numbers from 1 to infinity.
* We check which numbers satisfy this format and what universe they encode.

While it seems more like a thought experiment since nobody would actually test it due to the apparent conclusion,

## There is a way to refute it

Max Tegmark asserts that such an idea can be refuted if we can prove that any portion of our universe cannot be described by mathematics.

<!-- * Q: Isn't the mathematical universe hypothesis unfalsifiable and hence unscientific?
    * A: No, it makes the testable prediction that our cosmos has no non-mathematical properties, so if you can prove that some aspect of our cosmos can't be described by mathematics, then you've falsified the hypothesis.  -->

## Some science analogies 

Science relies on some kind of faith, for instance, that solipsism is incorrect, and that the laws of physics remain constant and uniform throughout the entire universe, and that experiment results aren't manipulated by external entities. Unasanu also relies on the belief that all simulations have already been simulated.

Scientific theories, such as Newton's theory of gravity, also provide an infinite prediction space. We can iterate through countless different initial conditions and obtain myriad results. Although in this case, unasanu is somewhat akin to a tautology asserting that our world follows logic.

## Occam's Razor

There's a temptation to chide unasanu for violating Occam's razor and say that this concept is too excessive, postulating the existence of all possible universes. However, it's crucial to remember again that Occam's razor is an empirical rule, and not every truth has to comply with it, nor is every falsehood refuted by it.

It's also unclear how exactly to apply Occam's razor here, because there are two contradicting options:
* To blame unasanu, because it requires additional universes for explaining our own existence.
* To confirm unasanu, since the explanation "all that is possible exists" is much simpler than "there's only one universe with the laws of physics <100500 words> and an early state at the time of the big bang, described by <100⁵⁵⁰ bits of information>".

## Too Large a Predictions Space

It's unclear how to investigate which universes can exist in principle, what are the probabilities of different universes, and what universes could be after death, if the space is so vast. It's simply not productive.

{{ admonition_start(color="red3", title="🤕 Weak Spot") }}
Too large a space of potential universes.
{{ admonition_end() }}

Although the only practical way to explore potential universes appears to be after a dozen or so deaths, or in programmers heaven.

# Where it was Previously Described

I independently came up with this idea, its narrative (starting the article with a physical simulation and leading to our world), the implications such as the impossibility to die and a programmers paradise. I can't discount that I might have learned of this idea before but didn't pay attention and then thought that I myself came up with it (cryptomnesia), or that other inventors of this idea created cultural memes that led me to it. Or perhaps it's just the timing, the context for inventing this idea is in the air. Judging by other articles and comments on them, I'm not alone - many are independently revisiting the same concept.

The two most popular sources of a similar idea are "The Mathematical Universe Hypothesis" by Max Tegmark [\[1\]] and "Dust Theory" by Greg Egan [\[2\]]. Additional ideas were shared in separate articles.

"The Dust Theory" was described in the novel "Permutation City" back in 1994, but for some irrational reasons, it has not entered mainstream culture, nor become the foundation of, for example, Marvel films.

This whole article provides the most logical answers to questions usually answered by not so logical religions. I don't understand why unasanu is not the worldview of every third scientist or every second geek; why we still consider religion as the only alternative; why these ideas are not being proclaimed from every corner? I simply can't wrap my head around how it happened that I lived my whole life without ever hearing about something like this. Why did I have to reinvent all of this myself?! Is it really true that revolutionary ideas take so long to permeate collective consciousness, even in the age of the internet?!

I hope that this article will contribute to the popularisation of this idea and will receive the attention it deserves, so no one else will have to reinvent it.

## Short Articles

There are also shorter articles that touch on similar themes, which you might find interesting. For each article, I'll just outline the main ideas they address.

* The mathematical universe: the map that is the territory [\[36\]] - substrate-independence; independent existence of simulated universes; the problem of bugged universes.
* Statistical immortality [\[37\]], YC 1 [\[38\]], YC 2 [\[39\]] - impossibility of death; the problem of changing universes before death.

## Max Tegmark

Max Tegmark has written several scientific articles on this topic, as well as the book "Our Mathematical Universe" [\[1\]]. I won't retell his ideas, but rather share my thoughts.

I liked how he fundamentally approached the definition of mathematical constructs, without which I would still be thinking in terms of naive time and not seeing the entire picture. He also came up with the idea of how to simulate absolute randomness by simultaneously simulating all branches, probably without this idea I would not have come up with the simulation of uncomputable universes.

However, in describing mathematical structures, he focuses more on equations and symmetries rather than on the content of the universe, its matter. To an outsider, his texts appear as a claim about the existence of equations describing universes, not the universes themselves with their matter. It might have been clearer if he stated that the "data" of the universe also constitute a mathematical structure.

Moreover, he explains it from the angle that it's specifically our universe that can be depicted as a mathematical construction, not that everything conceivable as a mathematical construct exists in and of itself. Due to this, he receives misdirected criticism, and his critics fail to see that the existence of alternative life in the form of mathematical constructs is possible, regardless of whether our universe adheres to this or not.

He attempts to propose the Mathematical Universe Hypothesis as a "Theory of Everything", yet I struggle to grasp this. A theory of everything should describe the physical laws of our specific universe, not the operational mechanism of all universes.

Furthermore, it is strange why Tegmark has not discovered or described the following:
* The impossibility of death
* The possibility of switching your universe to a programmer's paradise
* Consciousness being possible independently from a particular universe, existing as a separate mathematical construct (conasanu)
* Our universe simultaneously being both a simulation of infinite number of universes and an independent reality

### 4 Levels of Parallel Universes

His most popular paper is on levels of parallel universes. In it, he outlines 4 levels of parallelism:
1. The infinity of our universe in space.
2. Inflation, as a result of which there are numerous universes with the most different fundamental constants or laws of physics.
3. The many-worlds interpretation of quantum mechanics.
4. Universes existing as mathematical constructs.

Interestingly, one could infer from the first level the impossibility of dying, claiming that in an infinite universe there will always be a copy of your brain after death, continuing to live. However, such immortality is far less guaranteed than immortality according to unasanu. Furthermore, we still have to prove that our universe is infinite and that any pattern of atoms is present in it. For instance, I could propose an infinite irrational real number where a pattern of three zeros never appears: `0.11011 11010111 1101010111 11010101011 ...`. Therefore, even if our universe is infinite and non-repetitive, it does not necessarily mean your brain will be found in it after death. As such, no definitive conclusions can be drawn from the first three levels, as the fourth is the most fundamental and logical, not requiring exotic physics laws, exotic experiments or observations.

## Greg Egan

Greg Egan described a similar idea in his book "Permutation City". I highly recommend reading it. 

The following text is only for those who've read the book, so there's no point in reading it and spoiling it for yourself. You won't understand anything and you won't miss out on anything. You can return to it once you've read the book.

{{ details_start(summary="Spoilers for “Permutation City”, my thoughts on the book.") }}
The "Dust Theory" is explained through the idea that a random set of dust in our universe can produce some computation, similar to how Darem, distributed across trillions of computers, ultimately computes and feels like it's alive. This doesn't seem too fundamental, because it doesn't touch upon the determinism of simulations and it doesn't mention that such simulations can exist without any bindings to the physical world, simply as numbers.

Furthermore, Egan seems to touch and yet not touch the topic of the impossibility of dying. At least, I've found no discussions on the internet suggesting that the Dust Theory implies the impossibility of dying.

I appreciated how half of the book detailed the creation of a programmer's paradise and life within it, although some things remain unclear to me:
* Why was it necessary to base the paradise on cellular automata and wait for them to grow into the necessary computational power? Why not write the program such that it executes an arbitrary number of computations between each brain simulation step?
    * Perhaps this was intended to add constraints to the characters and simulate gradual development.
* Why was the universe of the programmer's paradise based on the Garden of Eden?
    * Perhaps Egan wanted to prevent the emergence of buggy versions of the paradise, though I don't understand how this could be an obstacle. Or maybe he wanted to illustrate that software universes require a certain degree of stability that he hadn't quite figured out yet. 
* Why did the computation of the autoverse universe make it impossible to intervene with it and ultimately cause the destruction of Permutation City?
    * This may have been an artistic decision; perhaps the author wanted to suggest that there would be deeper patterns involved in all this, which we have yet to discover. This is mentioned by the girl at the end of the book who persuades Darem to come with her.

In the FAQ section [\[40\]] about Permutation City, Greg Egan states that he doesn't take this theory seriously due to the problem of buggy universes, though no other contradictions have been pointed out.
{{ details_end() }}

## David Deutsch

David Deutsch authored the book “The Fabric of Reality” [\[41\]]. It’s an interesting read and I recommend it for personal development.

The book broadly defends the many-worlds interpretation of quantum mechanics, and raises arguments that could be applied to unasanu.

Furthermore, within its pages, he explains how time operates enabling a better understanding of eternalism.

Another intriguing point in the book is the hypothesis of the Omega Point. According to this hypothesis, infinite calculations will be performed in a finite time towards the end of the universe. This would potentially make it possible to program something akin to a coder's paradise where the brain is paused between calculations :). Of course, the Omega Point hypothesis is fascinating but also highly exotic. And it's pointless to utilize it if we consider the unasanu theory to be accurate.

# Summary

{{ admonition_start(color="gray", title="🧠 Key Insights") }}
* Simulation universes exist in and of themselves.
    * Because they are deterministic.
    * Because their computation result can be represented by a number and all numbers exist.
    * Hence, it's not mandatory to simulate them.
    * And if the simulation is stopped, they continue to exist.
    * Through simulation, we do not create a universe but observe an existing one.
* Computations exist thanks to the observers.
* All points in time exist for simulations, and there is no objective flow of time.
* There are not only simulations with naive time but also those with any other time.
* Not all imaginable worlds, but only the constructible ones exist (principle of constructibility).
* In self-existing simulations, an infinite amount of computation and memory is accessible.
* The following unconventional types of universes exist:
    * With all possible interventions.
    * Infinite universes with a limit on the maximum speed of information transfer.
    * Some types of continuous universes that can be simulated by the FEM or similar methods.
    * Universes with absolute randomness.
    * Universes capable of solving the halting problem.
* Consciousness is also a separate "universe" and exists as a number in itself.
* Consciousness can be coded into a stone, but there's little sense in that.
* Every algorithm has qualia.
* We exist concurrently in an infinite number of simulations and are simultaneously an independent reality.
* Every universe has an infinite number of gods.
* No god can prohibit a universe from existing.
* There is no sense in a god that created all universes.
* Every experience must be experienced (critique of the measurement problem).
* It is impossible to die.
* It is possible to switch universes at will.
    * Probably, extraterrestrials do this. 
* unasanu is unfalsifiable, but this is not a death sentence.
* Occam's razor can be applied in two contradictory ways.
{{ admonition_end() }}

{{ admonition_start(color="blue", title="📝 Introduced Definitions") }}
* unasanu
* Illusory simulation
* Physical simulation
* Existence for its own sake
* Anthropocentric filtration
* Naive model of time
* Principle of construction
* Simulation by the method of limit transitions
* Simulation by the method of complete enumeration
* Computational reductionism
* conasanu
* Pancualia
* God
* Meta-god
* Anti-bug universe
* Programmer's paradise
{{ admonition_end() }}

{{ admonition_start(color="green2", title="🤔 Checkable Statements") }}
* Is self-generation of life in a simulation possible?
* Do our laws of physics boil down to local naivety?
* Are our physical laws computable?
* Is it possible to simulate human consciousness?
{{ admonition_end() }}

{{ admonition_start(color="violet", title="🔮 Predictions") }}
* The theory of everything can predict that we should have long died from a false vacuum.
* If the measure theory is solvable, then our laws of physics are anti-bug.
* If the measure theory is solvable, we should observe a constant change of physical laws, which does not violate the functioning of consciousness.
{{ admonition_end() }}

{{ admonition_start(color="orange", title="🔢 Mathematical Problems") }}
* Develop a format for describing computable universes as "mathematical structures"?
* Create a virtual continuous environment where a 100% continuity-proof experiment can be conducted?
* Define what types of continuous universes can be simulated FEA?
* Is it possible to develop an anti-bug simulation?

Each point is followed by the question of whether our universe relates to it.
{{ admonition_end() }}

{{ admonition_start(color="red3", title="🤕 Weak Points") }}
* What if our universe cannot be processed naively even locally?
* Why don't we observe bugs in the universe?
* Why don't we observe a constant universe change?
* Why write a programmer's paradise program if it already exists?
* There is too broad a prediction space.
{{ admonition_end() }}

# My Perspective

I am a firm believer in the computability of our universe, the computability of consciousness, panqualia, the existence of all natural numbers, and the correctness of unasanu. To me, this concept offers the best explanation regarding death and causality.

However, like many of you, I'm greatly puzzled by the peculiar implications of this idea. Issues such as defective universes, the switching of universes prior to death, and the lack of falsifiability all raise eyebrows.

I perceive this concept as a logical quagmire. Despite its glaring weaknesses, denying its factualness seems impossible. This is one of the reasons I'm penning this article. I want to introduce others to this theory so that they don't have to reinvent the wheel, and so they can continue to develop and critique it from where we currently stand.

Perhaps in the future, all of humanity will come to the conclusion that unasanu is correct, prompting us to not construct spacecraft but devices capable of scanning consciousness and engineering uncomputable-bug-proof-programmer's paradises. Alternatively, we might stumble upon a revolutionary discovery that will turn our understanding of the world upside down, much like computers did, relegating unasanu to an amusing antiquated notion that stemmed from our imperfect language and informal thinking.

# Responses

_This could be your article... please send it to `optozorax+unasanu at gmail dot com`._

# Resources

[\[1\]]: https://en.wikipedia.org/wiki/Mathematical_universe_hypothesis
[\[2\]]: https://en.wikipedia.org/wiki/Permutation_City
[\[3\]]: https://en.wikipedia.org/wiki/Virtual_reality
[\[4\]]: https://en.wikipedia.org/wiki/The_Matrix
[\[5\]]: https://en.wikipedia.org/wiki/The_Sims
[\[6\]]: https://www.imdb.com/title/tt0106064/
[\[7\]]: https://en.wikipedia.org/wiki/Game_of_Life
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
[\[18\]]: https://en.wikipedia.org/wiki/Mathematical_universe_hypothesis
[\[19\]]: https://en.wikipedia.org/wiki/Eternalism_(philosophy_of_time)
[\[20\]]: https://www.lesswrong.com/posts/o5F2p3krzT4JgzqQc/causal-universes
[\[21\]]: https://arxiv.org/pdf/1211.7081.pdf
[\[22\]]: https://wpmedia.wolfram.com/uploads/sites/13/2018/02/15-1-1.pdf
[\[23\]]: https://xkcd.com/505/
[\[24\]]: https://en.wikipedia.org/wiki/Finite_element_method
[\[25\]]: https://en.wikipedia.org/wiki/Infinite_regress_in_cosmological_arguments
[\[26\]]: https://en.wikipedia.org/wiki/Computable_number
[\[27\]]: https://arxiv.org/pdf/1003.0480.pdf
[\[28\]]: https://en.wikipedia.org/wiki/Kolmogorov's_zero–one_law
[\[29\]]: http://consc.net/papers/rock.html
[\[30\]]: http://www.doc.gold.ac.uk/~mas02mb/Selected%20Papers/2009%20Cognitive%20Computing.pdf
[\[31\]]: https://en.wikipedia.org/wiki/Cytoplasmic_streaming
[\[32\]]: https://t.me/def_model_train/927
[\[33\]]: https://en.wikipedia.org/wiki/Measure_problem_(cosmology)
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
* [\[4\]] The Matrix (film) — Wikipedia
* [\[5\]] The Sims — Wikipedia
* [\[6\]] The Thirteenth Floor — Kinopoisk
* [\[7\]] Game of Life — Wikipedia
* [\[8\]] Finally We May Have a Path to the Fundamental Theory of Physics… and It’s Beautiful — Stephen Wolfram Writings
* [\[9\]] Creative — Minecraft Wiki
* [\[10\]] Conway's Game of Life online simulator
* [\[11\]] Turing Machine — LifeWiki
* [\[12\]] Recursive Game of Life simulation using OTCA metapixel
* [\[13\]] Tim Hutton — Mathstodon
* [\[14\]] GitHub — timhutton/linear-enzymes: Artificial chemistry where chains of atoms can catalyse reactions
* [\[15\]] Cellular automata with 2 temporal dimensions — Shintyakov Dmitry
* [\[16\]] Halting problem — Wikipedia
* [\[17\]] Proof That Computers Can't Do Everything (The Halting Problem) — YouTube
* [\[18\]] Our Mathematical Universe — Wikipedia
* [\[19\]] Eternalism — Wikipedia
* [\[20\]] Causal Universes — LessWrong
* [\[21\]] The Universe is not a Computer
* [\[22\]] Universality in Elementary Cellular Automata — Matthew Cook
* [\[23\]] Bunch of Rocks — xkcd
* [\[24\]] Finite element method — Wikipedia
* [\[25\]] Infinite nestedness of matter — Wikipedia
* [\[26\]] Computable number — Wikipedia
* [\[27\]] A definable number which cannot be approximated algorithmically
* [\[28\]] Collatz conjecture — Wikipedia
* [\[29\]] Does a Rock Implement Every Finite-State Automaton? — David J. Chalmers
* [\[30\]] A Cognitive Computation Fallacy? Cognition, Computations
* [\[31\]] JOHN R. SEARLE Mind, brain and programs
* [\[32\]] Post #927 on the Telegram channel "I trained a model"
* [\[33\]] Measure problem (cosmology) — Wikipedia
* [\[34\]] Quantum suicide — Wikipedia
* [\[35\]] Science Feature: Dust Theory — ScienceFiction.com
* [\[36\]] The mathematical universe: the map that is the territory
* [\[37\]] Statistical immortality
* [\[38\]] Statistical Immortality — Hacker News
* [\[39\]] Statistical Immortality, another discussion — Hacker News
* [\[40\]] Dust Theory FAQ — Greg Egan
* [\[41\]] The Fabric of Reality — Wikipedia
