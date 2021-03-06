from ..utils import *


##
# Minions

# Vitality Totem
class GVG_039:
	events = [
		OWN_TURN_END.on(Heal(FRIENDLY_HERO, 4))
	]


# Siltfin Spiritwalker
class GVG_040:
	events = [
		Death(FRIENDLY + MURLOC).on(Draw(CONTROLLER))
	]


# Neptulon
class GVG_041:
	action = [Give(CONTROLLER, RandomMinion(race=Race.MURLOC)) * 4]


##
# Spells

# Ancestor's Call
class GVG_029:
	action = [
		ForcePlay(CONTROLLER, RANDOM(CONTROLLER_HAND + MINION)),
		ForcePlay(OPPONENT, RANDOM(OPPONENT_HAND + MINION)),
	]


# Crackle
class GVG_038:
	def action(self, target):
		return [Hit(TARGET, random.randint(3, 6))]


##
# Weapons

# Powermace
class GVG_036:
	action = [Buff(RANDOM(FRIENDLY_MINIONS + MECH), "GVG_036e")]
