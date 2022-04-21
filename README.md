# Comet Catalog Files for NASA Cosmographia

## Cosmographia

NASA Cosmographia solar system and mission visualization tool main page: https://naif.jpl.nasa.gov/naif/cosmographia.html

## Usage

Within Cosmographia load the comet JSON files from File -> Open Catalog and change the time to a day around the comet perihelion to view it with its dust tail, ion tail and for some also the sodium tail. 

To get a simulation of viewing it from Earth, search for Earth, go to it and then search for the comet and select Point At to view it. Change the distance from Earth with the Touchpad Scroll Up/Down gesture and adjust the field of view with the Touchpad Zoom In/Out gesture.

## Comet Tail Simulation

It's not a real simulation of the dust, ion and sodium tails of comets, but the visual appearance and its change around the few days to weeks of perihelion closely matches the actual observation of those comets.

It's achieved by using the Cosmographia Particle System (ParticleSystem keyword) with a workaround to simulate the combined effect of the solar wind force pushing the tail particles radially outwards from the Sun and the effect of falling behind the nucleus orbit with increased orbit radius due to the radially outwards movement by the solar wind. Instead of applying a force radially to the particles, the workaround uses a constant radially particle ejection speed combined with a force pushing tangentially to the nucleus orbit against the orbital velocity vector. That combination results mathematically almost to he same and is used as I couldn't find any other way yet in Cosmographia to simulate the tails.
