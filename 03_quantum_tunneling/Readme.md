# 03 - Quantum Tunneling

## Introduction
 
Quantum Tunneling is one of the most surprising predictions of quantum mechanics.

According to classical physics, a particle cannot pass through an energy barrier if it does not possess enough energy.

However, quantum mechanics predicts something very different.

Particles behave like waves, and these waves can sometimes penetrate and pass through barriers that would be impossible to cross according to classical physics.

This phenomenon is called **Quantum Tunneling**.

---

## Classical View

Imagine a ball rolling toward a wall.

If the ball does not have enough energy to climb over the wall, it will bounce back.

Classical physics predicts:

```text
Ball < Wall

Cannot Cross
```

The outcome is completely predictable.

---

## Quantum View

In quantum mechanics, particles are described by wave functions.

When a quantum particle encounters a barrier:

* Most of the wave may be reflected.
* A small portion of the wave can pass through the barrier.

This means there is a probability that the particle appears on the other side.

Quantum prediction:

```text
Particle < Barrier

May Cross
```

Even though it does not have enough energy.

---

## Why Does Tunneling Happen?

Quantum particles are not tiny solid balls.

They behave like waves.

A wave does not stop abruptly at a barrier.

Instead, part of the wave extends into and sometimes beyond the barrier.

This creates a non-zero probability of finding the particle on the other side.

---

## Real-World Applications

Quantum tunneling plays an important role in modern science and technology.

### Nuclear Fusion

Inside the Sun, hydrogen nuclei tunnel through energy barriers and fuse together.

Without tunneling:

* The Sun would not shine.
* Life on Earth would not exist.

### Radioactive Decay

Many radioactive processes occur through tunneling.

### Flash Memory

Modern SSDs use quantum effects that depend on tunneling.

### Scanning Tunneling Microscope (STM)

Scientists can image individual atoms using tunneling currents.

---

## Tunneling Probability

A simplified approximation for tunneling probability is:

T ≈ exp(-2κL)

Where:

* T = tunneling probability
* κ = constant depending on particle and barrier properties
* L = barrier width

Important observations:

* Wider barriers reduce tunneling.
* Higher barriers reduce tunneling.
* Smaller particles tunnel more easily.

---

## Files in This Folder

### tunneling_probability.py

Calculates the probability that a particle tunnels through a barrier.

Concepts:

* Exponential decay
* Barrier width
* Quantum probability

---

### barrier_visualization.py

Visualizes a particle's energy compared to a potential barrier.

Concepts:

* Potential energy barriers
* Particle energy
* Quantum interpretation

---

### quantum_tunnel_simulation.py

Simulates many particles attempting to tunnel through a barrier.

Concepts:

* Random events
* Probability
* Quantum measurement outcomes

---

## Key Takeaways

* Quantum tunneling is impossible according to classical physics.
* Quantum mechanics predicts a finite probability of crossing barriers.
* Particles behave like waves.
* Tunneling powers many natural and technological processes.
* The Sun's energy production depends on quantum tunneling.

Quantum tunneling is one of the clearest demonstrations that the microscopic universe behaves very differently from our everyday experience.
