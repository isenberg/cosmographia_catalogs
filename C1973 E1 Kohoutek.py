# show comet C/1973 E1 Kohoutek
#
# source: https://github.com/isenberg/cosmographia_comets
#
# start Cosmographia from the directory where the comet file is stored
# then select in the menu File -> Run Script and load the comet script with ending .py
#
# Cosmographia script documentation: https://cosmoguide.org

import os
import cosmoscripting

cosmo = cosmoscripting.Cosmo()
comet="C/1973 E1 Kohoutek"
cometfile=os.path.join(cosmo.scriptDir(), "C1973 E1 Kohoutek.json")
cosmo.displayNote( "Viewing comet " + comet, 3)
cosmo.loadCatalogFile(cometfile)
cosmo.setTimeRate(1)
cosmo.setTime("1973-12-20 01:00:00 UTC")
cosmo.setFov(90, 1)
cosmo.gotoHome(1)
cosmo.gotoObject("Earth", 3)
cosmo.moveTowardsCenter(12600, 3)
cosmo.pointAtObject(comet)
cosmo.rollLeft(80, 3)
#cosmo.rollToBodyFixedVector("Earth", "[0.0,1.0,0.0]", 3)
cosmo.trackObject(comet)
#cosmo.hideObject("Earth")
cosmo.showTrajectory(comet)
cosmo.showVelocityVector(comet)
cosmo.showDirectionVector(comet, "Sun")
cosmo.showDirectionVector(comet, "Earth")
cosmo.setTimeRate(10000)
cosmo.wait(10)
cosmo.setFov(6, 3)
cosmo.wait(90)
cosmo.setFov(90, 3)
cosmo.wait(10)
cosmo.setTimeRate(1)
