# Einstein's General Relativity Theory Visualization

An interactive Python visualization tool to demonstrate key concepts from Einstein's General Theory of Relativity in 2D and 3D.

## Overview

This project is an educational tool to visualize three fundamental aspects of General Relativity:

1. **Spacetime Curvature** - How massive objects curve spacetime
2. **Gravitational Lensing** - How light bends around massive objects
3. **Gravitational Time Dilation** - How time flows in gravitational fields

## Features

* 3D spacetime curvature with orbiting particles
* Visual representation of gravitational lensing effects on light sources
* Graph of time dilation at different distances from a massive object
* Simple menu-driven interface
* Educational explanations

## Requirements

* Python 3.6+
* NumPy
* Matplotlib
* Matplotlib's Animation and 3D Toolkit

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/general-relativity-visualization.git
   cd general-relativity-visualization
   ```

2. Install required dependencies:
   ```
   pip install numpy matplotlib
   ```

## Usage

Run the main script to start the interactive visualization:

```
python relativity_sim.py
```

Follow the on-screen menu to select which visualization you'd like to see:
* Option 1: Spacetime Curvature
* Option 2: Gravitational Lensing
* Option 3: Gravitational Time Dilation

## Simulation Details

### Spacetime Curvature
A simplified 3D model of the Schwarzschild metric. A yellow sphere is a massive object, an orbiting particle shows the curved path objects follow in spacetime.

### Gravitational Lensing
Light paths bending around massive objects. Blue dots are original light source positions, cyan dots are apparent positions after lensing. White arrows are displacement vectors.

### Time Dilation
Time passage on Earth vs a satellite near a massive object. Why GPS satellites need to account for relativistic effects.

## Educational Context
For educational purposes only to help students and enthusiasts grasp General Relativity concepts. Simulations use simplified models to capture the essence of relativistic effects.

## Contribute
Pull Requests welcome.

## License
MIT License - see LICENSE file.

## Credits
* Einstein's General Theory of Relativity (1915)
* Modern physics education resources
