# Comet catalog files for NASA Cosmographia simulating visual dust / ion tail appearance

## Cosmographia

NASA Cosmographia solar system and mission visualization tool is available for free download: https://naif.jpl.nasa.gov/naif/cosmographia.html

## Usage

Download all files with `git clone https://github.com/isenberg/cosmographia_catalogs` or as ZIP from the green Code icon in the upper right and place them into a directory in your Documents folder or some other location.

Start Cosmographia and select from its menu **File -> Open Catalog** to load one of the Comet.json files and afterwards change the time with the clock icon to a day around the comet perihelion to view it with its dust tail, ion tail and for some also the sodium tail.

To view the orbit trail of its previous locations during the last few hours, select **Guides -> Plot Trajectory** in the menu or right-click on the comet nucleus and toggle Trajectory. For some comets, like Arend-Roland or 2022 E3 ZTF, this matches the anti-tail. Some comets have large visible vectors toward Sun and Earth added which can be disabled with a **right-click on the nucleus** and selecting **Sun Direction** and **Earth Direction**.

To get a simulation of viewing it from Earth, search for Earth, go to it and then search for the comet and select Point At to view it. Change the distance from Earth with the Touchpad Scroll Up/Down gesture and adjust the field of view with the Touchpad Zoom In/Out gesture.

The radius displayed when clicking on the comet is an approximation of the visual coma radius, not the solid nucleus radius.

## Comet Tail Simulation

It's not a real simulation of the dust, ion and sodium tails of comets, but the visual appearance and its change around the few days to weeks of perihelion closely matches the actual observation of those comets.

It's achieved by using the Cosmographia Particle System (ParticleSystem keyword) with a workaround to simulate the combined effect of the solar wind force pushing the tail particles radially outwards from the Sun and the effect of tangentially falling behind the nucleus orbit with increased orbit radius due to the radially outwards movement by the solar wind. Instead of applying a force radially to the particles, the workaround uses a constant radially particle ejection speed combined with a force pushing tangentially to the nucleus orbit against the orbital velocity vector. That combination results visually almost to he same and is used as I couldn't find any other way yet in Cosmographia to simulate the tails.

Please note that in nature there isn't any force tangentially pushing against the orbit velocity vector into the tail particles, it's only used here as mathematical workaround until a better solution exists.

## Orbital Elements / SPICE data

Source of the keplerian orbital elements included in the JSON files: https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html

The .bsp SPICE kernel used for those comets with hyperbolic trajectories was generated as Small Body SPK File here: https://ssd.jpl.nasa.gov/horizons/app.html

## Example Images

Screenshots taken in Cosmographia and visually similar real observations:
* [C1995 O1 Hale-Bopp.jpg](C1995%20O1%20Hale-Bopp.jpg) matches https://apod.nasa.gov/apod/ap070331.html
* [C2006 P1 McNaught.jpg](C2006%20P1%20McNaught.jpg) matches https://www.eso.org/public/images/esopia00100teles
* [C2022 E3 ZTF.jpg](C2022%20E3%20ZTF.jpg) matches https://www.astrobin.com/07qt67/?q=C/2022%20E3%20ZTF
* [C1956 R1 Arend-Roland.jpg](C1956%20R1%20Arend-Roland.jpg) matches http://stony-ridge.org/AlanMcClure.html
* [C1973 E1 Kohoutek.jpg](C1973%20E1%20Kohoutek.jpg) matches https://commons.wikimedia.org/wiki/File:Edward_Gibson_illustration_of_Comet_Kohoutek.jpg
* [96P Machholz.jpg](96P Machholz.jpg) matches https://twitter.com/SungrazerComets/status/1620118054268211202 LASCO C3
